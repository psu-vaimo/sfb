"""Räknar start och slut för uppgifter i SFB_Uppgifter_*.ord.

Kör från repots rot: python3 Planering/tidplan.py
Läser längd (arbetsdagar), beror på och status för varje +uppgift och skriver
start och slut på samma rader. Projektstart läses från fältet projektstart på
första nivån i SFB_Uppgifter_AP01.ord. Klara uppgifter [x] flyttas inte, och
pågående [-] behåller sin start. Skriptet skriver ut kritisk linje per milstolpe
och uppgifter som slutar efter sitt senast-datum.
"""
import datetime as dt
import glob
import re
import sys

HELGDAGAR = {
    # Svenska helgdagar och dagar som i praktiken är lediga, 2026 till 2027.
    "2026-12-24", "2026-12-25", "2026-12-31",
    "2027-01-01", "2027-01-06", "2027-03-26", "2027-03-29",
    "2027-05-06", "2027-06-25", "2027-12-24", "2027-12-31",
}


def arbetsdag(d):
    return d.weekday() < 5 and d.isoformat() not in HELGDAGAR


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


def main():
    filer = sorted(glob.glob("SFB_Uppgifter_*.ord"))
    if not filer:
        sys.exit("Inga SFB_Uppgifter_*.ord i katalogen.")
    m = re.search(r"^\tprojektstart:: (\S+)$", open("SFB_Uppgifter_AP01.ord", encoding="utf-8").read(), re.M)
    projektstart = forsta_arbetsdag(dt.date.fromisoformat(m.group(1)))
    uppg = las(filer)
    beroenden = {k: [x.strip() for x in u["falt"].get("beror på", "").split(";") if x.strip()] for k, u in uppg.items()}
    saknas = sorted({d for ds in beroenden.values() for d in ds if d not in uppg})
    start, slut, faller = {}, {}, {}

    def berakna(k, stack=()):
        if k in slut:
            return
        if k in stack:
            sys.exit("Cykel: " + " > ".join(stack + (k,)))
        u = uppg[k]
        ds = [d for d in beroenden[k] if d in uppg]
        for d in ds:
            berakna(d, stack + (k,))
        langd = int(float(u["falt"].get("längd", "1") or 1))
        gammal_start = u["falt"].get("start")
        if u["status"] == "x" and gammal_start and u["falt"].get("slut"):
            start[k] = dt.date.fromisoformat(gammal_start)
            slut[k] = dt.date.fromisoformat(u["falt"]["slut"])
            return
        if ds:
            senaste = max(ds, key=lambda d: slut[d])
            faller[k] = senaste
            tidigast = slut[senaste] if langd == 0 else nasta_arbetsdag(slut[senaste])
        else:
            tidigast = projektstart
        if u["status"] == "-" and gammal_start:
            tidigast = dt.date.fromisoformat(gammal_start)
        start[k] = tidigast
        slut[k] = tidigast if langd == 0 else lagg_till(tidigast, langd)

    for k in uppg:
        berakna(k)

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
