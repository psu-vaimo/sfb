# SFB berikning och PIM: upplägg för genomförandet

Vaimo, utkast 2026-11-16. Omfattningsbas: kravspecifikation och kravkatalog version 1.3-V. Priserna står i Svar på förfrågan om estimat och hela planen per part i Gemensam tidplan och spårbarhet.

## Mål

C4 ersätts i flödet Finfo, C4, MagicBox, Optimizely med en PIM-applikation byggd på Medusa v2, med så få ändringar i MagicBox som möjligt. Från 18 dec 2026, före C4:s stängning 31 dec, ska PIM ta emot källdata och leverera till MagicBox. Resten av F1 levereras under våren 2027.

## Bemanning

Vaimo bemannar med Pontus Sundén med stöd av utvecklare, projektledare, teknisk arkitekt. Arbetet görs med AI-stöd. Till 18 dec är beläggningen cirka 70 timmar per vecka: Pontus cirka 45 och stödrollerna cirka 25. 21 dec till 6 jan är ledigt, utom tillsyn av delleveransen 28 till 30 dec. Från 7 jan är beläggningen cirka 35 timmar per vecka utöver projektledningen. SFB:s medverkan är cirka 20 timmar per vecka under hela genomförandet, fördelat på produktägare, sponsor och de två administratörerna. Den ökar under migreringsurval, datastädning och acceptanstest.

## Faser

| Fas | Innehåll | Tid |
|---|---|---|
| AP01 Teknisk precisering | Verifierade kontrakt, fältmatris, identiteter, export- och medieinventering, arkitektur, reviderat estimat och plan | 17 nov 2026 till 18 jan 2027. Avbrottsverifiering i februari |
| F1 delleverans | PIM tar emot källdata och skickar vidare till MagicBox. Ingen migrering | I drift 18 dec 2026 |
| F1 resten | Gränssnitt, Excel, medier, migrering, Snicken, test, överlämning | Januari till april 2027. Driftstart 12 apr, klar efter tio dagars stöd 26 apr |
| V2 och tillval | AP17 till AP19, automatisk webbstatus, AP20, AP21, arkivtjänst | April till maj 2027, efter beslut |

## Före årsskiftet

Sista arbetsdag före jul är 18 dec. Fram till dess görs bara det som delleveransen kräver, cirka 290 timmar på 24 arbetsdagar. Övriga delar av AP01 görs i januari.

| Vecka | Precisering i AP01 | Bygge och drift |
|---|---|---|
| 47 (17 nov) | Startmöte med SFB och ITM8. Genomgång av återanvändningen av förstudien. Startlista för egna egenskaper och skyddade fält godkända (19 nov) | Nuvarande part levererar historik och ändringslogg (19 till 23 nov) |
| 48 | Export-, medie- och volyminventering, drift och identitet (23 till 27 nov). Identitetsregler (25 nov). Fältmatris och icke-funktionella krav (30 nov) | |
| 49 | Kontrakten mellan MagicBox och PIM godkända med ITM8 (3 dec) | ITM8 bygger källintegrationer och MagicBox-sidan (2 till 8 dec). Test- och produktionsmiljö |
| 50 | Arkitektur och säkerhet godkänd (7 dec). Fel- och transportkontrakt (8 dec) | Datamodell (11 dec). ITM8 verifierar ERP-matchningen (9 till 11 dec). Frys av berikning i C4 11 dec. Slutexport från C4 12 dec |
| 51 | Kontraktsexempel validerade (17 dec) | Slutexporten avstämd med SFB (14 dec). Gemensamma fält- och valideringsregler (16 dec). Miljöer godkända av ITM8 (16 dec). Integrationstest med ITM8 17 dec. Delleveransen i drift 18 dec |
| 52 till 53 | | Ledigt. Vaimo har tillsyn av delleveransen 28 till 30 dec. C4 stängs 31 dec |

I januari, från 7 jan: kontrakt MagicBox till PIM, fel och transport och Snicken, validerade kontraktsexempel, fast Excel-mall, äldre dokumentversioner, underlag för migreringsurval, verifiering av åtkomst vid PIM-avbrott, motsägelser mot förstudien, och reviderat estimat och plan. Snickenkontraktet godkänns 20 jan och verifieringen av åtkomst vid PIM-avbrott 18 feb. AP01 är klar 18 jan.

## Villkor för delleveransen

- Berikningen i C4 fryses från 11 dec, och slutexporten tas 12 dec med allt som berikats fram till dess. MagicBox växlar till PIM 18 dec.
- MagicBox behåller senaste kategori och webbstatus från C4 tills migreringen är klar. PIM skickar inga tomma värden för dem.
- Snicken får inga uppdateringar från 18 dec tills Snicken-adaptern är klar, och får då en full startleverans.
- Medielagringen och media.woody.se ligger kvar efter C4:s stängning. Det bekräftas i AP01.
- Egen berikning säkras genom en slutexport före stängningen och migreras efteråt.
- ITM8 är driftägare och godkänner miljöer, övervakning och runbook.

## Teknik

Medusa v2 med Node.js, TypeScript, PostgreSQL och Redis, driftat i SFB:s Azure-tenant. Medusa ger ramverket för administratörsgränssnittet, inloggning och användare, filhantering, kategoriträd, workflows med återförsök, händelser, schemalagda jobb och sökning. Artiklar med käll- och egna värden, dokumentversioner, Excelregler och migrering byggs som egna moduler, och gränssnittet som tillägg till Medusa Admin i React med Medusas komponentbibliotek. Tabellredigeringen byggs med en gridkomponent med öppen källkod. SFB äger den kundspecifika koden, och allt kan lämnas över till en annan partner.

## Senaste datum

- Beställning av AP01: 17 nov.
- C4-historik och ändringslogg från nuvarande part: 24 nov. Frys av berikning i C4: 11 dec. Komplett slutexport: 12 dec.
- SFB:s och ITM8:s godkännande av kontrakten mellan MagicBox och PIM 3 dec och SFB:s godkännande av arkitekturen 7 dec.
- ITM8: källintegrationer och MagicBox-sidan byggda 8 dec och ERP-matchningen verifierad 11 dec, före integrationstestet 17 dec.
- Migreringsurval 13 jan och datastädning 21 jan.
- Beslut om genomförandet av resten av F1: efter AP01, 18 jan.

## Efter årsskiftet

Excel och tabellredigering i januari och februari, gränssnitt och medier klara i mars. Migreringsverktyg i februari, prov- och korrigeringskörning avstämda 24 feb och äldre dokumentversioner 12 mars. Integrationstest och acceptanstest 15 till 25 mars. Slutkörning och driftsättning 31 mars till 12 apr, utbildning 13 till 14 apr och stöd till 23 apr. Testfönster och beslutspunkter per part står i Gemensam tidplan och spårbarhet.

## Största riskerna

C4-exporten kan avvika eller ha luckor. December är kort, och ITM8 och SFB behöver granska och testa före 18 dec. Båda hanteras tidigt i AP01, med exportprov och bokade tider för granskning och test.
