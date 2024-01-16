# Failu sorteris

### Projekta uzdevums

Projekta uzdevums ir izveidot programmu kas atrisinātu autoram kādu ikdienas problēmu, izmantojot `Python` valodu. Kā problēmu, autors izvēlējas savu nesakārtoto `downloads` mapi, un uzrakstīt programmu kas to atrisinās. Lai atrisinātu šo problēmu, tika uzrakstīta programma kas automātiski nolasīa un kategorizē failus lietotāja `downloads` mapē, un pārvieto tos uz lietotāja izveidotajām mapēm attiecīgajiem failiem. 

Programmas realizēšanai ir jāizveido metodes pēc kurām varētu veikt failu atpazīšanu, kategorizēšanu un pārvietošanu. Lai veiktu programma spētu atpazīt vai kadai kategorijai pieder fails, ir izveidoti saraksti ar `karogiem` un tad programma meklē šos karogus faila nosaukumā un ja viens vai vairāki karogi tiek atrasti, fails tiek kategorizēts ar tā karoga kategoriju. Piemēram, lejuplādētām bildēm nosaukumā mēdz būt atribūts `IMG_` un sufiks `.png` vai `.jpg`, šādi un citi karogi (atribūti) tiek meklēti katra faila nosaukumā. Tie faili kuriem nav atrasts neviens karogs nosaukumā, vai arī ir vairāki karogi no dažādām kategorijām tiek kategorizēti kā `nekategorizēts`. Kad pirmā parbaude ir pabeigta, visiem failiem kas netika kategorizēti ar karogiem tiek veikta otra pārbaude kas, ar loģiskajām operācijām, meklē atslēgvārdu kombinācijas kādas mēdz būt failiem kas jau pieder kādai mapei. Piemēram, sufiks `.pptx` ir ļoti neskaidrs, tas var piederēt jebkādai kategorijai, un tāpēc nevar izmantot kā karogu kas noteiks kurai mapei šis fails pieder - tas tiek kategorizēts kā `nekategorizēts`. Tad pēc atslēgvārdu kombinācijām tiek parbāudīts vai šī faila nosaukumam pirmais simbols ir kāds cipars un beidzas ar "lekcija.pptx", jo tādā gadījumā šis fails pieder "matemātikas" mapei, ja šāda kombinācija nav nosaukumaam tad tiek pārbaudītas vēl daudzas citas. Galu galā, ja arī šis kombinācijas neatrod faila piederību kādai mapei, tad tās paliek nekategorizētas un netiks pārvietotas.

### Izmantotās bibliotēkas

`os` un `shutil`, izmantotas lai veiktu darbības ar failiem. T.i. tos nolasīt, pārvietot, dzēst, rakstīt.

`distutils`, izmantota lai veiktu darbības ar mapēm, tās veidot pārvietot un dzēst.

`re`, izmantota lai salīdzinātu failu nosaukumus ar karogiem un atslēgvārdiem, un veiktu failu kategorizēšanu.

### pielotosanas metodes

Programma ir izvedota ļoti specifiski autora vajadzībām, tāpec citiem litotājiem tā var nebūt noderīga vai pat funkcionāla. Programmas `galapunkti.py` lapā ir irakstīti ceļi uz failu mapēm, karogi un funkcijas kas kategorizē katru failu lietotāja `downloads` mapē. Tāpēc, lai pievieotu janu kategoriju jauniem failu tipiem ir ne tikai nepieciešams izveidot jaunu/as mapes un pierakstīt ceļu uz tām programmas kodā, bet arī uzrakstīt funkcijas kas šos failus spēs atpazīt.

Kad tiek palaista programmas `galvenais.py` kods, programma izprintēs konsolē cik daudz faili ir atpazīti un ir gatavi tikt parvietoti uz attiecīgajām mapēm, kā arī tiek izprintēts cik daudz failu netika atpazīti un tiks atstāti `downloads` mapē. Tad lietotājs apstiprina failu pārvietošanu ierakstot paroli, vai atceļ pārvietošanu paroles laukā ierakstot "cancel". Pēc tam programma uzsāk failu pārvietošanu un kad tas ir beidzies konsolē tiek izprintēts "done".
