#Failu sorteris
###Projekta uzdevums
Izveidot programmu kas automātiski nolasīs un kategorizēs failus lietotāja `downloads` mapē, un pārvietos tos uz lietotāja izveidotajām mapēm attiecīgajiem failiem.
###Izmantotās bibliotēkas
`os` un `shutil`, izmantotas lai veiktu darbības ar failiem. T.i. tos nolasīt, pārvietot, dzēst, rakstīt.
`distutils`, izmantota lai veiktu darbības ar mapēm, tās veidot pārvietot un dzēst.
`re`, izmantota lai salīdzinātu failu nosaukumus ar karogiem un atslēgvārdiem, un veiktu failu kategorizēšanu.
###pielotosanas metodes
Programma ir izvedota ļoti specifiski autora vajadzībām, tāpec citiem litotājiem tā var nebūt noderīga vai pat funkcionāla. Programmas `galapunkti.py` lapā ir irakstīti ceļi uz failu mapēm, karogi un funkcijas kas kategorizē katru failu lietotāja `downloads` mapē. Tāpēc, lai pievieotu janu kategoriju jauniem failu tipiem ir ne tikai nepieciešams izveidot jaunu/as mape un pierakstīt ceļu uz to programmas kodā, bet arī uzrakstīt funkcijas kas šos failus spēs atpazīt.
