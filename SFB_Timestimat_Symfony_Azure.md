# Timestimat: Symfony på Azure med AI-stöd

Grovt utkast för intern diskussion. Siffrorna är en första bedömning utifrån kravspecifikationen version 1.3-V, inte en verifierad kalkyl. De ska stämmas av med utvecklare och arkitekt.

---

## Teknik

| Del | Val |
|---|---|
| Ramverk | Symfony (PHP), med Symfony Messenger för bakgrundsjobb |
| Körmiljö | Azure Container Apps, en container för webben och en för bakgrundsjobb |
| Databas | Azure Database for PostgreSQL. Attribut lagras som data, inte som kolumner |
| Sök | PostgreSQL. Separat sökmotor bara om mätningar visar att det behövs |
| Filer och tioårsarkiv | Azure Blob Storage med skydd mot ändring och radering |
| Inloggning | Microsoft Entra ID |
| Hemligheter | Azure Key Vault |
| Övervakning | Application Insights via OpenTelemetry |
| Infrastruktur | Beskrivs som kod (Bicep eller Terraform), samma uppsättning för test och produktion |
| Tabellkomponent | Färdig komponent, eventuell licens redovisas separat |

**AI-stöd:** utvecklarna använder AI-verktyg för kod, tester och dokumentation. All kod granskas och täcks av automatiska tester. Besparingen är störst när man bygger ny kod och minst för det som beror på andra parter eller på data.

---

## Reglerna: varför de är det svåra

Varje regel nedan är liten för sig. Svårigheten är att de påverkar varandra, att de måste fungera exakt likadant i alla sätt att ändra data (artikelsida, tabell, Excel, källimport) och i det som skickas ut, och att ett fel ofta syns först när data redan har gått förlorad. Dataförlust och överskrivna egna värden stoppar driftstart enligt kravspecen.

| Område | Regeln | Det som gör den svår |
|---|---|---|
| **Källvärde och eget värde** | Källans värde och SFB:s eget värde sparas var för sig. Det egna används om det finns, annars källans. Gäller namn, text och sju egenskaper | Effektivt värde räknas ut på ett ställe men används överallt. Bara blanksteg räknas som tomt. Fyra källtexter slås ihop till en, utan tomma stycken. Ett eget värde 0 är ett värde, inte en rensning |
| **Notiser** | När källan ändrar något som SFB har ett eget värde för skapas en notis med före och efter | En oförändrad omsändning ska inte ge notis. En kvitterad notis ska ge ny notis vid nästa ändring. Samma sak för bilder som dolts från webben |
| **Skyddade fält** | Källans fält, identifierare och externa bedömningar får inte ändras manuellt | Skyddet måste gälla i artikelsidan, tabellen och Excel. Fältmatrisen styr vilka fält som är skyddade, och den kan ändras över tid |
| **Excel** | Tom cell betyder oförändrat. Rensning kräver en särskild markering | En gammal Excel-fil får inte skriva över nyare ändringar. Giltiga rader ska kunna sparas fast andra rader har fel. En omkörning får inte skapa dubbletter |
| **Samtidig redigering** | Två administratörer arbetar samtidigt | Konflikter ska upptäckas per fält och visas, inte lösas genom att den som sparar sist vinner |
| **Matchning** | Källdata kopplas till rätt artikel via källans nyckel, inte GTIN | Samma GTIN finns hos flera leverantörer. Tvetydiga träffar ska till en felkö. Manuella artiklar får aldrig kopplas ihop automatiskt med källdata |
| **Källprioritet** | Finfo, BASTA och BVB kan ha olika värden för samma fält | Prioritet bestäms per fält. Senast inkommet värde får inte vinna automatiskt |
| **Produktgrupper** | Artikel i högst en variantgrupp men flera bundles. Gruppens värden hålls skilda från artikelns | En ändring på gruppen ska markera alla berörda artiklar som ändrade i flödet ut |
| **Dokumentversioner** | Nytt innehåll ger ny version som aldrig ändras. Sparas i tio år från att den ersätts | Ändrat innehåll bakom samma länk ska upptäckas via innehållets fingeravtryck. Samma fil skickad igen ska inte bli en ny version. Ny version ärver webbexkludering. Färgkarta och Produktkatalog undantas |
| **Flödet ut** | Allt som ändras skickas till MagicBox och rätt urval till Snicken | Saknat fält, tomt värde, rensning, ändrad livscykelstatus och borttagen relation måste gå att skilja åt. Egna värden får inte komma tillbaka som källvärden och skapa en evig loop. Snicken har egen position i flödet och ska få besked när en artikel lämnar urvalet |
| **Status** | Webbstatus, livscykelstatus och arkivering är tre olika saker | Inaktiv artikel ska ändå skickas ut. Utgångsdatum ändrar ingenting automatiskt |

**Följden för arkitekturen:** reglerna ska ligga samlade i en kärna som alla delar använder (artikelsida, tabell, Excel, import, flöde ut). De ska ha många automatiska tester. Det är därför ett ramverk med tydlig struktur, som Symfony, passar bättre än ett där det är lätt att lägga logik lite här och där.

---

## F1: timmar per paket

| Paket | Innehåll | Låg | Normal | Hög | Kommentar |
|---|---|---:|---:|---:|---|
| AP01 | Teknisk förstudie, inklusive Azure-arkitektur | 160 | 220 | 300 | AI-stöd påverkar lite, mest samordning och analys |
| AP02 | Datamodell och grundplattform | 130 | 190 | 280 | |
| AP03 | Gränssnitt, berikning och regelkärnan | 470 | 660 | 950 | Största paketet. Regelkärnan och testerna av den ligger här |
| AP16 | Tabellredigering | 160 | 240 | 360 | |
| AP06 | Excel | 120 | 180 | 270 | Använder regelkärnan från AP03 |
| AP04 | Integrationsgränssnitt | 290 | 410 | 620 | PHP-stödet för Azure Service Bus är svagt, kan kräva REST i stället |
| AP05 | Bilder, dokument och versioner | 190 | 290 | 430 | Blob Storage skyddar versioner mot ändring, det förenklar |
| AP11 | Migrering | 260 | 390 | 610 | Beror mest på C4-exporten |
| AP22 | Gamla dokumentversioner | 80 | 160 | 320 | Oförändrat, helt beroende av vad som finns i C4 |
| AP12 | Test och acceptans | 280 | 420 | 620 | |
| AP13 | Miljöer, drift, återställning, inloggning via Entra ID | 160 | 240 | 340 | Inloggning via Entra ID ingår |
| AP14 | Driftsättning och överlämning | 160 | 220 | 300 | |
| **Delsumma** | | **2 460** | **3 620** | **5 400** | |
| AP15 | Projektledning, ca 12 % | 300 | 430 | 650 | |
| **Totalt F1** | | **2 760** | **4 050** | **6 050** | |

---

## Jämförelse

| Alternativ | Låg | Normal | Hög |
|---|---:|---:|---:|
| Egenutveckling utan AI-stöd | 3 210 | 4 740 | 6 970 |
| Akeneo CE | 2 830 | 4 230 | 6 410 |
| **Symfony på Azure med AI-stöd** | **2 760** | **4 050** | **6 050** |

**Observera:** Akeneo-estimatet räknade inte med AI-stöd. Med AI-stöd skulle även Akeneo CE bli något billigare, men troligen mindre än här, eftersom mycket av arbetet där är att anpassa sig till Akeneos befintliga kod.

**Kalendertid:** cirka 8 till 10 månader från start med fyra till fem personer.

---

## Senare och separat (indikativt)

| Paket | Låg | Normal | Hög |
|---|---:|---:|---:|
| AP17 (V2) Prioritering | 100 | 160 | 250 |
| AP18 (V2) Automatisk gruppering | 170 | 270 | 420 |
| AP19 (V2) Arkivering och återaktivering | 100 | 150 | 230 |
| AP20 (tillval) Nya mediedomäner | 40 | 70 | 130 |
| AP21 (tillval) Förhandsvisning | 50 | 100 | 170 |
| ALT03 Nödlösning | 80 | 200 | 400 |

---

## Återkommande kostnader på Azure

Belopp sätts när volymerna är mätta i AP01.

| Tjänst | Beror på |
|---|---|
| Container Apps | Antal containrar och hur mycket bakgrundsjobb som körs |
| PostgreSQL | Databasstorlek och prestanda för 1,4 miljoner artiklar |
| Blob Storage | Total filvolym för bilder, dokument och tio års versioner |
| Backup | Lagringstid och volym |
| Application Insights | Mängd loggar och hur länge de sparas |
| Tabellkomponent | Licens per utvecklare eller per år |
| Förvaltning och support | Svensk kontorstid enligt kravspecen |

---

## Risker

- **AI-besparingen är en bedömning.** Den ska följas upp under bygget och inte lovas som fast rabatt.
- **Sök i PostgreSQL** kan visa sig för långsamt för fria sökningar i 1,4 miljoner artiklar. Då tillkommer en sökmotor, cirka 60 till 120 timmar.
- **PHP och Azure:** några kopplingar kräver mer eget arbete än med .NET, främst mot Service Bus.
- **Ingen färdig PIM i botten.** Allt som SFB senare vill ha utöver kravspecen måste byggas. Det gäller också funktioner som en PIM-plattform hade haft färdigt.
