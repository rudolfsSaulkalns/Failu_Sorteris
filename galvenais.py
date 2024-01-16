import os, shutil
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
from distutils.file_util import move_file
from distutils.dir_util import mkpath
import galapunkti

downloads = r"C:\Users\Rudolfs\Downloads - Copy"
downloadsTurp = r"C:\Users\Rudolfs\Downloads - Copy"

faili = os.listdir(downloads)

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
        if os.path.isdir(downloadsTurp + item):
            copy_tree(downloadsTurp + item, path + "\\" + item)
            remove_tree(downloadsTurp + item)
            continue
        else:
            shutil.move(downloadsTurp +"\\"+ item, path)
            continue
    return

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

for item in reversed(galapunkti.nekategorizeti):
    if item in galapunkti.nekategorizeti:
        galapunkti.filmas(item)
        galapunkti.matematika(item)
        galapunkti.dzjaava(item)
        galapunkti.datorgrafika(item)
        galapunkti.bildes(item)
        galapunkti.programmas(item)

for item in galapunkti.dokFold:
    galapunkti.matematika(item)
    galapunkti.dzjaava(item)
    galapunkti.datorgrafika(item)

skaitKat = len(galapunkti.dokFold) + len(galapunkti.musicFold) + len(galapunkti.progrFold) + len(galapunkti.bildFold) + len(galapunkti.filmFold)
print("kategorizēti faili: " + str(skaitKat))
print("nekategorizēti faili: "+str(len(galapunkti.nekategorizeti)))

def reporteris():
    print(str(len(galapunkti.katDat)+len(galapunkti.katMat)+len(galapunkti.katDzjav))+ " faili uz matematiku, dzjavu vai datorgrafiku")
    print(str(len(galapunkti.filmFold)) + " faili gatavi uz FILMAM")
    print(str(len(galapunkti.progrFold)) + " faili gatavi uz PROGRAMMAM")
    print(str(len(galapunkti.musicFold)) + " faili gatavi uz MUSICU")
    print(str(len(galapunkti.bildFold)) + " faili gatavi uz BILDES")
    print(str(len(galapunkti.dokFold)) + " faili ir nekategorizēti un paliek (nezinams galamerkis)")
    return

reporteris()

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
    else:
        print("nepareize parole")
        confirm()

confirm()
print("done")