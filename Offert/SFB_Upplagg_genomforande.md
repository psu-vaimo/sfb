# SFB berikning och PIM: upplägg för genomförandet

Vaimo, utkast 2026-11-16. Omfattningsbas: kravspecifikation och kravkatalog version 1.3-V. Priserna står i Svar på förfrågan om estimat och hela planen per part i Gemensam tidplan och spårbarhet.

## Mål

C4 ersätts i flödet Finfo, C4, MagicBox, Optimizely med en PIM-applikation byggd på Medusa v2, med så få ändringar i MagicBox som möjligt. Före C4:s stängning 2026-12-31 ska PIM ta emot källdata och leverera till MagicBox. Resten av F1 levereras under våren 2027.

## Bemanning

Vaimo bemannar med Pontus Sundén med stöd av utvecklare, projektledare, teknisk arkitekt. Arbetet görs med AI-stöd. Beläggningen är cirka 45 timmar per vecka till 30 dec och därefter heltid. SFB:s medverkan är cirka 20 timmar per vecka under hela genomförandet, fördelat på produktägare, sponsor och de två administratörerna. Den ökar under migreringsurval, datastädning och acceptanstest.

## Faser

| Fas | Innehåll | Tid |
|---|---|---|
| AP01 Teknisk precisering | Verifierade kontrakt, fältmatris, identiteter, export- och medieinventering, arkitektur med lasttest av Medusa, reviderat estimat och plan | 17 nov 2026 till 26 jan 2027 |
| F1 delleverans | PIM tar emot källdata och skickar vidare till MagicBox. Ingen migrering | I drift 4 jan 2027 |
| F1 resten | Gränssnitt, Excel, medier, migrering, Snicken, test, överlämning | Februari till maj 2027. Driftstart i början av maj, klar efter tio dagars stöd i mitten av maj |
| V2 och tillval | AP17 till AP19, automatisk webbstatus, AP20, AP21, arkivtjänst | Juni 2027, efter beslut |

## Före årsskiftet

Före jul görs bara det som delleveransen kräver, cirka 290 timmar. Övriga delar av AP01 görs i januari.

| Vecka | Precisering i AP01 | Bygge och drift |
|---|---|---|
| 47 (17 nov) | Startmöte med SFB och ITM8. Genomgång av återanvändningen av förstudien. Låst startlista för egna egenskaper och skyddade fält | |
| 48 | Export-, medie- och volyminventering, drift och identitet. Identitetsregler och kontroll av produktgrupper | Beställ C4-historik och ändringslogg från nuvarande part (24 nov) |
| 49 | Lasttest av Medusa med 1,4 miljoner artiklar (1 till 3 dec). Fältmatris och icke-funktionella krav | |
| 50 | Arkitektur och säkerhet godkänd (7 dec). Kontrakt PIM till MagicBox granskat med ITM8 (11 dec) | Test- och produktionsmiljö, inloggning och tekniska identiteter |
| 51 | | Datamodell (16 dec). Gemensamma fält- och valideringsregler (21 dec). ITM8:s källintegrationer |
| 52 | | Komplett slutexport från C4 (22 dec), avstämd 23 dec. Utgående flöde testat |
| 53 | | Källmottagning. Integrationstest med ITM8 28 till 30 dec |
| 1 (4 jan) | | Delleveransen i drift |

I januari: kontrakt MagicBox till PIM, fel och transport och Snicken, validerade kontraktsexempel, fast Excel-mall, äldre dokumentversioner, underlag för migreringsurval, verifiering av åtkomst vid PIM-avbrott, motsägelser mot förstudien, och reviderat estimat och plan. AP01 är klar 26 jan.

## Villkor för delleveransen

- MagicBox behåller senaste kategori och webbstatus från C4 tills migreringen är klar. PIM skickar inga tomma värden för dem.
- Snicken får inga uppdateringar från 31 dec tills Snicken-adaptern är klar, och får då en full startleverans.
- Medielagringen och media.woody.se ligger kvar efter C4:s stängning. Det bekräftas i AP01.
- Egen berikning säkras genom en slutexport före stängningen och migreras efteråt.
- ITM8 är driftägare och godkänner miljöer, övervakning och runbook.

## Teknik

Medusa v2 med Node.js, TypeScript, PostgreSQL och Redis, driftat i SFB:s Azure-tenant. Medusa ger ramverket för administratörsgränssnittet, inloggning och användare, filhantering, kategoriträd, workflows med återförsök, händelser, schemalagda jobb och sökning. Artiklar med käll- och egna värden, dokumentversioner, Excelregler och migrering byggs som egna moduler, och gränssnittet som tillägg till Medusa Admin. SFB äger den kundspecifika koden, och allt kan lämnas över till en annan partner.

## Senaste datum

- Beställning av AP01: 17 nov.
- C4-historik och ändringslogg från nuvarande part: 24 nov. Komplett slutexport: 22 dec.
- SFB:s godkännande av arkitektur 7 dec och av kontraktet PIM till MagicBox 11 dec.
- ITM8: källintegrationer och MagicBox-sidan klara till integrationstestet 28 dec.
- Migreringsurval och datastädning: januari, före migreringsverktyget.
- Beslut om genomförandet av resten av F1: efter AP01, 26 jan.

## Efter årsskiftet

Gränssnitt, Excel, tabellredigering och medier i februari. Migrering och dokumentversioner i mars. Acceptanstest med SFB:s administratörer, ITM8 och Snicken i april. Slutkörning, driftsättning och utbildning i maj. Testfönster och beslutspunkter per part står i Gemensam tidplan och spårbarhet.

## Största riskerna

Medusa lastprovas med 1,4 miljoner artiklar i AP01 innan datamodellen byggs. C4-exporten kan avvika eller ha luckor. ITM8 eller SFB kanske inte hinner granska under december. Alla tre hanteras tidigt i AP01, med lasttest och exportprov före beslut om genomförandet.
