import os, shutil
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
import galapunkti

downloads = r"C:\Users\Rudolfs\Downloads - Copy"

def end():
    reporteris()
    exit()

faili = os.listdir(downloads)
# print(len(faili))

# funkcija parskata vai fails pieder kadai kategorijai, salidzinot to ar 
# kategoriju karogiem
def parskats(nosaukums):
    tags = dokSk + filmSk + progrSk + musicSk + bildSk
    if tags >0:
        if dokSk > filmSk+progrSk+musicSk+bildSk:
            galapunkti.dokFold.append(nosaukums)
        elif filmSk > dokSk+progrSk+musicSk+bildSk:
            galapunkti.filmFold.append(nosaukums)
        elif progrSk > dokSk+filmSk+musicSk+bildSk:
            galapunkti.progrFold.append(nosaukums)
        elif musicSk > dokSk+filmSk+progrSk+bildSk:
            galapunkti.musicFold.append(nosaukums)
        elif bildSk > dokSk+filmSk+progrSk+musicSk:
            galapunkti.bildFold.append(nosaukums)
        else:
            galapunkti.nekategorizeti.append(nosaukums)
    else: 
        galapunkti.nekategorizeti.append(nosaukums)
    return

# funkcija reali parvieto failu no downloads foldera uz vajadzigo folderi
def parvietosana(mape,path):
    for item in mape:
        if os.path.isdir(downloads + item):
            copy_tree(downloads + item, path + "\\" + item)
            remove_tree(downloads + item)
            continue
        else:
            shutil.move(downloads +"\\"+ item, path)
            continue
    return

# cikls salidzina katra faila nosaukumu ar nodefinetajiem karogiem,
# pieskir katram failam skaitu ar to, cik un kadu kategoriju karogi tika pacelti, 
# un padod talak uz parskats() funkciju. parskats() funkcija tad izverte,
# kura kategorija failu ielikt
for item in faili:
    nosaukums = str(item)
    dokSk = 0; filmSk = 0; progrSk = 0; musicSk = 0; bildSk = 0

    res = [ele for ele in galapunkti.dokKarogi if(ele in nosaukums)]
    dokSk += len(res)

    res = [ele for ele in galapunkti.filmKarogi if(ele in nosaukums)]
    filmSk += len(res)

    res = [ele for ele in galapunkti.progrKarogi if(ele in nosaukums)]
    progrSk += len(res)

    res = [ele for ele in galapunkti.musicKarogi if(ele in nosaukums)]
    musicSk += len(res)

    res = [ele for ele in galapunkti.bildKarogi if(ele in nosaukums)]
    bildSk += len(res)

    parskats(nosaukums)

# izprinte sarakstu ar visiem failiem un to kategoriju
def reporteris():
    print(str(len(galapunkti.katDat)+len(galapunkti.katMat)+len(galapunkti.katDzjav))+ " faili uz matematiku, dzjavu vai datorgrafiku")
    for item in galapunkti.katMat:
        print(" Matemātika: " + item)
    for item in galapunkti.katDzjav:
        print(" Java:    " + item)
    for item in galapunkti.katDat:
        print(" datorgrf.:    " + item)
    print(str(len(galapunkti.filmFold)) + " faili gatavi uz FILMAM")
    for item in galapunkti.filmFold:
        print(" Filma:   " + item)
    print(str(len(galapunkti.progrFold)) + " faili gatavi uz PROGRAMMAM")
    for item in galapunkti.progrFold:
        print(" Programmas: " + item)
    print(str(len(galapunkti.musicFold)) + " faili gatavi uz MUSIKU")
    for item in galapunkti.musicFold:
        print(" Muzika:   " + item)
    print(str(len(galapunkti.bildFold)) + " faili gatavi uz BILDES")
    for item in galapunkti.bildFold:
        print(" Bildes:   " + item)
    print(str(len(galapunkti.nekategorizeti)) + " faili ir nekategorizēti un paliek (nezinams galamerkis)")
    for item in galapunkti.nekategorizeti:
        print(" Nav kat.:    " + item)
    for item in galapunkti.dokFold:
        print(" random dokumenti:    " + item)
    return
#end()

# dok fold kategorija tika samesti visi dokumentu tipa faili, kas ieklauj ari
# failus uz matematikas, javas un datorgrafikas mapem. Cikls iziet cauri 
# dokumentu folderim un izsijā failus kas pieder matematikas, javas un 
# datorgrafikas mapem
for item in (galapunkti.dokFold):
    galapunkti.matematika(item)
    galapunkti.dzjaava(item)
    galapunkti.datorgrafika(item)
# end()

# tiem failiem kuriem netika pieskirta kategorija pec salidzinasanas ar karogiem,
# tiks veikta parbaude ar atslegvardu kombinacijam, ja ari tad netiek atrasta 
# piederiba, tad tie paliek nekategorizeti un netiks nekur parvietoti
for item in reversed(galapunkti.nekategorizeti):
    galapunkti.filmas(item)
    galapunkti.matematika(item)
    galapunkti.dzjaava(item)
    galapunkti.datorgrafika(item)
    galapunkti.bildes(item)
    galapunkti.programmas(item)
# end()

# cikls parbauda vai failu kategorizesanas procesa nav radusies duplikati
# starp "nekategorizeti" un parejam kategorijam, ja ir, tad fails tiek nonemts
# ne nekategorizetajiem
galapunkti.salidzinajums(galapunkti.dokFold)
galapunkti.salidzinajums(galapunkti.nekategorizeti)

galapunkti.pazudusie()

# izprintee cik faili ir kategorizēti un cik nekategorizeti
skaitKat = len(galapunkti.katMat)+len(galapunkti.katDzjav)+len(galapunkti.katDat) + len(galapunkti.musicFold) + len(galapunkti.progrFold) + len(galapunkti.bildFold) + len(galapunkti.filmFold)
print("kategorizēti faili: " + str(skaitKat))
print("nekategorizēti faili: "+str(len(galapunkti.nekategorizeti)))


# apstiprināt darbibas
def confirm():
    parole = input("parole: ")
    if parole == "000":
        print("notiek kopesana...")  
        parvietosana(galapunkti.filmFold,    galapunkti.pathFilmas)
        parvietosana(galapunkti.progrFold,   galapunkti.pathProgr)
        parvietosana(galapunkti.musicFold,   galapunkti.pathMusic)
        parvietosana(galapunkti.bildFold,    galapunkti.pathBildes)
        parvietosana(galapunkti.katMat,      galapunkti.pathMatematika)
        parvietosana(galapunkti.katDzjav,    galapunkti.pathDzjaava)
        parvietosana(galapunkti.katDat,      galapunkti.pathDatorgrafika)
        return
    elif parole == "cancel":
        print("canceled")
        return
    elif parole == "report":
        reporteris()
        confirm()
    else:
        print("nepareize parole")
        confirm()

confirm()
print("done")