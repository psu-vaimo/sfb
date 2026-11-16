# SFB berikning och PIM: svar på förfrågan om estimat

Vaimo, utkast 2026-11-16. Omfattningsbas: kravspecifikation och kravkatalog version 1.3-V, 63 krav och 22 arbetspaket. Teknikstack: Medusa v2. Alla belopp i SEK exklusive moms.

## Sammanfattning

| Del | Timmar, bas | Kostnad, bas | Intervall |
|---|---|---|---|
| AP01 Teknisk precisering | 280 | 0,47 MSEK | 0,42 till 0,52 MSEK, tak 0,50 MSEK |
| F1 genomförande, AP02 till AP16 och AP22 | 715 | 1,14 MSEK | 0,86 till 1,71 MSEK |
| **F1 totalt inklusive AP01** | **1 000** | **1,61 MSEK** | |
| V2, AP17 till AP19 och automatisk webbstatus | 120 | 0,19 MSEK | 0,17 till 0,22 MSEK |
| Tillval, AP21 och mottagartjänst för tioårsarkivet | 30 | 0,05 MSEK | |
| ITM8:s paket AP07 till AP10, AP20 och ALT01 | | Saknas | Lämnas av ITM8 |

Grupperna summeras inte med varandra. Viktat timpris för F1 är cirka 1 620 SEK. Bemanning för alla paket är Pontus Sundén. Kalendertid och beläggning står i dokumentet om upplägget.

## Drift före C4:s stängning

Ja, för delleveransen på de villkor som anges i upplägget. PIM tar emot källdata och levererar till MagicBox från 4 jan 2027. Hela F1 är i drift och överlämnad i mitten av maj 2027. ALT03 behövs därför inte, men kan estimeras på begäran.

## AP01

Avgränsad leverans med eget pris, 17 nov 2026 till 22 jan 2027. Det som delleveransen kräver görs före jul och resten i januari. Alla sex leverabler i avsnitt 7.1 ingår, plus ett lasttest av Medusa med 1,4 miljoner artiklar före beslut om genomförandet. Förstudien (discoveryrapport v0.5 med bilagor) återanvänds, och bara återstående arbete estimeras. En återanvändningsmatris per leverabel lämnas första veckan och visar vad som är verifierat, vad som återstår och kvarvarande osäkerhet. Resultatet kan lämnas till en annan partner. ITM8:s medverkan räknas bara i AP01, och ITM8:s timmar lämnas av ITM8.

## F1 per arbetspaket, Vaimos del

| Paket | Timmar | Låg till hög | Timpris | kSEK |
|---|---|---|---|---|
| AP02 Datamodell och grundstruktur | 61 | 52 till 70 | 1 544 | 94 |
| AP03 Gränssnitt och berikning | 69 | 58 till 79 | 1 533 | 105 |
| AP04 Integrationsgränssnitt | 29 | 22 till 37 | 1 548 | 46 |
| AP05 Bilder, dokument, versioner | 31 | 25 till 37 | 1 500 | 47 |
| AP06 Excelimport och export | 26 | 20 till 32 | 1 500 | 39 |
| AP16 Tabellredigering | 26 | 20 till 33 | 1 578 | 42 |
| AP11 Migrering, fast del och tre körningar | 64 | 52 till 76 | 1 586 | 101 |
| AP22 Äldre dokumentversioner och historikexport | 21 | 15 till 27 | 1 583 | 33 |
| AP12 Gemensamt test och acceptans | 100 | 81 till 119 | 1 517 | 152 |
| AP13 Miljöer, drift, återställning | 43 | 35 till 51 | 1 585 | 68 |
| AP14 Driftsättning, utbildning, överlämning | 95 | 77 till 112 | 1 693 | 160 |
| AP15 Projektledning | 147 | 98 till 195 | 1 700 | 249 |

AP10 innehåller 2 timmar samordning från Vaimo. Varje paket är sin egen kostnadsplats. Egen komponenttestning ligger i respektive paket, och sammanhängande test, acceptansstöd och omtest i AP12. Gemensamma regler räknas bara i AP03, och AP06 och AP16 använder dem. Samma fil eller körning räknas inte i både AP11 och AP22.

## Migrering

Fast del: mappning, verktyg, avstämning och tre körningar (prov, korrigering och slut). En extra körning kostar cirka 6 kSEK. Pris per 100 000 artiklar eller filer och per GB filöverföring lämnas efter exportprovet i AP01, när bytevolymen är mätt. Beräkningsvolymen är 1,4 miljoner artiklar, 22 442 produktgrupper, 519 781 bilder och 118 228 dokument. Om äldre dokumentversioner saknas tar AP01 fram en kostnadssatt åtkomstlösning före C4:s stängning. Eventuella avgifter från nuvarande part för export redovisas separat.

## Så har vi räknat

Trepunktsestimat per arbetsmoment och roll, kopplat till produkter och uppgifter i en produktnedbrytning per paket. Där Medusa ger färdiga delar är insatsen lägre. Pontus gör allt arbete med AI-stöd, och därför är utvecklingstiden minskad med 75 % och övrig tid med 50 %. Utan AI-stöd är F1 2 640 timmar och 4,20 MSEK. Avdraget följs upp mot utfallet i delleveransen. Medusa-riskerna ingår som riskreserv i AP02, AP03 och AP13. Bas är P50 och intervallet P10 till P90. Estimatet är klass 4 och görs om till klass 3 i AP01. Timpriser: affärskonsult, teknisk arkitekt och projektledare 1 700 SEK, utvecklare och testledare 1 500 SEK.

## Antaganden och avvikelser

- Antagandena B01 till B14 och de sex besluten B03, B04, B07, B09, B10 och B12 gäller utan avvikelse, inklusive driftmålen RPO en timme, RTO en arbetsdag och support under svensk kontorstid.
- Medusa klarar svarstidsmålen i B08 med full datamängd. Lasttestet i AP01 visar det, eller vilka anpassningar som krävs.
- ITM8 bygger Snicken-adaptern (AP09) och samordnar befintlig mediedrift (AP10). Håller inte det ökar Vaimos del.
- Underlag: kravspecifikationen och kravkatalogen 1.3-V, och förstudien som bakgrund. Förstudien föreslog Occtoo. Vi följer kravspecifikationen, och övriga motsägelser redovisas i AP01.
- SFB:s egen medverkan är cirka 125 timmar i F1 och ingår inte i priset.

## Test, stöd och överlämning

Dataförlust, obehörig åtkomst, utebliven central distribution och överskrivna interna värden blockerar driftstart. Felrättning och omtest ingår. Två utbildningar för två administratörer och tio dagars förstärkt stöd ingår i AP14. Stöd betyder svar på frågor och hjälp i arbetet. Incidenthantering betyder felsökning efter larm eller felanmälan inom supporttiden. Felrättning betyder rättning av fel i levererad kod. Överlämningen omfattar källkod med historik, tester, dokumentation, migreringsverktyg, konfiguration, återställningsrutin och felsökningshandledning.

## Tredjepart och återkommande kostnader

Medusa, PostgreSQL och Redis är öppen källkod utan licensavgift. Komponenten för tabellredigering väljs i AP01, med eventuell licens. Data och filer ligger i PostgreSQL och Azure Blob Storage och kan exporteras vid byte av partner. Ingen tjänst kräver fortsatt avtal med Vaimo. Återkommande kostnader för miljöer, lagring med tioårsarkiv, backup, övervakning, licenser, integrationer, support och uppgraderingar av Medusa redovisas separat med volymantaganden efter mätningen i AP01.

## Kommersiellt

Löpande räkning med fakturering kopplad till godkända delleveranser: AP01, delleveransen 4 jan och F1 klar. AP01 har ett tak. Kostnad för AI-verktyg debiteras enligt förbrukning, skilt från arbetstid. SFB äger den kundspecifika koden. Befintlig MagicBox-kod och tredjepartskomponenter ägs som i dag.
