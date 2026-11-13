# Kravspecifikationen i enkel svenska

Förenklad sammanfattning av *Kravspecifikation för egen berikningsdel och PIM, version 1.3-V* från Sveriges Fria Bygghandlare (SFB). Originalets ID:n står inom parentes så att du kan hitta tillbaka.

---

## 1. Uppdraget i en mening

SFB vill att Vaimo **räknar på vad det kostar och hur lång tid det tar** att bygga ett nytt system för produktinformation (PIM) som ersätter det gamla systemet C4, innan C4 stängs ner.

Det är **inte en beställning**. Det är en förfrågan om estimat (en uppskattning), som SFB ska använda för att bestämma om och hur de ska gå vidare. SFB har ingen fastställd budget ännu.

## 2. Ordlista

| Förkortning / namn | Betyder |
|---|---|
| PIM | Product Information Management, system för att lagra och förbättra produktinformation |
| Berikningsdel / berikning | Delen där SFB:s egna medarbetare förbättrar produktdata, t.ex. skriver bättre namn och texter |
| C4 | SFB:s nuvarande system för produktinformation. Ska stängas ner |
| MagicBox | SFB:s befintliga integrationsnav. All data till och från PIM går via MagicBox |
| ITM8 | IT-partner som äger MagicBox och bygger kopplingarna där |
| Snicken | En mottagare av artikeldata som bara vill ha ett urval av artiklarna |
| Finfo, BASTA, BVB | Externa källor för produktdata (branschens produktdatabas, miljö- och kemikaliebedömning, Byggvarubedömningen) |
| Delägare | SFB:s ägarbutiker |
| Artikel | En vara från en viss leverantör, med egen identitet |
| Produktgrupp | En samling artiklar, t.ex. samma trall i olika längder (variantgrupp) eller saker som säljs ihop (bundle) |
| GTIN | Streckkodsnumret på en vara |
| BK04 | Svenskt klassificeringssystem för byggvaror |
| ERP | Affärssystemet (pris, lager, order) |
| F1 | Första driftversionen, det som ska vara klart först |
| V2 | Version 2, senare utveckling |
| Tillval | Extra funktioner som kan köpas till separat |
| AP01 till AP22 | Arbetspaket 1 till 22, delarna som projektet är uppdelat i |
| B01 till B14 | Beslut och antaganden som SFB har gjort |
| ALT01, ALT03 | Alternativa lösningar som ska prissättas separat |
| PIM-W01, PIM-A01 osv. | Krav-ID:n i kravkatalogen (Excel-bilagan) |
| RPO | Hur mycket data man högst får förlora vid ett haveri |
| RTO | Hur snabbt systemet ska vara igång igen efter ett haveri |

## 3. Bakgrund

- Idag jobbar två PIM-administratörer på SFB:s servicekontor med produktinformation i C4.
- C4 och dess meddelandekö ska stängas. Efter det får man **inte räkna med att C4 finns kvar**, varken för drift eller för att hämta data.
- Vaimo gjorde förstudien åt SFB, så Vaimo har redan mycket kunskap. SFB vill att Vaimo återanvänder det arbetet och **inte tar betalt två gånger** för sådant som redan är gjort.
- Gamla förslag från förstudien (plattform, arkitektur, faser) gäller inte om de krockar med denna kravspec. Om Vaimo ser en krock ska den nämnas i svaret.

## 4. Vad Vaimo ska leverera i sitt svar

1. **Ett grundestimat** för första driftversionen (F1) enligt kravkatalogen, med:
   - timmar per arbetspaket
   - timpris per paket och kostnad i kronor exklusive moms
   - låg, normal och hög bedömning
   - bemanning (hur många och vilka roller)
   - kalendertid med verklig startdag, beroenden och testperiod
   - återkommande kostnader (drift, lagring, licenser, backup, övervakning, support) separat
   - övriga engångskostnader separat från arbetstid
2. **Ett eget pris för den tekniska förstudien (AP01)**, se avsnitt 8 nedan. Detta är ett krav. Grundestimatet för resten av F1 ska ändå lämnas nu, som ett preliminärt estimat. Det bindande priset för osäkra delar kommer efter AP01.
3. **En tidsplan mot C4-stängningen**: kan F1 vara i drift innan C4 stängs? Med vilken bemanning? Vilka beslut behöver SFB ta och senast när?
4. **Om F1 inte hinner bli klar**: beskriv och prissätt en nödlösning (ALT03) som håller verksamheten igång. Den får inte gömmas inuti F1-priset.
5. **Egna förslag och förenklingar** är välkomna men ska redovisas **separat** från grundestimatet, med vilka krav som påverkas och vad det betyder för pris och tid.
6. **Pris för senare utveckling (V2) och tillval** som egna rader.

Vaimo får lämna offerten i eget format.

## 5. Vad systemet ska klara i första versionen (F1)

| Område | Vad administratörerna ska kunna göra | Krav-ID |
|---|---|---|
| Hitta artiklar | Söka på namn och nummer, kombinera filter, se brister, arbeta med urval på minst 100 artiklar. Två personer samtidigt | PIM-W01, PIM-Q01 till Q03 |
| Snabb tabellredigering | Ändra många artiklar direkt i en tabell på skärmen, som i ett kalkylark men enklare. Kopiera och klistra in, sätta samma värde på flera rader. Se ändringar innan man sparar | PIM-N01 |
| Redigera en artikel | Skapa egna artiklar och ändra tillåtna fält. Egna texter och egna värden ska skyddas när källan skickar ny data | PIM-W02 till W05, W08, W09 |
| Grupper och kategorier | Gruppera artiklar till produkter manuellt. Hantera tre kategoriträd (Produktkatalog, Brukspecialisten, Weydes) | PIM-D01 till D07 |
| Excel | Ladda ner urval, redigera, ladda upp igen. Skapa nya artiklar via Excel. Fast mall, upp till 5 000 rader, tydliga felmeddelanden per rad | PIM-X01 till X03 |
| Bilder och dokument | Ladda upp flera filer till en artikel, välja ordning, dölja från webben. Spara alla dokumentversioner i tio år | PIM-A01 till A08 |
| Status och spårbarhet | Sätta webbstatus (aktiv/inaktiv) manuellt, se livscykelstatus, se vem som ändrat vad | PIM-W06, W07, Q04 |
| Dataflöde | Ta emot data från källorna via MagicBox, skicka ändringar tillbaka till MagicBox och rätt urval till Snicken. Upptäcka fel och skicka om | PIM-I01 till I10 |
| Drift | Migrerad data, personliga inloggningar, backup, utbildning, dokumentation och överlämning av koden | PIM-O01 till O05, M01 till M06, H01 till H04 |

### Den viktigaste regeln: egen text och källans text hålls isär

Systemet sparar **både** källans senaste värde och SFB:s eget värde. Det egna värdet används om det finns.

Exempel:

| Händelse | Källans namn | SFB:s eget namn | Det som används |
|---|---|---|---|
| Artikeln kommer in | Trall 28x120 | tomt | Trall 28x120 |
| SFB förbättrar namnet | Trall 28x120 | Impregnerad trall 28 x 120 mm | Det egna namnet |
| Källan ändrar | Trall NTR AB 28x120 | oförändrat | Det egna namnet. En notis visas |
| SFB tömmer sitt fält | Trall NTR AB 28x120 | tomt | Källans nya namn |

Samma princip gäller för sju produktegenskaper: **material, färg, längd, bredd, höjd, tjocklek och diameter** (B07). Identifierare och externa bedömningar (t.ex. miljöbedömningar) får aldrig skrivas över.

Samma regler ska gälla oavsett om man ändrar i en artikel, i tabellen eller via Excel.

## 6. Vad som INTE ingår i F1

**Kommer i version 2 (ska prissättas separat):**
- Prioritering av artiklar utifrån affärssystemets data (AP17)
- Automatisk gruppering av artiklar till produkter (AP18)
- Manuell arkivering, arkivsökning och återaktivering (AP19)

**Tillval:**
- Nya domäner för bilder och dokument (AP20)
- Avancerad förhandsvisning av fler filformat (AP21)

**Helt utanför:**
- Automatisk generering av artikelnummer (WB-nummer), regelmotor, AI-berikning, leverantörsportal, orderhantering, ombyggnad av affärssystem eller e-handel
- Sammanslagning av attribut och byte av datatyper (kräver eget städprojekt)
- Portal för upp till 40 användare hos delägarna (kan bli aktuellt långt senare)
- E-post- eller push-notiser

## 7. Vem gör vad

Dataflödet ser ut så här:

**Källor (Finfo, BASTA, BVB) → MagicBox → nya PIM → MagicBox → butiker och e-handel**, plus en separat koppling till Snicken.

| Part | Ansvar |
|---|---|
| **Vaimo** (kallas "PIM-partner" i dokumentet) | Själva PIM-systemet, PIM:s sida av integrationen, migrering, test, drift, utbildning, projektledning |
| **ITM8** | Kopplingar från källorna till MagicBox, MagicBox-sidan, Snickens koppling, befintlig bildlagring och länkar |
| **SFB** | Beslut, städa data, välja vad som ska flyttas, beställa export från C4, godkänna |
| **Snicken** | Tala om vilka artiklar de vill ha och hur de tar emot data |

**Viktigt:** ITM8:s arbete (AP07 till AP10) ska **inte** ingå i Vaimos pris. Vaimo ska lista det som externa beroenden, med ITM8:s pris om det finns. Ett pris som saknas får inte skrivas som noll.

Antagandet att ITM8 bygger Snicken-kopplingen är inte bekräftat. Alternativet att lägga Snicken inne i MagicBox ska redovisas som ALT01.

## 8. Teknisk förstudie först (AP01)

Innan det går att ge ett bindande pris behöver flera saker undersökas. Det sker i AP01, som ska ha **eget pris och tydligt slut** (inte en öppen förstudie). Resultatet ska kunna lämnas vidare till en annan leverantör.

AP01 ska ge:
- **Fältmatris**: lista över alla fält, vem som äger dem, vem som får ändra, regler för tomma värden
- **Identiteter och exempeldata**: hur artiklar, leverantörer, grupper, filer m.m. känns igen
- **Utbyteskontrakt**: exakt vad som skickas mellan PIM, MagicBox och Snicken, och hur fel hanteras
- **Fast Excel-mall**
- **Inventering av export och filer** från C4: vad finns, hur mycket, vad saknas
- **Reviderat estimat och plan** baserat på det som verifierats

Vaimo ska ange vad från förstudien som kan återanvändas och bara räkna på det som återstår.

## 9. Siffror att räkna med

| Vad | Värde |
|---|---|
| Artiklar | ca 1 400 000 |
| Produktgrupper | 22 442 |
| Bilder | 519 781 |
| Dokument (mest PDF) | 118 228 |
| Artiklar som administratörerna faktiskt jobbar med | ca 700 000 till 800 000 |
| Samtidiga användare | 2 |
| Urval i gränssnittet | minst 100 artiklar |
| Excel-import/export | 5 000 rader, klart inom 10 minuter (förslag) |
| Svarstid för sök, öppna, spara | max 3 sekunder i 95 % av fallen (förslag) |

Siffrorna är beräkningsgrund, inte beslut om att allt ska flyttas. SFB väljer senare vad som ska migreras.

## 10. Krav på drift

**Bestämt av SFB:**
- Max **en timmes** dataförlust vid haveri (RPO)
- Systemet igång igen inom **en arbetsdag** (RTO)
- Support under svensk kontorstid
- Test av återställning innan systemet går i drift
- Två miljöer: test och produktion
- Personliga inloggningar
- Om PIM ligger nere ska webben och bildlänkarna fortsätta fungera

**Förslag:** svar inom åtta supporttimmar, måndag till fredag kl. 8 till 17.

Vaimo föreslår själv teknik, hosting och säkerhetslösning.

## 11. Migrering

- SFB städar och väljer vad som ska flyttas.
- Vaimo ansvarar för mappning, importverktyg, körningar och kontroller.
- Grundestimatet ska innehålla **en provmigrering, en rättningskörning och en slutkörning**. Extra körningar prissätts per styck.
- Pris ska anges per extra 100 000 artiklar eller filer och per GB filöverföring.
- Alla attributdefinitioner ska följa med. Bara de tre kategoriträden flyttas som aktiva.
- Gamla dokumentversioner från C4 ska följa med (AP22, egen kostnadsrad).
- Om något inte går att få ut ur C4 behövs en prissatt lösning för att ändå komma åt det.

## 12. När är F1 godkänd?

SFB godkänner. Driftstart **stoppas** om något av detta inträffar:
- data har försvunnit
- egna texter eller värden har skrivits över
- obehöriga kommer åt systemet
- data når inte ut till mottagarna

Övriga fel kan godkännas om SFB uttryckligen säger ja och det finns en plan för att rätta dem. Felrättning och omtest före godkännande ska ingå i priset.

## 13. Kod, överlämning och utbildning

- **SFB ska äga koden** som skrivs för dem.
- Överlämningen ska göra det möjligt för en annan leverantör att ta över: källkod, tester, dokumentation, instruktioner, migreringsverktyg, konfiguration.
- Vaimo ska lista alla tredjepartskomponenter, licenser och löpande avgifter, och tala om vad som kräver fortsatt avtal med Vaimo.
- Ingår i priset: **två utbildningstillfällen** och **tio dagars extra stöd** efter driftstart.
- Löpande support efter det prissätts som återkommande tjänst.

## 14. Arbetspaketen i korthet

| Paket | Innehåll | Vem |
|---|---|---|
| AP01 | Teknisk förstudie och inventering | Vaimo (med ITM8) |
| AP02 | Datamodell | Vaimo |
| AP03 | Gränssnitt för administratörerna och berikning | Vaimo |
| AP04 | PIM:s integrationsgränssnitt | Vaimo |
| AP05 | Bilder, dokument och versioner | Vaimo |
| AP06 | Excel-import och export | Vaimo |
| AP07 | Källkopplingar till MagicBox | ITM8 |
| AP08 | MagicBox-anslutning och distribution | ITM8 |
| AP09 | Snickens koppling | ITM8 |
| AP10 | Befintliga bilder och länkar | ITM8 |
| AP11 | Migrering | Vaimo |
| AP12 | Gemensamt test och godkännande | Vaimo (med alla) |
| AP13 | Miljöer, drift och återställning | Vaimo |
| AP14 | Driftsättning, utbildning och överlämning | Vaimo |
| AP15 | Projektledning | Vaimo |
| AP16 | Tabellredigering | Vaimo |
| AP22 | Gamla dokumentversioner och historik | Vaimo |
| AP17 till AP19 | Version 2 | Vaimo, separat pris |
| AP20, AP21 | Tillval | Vaimo, separat pris |

Samma arbete får inte räknas i flera paket.

## 15. Största riskerna enligt SFB

| Risk | Vad Vaimo ska göra |
|---|---|
| C4 stängs innan nya systemet är klart | Visa realistisk plan och senaste datum för beslut. Annars föreslå nödlösning (ALT03) |
| Exporten från C4 är oprövad, data kan saknas | Ta fram exportprov i AP01, ange prisintervall |
| Okänd filmängd, tio års arkiv kan bli dyrt | Mät volymen, separera kostnader för original, arkiv och backup |
| Befintlig bildtjänst kanske inte går att använda | Kontrollera i AP01 |
| Olika tolkning av fält och grupper | Kontrollera mot verklig data |
| Beroenden mellan Vaimo, ITM8 och Snicken | Gemensam plan med testfönster och beslutspunkter |
| Massändring som går fel | Visa urval och fel innan man sparar, samma regler i tabell och Excel |

---

## Essensen

**Uppgiften:** Ge SFB ett estimat (pris, tid, bemanning) för att bygga ett nytt PIM som ersätter C4. Inte en beställning ännu.

**Förutsättningarna:**
1. C4 stängs, och det är den hårda tidsgränsen. Säg tydligt om ni hinner.
2. Räkna exakt på kravkatalogen version 1.3 (63 krav, 22 arbetspaket), så att svaret går att jämföra med andra leverantörer.
3. Lämna ett eget pris för den tekniska förstudien (AP01) **och** ett preliminärt estimat för resten av F1 redan nu. AP01 med eget pris och tydligt slut är ett krav. Att det bindande priset för de osäkra delarna kommer först efter AP01 är SFB:s beslutsordning. Osäkra delar ska fram till dess ha intervall eller enhetspriser.
4. ITM8:s arbete räknas inte in i Vaimos pris.
5. Återanvänd förstudien, ta inte betalt två gånger.
6. Egna förslag är välkomna, men separat.
7. SFB äger koden och ska kunna byta leverantör.
