# Första timestimat per arbetspaket

Grovt utkast för intern diskussion. Siffrorna är en första bedömning utifrån kravspecifikationen version 1.3-V, inte en verifierad kalkyl. De ska stämmas av med utvecklare och arkitekt innan något lämnas till SFB.

---

## Antaganden

1. **Egenutvecklad lösning.** Kravspecen talar om en "egen berikningsdel" och ber Vaimo föreslå teknikstack och hosting. Estimatet antar en egen webbapplikation byggd med standardkomponenter: databas, sökindex, fillagring och en färdig tabellkomponent. Om vi i stället föreslår en färdig PIM-plattform ändras siffrorna kraftigt (se sist).
2. **Vaimo bygger allt på PIM-sidan.** ITM8:s paket (AP07 till AP10) ingår inte.
3. **Förstudien återanvänds** i AP01, vilket sänker AP01 jämfört med att börja från noll.
4. **Volymer enligt kravspecen:** 1,4 miljoner artiklar, 520 000 bilder, 118 000 dokument, två administratörer.
5. **Tre migreringskörningar** (prov, rättning, slut) ingår.
6. **Normal** betyder mest troligt utfall. **Låg** betyder att AP01 visar att data och gränssnitt är i gott skick. **Hög** betyder att C4-exporten, mediehanteringen eller kontrakten med ITM8 visar sig krångliga.

---

## F1: Vaimos paket

| Paket | Innehåll i korthet | Låg | Normal | Hög | Det som driver osäkerheten |
|---|---|---:|---:|---:|---|
| AP01 | Teknisk förstudie: fältmatris, kontrakt, Excel-mall, exportinventering, reviderat estimat | 160 | 220 | 300 | Hur mycket av förstudien som håller, hur snabbt ITM8 och C4-ansvarig levererar underlag |
| AP02 | Datamodell och grundarkitektur: objekt, käll- och egna värden, historik, grundplattform, inloggning | 160 | 240 | 340 | Antal fält och regler i fältmatrisen |
| AP03 | Gränssnitt och berikning: sök och filter i 1,4 miljoner artiklar, redigera artikel, produktgrupper, tre kategoriträd, webbstatus, notislista, attributstädning, gemensamma valideringsregler | 600 | 850 | 1 200 | Största paketet. Hur mycket gränssnittet behöver justeras med administratörerna |
| AP16 | Tabellredigering: tabell, kopiera och klistra in, samma värde på flera rader, förhandsgranskning, konflikter, bakgrundsjobb | 200 | 300 | 450 | Val av tabellkomponent, krav på tangentbordsstöd |
| AP06 | Excel: export och import av 5 000 rader, skapa manuella artiklar, radvisa fel, konfliktkontroll | 160 | 240 | 340 | Hur komplex mallen blir för relationer och rensning |
| AP04 | PIM:s integrationsgränssnitt: ta emot källdata, matchning, ändringsflöde ut, kvittens, omsändning, felvy | 350 | 500 | 750 | Hur kontraktet med MagicBox ser ut, hur stora de dagliga volymerna är |
| AP05 | Bilder, dokument och versioner: uppladdning av flera filer, ordning, dölja från webben, oföränderliga versioner i tio år, versionsvy | 250 | 380 | 550 | Befintlig lagring och länkar, hur versioner känns igen |
| AP11 | Migrering: mappning, importverktyg, tre körningar, avstämning | 300 | 450 | 700 | Kvaliteten på C4-exporten, avvikande produktgrupper |
| AP22 | Gamla dokumentversioner och läsbar historikexport | 80 | 160 | 320 | Helt okänt vad som finns i C4. Bredast intervall |
| AP12 | Gemensamt test och acceptans: hela kedjan, prestandatest, stöd till administratörerna, felrättning och omtest | 300 | 450 | 650 | Hur väl ITM8 och Snicken håller sina testfönster |
| AP13 | Miljöer, drift och återställning: test och produktion, backup, övervakning, återställningsprov | 150 | 220 | 320 | Val av hosting, koppling till befintlig inloggning |
| AP14 | Driftsättning och överlämning: växling från C4, två utbildningar, tio dagars stöd, dokumentation och kod | 160 | 220 | 300 | Om ändringsstopp eller fångat delta krävs vid växlingen |
| **Delsumma** | | **2 870** | **4 230** | **6 220** | |
| AP15 | Projektledning, ca 12 % | 340 | 510 | 750 | Kalendertid och antal parter |
| **Totalt F1** | | **3 210** | **4 740** | **6 970** | |

### Hur timmarna fördelar sig

| Del | Normal | Andel |
|---|---:|---:|
| Bygga själva PIM (AP02, AP03, AP16, AP06, AP04, AP05) | 2 510 | 53 % |
| Migrering (AP11, AP22) | 610 | 13 % |
| Test, drift och överlämning (AP12, AP13, AP14) | 890 | 19 % |
| Förstudie och projektledning (AP01, AP15) | 730 | 15 % |

---

## Kalendertid, grov bedömning

Med ett team på cirka fyra till fem personer (projektledare, arkitekt, två till tre utvecklare, testare på deltid):

| Fas | Tid |
|---|---|
| AP01 | 6 till 8 veckor |
| Bygge (AP02 till AP06, AP16) | 5 till 6 månader |
| Migrering och test (AP11, AP22, AP12), delvis parallellt | 2 till 3 månader |
| Växling och stöd (AP14) | 3 till 4 veckor |
| **Totalt från start** | **cirka 9 till 12 månader** |

---

## Senare och separat (indikativt)

| Paket | Innehåll | Låg | Normal | Hög |
|---|---|---:|---:|---:|
| AP17 (V2) | Prioritering utifrån affärssystemets data | 120 | 200 | 300 |
| AP18 (V2) | Automatisk gruppering till produkter | 200 | 320 | 500 |
| AP19 (V2) | Arkivering, arkivsökning, återaktivering | 120 | 180 | 280 |
| AP20 (tillval) | Nya domäner för bilder och dokument | 40 | 80 | 150 |
| AP21 (tillval) | Avancerad förhandsvisning | 60 | 120 | 200 |
| ALT03 | Nödlösning om F1 inte hinner före C4 stängs | 80 | 200 | 400 |

---

## Om vi föreslår en färdig PIM-plattform i stället

AP02 och delar av AP03 blir mindre, kanske 30 till 40 % lägre. Men flera krav är ovanliga för standardplattformar och kräver anpassning: separata käll- och egna värden med automatiskt effektivt värde, notislistan, tabellredigering med konfliktkontroll, oföränderliga dokumentversioner i tio år och separata leveranspositioner per mottagare. Till det kommer licenskostnad för 1,4 miljoner artiklar. Nettoeffekten är osäker och bör räknas separat om det blir aktuellt.

---

## Att kontrollera innan siffrorna används

1. När stänger C4? Det avgör om kalendertiden räcker eller om ALT03 behövs.
2. Vilken plattform vill vi föreslå?
3. Hur mycket av förstudien går att återanvända rakt av i AP01?
4. Låt en utvecklare och en arkitekt gå igenom AP03, AP04 och AP11, som står för störst risk.
