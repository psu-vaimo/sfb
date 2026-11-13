# Skiss: prisupplägg per arbetspaket

Utkast för diskussion internt på Vaimo. Bygger på kravspecifikationen version 1.3-V. Inga timmar eller belopp är satta än.

---

## Grundidé: två steg

| Steg | När | Vad Vaimo lämnar | Hur bindande |
|---|---|---|---|
| **Steg 1** | Nu, i svaret på förfrågan | Fast pris för AP01. Estimat med låg, normal och hög bedömning för resten av F1. Enhetspriser för det som beror på volym | Bara AP01 är bindande |
| **Steg 2** | Efter AP01 | Bindande pris per paket, i den form som passar paketet (se nedan) | Bindande enligt vald modell |

Det matchar SFB:s egen beslutsordning: först AP01, sedan bindande genomförandepris.

## Prismodeller som används

| Modell | Betyder | Passar när |
|---|---|---|
| **Fast pris** | Ett belopp för en bestämd leverans | Omfattningen är tydlig och osäkerheten låg |
| **Takpris** | Löpande räkning, men aldrig över ett maxbelopp | Omfattningen är känd men detaljerna kräver arbete tillsammans med kunden |
| **Löpande räkning med estimat** | Betalt för faktisk tid, med intervall som riktmärke | Arbetet beror mycket på kunden eller andra parter |
| **Enhetspris** | Pris per styck, t.ex. per körning, per 100 000 artiklar eller per GB | Volymen är okänd |
| **Månadspris** | Återkommande kostnad | Drift, lagring, licenser, support |

---

## F1: Vaimos paket

### AP01 Teknisk precisering och inventering
**Innehåll:** Den tekniska förstudien. Tar fram fältmatris, identiteter och exempeldata, utbyteskontrakt med ITM8 och Snicken, fast Excel-mall, inventering av C4-export och filer, samt reviderat estimat och plan. Återanvänder Vaimos tidigare förstudie.
**Nu:** Fast pris (eller takpris). Ange vad från förstudien som återanvänds och att det inte debiteras igen. Visa ITM8:s insats separat.
**Efter AP01:** Avslutat.
**Kommentar:** Det enda paketet SFB uttryckligen vill ha avgränsat och prissatt nu. Ett fast pris här visar att vi inte säljer en öppen förstudie.

### AP02 Datamodell och grundstruktur
**Innehåll:** Artiklar, produktgrupper (variantgrupper och bundles), attribut, tre kategoriträd, leverantörer, varumärken, separata fält för källvärde och eget värde.
**Nu:** Estimat med intervall.
**Efter AP01:** Fast pris. Med fältmatrisen klar är modellen väl definierad.

### AP03 Administratörsgränssnitt och berikning
**Innehåll:** Sök och filter, redigering av en artikel, skapa manuella artiklar, produktgrupper, kategorier, webbstatus, ändringshistorik, notislistan för källändringar, skyddet av egna texter och egna egenskapsvärden, attributstädning (byta visningsnamn, stoppa användning). Här ligger de gemensamma reglerna för validering som också används av tabell och Excel.
**Nu:** Estimat med intervall. Störst paket och störst osäkerhet i hur gränssnittet ska se ut.
**Efter AP01:** Takpris. Gränssnittet behöver justeras tillsammans med administratörerna, så ett fast pris blir dyrt för SFB eller riskabelt för Vaimo.

### AP16 Tabellredigering och massändring
**Innehåll:** Redigera många artiklar i en tabell, kopiera och klistra in, sätta samma värde på flera rader, förhandsgranska och spara med kontroll av konflikter.
**Nu:** Estimat med intervall. Ange föreslagen komponent och eventuell licenskostnad separat.
**Efter AP01:** Takpris, eller fast pris om en färdig komponent väljs.
**Kommentar:** Använder reglerna från AP03, de ska inte räknas igen här.

### AP06 Excel-import och export
**Innehåll:** Ladda ner urval i fast mall, redigera, ladda upp igen, skapa manuella artiklar, radvisa fel, konfliktkontroll, 5 000 rader.
**Nu:** Estimat med intervall.
**Efter AP01:** Fast pris. Mallen är låst i AP01.
**Kommentar:** Använder reglerna från AP03.

### AP04 PIM:s integrationsgränssnitt
**Innehåll:** PIM:s sida av utbytet med MagicBox och Snicken: ta emot källdata, skicka ändringar, kvittens, omsändning, felhantering, dubblettskydd.
**Nu:** Estimat med intervall. Beroende av ITM8.
**Efter AP01:** Fast pris eller takpris när kontraktet är låst. Villkor: ändringar i kontraktet efter AP01 hanteras som ändringsbeställning.

### AP05 Bilder, dokument och versioner
**Innehåll:** Koppla filer till artiklar och produkter, uppladdning av flera filer, ordning, dölja från webben, dokumentversioner som sparas i tio år, versionsvy.
**Nu:** Estimat med intervall. Lagringskostnad som månadspris, separat.
**Efter AP01:** Takpris. Beror på hur befintlig bildlagring ser ut (ITM8, AP10).

### AP11 Migrering
**Innehåll:** Mappning, importverktyg, en provkörning, en rättningskörning, en slutkörning, avstämning av antal och relationer.
**Nu:** Fast del (mappning och verktyg) som estimat med intervall. Volymdel som enhetspriser: per extra körning, per 100 000 artiklar, per 100 000 filer, per GB.
**Efter AP01:** Fast pris för verktyg och de tre körningarna. Enhetspriser kvar för volym utöver det som mätts.

### AP22 Äldre dokumentversioner och historikexport
**Innehåll:** Flytta gamla dokumentversioner från C4 med koppling till artikel, plus läsbar export av gammal ändringslogg.
**Nu:** Intervall plus enhetspris per GB eller per 10 000 filer. Största okända i hela projektet.
**Efter AP01:** Takpris plus enhetspris. Om exporten har luckor: separat prissatt lösning för åtkomst.
**Kommentar:** En fil får inte räknas både här och i AP11.

### AP12 Gemensamt test och acceptans
**Innehåll:** Test av hela kedjan med ITM8 och Snicken, administratörernas acceptanstest, prestandamätning, felrättning och omtest före godkännande.
**Nu:** Estimat med intervall. Visa insats per part.
**Efter AP01:** Takpris. Rättning av egna fel ingår, väntan på andra parter gör det inte.

### AP13 Miljöer, drift och återställning
**Innehåll:** Test- och produktionsmiljö, inloggning, backup, övervakning, återställningsprov (RPO en timme, RTO en arbetsdag).
**Nu:** Uppsättning som estimat. Drift som månadspris med volymantaganden.
**Efter AP01:** Fast pris för uppsättning. Månadspris för drift.

### AP14 Driftsättning och överlämning
**Innehåll:** Växling från C4, två utbildningstillfällen, tio dagars förstärkt stöd, överlämning av kod och dokumentation.
**Nu:** Estimat.
**Efter AP01:** Fast pris. Omfattningen är tydligt definierad.

### AP15 Projektledning
**Innehåll:** Planering, samordning med SFB, ITM8 och Snicken, uppföljning, beslutspunkter.
**Nu:** Löpande räkning, angiven som kostnad per månad gånger planerad kalendertid.
**Efter AP01:** Takpris eller fast månadspris. Följer kalendertiden, så förseningar hos andra parter påverkar.

---

## F1: ITM8:s paket (inte i Vaimos pris)

| Paket | Innehåll | Hur det redovisas |
|---|---|---|
| AP07 | Källkopplingar från Finfo, BASTA och BVB till MagicBox | Externt beroende. ITM8:s pris om det finns, annars "pris saknas" (inte noll) |
| AP08 | MagicBox-anslutning mot PIM och vidare distribution | Som ovan |
| AP09 | Snickens separata koppling | Som ovan |
| AP10 | Befintlig bildlagring, bildvarianter och länkar | Som ovan |

---

## Senare och separat

| Paket | Innehåll | Pris nu |
|---|---|---|
| AP17 (V2) | Prioritering av artiklar utifrån data från affärssystemet | Indikativt intervall |
| AP18 (V2) | Automatisk gruppering av artiklar till produkter | Indikativt intervall |
| AP19 (V2) | Manuell arkivering, arkivsökning och återaktivering | Indikativt intervall |
| AP20 (tillval) | Nya domäner för bilder och dokument | Indikativt intervall |
| AP21 (tillval) | Avancerad förhandsvisning av fler filformat | Indikativt intervall |
| ALT01 | Snicken inne i MagicBox i stället för egen koppling | Mest ITM8. Vaimo anger påverkan på AP04 |
| ALT03 | Nödlösning om F1 inte hinner före C4 stängs | Intervall, bara om planen visar att F1 inte hinner |
| Egna förslag | Förenklingar Vaimo föreslår | Separat rad med påverkan på krav, pris och tid |

## Återkommande kostnader (månadspris)

Hosting och miljöer, lagring inklusive tioårsarkiv, backup, övervakning, licenser (t.ex. tabellkomponent), support och förvaltning. Varje rad med volymantagande.

---

## Sammanfattning per modell

| Modell | Paket |
|---|---|
| Fast pris nu | AP01 |
| Fast pris efter AP01 | AP02, AP06, AP14, AP11 (fast del), AP13 (uppsättning) |
| Takpris efter AP01 | AP03, AP16, AP04, AP05, AP12, AP22 |
| Löpande eller månadspris | AP15, drift och förvaltning |
| Enhetspriser | AP11 och AP22 (volym), extra migreringskörningar |

## Frågor att bestämma internt

1. Vill vi ta fast pris på AP01, eller takpris?
2. Vilken prisnivå på takpriserna jämfört med normalbedömningen (t.ex. normal plus 15 %)?
3. Ska förseningar som orsakas av ITM8 eller SFB hanteras genom takpriset eller som ändringsbeställning?
4. Ska vi föreslå hosting och drift själva, eller lämna det till SFB eller ITM8?
