# SFB berikning och PIM: återanvändning av förstudien i AP01

Vaimo, utkast 2026-11-16. Svar på kravspecifikationen avsnitt 1.1 och 7.1.

## Underlag som återanvänds

- Discoveryrapport v0.5 med bilagor C till M. Avsnitt 4 nuläge, 5 data audit, 6 målbild, 7 och bilaga K och L datamodell, 8 integrationspunkter, 10 paketordning. Bilaga G pain points och bilaga H kravregister.
- Data audit på C4-exporten 2026-09-30 med bruttolistan över egna egenskaper.
- Integrationsworkshop med SFB och ITM8 2026-10-08.
- Woody-Finfo, ITM8:s dokumentation v2. Berikningsfil Lokalt Sortiment 2026-06-11. Fältbeskrivning Vilma 2.8.0, 2025-11-10. Konverteringsregler för bilder från C4 till Azure.
- Datautdrag: full C4-export (3,4 miljoner artiklar, 1,2 TB filer), Finfo XML från två konton med förändringsfiler för en vecka, C4 till MagicBox-JSON och Finfo XML för referensartiklar, BMEcat-fält och en exempelexport till Snicken.

Plattformsspecifika delar av förstudien, som Happy Flow och datamodellen i Occtoo, återanvänds bara för innehållet, inte för tekniken.

## Per leverabel i avsnitt 7.1

| Leverabel | Förstudien täcker | Verifierat | Återstår i AP01 |
|---|---|---|---|
| Fältmatris | Data audit och bruttolista: egenskapsdefinitioner, 19 441 listvärden, cirka 2 400 egna egenskaper, ETIM. Fältbeskrivning Vilma 2.8.0 | Vilka egenskaper och värden som finns i C4 | Ägare, skyddsnivå, validering, tomvärde och mottagarmappning per fält. Startlistans sju egenskaper knutna till bestämda attribut, eftersom samma begrepp finns i flera, till exempel Langdmm och LANGDM |
| Identiteter och exempeldata | Bilaga K: förslag på artikelnyckel och prioritetsordning. 22 442 produktgrupper, 2 042 med tre eller fler variantegenskaper, 2 bundles. Referensartiklar | Gruppbeståndet och dess storlek | Sammansatt nyckel, leverantörs-id, manuella artiklar och exempel med samma GTIN. Kontroll av gruppregeln i B12 mot verkliga relationer |
| Utbyteskontrakt | Avsnitt 8.1: integrationspunkter, riktning, trigger och byggansvar. C4 till MagicBox-JSON. BMEcat-fält och exempelexport till Snicken | Vilka flöden som finns och vem som bygger dem | Fält, format, startleverans, förändringsleverans, kvittens, återförsök och fel per riktning. Kontroll av samma exempel med ITM8. Snickens bekräftelse av urval och format |
| Fast Excel-mall | Berikningsfil Lokalt Sortiment och SQARP:s Excelfiler | Dagens arbetssätt | Kolumner, redigerbara fält, relationsformat, rensningsmarkör och konflikthantering, med exempel |
| Export- och medieinventering | Data audit på 3 403 330 artiklar och 22 posttyper. 99,98 % av medieposterna pekar på en fil, 421 550 bilder och 75 912 dokument i urvalet, cirka 1,1 TB. Finfos förändringsfiler för en vecka | Bestånd och filvolym | Historik, filoriginal och äldre dokumentversioner. Ändringstoppar. Ägarskap för ImageMagick och Azure Storage. Åtkomst vid PIM-avbrott |
| Reviderat estimat och plan | Avsnitt 10.1: paketordning och beroenden. Öppna frågor i avsnitt 5.6 och 10.3 och bilaga K | Inget, förstudien gav inget estimat på kravbasen 1.3 | Estimat i klass 3 och plan, byggda på verifierade kontrakt, volymer och beslut |

Kvarvarande osäkerhet efter förstudien: dagens gränssnitt, exportformat för historik och dokumentversioner, och ändringsvolym med toppar. ITM8 medverkar i kontrakten, identifierarmappningen och medieinventeringen. Snicken medverkar i sitt kontrakt. Nuvarande part levererar historik och slutexport.

## Skillnader mot förstudien

Vi följer kravspecifikationen. Påverkan finns i estimatet.

- Förstudien räknar om webbstatus med regel. Kravspecifikationen låter administratören sätta den manuellt (PIM-W06).
- Förstudien arkiverar automatiskt. F1 har ingen automatisk arkivering (PIM-W07, B14).
- Förstudien flyttar BVB-kopplingen till PIM. Kravspecifikationen behåller den i MagicBox (PIM-I07).
- Förstudien låter SFB och Snicken bygga Snickenintegrationen. Kravspecifikationen antar ITM8 (AP09, B02).
- Förstudien lägger migreringen utanför projektet. Kravspecifikationen lägger den i AP11.
- Förstudien gör om textvärden för mått till tal. Kravspecifikationen utesluter generell enhetskonvertering (PIM-D03).
- Förstudien lägger bildkonvertering och URL:er i ett paket med oklar ägare. Kravspecifikationen lägger dem hos ITM8 i AP10.
- Förstudien föreslog Occtoo. Vi föreslår Medusa v2, och det påverkar inte kravbasen.
