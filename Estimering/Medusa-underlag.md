# Medusa-underlag för estimering av SFB PIM

Underlag till estimeringsworkshopen för raderna i `SFB Estimat rader.csv`. För varje funktionskrav: vad Medusa v2 ger färdigt, vad som måste byggas, vad som driver timmarna och en bedömning.

## Stack och version

- **Version:** Medusa v2.22.7, släppt 2026-11-13. Det är `latest` på npm 2026-11-18. En förhandsversion av 2.22.8 finns men är inte släppt [1][2].
- **Stack enligt beslut 2026-11-16** (`SFB PBS AP01.ord`, PA-1-8): Medusa v2 på Node.js, TypeScript, PostgreSQL och Redis i SFB:s Azure. PIM:s egna data ligger i egna Medusa-moduler med modullänkar till produktmodulen. Administratörsgränssnittet byggs som tillägg till Medusa Admin.
- **Grundantagande i underlaget:** De 1,4 miljoner artiklarna med käll- och egna värden ligger i en egen artikelmodul och inte som `Product`/`ProductVariant` i Medusas produktmodul. Det stämmer med PBS F1 ("Artiklar med käll- och egna värden … byggs som egna moduler"). Produktmodulen används främst för kategoriträden.
- **Märkning:** "Verifierat" betyder att uppgiften är kontrollerad i dokumentationen, release notes eller GitHub, med källhänvisning [n]. "Bedömning" är vår tolkning och inte kontrollerad.

### Ändringar i Medusa som påverkar tidigare antaganden

1. **Index-modulen är avvecklad (deprecated) sedan v2.22.7.** Ersättningen är cross-module joins i `query.graph` [1][3][4]. PBS F1, PBS V2 och PA-1-8 bygger sökningen på Index-modulen, och lasttestet med 1,4 miljoner artiklar är definierat mot den. Lasttestet behöver definieras om.
2. **SSO via OIDC (Entra ID) och RBAC (roller) kräver enterprise-licens** och Medusa v2.21 eller senare [21][22]. Licensen finns inte i `SFB Estimat kostnader.csv`.
3. **Den nya Audit-modulen (v2.22.7) är licensierad.** Den loggar API-anrop men inte före- och eftervärden [24]. Den täcker alltså inte PIM-Q04.
4. **Admin-komponenter exporteras sedan v2.21.0,** bland annat `DataGrid`, ett kalkylbladsliknande rutnät med kopiera/klistra och ångra [12]. Det sparar tid i PIM-N01 och i listvyerna.
5. **Translation-modulen är stabil sedan v2.22.7** [1][25]. SFB har bara svenska, så den behövs inte.

---

## Datamodell (PIM-D)

### PIM-D01 Identitet
- **Medusa ger:** Verifierat: DML för egna datamodeller med id-generering, index och check constraints [6]. Det finns ingen färdig modell för flera affärsidentifierare per artikel.
- **Bygga själv:** En artikelmodul (DML) med fält för Finfo-nr, leverantörs-id, leverantörsartikelnr, WB-nr, GTIN och C4-ref, alla som text. Unikt index på den överenskomna källnyckeln, men inte på GTIN. Upsert på källnyckel i mottagningsworkflowen.
- **Timdrivare och osäkerhet:** Att fastställa nyckelreglerna i AP01, till exempel samma GTIN hos olika leverantörer. Själva modellen är enkel.
- **Bedömning:** Eget bygge (litet).

### PIM-D02 Produktgrupper
- **Medusa ger:** Verifierat: En variant tillhör exakt en produkt. Bundles hanteras bara som inventory kits [7]. Globala produktoptioner finns sedan v2.17 [28].
- **Bygga själv:** En gruppmodul med variantgrupp och bundle, gruppvärden (namn, bild, variantdimensioner, leverantör, BK04, kategorier) och en länktabell artikel–grupp. Regeln "högst en variantgrupp, flera bundles" läggs i workflow och check. Widget eller UI-route för att koppla på och av.
- **Timdrivare och osäkerhet:** Bedömning: Medusas Product/Variant passar inte. En artikel kan ligga i flera bundles och kan sakna grupp, och 1,4 miljoner varianter som kräver en produkt var ger fel modell. Distributionen av gruppfält separat från artiklar (I03) tillkommer.
- **Bedömning:** Eget bygge.

### PIM-D03 Attribut
- **Medusa ger:** Verifierat: Produktmodulen har bara fasta egenskaper (till exempel vikt och mått som float sedan v2.15) plus `metadata` [1][7]. Det finns ingen generisk attributmodell med datatyp, enhet och listvärden. DML har JSON-fält (typade sedan v2.19) [6].
- **Bygga själv:** En attributmodul med definition (datatyp, enhet, listvärden, källmappning) och värden per artikel. Välj mellan EAV-tabell och JSONB per artikel. Källvärde och eget värde måste lagras separat (W09).
- **Timdrivare och osäkerhet:** Valet av lagringsmodell vid 1,4 miljoner artiklar, det vill säga hur många värden totalt och hur filtrering och export ska fungera. Bedömning: JSONB med GIN-index eller EAV med partiella index måste provas i lasttestet.
- **Bedömning:** Eget bygge. Det är kärnan i PIM:et och den största enskilda modellrisken.

### PIM-D04 Attributförvaltning
- **Medusa ger:** Verifierat: Admin-UI-routes, widgets och exporterade `DataTable`/`ConfigurableDataTable` [11][12].
- **Bygga själv:** En UI-route för att lista och söka attributdefinitioner, visa användning (antal artiklar), ändra namn och beskrivning och sätta flaggan "ej för ny berikning". Validering i berikningsworkflows.
- **Timdrivare och osäkerhet:** Att räkna användning snabbt vid stora volymer. Bedömning: kräver aggregat eller cache.
- **Bedömning:** Delvis. UI-ramen finns, logiken är egen.

### PIM-D05 Kategorier
- **Medusa ger:** Verifierat: Produktkategorier i produktmodulen, nästlade, med rangordning via drag-och-släpp, intern/publik synlighet och aktiv/inaktiv. En produkt kan ligga i flera kategorier [7][8].
- **Bygga själv:** Tre träd som tre rotkategorier (bedömning: inget eget "träd"-begrepp är dokumenterat). En modullänk artikel–kategori och grupp–kategori, many-to-many [5]. Migrering av de tre träden.
- **Timdrivare och osäkerhet:** Kategorirelationerna i admin finns bara för Medusa-produkter, så artikelns kategoriväljare blir en egen widget. Bedömning: avdraget på 50 % i estimatet är rimligt för själva trädet men inte för relationerna.
- **Bedömning:** Delvis.

### PIM-D06 Kategoriförvaltning
- **Medusa ger:** Verifierat: Skapa, byta namn på, rangordna och flytta noder (nästling) i Medusa Admin [8].
- **Bygga själv:** Spärr mot borttagning när artikel- eller grupplänkar finns, via en workflow-hook eller egen route. Subscriber som skickar kategoriändringar till MagicBox (I03).
- **Timdrivare och osäkerhet:** Om standardvyn räcker för SFB:s trädstorlek. Bedömning: avdraget på 60 % i estimatet håller om standard-UI:t accepteras.
- **Bedömning:** Färdigt eller Delvis (mest färdigt).

### PIM-D07 Referensdata
- **Medusa ger:** Verifierat: Det finns ingen leverantörs- eller varumärkesmodell i produktmodulen [7]. DML och modullänkar finns [5][6].
- **Bygga själv:** En referensmodul för leverantör och varumärke med unik referensnyckel och flagga för källägd post. Enkel UI-route och väljare i artikelvyn.
- **Timdrivare och osäkerhet:** Liten volym och enkel CRUD.
- **Bedömning:** Eget bygge (litet).

## Administratörsgränssnitt och berikning (PIM-W)

### PIM-W01 Sökning
- **Medusa ger:** Verifierat: Index-modulen är avvecklad sedan v2.22.7 [1][3]. `query.graph` filtrerar och sorterar över modullänkar i databasen sedan v2.18. Den faller tillbaka på filtrering i minnet vid vissa villkor, och då ignoreras paginering vid laddning [4]. Listkomponenter finns [12]. Sparade vyer (view configurations) kräver en experimentell feature flag [13].
- **Bygga själv:** Ett sök-API i artikelmodulen (identifierare, benämning) med filter på leverantör, kategori, webbstatus, utgående, saknar bild och saknar kategori. Listvy som UI-route.
- **Timdrivare och osäkerhet:** Bedömning: Eftersom artiklarna ligger i en egen modul bör sökningen göras med egna PostgreSQL-index (B-tree, trigram eller tsvector via migrering) och inte med cross-module joins. Filtren "saknar kategori/bild" är anti-joins mot länktabeller och måste lasttestas. Avdraget på 30 % antog Index-modulen.
- **Bedömning:** Delvis (UI) och Eget bygge (sökmotor).

### PIM-W02 Artikelredigering
- **Medusa ger:** Verifierat: UI-routes, widgets, formulärkomponenter (`Form`, `Combobox`, `RouteFocusModal`) och data-hooks exporterade sedan v2.21 [11][12]. Workflows med kompensation [14].
- **Bygga själv:** Artikelns detalj- och skapavy (UI-route, eftersom artikeln inte är en Medusa-produkt). Admin-API-routes och workflows för att skapa och uppdatera med fältanknuten validering.
- **Timdrivare och osäkerhet:** Fältmatrisen (vad som är tillåtet per artikeltyp) och mängden fält. Bedömning: avdraget på 25 % för artikelvyn är rimligt tack vare de exporterade komponenterna.
- **Bedömning:** Delvis.

### PIM-W03 Textfält
- **Medusa ger:** Verifierat: Text- och JSON-fält i DML [6]. `ExpandableTextCell` och flerradsceller i DataGrid [12].
- **Bygga själv:** Sju lagrade fält och ett härlett sammanslaget fält, antingen beräknat vid läsning eller lagrat och uppdaterat i workflow.
- **Timdrivare och osäkerhet:** Liten. Regeln för stycken och tomma fält testas.
- **Bedömning:** Eget bygge (litet).

### PIM-W04 Textöverstyrning
- **Medusa ger:** Ingenting specifikt (bedömning).
- **Bygga själv:** Regeln för effektivt värde (internt om ifyllt, annars källvärdet; bara blanksteg räknas som tomt). Den ska användas lika i UI, Excel, tabell och utgående flöde. Delad tjänstemetod i artikelmodulen.
- **Timdrivare och osäkerhet:** Att samma regel används överallt, och att testa den.
- **Bedömning:** Eget bygge.

### PIM-W05 Ändringsnotiser
- **Medusa ger:** Verifierat: Event bus och subscribers [17]. Admin har notiser (bell) som används för import och export [9][10], men dessa är inte en kvitterbar åtgärdslista.
- **Bygga själv:** En notismodul med artikel, fält, tid, före/efter och kvittering. Skapas i mottagningsworkflowen vid ändrat källvärde när internvärde finns. Listvy som UI-route.
- **Timdrivare och osäkerhet:** Regeln "oförändrad omsändning ger ingen notis" och att en notis öppnas igen.
- **Bedömning:** Eget bygge.

### PIM-W06 Webbstatus
- **Medusa ger:** Verifierat: Produktstatus (draft/published osv.) finns, men bara för Medusa-produkter [9].
- **Bygga själv:** Fältet webbstatus på artikeln och överföring i I03.
- **Timdrivare och osäkerhet:** Liten.
- **Bedömning:** Eget bygge (litet).

### PIM-W07 Livscykelstatus i första versionen
- **Medusa ger:** Ingenting specifikt (bedömning).
- **Bygga själv:** Fält för livscykelstatus och utgåendedatum, visning och överföring. Ingen arkivlogik i F1.
- **Timdrivare och osäkerhet:** Liten.
- **Bedömning:** Eget bygge (litet).

### PIM-W08 Validering
- **Medusa ger:** Verifierat: Workflows med fel och kompensation [14]. Zod v4 för validering av request-body (v2.14) [1]. DML check constraints [6].
- **Bygga själv:** En gemensam valideringstjänst (identitet, referenser, datatyp, listvärden) som anropas från UI, tabell, Excel och mottagning. Flaggor för brister (saknar bild eller kategori) utan att blockera.
- **Timdrivare och osäkerhet:** Att samma regler återanvänds i fyra kanaler och att felen anges per rad och fält.
- **Bedömning:** Delvis (ramverk) och Eget bygge (regler).

### PIM-W09 Egen berikning av produktegenskaper
- **Medusa ger:** Ingenting specifikt (bedömning). Det är den egna attributmodellen i D03.
- **Bygga själv:** Separat källvärde och eget värde per egenskap (sju startattribut), effektivt värde, "ta bort överstyrning" och skydd av identifierare. Samma logik i UI, tabell och Excel.
- **Timdrivare och osäkerhet:** Att skilja eget nollvärde från tomt, och att få det rätt i export och återimport.
- **Bedömning:** Eget bygge.

## Excel (PIM-X)

### PIM-X01 Excelimport
- **Medusa ger:** Verifierat: Den inbyggda importen läser bara CSV för Medusa-produkter, en rad per variant, i bakgrunden med status i notiserna [9]. Long-running workflows [14]. Worker mode för bakgrundsjobb [26].
- **Bygga själv:** Import av en fast Excel-mall (.xlsx via ett npm-bibliotek, bedömning) till artikelmodulen. Upload-route, långkörande workflow med batchar, fältmatris, skydd av källfält och regeln "tom cell = oförändrat".
- **Timdrivare och osäkerhet:** Regelverket och testerna, 5 000 rader. Den inbyggda importen går inte att återanvända, bara mönstret.
- **Bedömning:** Eget bygge.

### PIM-X02 Excelexport
- **Medusa ger:** Verifierat: Den inbyggda produktexporten ger CSV av Medusa-produkter, filtrerad på listan, i bakgrunden med nedladdning via notis [10].
- **Bygga själv:** Export av urval till .xlsx med stabila id:n, egna fält och skrivskyddade, markerade källfält. Workflow plus File Module för filen.
- **Timdrivare och osäkerhet:** Formatet för att tömma en överstyrning, och prestanda för 5 000 rader (låg risk).
- **Bedömning:** Delvis (mönster och infrastruktur) och Eget bygge.

### PIM-X03 Importkontroll
- **Medusa ger:** Verifierat: Workflow-exekveringar kan lagras och följas [14]. Idempotens i workflow-motorn sedan v2.10 [1].
- **Bygga själv:** Förhandskontroll (dry run), svar per rad, sammanfattning, omkörning av avvisade rader och konfliktkontroll mot ändringar efter export (versionsfält, se Q03).
- **Timdrivare och osäkerhet:** Konfliktregeln och UI:t för resultatet.
- **Bedömning:** Eget bygge.

## Medier och dokumentversioner (PIM-A)

### PIM-A01 Medierelationer
- **Medusa ger:** Verifierat: File Module med Local- och S3-provider. Bara en provider kan registreras. Azure Blob saknas, men en egen provider kan byggas [19]. Bedömning: Azure-plugins som finns i communityn är för v1.
- **Bygga själv:** En egen File Module Provider för Azure Blob, eller S3-kompatibel åtkomst om SFB:s lagring kan det. En mediemodul (fil, typ) och länktabeller till artikel och grupp. Uppladdning av flera filer med resultat per fil i en widget.
- **Timdrivare och osäkerhet:** Azure-providern, och 1,2 TB befintliga filer som ska refereras och inte kopieras (A07, AP01).
- **Bedömning:** Delvis (filhantering) och Eget bygge (relationer).

### PIM-A02 Ordning och bortval
- **Medusa ger:** Verifierat: Länktabeller kan ha egna kolumner [5].
- **Bygga själv:** Fälten ordning och webbexkludering på relationen fil–artikel och fil–grupp. Bevaras vid källuppdatering. Notis vid ändring av exkluderat media.
- **Timdrivare och osäkerhet:** Liten modell men logiken för den logiska bildidentiteten vid källuppdatering.
- **Bedömning:** Eget bygge.

### PIM-A03 Dokumentversioner
- **Medusa ger:** Verifierat: File Module saknar dokumenterad versionering [19].
- **Bygga själv:** Versionstabell (oföränderliga filer, checksumma för att upptäcka oförändrad omsändning), bevarande i tio år och koppling till Blob-livscykel eller svalare lagringsnivå.
- **Timdrivare och osäkerhet:** Bevarandet och att samma käll-URL kan få nytt innehåll.
- **Bedömning:** Eget bygge.

### PIM-A04 Versionsvisning
- **Medusa ger:** UI-komponenter [12].
- **Bygga själv:** Markering av aktuell version, ärvd exkludering och versionslista i artikelvyn (widget).
- **Timdrivare och osäkerhet:** Liten.
- **Bedömning:** Eget bygge (litet).

### PIM-A05 Versionsundantag
- **Medusa ger:** Ingenting specifikt.
- **Bygga själv:** En typregel för Färgkarta och Produktkatalog: byte av aktuell fil utan krav på historik.
- **Timdrivare och osäkerhet:** Liten.
- **Bedömning:** Eget bygge (litet).

### PIM-A08 Källborttagning
- **Medusa ger:** Verifierat: Events och subscribers [17].
- **Bygga själv:** Registrering och flagga för borttaget i källan, notis (W05), och skydd mot fysisk radering av versioner.
- **Timdrivare och osäkerhet:** Liten. Konfliktregeln ska fastställas.
- **Bedömning:** Eget bygge (litet).

## PIM:s integrationsgränssnitt (PIM-I)

### PIM-I02 Källmottagning i PIM
- **Medusa ger:** Verifierat: Egna API-routes, workflows med retry och kompensation, idempotens (v2.10) och long-running workflows [14][15]. Secret API keys för systemanrop [23].
- **Bygga själv:** En mottagnings-route eller kökonsument enligt kontraktet (I01), upsert på källnyckel, revisionskontroll (äldre skriver inte över nyare), uppdatering av bara källägda fält, spårbar ändringsidentitet och isolering av felaktig post.
- **Timdrivare och osäkerhet:** Kontraktet och volymen av dagliga deltan. Bedömning: Medusa-workflows per artikel ger overhead vid stora leveranser och bör batchas.
- **Bedömning:** Delvis (ramverk) och Eget bygge (logik).

### PIM-I03 Utgående från PIM
- **Medusa ger:** Verifierat: Event bus med prioritet (v2.13), subscribers, scheduled jobs och Redis-baserad event- och workflowmotor för produktion [15][17][18].
- **Bygga själv:** Utgående ändringslogg (outbox-tabell) per artikel, grupp, kategori och media. Spridning från grupp och media till beroende artiklar. Leverans till MagicBox med position per mottagare.
- **Timdrivare och osäkerhet:** Spridningen (en mediaändring kan beröra många artiklar) och att garantera ordning. Bedömning: en outbox i egen tabell är säkrare än att lita på events.
- **Bedömning:** Delvis (infrastruktur) och Eget bygge.

### PIM-I04 Fel och omsändning
- **Medusa ger:** Verifierat: `maxRetries`, `retryInterval` och manuell `retryStep` (v2.10.2). Lagrade exekveringar och admin-routes för att lyckas eller misslyckas med ett steg [14][15].
- **Bygga själv:** Felstatus per post, omsändning av post eller urval och en administratörsvy med senaste lyckade överföring och kvarstående fel (UI-route).
- **Timdrivare och osäkerhet:** Att positionen per mottagare inte påverkas av omsändning. Avdraget på 40 % i estimatet är rimligt.
- **Bedömning:** Delvis.

## Tabellredigering, V2 och tillval (PIM-N)

### PIM-N01 Tabellredigering och massändring
- **Medusa ger:** Verifierat: `DataGrid` exporteras sedan v2.21. Den har tangentbordsnavigering, områdesmarkering, kopiera och klistra mellan celler, ångra och gör om, celltyperna text, flerradstext, tal och boolesk, skrivskyddade celler och lazy loading [12]. Ifyllnadshandtag, validering utöver min/max och sparflöde är inte dokumenterade.
- **Bygga själv:** En tabell-UI-route ovanpå DataGrid, fältmatris (skrivskyddade källfält), "samma värde på valda rader", kategoriväljare i cell, förhandsgranskning av ändringar och batch-sparning via workflow med svar per rad och konfliktkontroll (Q03).
- **Timdrivare och osäkerhet:** Bedömning: DataGrid kan ersätta den separata gridkomponenten med öppen källkod som offerten nämner, men API:t är nytt (v2.21) och kan ändras. Egna celltyper (kategori, listvärde) behöver byggas.
- **Bedömning:** Delvis.

### PIM-N02 ERP-baserad prioritering (V2)
- **Medusa ger:** Verifierat: DML och filtrering över länkar [4][6].
- **Bygga själv:** En modul för ERP-uppgifter per delägare (matchning, aktiv, webbflagga, saldo, tid), mottagning och filter i listan.
- **Timdrivare och osäkerhet:** Volymen, 1,4 miljoner artiklar gånger antalet delägare, och filterprestanda.
- **Bedömning:** Eget bygge.

### PIM-N03 Automatisk produktgruppering (V2)
- **Medusa ger:** Verifierat: Scheduled jobs och workflows [14][18].
- **Bygga själv:** En regelmotor för säker eller osäker träff, förslagslista, skydd av manuella grupper och notiser.
- **Timdrivare och osäkerhet:** Reglerna (utredning i AP18). Medusa bidrar bara med körmiljö.
- **Bedömning:** Eget bygge.

### PIM-N04 Samlad arkivhantering (V2)
- **Medusa ger:** Bedömning: Soft delete (`deleted_at`) i DML, men den är inte en arkivstatus med återaktivering.
- **Bygga själv:** Arkivstatus för artikel, bild och dokument, arkivsökning, återaktivering, spärr mot automatisk återaktivering och statusbesked i I03.
- **Timdrivare och osäkerhet:** Att relationer och historik ska bestå över tre entitetstyper.
- **Bedömning:** Eget bygge.

### PIM-N05 Nya mediedomäner (tillval)
- **Medusa ger:** Ingenting. Det är en drifts- och DNS-fråga (bedömning). Den egna File-providern (A01) styr URL-prefix.
- **Bygga själv:** Utredning, länkmappning och ompekning.
- **Timdrivare och osäkerhet:** Påverkas inte av Medusa.
- **Bedömning:** Eget bygge (utanför Medusa).

### PIM-N06 Förhandsvisningar (tillval)
- **Medusa ger:** Verifierat: `Thumbnail`-komponenten exporteras [12]. Ingen renderingstjänst för filformat är dokumenterad.
- **Bygga själv:** Integration med en renderingstjänst per formatlista och generering av tumnaglar i ett bakgrundsjobb.
- **Timdrivare och osäkerhet:** Formatlistan och tjänstevalet.
- **Bedömning:** Eget bygge.

## Volym, samtidighet och historik (PIM-Q)

### PIM-Q02 Arbete med större urval
- **Medusa ger:** Verifierat: Worker mode (separata server- och workerprocesser), long-running workflows i bakgrunden och status via notiser [9][14][26].
- **Bygga själv:** Jobbstatus och resultatvy för import, export och massändring (UI-route). Konfiguration av worker-instanser i Azure Container Apps.
- **Timdrivare och osäkerhet:** Lasttestet. Bedömning: avdraget på 50 % för jobbstatus är rimligt.
- **Bedömning:** Delvis.

### PIM-Q03 Samtidig redigering
- **Medusa ger:** Verifierat: Locking Module (Redis eller PostgreSQL) och `acquireLockStep` ger ömsesidig uteslutning, inte versionskontroll. Optimistisk samtidighet är inte dokumenterad [16].
- **Bygga själv:** Versionsfält per artikel (optimistisk låsning), kontroll i alla sparvägar (vy, tabell, Excel) och en konfliktdialog i UI.
- **Timdrivare och osäkerhet:** Att täcka alla sparvägar, och konflikthantering per rad i tabell och Excel.
- **Bedömning:** Eget bygge.

### PIM-Q04 Ändringshistorik
- **Medusa ger:** Verifierat: Audit-modulen (v2.22.7, licensierad) loggar ändrande API-anrop med aktör, resurs och utfall men inte request- eller response-body [24]. Den har ännu ingen sida i dokumentationen.
- **Bygga själv:** En historikmodul med fält, före/efter, aktör eller källa (användare eller leverans) och åtskillnad mellan källvärde och överstyrning. Skrivs från mottagning, vy, tabell och Excel. Visning per artikel.
- **Timdrivare och osäkerhet:** Lagringsvolymen över tid (bevarandet ska bekräftas) och att varje skrivväg loggar.
- **Bedömning:** Eget bygge.

## Inloggning (PIM-O)

### PIM-O01 Inloggning
- **Medusa ger:** Verifierat: Auth- och User-modulerna med `emailpass` för admin. Inbjudan och borttagning av admin-användare (v2.12) [20][27]. Secret API keys för integrationer, men varje nyckel är knuten till en admin-användare och saknar scopes [23]. OIDC-SSO (Entra ID) för admin och RBAC kräver enterprise-licens, v2.21 eller senare [21][22].
- **Antagande för estimatet:** Ingen SSO. Administratörerna loggar in med Medusas inbyggda `emailpass` och personliga konton, så ingen enterprise-licens behövs. Om SFB vill ha inloggning via Entra ID är det ett tillägg som prissätts separat, med licens eller en egen OIDC-integration.
- **Bygga själv:** Behörigheterna. Tekniska användare för integrationerna, så att inget personkonto används, och egen middleware som begränsar varje integrationsidentitet till de anrop som dess kontrakt tillåter. Avslutade användare och återkallade nycklar ska avvisas direkt.
- **Timdrivare och osäkerhet:** Behörighetsmodellen för integrationerna, som Medusa inte har utan RBAC-licensen. Bedömning: avdraget på 30 % håller för inloggningen, men behörigheterna är eget bygge.
- **Bedömning:** Delvis.

## Migrering (PIM-M02 och M03), bara inladdningen av 1,4 miljoner artiklar

### PIM-M02 Mappning och PIM-M03 Provmigrering, inladdning i Medusa
- **Medusa ger:** Verifierat: Den inbyggda produktimporten är CSV för Medusa-produkter, en rad per variant [9], och passar inte de egna modulerna. Egna CLI-skript med `medusa exec` och tillgång till alla moduler [26]. Datamigreringsskript sedan v2.3 [1]. Events skickas bara när det finns subscribers (v2.12) [27]. Länktabeller saknar främmande nycklar [5].
- **Bygga själv:** En egen laddare som CLI-skript. Den läser exportfiler i batchar, skriver till de egna modulernas tabeller med bulk-insert (bedömning: PostgreSQL `COPY` eller multi-row insert direkt mot tabellerna, inte en workflow per artikel) och fyller länktabellerna direkt. Kategorier skapas via produktmodulens tjänst. Utgående synk och notiser stängs av under laddningen. Index byggs efter laddningen. Delta-körning med samma upsert-logik som I02.
- **Timdrivare och osäkerhet:** Bedömning: Att gå via modultjänster och workflows för 1,4 miljoner artiklar med attribut och relationer blir troligen för långsamt för ett ändringsstopp. Att skriva direkt mot tabellerna kringgår Medusas validering och events, så avstämningen (M03) blir viktigare. Laddtiden ska mätas i lasttestet.
- **Bedömning:** Eget bygge.

---

## Källor

1. Medusa releases på GitHub, v2.22.7 och tidigare minor-versioner (v2.3, v2.10, v2.13, v2.14, v2.15, v2.17, v2.18, v2.19, v2.21): https://github.com/medusajs/medusa/releases, särskilt https://github.com/medusajs/medusa/releases/tag/v2.22.7
2. npm, `@medusajs/medusa` dist-tags (latest 2.22.7, 2026-11-18): https://www.npmjs.com/package/@medusajs/medusa
3. Index Module (deprecated sedan v2.22.7): https://docs.medusajs.com/learn/fundamentals/module-links/index-module
4. Query, filtrering och sortering över länkade modeller: https://docs.medusajs.com/learn/fundamentals/module-links/query
5. Module links: https://docs.medusajs.com/learn/fundamentals/module-links
6. Data models (DML), properties, index och check constraints: https://docs.medusajs.com/learn/fundamentals/data-models
7. Product Module: https://docs.medusajs.com/resources/commerce-modules/product
8. Användarguide, kategorier: https://docs.medusajs.com/user-guide/products/categories
9. Användarguide, produktimport: https://docs.medusajs.com/user-guide/products/import
10. Användarguide, produktexport: https://docs.medusajs.com/user-guide/products/export
11. Admin widgets och UI routes: https://docs.medusajs.com/learn/fundamentals/admin/widgets, https://docs.medusajs.com/learn/fundamentals/admin/ui-routes
12. Exporterade admin-komponenter (v2.21.0) och DataGrid: https://github.com/medusajs/medusa/releases/tag/v2.21.0, https://docs.medusajs.com/resources/admin-components/components/data-grid
13. View configurations (feature flag): https://docs.medusajs.com/resources/commerce-modules/settings/view-configurations
14. Long-running workflows: https://docs.medusajs.com/learn/fundamentals/workflows/long-running-workflow
15. Retry av misslyckade steg: https://docs.medusajs.com/learn/fundamentals/workflows/retry-failed-steps
16. Lås i workflows och Locking Module: https://docs.medusajs.com/learn/fundamentals/workflows/locks, https://docs.medusajs.com/resources/infrastructure-modules/locking
17. Events och subscribers, prioritet: https://docs.medusajs.com/learn/fundamentals/events-and-subscribers, https://docs.medusajs.com/learn/fundamentals/events-and-subscribers/event-priority
18. Scheduled jobs: https://docs.medusajs.com/learn/fundamentals/scheduled-jobs
19. File Module: https://docs.medusajs.com/resources/infrastructure-modules/file
20. Auth Module: https://docs.medusajs.com/resources/commerce-modules/auth
21. OIDC SSO (enterprise-licens): https://docs.medusajs.com/resources/enterprise/sso
22. RBAC Module (enterprise-licens): https://docs.medusajs.com/resources/enterprise/rbac
23. API keys, secret keys: https://docs.medusajs.com/resources/commerce-modules/api-key/concepts
24. Audit Module, PR #17787 och #17795 (sammanslagna 2026-11-12 och 2026-11-13): https://github.com/medusajs/medusa/pull/17787, https://github.com/medusajs/medusa/pull/17795
25. Translation Module: https://docs.medusajs.com/resources/commerce-modules/translation
26. Egna CLI-skript och worker mode: https://docs.medusajs.com/learn/fundamentals/custom-cli-scripts, https://docs.medusajs.com/learn/production/worker-mode
27. Release v2.12.0 (eventsändning bara vid subscribers, borttagning av admin-användare): https://github.com/medusajs/medusa/releases/tag/v2.12.0
28. Release v2.17.0 (globala produktoptioner): https://github.com/medusajs/medusa/releases/tag/v2.17.0
