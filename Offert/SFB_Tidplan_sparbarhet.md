# SFB berikning och PIM: gemensam tidplan och spårbarhet

Vaimo, utkast 2026-11-16. Svar på kravspecifikationen avsnitt 11 och bilagan, avsnitt 5.

## Gemensam tidplan

| Period | Vaimo | SFB | ITM8:s del | Snicken och nuvarande part |
|---|---|---|---|---|
| v47 till 48 | Startmöte. Återanvändning, startlista, inventering av export, medier, volymer, drift och identitet. Identitetsregler och fältmatris | Godkänner startlista, inventeringar, identitetsregler och fältmatris | Startmöte. Underlag för integrationer och medielagring | Nuvarande part levererar historik och ändringslogg 19 till 23 nov |
| v49 till 50 | Kontrakt, arkitektur, miljöer och datamodell | Godkänner kontrakten 3 dec och arkitekturen 7 dec. Fryser berikningen i C4 11 dec | Granskar kontrakten. Bygger källintegrationer och MagicBox-sidan 2 till 8 dec och verifierar ERP-matchningen 9 till 11 dec | Nuvarande part levererar slutexporten 12 dec |
| v51 | Gemensamma regler, källmottagning och utgående flöde. Integrationstest 17 dec. Delleveransen i drift 18 dec | Stämmer av slutexporten 14 dec. Godkänner delleveransen 18 dec | Godkänner miljöerna som driftägare 16 dec. Integrationstest. Växlar MagicBox till PIM 18 dec | |
| v52 till 53 | Ledigt. Tillsyn av delleveransen 28 till 30 dec | | | C4 stängs 31 dec |
| Januari, från 7 jan | Resten av AP01 med reviderat estimat och plan. Migreringsmappning. Excel och tabellredigering påbörjas | Migreringsurval 12 jan och datastädning 19 jan. Beslut om resten av F1 15 jan | Kontrakt för fel och transport. Snicken-adaptern | Snicken och ITM8 granskar Snickenkontraktet 15 till 19 jan |
| Februari | Excel, tabellredigering, migreringsverktyg, prov- och korrigeringskörning. Avbrottsverifiering | Demo och godkännande av funktioner. Stämmer av körningarna 24 feb | Snicken-adaptern testad 1 feb | |
| Mars | Gränssnitt, medier och dokumentversioner klara. Miljöer, integrationstest och acceptanstest 15 till 25 mars | Administratörerna provar alla huvudflöden. Acceptansbeslut 25 mars | Provar leveranser till MagicBox | Snicken provar leveranser |
| April | Slutkörning, driftsättning 9 apr, utbildning 15 till 16 apr och stöd till 22 apr | Go/no-go före slutkörningen. Godkänner F1 23 apr | Växlar källflöden | |
| April till maj | V2 och tillval, efter beslut | Beslut om V2 och tillval | AP17 och AP20 om de beställs | |

SFB:s medverkan är cirka 20 timmar per vecka under hela perioden.

## Beslutspunkter

- 17 nov: beställning av AP01.
- 3 dec och 7 dec: kontrakten mellan MagicBox och PIM, och arkitekturen.
- 11 dec: berikningen i C4 fryses.
- 14 dec: slutexporten från 12 dec är avstämd.
- 18 dec: delleveransen godkänd och MagicBox växlad till PIM.
- 15 jan: AP01 godkänd och beslut om resten av F1.
- 25 mars: acceptansbeslut.
- Före slutkörningen i april: go/no-go.
- 23 apr: F1 godkänd.

## Produktnedbrytning för F1

F1 består av följande leveranser. Varje leverans granskas eller demonstreras och godkänns för sig. AP01:s leveranser har egen numrering.

| Område | Paket | Leveranser |
|---|---|---|
| Teknisk precisering | AP01 | 1.1 Återanvändningsmatris för förstudien. 1.2 Gränssnittskontrakt (kontrakt MagicBox till PIM, kontrakt PIM till MagicBox, kontrakt för Snickenflödet, fel- och transportkontrakt, validerade kontraktsexempel, ITM8:s granskning av kontrakten). 1.3 Fältmatris (låst startlista för redigerbara produktegenskaper, förteckning över skyddade fält, regel för sammanslagen extern text). 1.4 Identitetsregler och exempeldata (rapport över artiklar utan entydig identitet). 1.5 Kontrollrapport för produktgrupper. 1.6 Fast Excel-format. 1.7 Specifikation av icke-funktionella krav. 1.8 Teknisk arkitektur och säkerhetslösning. 2.1 C4-exportinventering (inventering av äldre dokumentversioner och ändringslogg, underlag för migreringsurval). 2.2 Medieinventering. 2.3 Volym- och lastinventering. 2.4 Verifiering av åtkomst vid PIM-avbrott. 2.5 Verifiering av drift och identitet. 3.1 Beslutsunderlag för öppna frågor. 3.2 Förteckning över skillnader mot förstudien. 3.3 Reviderat genomförandeestimat. 3.4 Reviderad genomförandeplan. 3.5 Granskade workshopanteckningar |
| PIM-applikationen | AP02, AP03, AP16, AP06, AP05, AP04 | 2.1 Datamodell (artikelmodell med identiteter, attributmodell med käll- och egna värden, referensdata för leverantörer och varumärken, tre kategoriträd, produktgruppsmodell). 2.2 Administratörsgränssnitt (sökning och filter, artikelvy och enskild redigering, gemensamma fält-, överstyrnings- och valideringsregler, ändringsnotislista, samtidighetsskydd, ändringshistorik, attributförvaltning, kategoriförvaltning). 2.3 Tabellredigering. 2.4 Excelimport och export (Excelimport med förhandskontroll, Excelexport, jobbstatus för långa jobb). 2.5 Medie- och dokumenthantering (medierelationer med flerfilsuppladdning, ordning och webbexkludering per relation, dokumentversionsarkiv, versionslista per artikel, flaggning av källborttagning). 2.6 PIM:s integrationsgränssnitt (källmottagning, utgående ändringsflöde, återförsök, omsändning och felvy) |
| Integrationer utanför PIM | AP07, AP08, AP09, AP10 | 3.1 Källintegrationer till MagicBox (omkopplad Finfo-hämtning, BASTA-anslutning, BVB-vidareföring). 3.2 MagicBox-anslutning och distribution. 3.3 Snicken-adapter. 3.4 Medielagring, transformering och länkar (godkända transformationsprofiler, bevarade medielänkar) |
| Migrerad data | AP11, AP22 | 4.1 Beslutat migreringsurval (städad C4-data före uttag). 4.2 C4-export för migrering. 4.3 Migreringsmappning. 4.4 Migreringsverktyg. 4.5 Avstämningsprotokoll för prov- och korrigeringskörning. 4.6 Migrerat bestånd i produktion. 4.7 Migrerade äldre dokumentversioner. 4.8 Läsbar export av C4:s ändringslogg. 4.9 Slutexport från C4 före stängningen |
| Miljöer och drift | AP13 | 5.1 Testmiljö. 5.2 Produktionsmiljö. 5.3 Inloggning och tekniska identiteter. 5.4 Backup och återställningsprotokoll. 5.5 Övervakning och larm. 5.6 Felsökningsrutin. 5.7 Verifierad lösning för åtkomst vid PIM-avbrott |
| Test och acceptans | AP12 | 6.1 Testplan med kravspårning. 6.2 Integrationstestprotokoll. 6.3 Kapacitets- och samtidighetsrapport. 6.4 Avbrottstestprotokoll. 6.5 Acceptanstestprotokoll. 6.6 Acceptansbeslut |
| Driftsättning och överlämning | AP14 | 7.1 Växlingsplan. 7.2 Driftsatt F1 med växlingsprotokoll. 7.3 Överlämnat kodarkiv. 7.4 Data- och gränssnittsdokumentation. 7.5 Komponent- och tjänsteförteckning. 7.6 Användarhandledning. 7.7 Runbook och ansvarsfördelning. 7.8 Genomförda utbildningar. 7.9 Ärendelogg från stödperioden |
| Projektledning | AP15 | 8.1 Leveransplan. 8.2 Risk- och beslutslogg. 8.3 Ändringslogg. 8.4 Statusrapporter |

## Spårbarhet

Alla 63 krav har ett arbetspaket och en leverans. Kravkatalogen i svaret har en kolumn per krav med Vaimos leveranser.

| Paket | Krav | Vaimos leveranser |
|---|---|---|
| AP01 | PIM-I01, PIM-M01 | Återanvändningsmatris, gränssnittskontrakt, fältmatris, identitetsregler, gruppkontroll, Excel-format, icke-funktionella krav, arkitektur, export-, medie- och volyminventering, avbrotts- och driftverifiering, skillnader mot förstudien, reviderat estimat och plan |
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
