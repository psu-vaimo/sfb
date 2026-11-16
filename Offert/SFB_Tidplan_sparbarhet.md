# SFB berikning och PIM: gemensam tidplan och spårbarhet

Vaimo, utkast 2026-11-16. Svar på kravspecifikationen avsnitt 11 och bilagan, avsnitt 5.

## Gemensam tidplan

| Period | Vaimo | SFB | ITM8:s del | Snicken och nuvarande part |
|---|---|---|---|---|
| v47 till 48 | Startmöte. Återanvändning, startlista, inventering av export, medier, volymer, drift och identitet. Lasttest av Medusa 25 till 27 nov | Godkänner startlista och inventeringar | Startmöte. Underlag för integrationer och medielagring | Nuvarande part levererar historik och ändringslogg senast 24 nov |
| v49 till 50 | Fältmatris, arkitektur, kontrakt PIM till MagicBox. Test- och produktionsmiljö, datamodell | Godkänner arkitektur 4 dec och kontrakt 9 dec. Fryser berikningen i C4 11 dec | Granskar kontraktet. Godkänner miljöerna som driftägare | Nuvarande part levererar slutexporten 12 dec |
| v51 | Kontroll av slutexporten. Gemensamma regler, källmottagning och utgående flöde. Integrationstest 15 till 17 dec. Delleveransen i drift 18 dec | Stämmer av slutexporten 14 dec. Godkänner delleveransen 18 dec | Källintegrationer och MagicBox-sidan klara 14 dec. Integrationstest. Växlar MagicBox till PIM 18 dec | |
| v52 till 53 | Ledigt. Tillsyn av delleveransen 28 till 30 dec | | | C4 stängs 31 dec |
| Januari, från 7 jan | Resten av AP01: kontrakt, Excel-mall, dokumentversioner, migreringsunderlag, avbrottsverifiering, reviderat estimat och plan | Migreringsurval och datastädning. Beslut om resten av F1 28 jan | Kontrakt för fel och transport | Snicken och ITM8 granskar Snickenkontraktet |
| Februari | Gränssnitt, Excel, tabellredigering, medier | Demo och godkännande av funktioner | Snicken-adaptern | |
| Mars | Miljöer klara, migreringsverktyg, provkörning och korrigeringskörning, dokumentversioner | Stämmer av körningarna | Identifierarmappning och länkar | Snicken provar startleverans |
| April | Gemensamt test och acceptanstest | Administratörerna provar alla huvudflöden | Provar leveranser till MagicBox | Snicken provar leveranser |
| Maj | Slutkörning, driftsättning, utbildning, tio dagars stöd | Go/no-go före slutkörning. Godkänner F1 | Växlar källflöden | |
| Juni | V2 och tillval, efter beslut | Beslut om V2 och tillval | AP17 och AP20 om de beställs | |

SFB:s medverkan är cirka 20 timmar per vecka under hela perioden.

## Beslutspunkter

- 17 nov: beställning av AP01.
- 4 dec och 9 dec: arkitektur och kontraktet PIM till MagicBox.
- 11 dec: berikningen i C4 fryses.
- 14 dec: slutexporten från 12 dec är avstämd.
- 18 dec: delleveransen godkänd och MagicBox växlad till PIM.
- 28 jan: AP01 godkänd och beslut om resten av F1.
- April: acceptanstest godkänt.
- Maj: go/no-go före slutkörning och driftstart av F1.

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
