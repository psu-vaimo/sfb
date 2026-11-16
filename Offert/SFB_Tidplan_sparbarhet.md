# SFB berikning och PIM: gemensam tidplan och spårbarhet

Vaimo, utkast 2026-11-16. Svar på kravspecifikationen avsnitt 11 och bilagan, avsnitt 5.

## Gemensam tidplan

| Period | Vaimo | SFB | ITM8:s del | Snicken och nuvarande part |
|---|---|---|---|---|
| v47 till 48 | Startmöte. Återanvändning, startlista, inventering av export, medier, volymer, drift och identitet. Identitetsregler och fältmatris | Godkänner startlista, inventeringar, identitetsregler och fältmatris | Startmöte. Underlag för integrationer och medielagring | Nuvarande part levererar historik och ändringslogg 19 till 23 nov |
| v49 till 50 | Lasttest av Medusa 1 till 2 dec. Kontrakt, arkitektur, miljöer och datamodell | Godkänner kontrakten 3 dec och arkitekturen 7 dec. Fryser berikningen i C4 11 dec | Granskar kontrakten. Bygger källintegrationer och MagicBox-sidan 2 till 8 dec och verifierar ERP-matchningen 9 till 11 dec | Nuvarande part levererar slutexporten 12 dec |
| v51 | Gemensamma regler, källmottagning och utgående flöde. Integrationstest 17 dec. Delleveransen i drift 18 dec | Stämmer av slutexporten 14 dec. Godkänner delleveransen 18 dec | Godkänner miljöerna som driftägare 16 dec. Integrationstest. Växlar MagicBox till PIM 18 dec | |
| v52 till 53 | Ledigt. Tillsyn av delleveransen 28 till 30 dec | | | C4 stängs 31 dec |
| Januari, från 7 jan | Resten av AP01 med reviderat estimat och plan. Migreringsmappning. Excel och tabellredigering påbörjas | Migreringsurval 13 jan och datastädning 21 jan. Beslut om resten av F1 18 jan | Kontrakt för fel och transport. Snicken-adaptern | Snicken och ITM8 granskar Snickenkontraktet 18 till 20 jan |
| Februari | Excel, tabellredigering, migreringsverktyg, prov- och korrigeringskörning. Avbrottsverifiering | Demo och godkännande av funktioner. Stämmer av körningarna 24 feb | Snicken-adaptern testad 1 feb | |
| Mars | Gränssnitt, medier och dokumentversioner klara. Miljöer, integrationstest och acceptanstest 15 till 25 mars | Administratörerna provar alla huvudflöden. Acceptansbeslut 25 mars | Provar leveranser till MagicBox | Snicken provar leveranser |
| April | Slutkörning, driftsättning 12 apr, utbildning 13 till 14 apr och stöd till 23 apr | Go/no-go före slutkörningen. Godkänner F1 26 apr | Växlar källflöden | |
| April till maj | V2 och tillval, efter beslut | Beslut om V2 och tillval | AP17 och AP20 om de beställs | |

SFB:s medverkan är cirka 20 timmar per vecka under hela perioden.

## Beslutspunkter

- 17 nov: beställning av AP01.
- 3 dec och 7 dec: kontrakten mellan MagicBox och PIM, och arkitekturen.
- 11 dec: berikningen i C4 fryses.
- 14 dec: slutexporten från 12 dec är avstämd.
- 18 dec: delleveransen godkänd och MagicBox växlad till PIM.
- 18 jan: AP01 godkänd och beslut om resten av F1.
- 25 mars: acceptansbeslut.
- Före slutkörningen i april: go/no-go.
- 26 apr: F1 godkänd.

## Spårbarhet

Alla 63 krav har ett arbetspaket och en leverans. Kravkatalogen i svaret har en kolumn per krav med Vaimos leveranser.

| Paket | Krav | Vaimos leveranser |
|---|---|---|
| AP01 | PIM-I01, PIM-M01 | Återanvändningsmatris, gränssnittskontrakt, fältmatris, identitetsregler, gruppkontroll, Excel-format, icke-funktionella krav, arkitektur, export-, medie- och volyminventering, avbrotts- och driftverifiering, motsägelser, reviderat estimat och plan |
| AP02 | PIM-D01, D02, D03, D05, D07 | Datamodell |
| AP03 | PIM-D04, D06, W01 till W09, Q03, Q04 | Administratörsgränssnitt |
| AP04 | PIM-I02, I03, I04 | PIM:s integrationsgränssnitt |
| AP05 | PIM-A01 till A05, A08 | Medie- och dokumenthantering |
| AP06 | PIM-X01, X02, X03 | Excelimport och export |
| AP07 | PIM-I05, I06, I07 | ITM8: källintegrationer till MagicBox |
| AP08 | PIM-I08 | ITM8: MagicBox-anslutning och distribution |
| AP09 | PIM-I09, I10 | ITM8: Snicken-adapter |
| AP10 | PIM-A06, A07 | ITM8: medielagring, transformering och länkar |
| AP11 | PIM-M02, M03 | Migreringsurval, export, mappning, verktyg, avstämning, migrerat bestånd, slutexport |
| AP22 | PIM-M06 | Äldre dokumentversioner och läsbar ändringslogg |
| AP12 | PIM-Q01, Q02, M04 | Testplan, integrationstest, kapacitet, avbrott, acceptanstest och acceptansbeslut |
| AP13 | PIM-O01 till O05 | Miljöer, inloggning, backup, övervakning, felsökning, åtkomst vid avbrott |
| AP14 | PIM-M05, H01, H02, H03 | Växling, driftsatt F1, kodarkiv, dokumentation, runbook, utbildning, stödperiod |
| AP15 | PIM-H04 | Leveransplan, risk- och beslutslogg, ändringslogg, statusrapporter |
| AP16 | PIM-N01 | Tabellredigering |
| AP17 | PIM-N02 | Fältanalys, återföring från MagicBox, prioriteringsfilter |
| AP18 | PIM-N03 | Grupperingsregler, automatisk gruppering, förslagskö |
| AP19 | PIM-N04 | Arkivering, arkivsökning, återaktivering |
| AP20 | PIM-N05 | Domän- och länkupplägg, föreslås hos ITM8 |
| AP21 | PIM-N06 | Förhandsvisning för valda format |
| Framtid | PIM-N07 | Prissätts inte nu |
