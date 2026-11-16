# SFB berikning och PIM: upplägg för genomförandet

Vaimo, utkast 2026-11-16. Omfattningsbas: kravspecifikation och kravkatalog version 1.3-V.

## Mål

C4 ersätts i flödet Finfo, C4, MagicBox, Optimizely med en PIM-applikation byggd på Medusa v2, med så få ändringar i MagicBox som möjligt. Före C4:s stängning 2026-12-31 ska PIM ta emot källdata och leverera till MagicBox. Resten av F1 levereras under första kvartalet 2027.

## Faser

| Fas | Innehåll | Tid |
|---|---|---|
| AP01 Teknisk precisering | Verifierade kontrakt, fältmatris, identiteter, export- och medieinventering, arkitektur med lasttest av Medusa, reviderat estimat och plan | 17 nov till 30 dec 2026, Snickenkontrakt och avbrottsverifiering i januari |
| F1 delleverans | PIM tar emot källdata och skickar vidare till MagicBox. Ingen migrering | I drift 4 jan 2027 |
| F1 resten | Gränssnitt, Excel, medier, migrering, Snicken, test, överlämning | Klar 8 mars 2027, inklusive tio dagars stöd |
| V2 och tillval | AP17 till AP19, automatisk webbstatus, AP20, AP21, arkivtjänst | 22 feb till 19 mars 2027, efter beslut |

## Före årsskiftet

AP01 och delleveransen körs parallellt. AP01 levererar det som bygget behöver först, så att utvecklingen kan starta i början av december.

| Vecka | Arbete i AP01 | Bygge och drift |
|---|---|---|
| 47 (17 nov) | Startmöte med SFB och ITM8. Återanvändningsmatris för förstudien. Låst startlista för egna egenskaper | |
| 48 | Export-, medie- och volyminventering, drift och identitet. Identitetsregler, kontroll av produktgrupper, motsägelser mot förstudien | Beställ C4-historik och ändringslogg från nuvarande part (24 nov) |
| 49 | Lasttest av Medusa med 1,4 miljoner artiklar (1 till 3 dec). Fältmatris, icke-funktionella krav, transport- och felkontrakt. Beslutsunderlag till SFB sponsor (1 dec) | Migreringsurval beslutat (2 dec). Städad C4-data (4 dec) |
| 50 | Arkitektur och säkerhet godkänd (7 dec). Kontrakt mellan MagicBox och PIM granskade med ITM8 (11 dec). Fast Excel-mall | Test- och produktionsmiljö, inloggning |
| 51 | Validerade kontraktsexempel. Samlat gränssnittskontrakt godkänt (21 dec) | Datamodell (16 dec). Gemensamma fält- och valideringsregler. ITM8:s källintegrationer |
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

Medusa v2 med Node.js, TypeScript, PostgreSQL och Redis, driftat i SFB:s Azure-tenant. Medusa ger ramverket för administratörsgränssnittet, inloggning och användare, filhantering, kategoriträd, workflows med återförsök, händelser, schemalagda jobb och sökning. Artiklar med käll- och egna värden, dokumentversioner, Excelregler och migrering byggs som egna moduler, och gränssnittet som tillägg till Medusa Admin. SFB äger den kundspecifika koden, och allt kan lämnas över till en annan partner.

## Det här behöver vi från SFB och andra parter före jul

- Namngiven produktägare och sponsor med tid för granskning varje vecka, cirka 125 timmar totalt i F1.
- Beslut om migreringsurval senast 2 dec och städning av C4-data senast 4 dec.
- C4-export, historik och slutexport från nuvarande part enligt datumen ovan.
- ITM8: kontraktsgenomgångar vecka 50, källintegrationer och MagicBox-sidan klara till 28 dec, miljögodkännanden.
- Beställning av AP01 senast 17 nov för att hålla 4 jan.

## Största riskerna

Medusa är byggt för e-handel, inte för en katalog med 1,4 miljoner artiklar. Därför lastprovas det i AP01 innan datamodellen byggs. C4-exporten kan avvika eller ha luckor. ITM8 eller SFB kanske inte hinner granska under december. Alla tre hanteras tidigt i AP01, med lasttest och exportprov före beslut om genomförandeestimatet.
