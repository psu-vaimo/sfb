"""Räknar start och slut för uppgifter i SFB Uppgifter *.ord.

Kör från repots rot: python3 Planering/tidplan.py

Uppgifter som Vaimo utför planeras efter kapacitet. Timmarna per uppgift hämtas
ur SFB Estimat rader.csv via kolumnen uppgift, med rollernas scenarioavdrag i
SFB Estimat.ord. Vaimos kapacitet i timmar per arbetsdag och lediga perioder
står i fälten kapacitet och ledigt på första nivån i SFB Uppgifter AP01.ord.
Projektledningens rader (E-AP15) ingår inte, eftersom kapaciteten anges netto
efter projektledning.

Varje arbetsdag får de Vaimo-uppgifter som är redo kapacitet i prioritetsordning:
den uppgift som senast måste vara klar först, räknat bakåt från fälten senast. En Vaimo-uppgift tar minst
en arbetsdag. Uppgifter med löpande:: ja, som stödperioden, tar sin längd i
arbetsdagar och planeras inte efter kapacitet. Uppgifter utan Vaimo-timmar, till exempel granskning hos SFB eller
ITM8:s arbete, tar sin längd i arbetsdagar.

Klara uppgifter [x] flyttas inte. En uppgift börjar aldrig före sitt
tidigast-datum. Skriptet skriver ut milstolparna, kritisk linje och uppgifter
som slutar efter sitt senast-datum.
"""
import csv
import datetime as dt
import glob
import re
import sys

HELGDAGAR = {
    # Svenska helgdagar och dagar som i praktiken är lediga, 2026 till 2027.
    "2026-12-24", "2026-12-25", "2026-12-31",
    "2027-01-01", "2027-01-06", "2027-03-26", "2027-03-29",
    "2027-05-06", "2027-05-14", "2027-06-25", "2027-12-24", "2027-12-31",
}
LEDIGT = []


def arbetsdag(d):
    if d.weekday() >= 5 or d.isoformat() in HELGDAGAR:
        return False
    return not any(a <= d <= b for a, b in LEDIGT)


def nasta_arbetsdag(d):
    d += dt.timedelta(days=1)
    while not arbetsdag(d):
        d += dt.timedelta(days=1)
    return d


def forsta_arbetsdag(d):
    while not arbetsdag(d):
        d += dt.timedelta(days=1)
    return d


def lagg_till(start, dagar):
    """Slutdag för en uppgift som börjar start och tar dagar arbetsdagar."""
    d = start
    for _ in range(max(dagar, 1) - 1):
        d = nasta_arbetsdag(d)
    return d


def las(filer):
    uppg = {}
    for f in filer:
        rader = open(f, encoding="utf-8").read().split("\n")
        for i, rad in enumerate(rader):
            m = re.match(r"^(\t*)(?:\[(.)\] )?(.*) \+uppgift \^(\S+)$", rad)
            if not m:
                continue
            ind = len(m.group(1))
            u = {"fil": f, "rad": i, "status": m.group(2) or " ", "namn": m.group(3), "falt": {}, "faltrad": {}}
            j = i + 1
            while j < len(rader) and (len(rader[j]) - len(rader[j].lstrip("\t"))) > ind:
                t = rader[j].strip()
                if len(rader[j]) - len(rader[j].lstrip("\t")) == ind + 1 and "::" in t:
                    k, v = t.split("::", 1)
                    u["falt"][k.strip()] = v.strip()
                    u["faltrad"][k.strip()] = j
                j += 1
            uppg[m.group(4)] = u
    return uppg


def las_roller():
    """Scenarioavdrag per roll för Vaimos roller i SFB Estimat.ord."""
    text = open("SFB Estimat.ord", encoding="utf-8").read()
    roller = {}
    for m in re.finditer(r"\+estimatroll \^(\S+)\n((?:\t{3}.*\n)*)", text):
        falt = dict(re.findall(r"^\t{3}(\S+):: ?(.*)$", m.group(2), re.M))
        if falt.get("part") == "Vaimo":
            roller[m.group(1)] = float(falt.get("scenarioavdrag") or 0)
    return roller


def vaimo_timmar(uppg):
    roller = las_roller()
    timmar = {}
    for r in csv.DictReader(open("SFB Estimat rader.csv", encoding="utf-8")):
        if r["roll"] not in roller or r["_parent"] == "E-AP15":
            continue
        try:
            o, m, p = float(r["optimistisk"]), float(r["trolig"]), float(r["pessimistisk"])
        except ValueError:
            continue
        n = float(r["antal"]) if r["antal"] else 1
        h = n * (o + 4 * m + p) / 6 * (1 - roller[r["roll"]])
        ups = [x.strip() for x in r["uppgift"].split(";") if x.strip() in uppg]
        for x in ups:
            timmar[x] = timmar.get(x, 0) + h / len(ups)
    return timmar


def main():
    filer = sorted(glob.glob("SFB Uppgifter *.ord"))
    if not filer:
        sys.exit("Inga SFB Uppgifter *.ord i katalogen.")
    huvud = open("SFB Uppgifter AP01.ord", encoding="utf-8").read()
    projektstart = dt.date.fromisoformat(re.search(r"^\tprojektstart:: (\S+)$", huvud, re.M).group(1))
    for a, b in re.findall(r"(\d{4}-\d\d-\d\d) till (\d{4}-\d\d-\d\d)",
                           (re.search(r"^\tledigt:: (.*)$", huvud, re.M) or [None, ""])[1]):
        LEDIGT.append((dt.date.fromisoformat(a), dt.date.fromisoformat(b)))
    kapacitet = sorted((dt.date.fromisoformat(a), float(b)) for a, b in re.findall(
        r"(\d{4}-\d\d-\d\d) (\d+(?:\.\d+)?)", (re.search(r"^\tkapacitet:: (.*)$", huvud, re.M) or [None, ""])[1]))
    if not kapacitet:
        sys.exit("Fältet kapacitet saknas i SFB Uppgifter AP01.ord.")
    projektstart = forsta_arbetsdag(projektstart)

    uppg = las(filer)
    ordning = {k: i for i, k in enumerate(uppg)}
    beroenden = {k: [x.strip() for x in u["falt"].get("beror på", "").split(";") if x.strip() in uppg]
                 for k, u in uppg.items()}
    saknas = sorted({x.strip() for u in uppg.values() for x in u["falt"].get("beror på", "").split(";")
                     if x.strip() and x.strip() not in uppg})
    timmar = vaimo_timmar(uppg)
    for k, u in uppg.items():
        if u["falt"].get("löpande") == "ja":
            timmar.pop(k, None)
    langd = {k: int(float(u["falt"].get("längd", "1") or 1)) for k, u in uppg.items()}

    # Prioritet: senaste tillåtna slut, räknat bakåt från fälten senast med
    # uppgifternas längd. Vaimo-uppgifter räknas med timmar delat med kapacitet.
    efter = {k: [] for k in uppg}
    for k, ds in beroenden.items():
        for d in ds:
            efter[d].append(k)
    dagar = [projektstart]
    while len(dagar) < 400:
        dagar.append(nasta_arbetsdag(dagar[-1]))
    index = {d: i for i, d in enumerate(dagar)}
    kap0 = kapacitet[0][1]
    tid = {k: (0 if langd[k] == 0 else max(1, -(-timmar[k] // kap0)) if timmar.get(k, 0) > 0 else langd[k]) for k in uppg}
    senast = {}

    def sen(k):
        if k not in senast:
            v = 10 ** 6
            if uppg[k]["falt"].get("senast"):
                v = index.get(forsta_arbetsdag(dt.date.fromisoformat(uppg[k]["falt"]["senast"])), 10 ** 6)
            for e in efter[k]:
                v = min(v, sen(e) - tid[e])
            senast[k] = v
        return senast[k]

    for k in uppg:
        sen(k)

    def kap(d):
        v = 0
        for a, h in kapacitet:
            if a <= d:
                v = h
        return v

    start, slut, faller, kvar = {}, {}, {}, {}
    for k, u in uppg.items():
        if u["status"] == "x" and u["falt"].get("start") and u["falt"].get("slut"):
            start[k] = dt.date.fromisoformat(u["falt"]["start"])
            slut[k] = dt.date.fromisoformat(u["falt"]["slut"])
    tidigast = {k: forsta_arbetsdag(dt.date.fromisoformat(u["falt"]["tidigast"]))
                for k, u in uppg.items() if u["falt"].get("tidigast")}

    dag = projektstart
    gräns = projektstart + dt.timedelta(days=800)
    while len(slut) < len(uppg) and dag < gräns:
        if not arbetsdag(dag):
            dag += dt.timedelta(days=1)
            continue
        andrat = True
        while andrat:
            andrat = False
            for k in uppg:
                if k in slut or k in start or not all(d in slut for d in beroenden[k]):
                    continue
                senaste = max(beroenden[k], key=lambda d: slut[d]) if beroenden[k] else None
                if senaste:
                    faller[k] = senaste
                if langd[k] == 0:
                    start[k] = slut[k] = slut[senaste] if senaste else projektstart
                    andrat = True
                    continue
                if senaste and slut[senaste] >= dag:
                    continue
                if k in tidigast and tidigast[k] > dag:
                    continue
                if timmar.get(k, 0) > 0:
                    kvar[k] = timmar[k]
                    start[k] = dag
                else:
                    start[k] = dag
                    slut[k] = lagg_till(dag, langd[k])
                    andrat = True
        c = kap(dag)
        for k in sorted(kvar, key=lambda x: (senast[x], ordning[x])):
            if c <= 0:
                break
            del_ = min(kvar[k], c)
            kvar[k] -= del_
            c -= del_
        for k in [x for x, v in kvar.items() if v <= 1e-9]:
            slut[k] = dag
            del kvar[k]
        dag += dt.timedelta(days=1)
    if len(slut) < len(uppg):
        sys.exit("Kunde inte planera: " + ", ".join(k for k in uppg if k not in slut))

    andrade = {}
    for k, u in uppg.items():
        andrade.setdefault(u["fil"], open(u["fil"], encoding="utf-8").read().split("\n"))
        rader = andrade[u["fil"]]
        for falt in ("start", "slut"):
            v = (start if falt == "start" else slut)[k].isoformat()
            if falt in u["faltrad"]:
                j = u["faltrad"][falt]
                rader[j] = rader[j][: len(rader[j]) - len(rader[j].lstrip("\t"))] + f"{falt}:: {v}"
    for f, rader in andrade.items():
        open(f, "w", encoding="utf-8").write("\n".join(rader))

    if saknas:
        print("Beroenden till uppgifter som inte finns än:", ", ".join(saknas))
    print(f"Vaimos timmar i planen: {sum(timmar.values()):.0f}, exklusive projektledning.")
    for k, u in uppg.items():
        s = u["falt"].get("senast")
        if s and slut[k] > dt.date.fromisoformat(s):
            print(f"FÖRSENAD: {k} {u['namn']} slutar {slut[k]}, senast {s}")
    for k, u in uppg.items():
        if u["falt"].get("längd") == "0":
            linje, n = [], k
            while n:
                linje.append(n)
                n = faller.get(n)
            print(f"\n{u['namn']} ({k}): {slut[k]}")
            print("  Kritisk linje: " + " < ".join(linje))


if __name__ == "__main__":
    main()
