# SFB berikning och PIM: svar på förfrågan om estimat

Vaimo, utkast 2026-11-16. Omfattningsbas: kravspecifikation och kravkatalog version 1.3-V, 63 krav och 22 arbetspaket. Teknikstack: Medusa v2. Alla belopp i SEK exklusive moms.

## Sammanfattning

| Del | Timmar, bas | Kostnad, bas | Intervall |
|---|---|---|---|
| AP01 Teknisk precisering | 655 | 1,07 MSEK | 0,97 till 1,17 MSEK, tak 1,14 MSEK |
| F1 genomförande, AP02 till AP16 och AP22 | 1 990 | 3,12 MSEK | 2,3 till 4,7 MSEK |
| **F1 totalt inklusive AP01** | **2 640** | **4,20 MSEK** | |
| V2, AP17 till AP19 och automatisk webbstatus | 405 | 0,63 MSEK | 0,55 till 0,71 MSEK |
| Tillval, AP21 och mottagartjänst för tioårsarkivet | 105 | 0,17 MSEK | |
| ITM8:s paket AP07 till AP10, AP20 och ALT01 | | Saknas | Lämnas av ITM8 |

Grupperna summeras inte med varandra. Viktat timpris för F1 är cirka 1 590 SEK.

## Drift före C4:s stängning

Ja, för den delleverans SFB beslutade 2026-11-16. PIM tar emot källdata och levererar till MagicBox från 4 jan 2027. Hela F1 är i drift och överlämnad 8 mars 2027. ALT03 behövs därför inte, men kan estimeras på begäran. Förutsättningarna står i dokumentet om upplägget.

## AP01

Avgränsad leverans med eget pris, 17 nov till 30 dec 2026. Snickenkontraktet och verifieringen av åtkomst vid PIM-avbrott görs i januari. Alla sex leverabler i avsnitt 7.1 ingår, plus ett lasttest av Medusa med 1,4 miljoner artiklar före beslut om genomförandet. Förstudien (discoveryrapport v0.5 med bilagor) återanvänds, och bara återstående arbete estimeras. En återanvändningsmatris per leverabel lämnas första veckan. Resultatet kan lämnas till en annan partner. ITM8:s medverkan räknas bara i AP01.

## F1 per arbetspaket, Vaimos del

| Paket | Timmar | kSEK | Paket | Timmar | kSEK |
|---|---|---|---|---|---|
| AP02 Datamodell | 195 | 295 | AP11 Migrering, fast del och tre körningar | 200 | 310 |
| AP03 Gränssnitt och berikning | 255 | 385 | AP22 Äldre dokumentversioner | 65 | 100 |
| AP04 Integrationsgränssnitt | 105 | 160 | AP12 Test och acceptans | 230 | 350 |
| AP05 Bilder, dokument, versioner | 125 | 190 | AP13 Miljöer, drift, återställning | 135 | 210 |
| AP06 Excel | 105 | 155 | AP14 Driftsättning och överlämning | 190 | 320 |
| AP16 Tabellredigering | 85 | 130 | AP15 Projektledning | 295 | 500 |

AP10 innehåller 3 timmar samordning från Vaimo. Gemensamma regler räknas bara i AP03. Samma fil eller körning räknas inte i både AP11 och AP22. En extra migreringskörning kostar cirka 25 kSEK.

## Så har vi räknat

Trepunktsestimat per arbetsmoment och roll, kopplat till produkter och uppgifter i en produktnedbrytning per paket. Där Medusa ger färdiga delar, till exempel kategoriträd, jobbstatus, återförsök, sökning, inloggning och miljöer, är insatsen lägre. Regler, versioner, migrering, test och kontrakt är oförändrade. Medusa-riskerna ingår som riskreserv i AP02, AP03 och AP13. Bas är P50, intervallet P10 till P90. Estimatet är klass 4: gränssnitt, export och volymer är inte verifierade. Därför har F1 ett brett intervall, och estimatet görs om till klass 3 i AP01. Timpriser: affärskonsult, teknisk arkitekt och projektledare 1 700 SEK, utvecklare och testledare 1 500 SEK.

## Scenario: AI-assisterad utveckling

Vaimo utvecklar med AI-stöd. Bedömt avdrag är 30 % för utvecklare, 25 % för testledare, 15 % för affärskonsult och teknisk arkitekt, och inget för projektledning. Med det blir F1 totalt cirka 2 090 timmar och 3,34 MSEK, alltså 0,86 MSEK lägre. Vi prissätter grundestimatet tills avdraget är mätt mot utfallet i delleveransen. Avdraget påverkar arbetstid, inte kalendertid.

## Antaganden och avvikelser

- Antagandena B01 till B14 och de sex besluten B03, B04, B07, B09, B10 och B12 gäller utan avvikelse.
- Medusa klarar svarstidsmålen i B08 med full datamängd. Lasttestet i AP01 visar det, eller vilka anpassningar som krävs.
- ITM8 bygger Snicken-adaptern (AP09) och samordnar befintlig mediedrift (AP10). Håller inte det ökar Vaimos del.
- Volymberoende migrering (1,4 miljoner artiklar, 520 000 bilder, 118 000 dokument) och filöverföring per GB prissätts som enhetspris när volymerna är mätta i AP01.
- Återkommande kostnader (Azure-miljöer, lagring med tioårsarkiv, backup, övervakning, licens för tabellkomponent, support och uppgraderingar av Medusa) redovisas separat med volymantaganden efter AP01.
- SFB:s egen medverkan är cirka 125 timmar i F1 och ingår inte i priset.

## Kommersiellt

Löpande räkning med fakturering kopplad till godkända delleveranser: AP01, delleveransen 4 jan och F1 klar. AP01 har ett tak. Förbrukning av AI-verktyg i utvecklingen debiteras enligt faktisk förbrukning. SFB äger den kundspecifika koden. Medusa är öppen källkod med MIT-licens och kräver ingen licensavgift.
