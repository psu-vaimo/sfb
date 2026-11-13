# Timestimat med Akeneo CE som bas

Grovt utkast för intern diskussion. Samma upplägg som `SFB_Timestimat_utkast.md`, men med Akeneo Community Edition (CE) som grund i stället för en egenutvecklad lösning. Bedömningen av vad CE har och saknar bygger på allmän kunskap om produkten och ska kontrolleras mot aktuell CE-version.

---

## Vad Akeneo CE ger och vad som saknas

| Krav i kravspecen | Finns i CE | Behöver byggas |
|---|---|---|
| Artiklar, attribut, familjer, validering | Ja | Uppsättning och import av alla attributdefinitioner från C4 |
| Tre kategoriträd | Ja | Inget |
| Variantgrupper (högst en per artikel) | Ja, produktmodeller | Anpassning till SFB:s gruppfält |
| Bundles (flera per artikel) med egna gruppfält | Delvis, associationer och grupper saknar egna attribut | Egen lösning för gruppfält på bundles |
| Sök och filter | Ja, med Elasticsearch | Prestandatrimning för 1,4 miljoner artiklar |
| Ändringshistorik, vem ändrade vad | Ja | Inget |
| Massändring av valda artiklar | Ja, enkel | Inget |
| Tabellredigering direkt i gränssnittet | Nej | Egen modul |
| Skrivskyddade källfält | Nej, behörighet per attribut finns bara i betalversionen | Egen modul |
| Källvärde och eget värde med effektivt värde | Nej, regelmotorn finns bara i betalversionen | Egen logik |
| Notislista när källan ändrar berikad artikel | Nej | Egen modul |
| Excel-import och export | Ja | Fast mall, regler för tomma celler, konfliktkontroll mot gammal fil, förhandsgranskning |
| Bildbibliotek med återanvändning, ordning och webbexkludering | Nej, bildbiblioteket finns bara i betalversionen | Egen mediemodul |
| Dokumentversioner som sparas i tio år | Nej | Egen modul |
| REST API för källdata | Ja | Matchning och felkö |
| Ändringsflöde ut med kvittens och position per mottagare | Nej, händelse-API finns inte i CE | Egen lösning |
| Inloggning via befintlig identitetstjänst (SSO) | Nej, bara i betalversionen | Egen koppling om SFB kräver det |
| Licenskostnad | Ingen | Inget |

**Slutsats:** CE ger en färdig grund för datamodell, sök, redigering, kategorier och historik. De delar som gör SFB:s krav speciella (medier och versioner, tabellredigering, skydd av källvärden, notiser, ändringsflöde ut) måste ändå byggas själva.

---

## F1: timmar per paket

| Paket | Vad som ändras jämfört med egenutveckling | Låg | Normal | Hög |
|---|---|---:|---:|---:|
| AP01 Teknisk förstudie | Lite mer, eftersom vi också ska passa in SFB:s modell i Akeneos begrepp | 180 | 240 | 320 |
| AP02 Datamodell och grundplattform | Mindre, Akeneo ger modellen. Kvar är familjer, attribut, produktmodeller, bundles och installation | 100 | 160 | 240 |
| AP03 Gränssnitt och berikning | Mycket mindre, Akeneo ger sök, redigering, kategorier och historik. Kvar är skrivskydd, effektivt värde, notislista, attributstädning | 300 | 450 | 700 |
| AP16 Tabellredigering | Mer, ingen inbyggd tabellredigering och egen kod i Akeneos gränssnitt är krångligare | 250 | 350 | 500 |
| AP06 Excel | Något mindre, import och export finns. Kvar är mall, tomma celler, konfliktkontroll, förhandsgranskning | 120 | 200 | 300 |
| AP04 Integrationsgränssnitt | Något mindre, API finns. Ändringsflöde ut med positioner byggs själv | 300 | 450 | 700 |
| AP05 Bilder, dokument och versioner | Mer, inget bildbibliotek i CE. Egen modul som ska passa in i Akeneos gränssnitt | 300 | 450 | 700 |
| AP11 Migrering | Något mindre, standardimport finns | 280 | 420 | 650 |
| AP22 Gamla dokumentversioner | Oförändrat | 80 | 160 | 320 |
| AP12 Test och acceptans | Ungefär oförändrat | 300 | 440 | 650 |
| AP13 Miljöer och drift | Lite mer, Akeneo kräver MySQL, Elasticsearch och mer drift | 160 | 240 | 340 |
| AP14 Driftsättning och överlämning | Oförändrat | 160 | 220 | 300 |
| **Delsumma** | | **2 530** | **3 780** | **5 720** |
| AP15 Projektledning, ca 12 % | | 300 | 450 | 690 |
| **Totalt F1** | | **2 830** | **4 230** | **6 410** |

Inloggning via befintlig identitetstjänst ingår inte ovan. Om SFB kräver det tillkommer cirka 40 till 80 timmar i AP13.

## Jämförelse med egenutveckling

| | Låg | Normal | Hög |
|---|---:|---:|---:|
| Egenutveckling | 3 210 | 4 740 | 6 970 |
| Akeneo CE | 2 830 | 4 230 | 6 410 |
| **Skillnad** | **380** | **510** | **560** |

Akeneo CE sparar cirka **10 %**. Besparingen i datamodell och gränssnitt äts delvis upp av att medier och tabellredigering blir dyrare.

**Kalendertid:** ungefär som tidigare, cirka 8 till 11 månader. Teamet kan komma igång snabbare eftersom grunden finns.

---

## Senare och separat (indikativt)

| Paket | Låg | Normal | Hög | Kommentar |
|---|---:|---:|---:|---|
| AP17 (V2) Prioritering | 120 | 200 | 300 | Oförändrat |
| AP18 (V2) Automatisk gruppering | 200 | 320 | 500 | Oförändrat |
| AP19 (V2) Arkivering och återaktivering | 80 | 130 | 200 | Lägre, Akeneo kan redan aktivera och avaktivera produkter |
| AP20 (tillval) Nya mediedomäner | 40 | 80 | 150 | Oförändrat |
| AP21 (tillval) Förhandsvisning | 60 | 120 | 200 | Oförändrat |
| ALT03 Nödlösning | 80 | 200 | 400 | Oförändrat |

---

## Fördelar och risker med Akeneo CE

**Fördelar**
- Ingen licenskostnad.
- Beprövad grund för produktdata.
- Lättare för SFB att byta partner, många kan Akeneo. Det stämmer med kravet på överlämning.
- Väg uppåt till Akeneos betalversion om SFB senare vill ha bildbibliotek, regler eller behörigheter.

**Risker**
- **CE:s framtid.** Akeneo satsar främst på sin molnversion. Kontrollera hur ofta CE uppdateras och hur länge säkerhetsuppdateringar ges.
- **Uppgraderingar.** Egna moduler i Akeneo gör större versionsbyten dyrare. Räkna med återkommande kostnad för detta i förvaltningen.
- **Prestanda.** 1,4 miljoner artiklar fungerar i Akeneo men kräver rätt dimensionerad Elasticsearch och databas.
- **Två system för medier.** Egen mediemodul vid sidan av Akeneo blir en del som Akeneo-kunniga partners inte känner igen.
- **Betalversionens funktioner saknas.** Behörigheter per attribut, regelmotor och bildbibliotek måste byggas själva, och blir svåra att byta mot betalversionen senare.

---

## Att kontrollera

1. Aktuell CE-version, uppdateringstakt och supportperiod.
2. Om bundles kan lösas med standardfunktioner, eller om egen lösning krävs.
3. Om SFB kräver inloggning via sin identitetstjänst.
4. Om Akeneos betalversion (bildbibliotek, regler, behörigheter) skulle bli billigare totalt än att bygga samma sak på CE. Det kan vara värt en egen jämförelse.
