# SFB berikning och PIM: upplägg för genomförandet

Vaimo, utkast 2026-11-16. Omfattningsbas: kravspecifikation och kravkatalog version 1.3-V.

## Mål

C4 ersätts i flödet Finfo, C4, MagicBox, Optimizely med en egen PIM-applikation, med så få ändringar i MagicBox som möjligt. Före C4:s stängning 2026-12-31 ska PIM ta emot källdata och leverera till MagicBox. Resten av F1 levereras under första kvartalet 2027.

## Faser

| Fas | Innehåll | Tid |
|---|---|---|
| AP01 Teknisk precisering | Verifierade kontrakt, fältmatris, identiteter, export- och medieinventering, arkitektur, reviderat estimat och plan | 17 nov till 30 dec 2026, Snickenkontrakt och avbrottsverifiering i januari |
| F1 delleverans | PIM tar emot källdata och skickar vidare till MagicBox. Ingen migrering | I drift 4 jan 2027 |
| F1 resten | Gränssnitt, Excel, medier, migrering, Snicken, test, överlämning | Klar 8 mars 2027, inklusive tio dagars stöd |
| V2 och tillval | AP17 till AP19, automatisk webbstatus, AP20, AP21, arkivtjänst | 22 feb till 19 mars 2027, efter beslut |

## Före årsskiftet

AP01 och delleveransen körs parallellt. AP01 levererar det som bygget behöver först, så att utvecklingen kan starta i början av december.

| Vecka | AP01 | Bygge och drift |
|---|---|---|
| 47 (17 nov) | Startmöte med SFB och ITM8. Återanvändningsmatris för förstudien. Låst startlista för egna egenskaper | |
| 48 | Exportinventering, medieinventering, volym och last, drift och identitet. Identitetsregler och kontroll av produktgrupper. Motsägelser mot förstudien | Beställ C4-historik och ändringslogg från nuvarande part (24 nov) |
| 49 | Fältmatris, icke-funktionella krav, transport- och felkontrakt, arkitektur och säkerhet. Beslutsunderlag till SFB sponsor (1 dec) | Migreringsurval beslutat (2 dec). Testmiljö i Azure |
| 50 | Kontrakt MagicBox till PIM och PIM till MagicBox granskade med ITM8 (11 dec). Fast Excel-mall | Datamodell, inloggning, produktionsmiljö |
| 51 | Validerade kontraktsexempel. Samlat gränssnittskontrakt godkänt (21 dec) | Gemensamma fält- och valideringsregler. ITM8:s källintegrationer klara |
| 52 | Reviderat estimat och plan till SFB sponsor | Komplett slutexport från C4 (22 dec), avstämd 23 dec |
| 53 | AP01 godkänd (30 dec) | Källmottagning och utgående flöde testade. Integrationstest 28 till 30 dec |
| 1 (4 jan) | | Delleveransen i drift |

## Beslutade villkor för delleveransen (2026-11-16)

- MagicBox behåller senaste kategori och webbstatus från C4 tills migreringen är klar. PIM skickar inga tomma värden för dem.
- Snicken får inga uppdateringar från 31 dec tills Snicken-adaptern är klar, och får då en full startleverans.
- Medielagringen och media.woody.se ligger kvar efter C4:s stängning. Det bekräftas i AP01.
- Egen berikning säkras genom en slutexport före stängningen och migreras efteråt.
- ITM8 är driftägare och godkänner miljöer, övervakning och runbook.

## Teknik

Symfony med API Platform för API:et mot MagicBox och Messenger för jobb. PostgreSQL Flexible Server, Blob Storage och Container Apps i SFB:s Azure-tenant. Ett separat grid för tabellredigering. SFB äger den kundspecifika koden, och allt kan lämnas över till en annan partner.

## Det här behöver vi från SFB och andra parter före jul

- Namngiven produktägare och sponsor med tid för granskning varje vecka, cirka 130 timmar totalt i F1.
- Beslut om migreringsurval senast 2 dec och städning av C4-data senast 4 dec.
- C4-export, historik och slutexport från nuvarande part enligt datumen ovan.
- ITM8: kontraktsgenomgångar vecka 50, källintegrationer och MagicBox-sidan klara till 28 dec, miljögodkännanden.
- Beställning av AP01 senast 17 nov för att hålla 4 jan.

## Största riskerna

C4-exporten avviker eller har luckor. Volymen kräver mer av plattformen än antaget. ITM8 eller SFB hinner inte granska under december. Alla tre hanteras tidigt i AP01, med exportprov och lasttest före beslut om genomförandeestimatet.
