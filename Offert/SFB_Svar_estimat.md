# SFB berikning och PIM: svar på förfrågan om estimat

Vaimo, utkast 2026-11-16. Omfattningsbas: kravspecifikation och kravkatalog version 1.3-V, 63 krav och 22 arbetspaket. Teknikstack: Medusa v2. Alla belopp i SEK exklusive moms.

## Sammanfattning

| Del | Timmar, bas | Kostnad, bas | Intervall |
|---|---|---|---|
| AP01 Teknisk precisering | 280 | 0,48 MSEK | 0,43 till 0,53 MSEK, tak 0,51 MSEK |
| F1 genomförande, AP02 till AP16 och AP22 | 740 | 1,26 MSEK | 0,94 till 1,88 MSEK |
| **F1 totalt inklusive AP01** | **1 020** | **1,74 MSEK** | |
| V2, AP17 till AP19 och automatisk webbstatus | 120 | 0,21 MSEK | 0,18 till 0,23 MSEK |
| Tillval, AP21 och mottagartjänst för tioårsarkivet | 30 | 0,05 MSEK | |
| ITM8:s paket AP07 till AP10, AP20 och ALT01 | | Saknas | Lämnas av ITM8 |

Grupperna summeras inte med varandra. Timpriset är 1 700 SEK för alla roller och paket. Bemanning för alla paket är Pontus Sundén med stöd av utvecklare, projektledare, teknisk arkitekt. Kalendertid och beläggning står i dokumentet om upplägget.

## Drift före C4:s stängning

Ja, för delleveransen på de villkor som anges i upplägget. PIM tar emot källdata och levererar till MagicBox från 4 jan 2027. Hela F1 är i drift i början av maj 2027 och klar efter stödperioden i mitten av maj. ALT03 behövs därför inte, men kan estimeras på begäran.

## AP01

Avgränsad leverans med eget pris, 17 nov 2026 till 26 jan 2027. Det som delleveransen kräver görs före jul och resten i januari. Alla sex leverabler i avsnitt 7.1 ingår, plus ett lasttest av Medusa med 1,4 miljoner artiklar före beslut om genomförandet. Förstudien (discoveryrapport v0.5 med bilagor) återanvänds, och bara återstående arbete estimeras. En återanvändningsmatris per leverabel lämnas första veckan och visar vad som är verifierat, vad som återstår och kvarvarande osäkerhet. Resultatet kan lämnas till en annan partner. ITM8:s medverkan räknas bara i AP01, och ITM8:s timmar lämnas av ITM8.

## F1 per arbetspaket, Vaimos del

| Paket | Timmar | Låg till hög | Timpris | kSEK | Kalendertid |
|---|---|---|---|---|---|
| AP02 Datamodell och grundstruktur | 61 | 52 till 70 | 1 700 | 103 | Dec 2026 och feb 2027 |
| AP03 Gränssnitt och berikning | 69 | 58 till 79 | 1 700 | 117 | Dec 2026 och feb 2027 |
| AP04 Integrationsgränssnitt | 29 | 22 till 37 | 1 700 | 50 | Dec 2026 och feb 2027 |
| AP05 Bilder, dokument, versioner | 31 | 25 till 37 | 1 700 | 53 | Feb 2027 |
| AP06 Excelimport och export | 26 | 20 till 32 | 1 700 | 45 | Feb 2027 |
| AP16 Tabellredigering | 26 | 20 till 33 | 1 700 | 45 | Feb 2027 |
| AP11 Migrering | 87 | 71 till 104 | 1 700 | 149 | Mars 2027, slutkörning i maj |
| AP22 Äldre dokumentversioner och historikexport | 22 | 16 till 28 | 1 700 | 37 | Mars 2027 |
| AP12 Gemensamt test och acceptans | 100 | 81 till 119 | 1 700 | 171 | Dec 2026 och april 2027 |
| AP13 Miljöer, drift, återställning | 43 | 35 till 51 | 1 700 | 73 | Dec 2026 och mars 2027 |
| AP14 Driftsättning, utbildning, överlämning | 95 | 77 till 112 | 1 700 | 161 | April till maj 2027 |
| AP15 Projektledning | 147 | 98 till 195 | 1 700 | 249 | Nov 2026 till maj 2027 |

AP10 innehåller 2 timmar samordning från Vaimo. Varje paket är sin egen kostnadsplats. Egen komponenttestning ligger i respektive paket, och sammanhängande test, acceptansstöd och omtest i AP12. Gemensamma regler räknas bara i AP03, och AP06 och AP16 använder dem. Samma fil eller körning räknas inte i både AP11 och AP22.

## Migrering

AP11 består av en fast del på 64 timmar och 109 kSEK (mappning, verktyg, avstämning och tre körningar: prov, korrigering och slut) och en volymberoende del på 23 timmar och 40 kSEK. Beräkningsvolymen är 1,4 miljoner artiklar, 22 442 produktgrupper, 519 781 bilder, 118 228 dokument och 1,2 TB filer. AP22 räknar med 100 000 äldre dokumentversioner. Volymerna mäts i AP01.

| Enhet | Pris |
|---|---|
| Per 100 000 artiklar | 1 800 SEK |
| Per 100 000 bild- eller dokumentfiler | 900 SEK |
| Per 100 000 äldre dokumentversioner (AP22) | 1 800 SEK |
| Per GB filöverföring | 5 SEK |
| Extra körning av hela beräkningsvolymen | 20 000 SEK | Om äldre dokumentversioner saknas tar AP01 fram en kostnadssatt åtkomstlösning före C4:s stängning. Eventuella avgifter från nuvarande part för export redovisas separat.

## Så har vi räknat

Trepunktsestimat per arbetsmoment och roll, kopplat till produkter och uppgifter i en produktnedbrytning per paket. Där Medusa ger färdiga delar är insatsen lägre. Arbetet görs med AI-stöd, och därför är utvecklingstiden minskad med 75 % och övrig tid med 50 %. Utan AI-stöd är F1 2 640 timmar och 4,49 MSEK. Avdraget följs upp mot utfallet i delleveransen. Medusa-riskerna ingår som riskreserv i AP02, AP03 och AP13. Bas är P50 och intervallet P10 till P90. Estimatet är klass 4 och görs om till klass 3 i AP01. Timpriset är 1 700 SEK för alla roller.

## Antaganden och avvikelser

- Antagandena B01 till B14 och de sex besluten B03, B04, B07, B09, B10 och B12 gäller utan avvikelse, inklusive driftmålen RPO en timme, RTO en arbetsdag och support under svensk kontorstid.
- Medusa klarar svarstidsmålen i B08 med full datamängd. Lasttestet i AP01 visar det, eller vilka anpassningar som krävs.
- ITM8 bygger Snicken-adaptern (AP09) och samordnar befintlig mediedrift (AP10). Håller inte det ökar Vaimos del.
- Underlag: kravspecifikationen och kravkatalogen 1.3-V, och förstudien som bakgrund. Förstudien föreslog Occtoo. Vi följer kravspecifikationen, och övriga motsägelser redovisas i AP01.
- SFB:s egen medverkan är cirka 20 timmar per vecka och ingår inte i priset.

## Test, stöd och överlämning

Dataförlust, obehörig åtkomst, utebliven central distribution och överskrivna interna värden blockerar driftstart. Felrättning och omtest ingår. Två utbildningar för två administratörer och tio dagars förstärkt stöd ingår i AP14. Stöd betyder svar på frågor och hjälp i arbetet. Incidenthantering betyder felsökning efter larm eller felanmälan inom supporttiden. Felrättning betyder rättning av fel i levererad kod. Överlämningen omfattar källkod med historik, tester, dokumentation, migreringsverktyg, konfiguration, återställningsrutin och felsökningshandledning.

## Tredjepart och återkommande kostnader

Medusa, PostgreSQL och Redis är öppen källkod utan licensavgift, och tabellkomponenten är öppen källkod i basen. Data och filer ligger i PostgreSQL och Azure Blob Storage och kan exporteras vid byte av partner. Ingen tjänst kräver fortsatt avtal med Vaimo.

| Återkommande kostnad | Per månad | Volymantagande |
|---|---|---|
| Azure i SFB:s tenant | Enligt Azures prislista | Test- och produktionsmiljö med Container Apps för Medusa och jobb, PostgreSQL Flexible Server (databas cirka 200 GB för 1,4 miljoner artiklar) och Redis. Blob Storage för originalfiler 1,2 TB, geo-redundant, med tioårsarkiv i svalare nivå och tillväxt cirka 10 % per år. Backup av databasen med återställning till valfri tidpunkt i 35 dagar och versionering av filer, skild från versionsarkivet. Application Insights och Log Analytics, cirka 10 GB loggar per månad med 90 dagars loggtid |
| Licenser och integrationer | 0 SEK | Öppen källkod. ITM8:s avgifter lämnas av ITM8 |
| Support från Vaimo | 13 600 SEK | 8 timmar per månad under svensk kontorstid, efter stödperioden |
| Uppgraderingar av Medusa | 4 500 SEK | Två uppgraderingar per år, provade i testmiljön |
| **Totalt från Vaimo** | **18 100 SEK** | Cirka 217 kSEK per år. Azure tillkommer |

Tillvalen tillkommer om de beställs: domäner och certifikat för AP20 cirka 2 000 SEK per år, och tjänst för förhandsvisning i AP21 cirka 1 000 SEK per månad.

## Ledtider i flödena

Förslag som fastställs när ändringslasten är mätt i AP01. En manuell ändring i PIM når MagicBox normalt inom 5 minuter och senast inom 1 timme. En källändring tas emot, bearbetas och levereras vidare normalt inom 15 minuter och senast inom 4 timmar vid toppar eller fulla källeveranser. Snickenleveranser går normalt inom 1 timme efter förändringen och senast inom 24 timmar. En full startleverans till Snicken tar högst ett dygn.

## Kommersiellt

Löpande räkning med fakturering kopplad till godkända delleveranser: AP01, delleveransen 4 jan och F1 klar. AP01 har ett tak. Kostnad för AI-verktyg debiteras enligt förbrukning, skilt från arbetstid. SFB äger den kundspecifika koden. Befintlig MagicBox-kod och tredjepartskomponenter ägs som i dag.
