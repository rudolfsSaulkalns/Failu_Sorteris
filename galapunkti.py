import re

pathMatematika = r"C:\Users\Rudolfs\testings\dokumenti\matematika"
pathDzjaava = r"C:\Users\Rudolfs\testings\dokumenti\dzjaava"
pathDatorgrafika = r"C:\Users\Rudolfs\testings\dokumenti\datorgrafika"
pathFilmas = r"C:\Users\Rudolfs\testings\filmas"
pathProgr = r"C:\Users\Rudolfs\testings\programmas"
pathBildes = r"C:\Users\Rudolfs\testings\bildes"
pathMusic = r"C:\Users\Rudolfs\testings\music"

dokKarogi = [".xlsx",  ".pdf", ".doc", ".pptx"]
filmKarogi = ["1080p", "720p", "BluRay", "x264", "[5.1]", "DVD", ".mp4", ".srt",]
progrKarogi = [".zip", "installer",  'setup', ".exe",  ".msi",  ".iso", "indows", "driver", "win64"]
musicKarogi = [".mp3", ".flac"]
bildKarogi = ["creenshot", ".MOV", ".png", ".jpg", "IMG_", ".JPG", ".PNG"]

dokFold = []
filmFold = []
progrFold = []
musicFold = []
bildFold = []
nekategorizeti = []

katMat = []
katDzjav = []
katDat = []

def matematika(item):
    kategorija = katMat
    item2 = item.lower()
    if item and item[0].isdigit() and re.findall("lekcija.pptx", item2):       
        # print("matematika 1   " + item)
        katMat.append(item)
        kategorizesana(kategorija, item)
        return
    elif re.findall(".m$", item2) or re.findall("atlab", item2):       
        # print("matematika 2   " + item)
        katMat.append(item)
        kategorizesana(kategorija, item)
        return
    elif item and item[0].isdigit() and (re.findall("jēdziens", item2) or re.findall("vienādoj", item2) or re.findall("plakn", item2) or re.findall("funkcij", item2) or re.findall("telp", item2) or re.findall("darbības ar", item2)):       
        # print("matematika 3   " + item)
        katMat.append(item)
        kategorizesana(kategorija, item)
        return
    elif re.findall("formul", item2) or re.findall("atematika", item2):
        # print("matematika 4   " + item)
        katMat.append(item)
        kategorizesana(kategorija, item)
        return
    else: return

def dzjaava(item): 
    kategorija = katDzjav
    item2 = item.lower()
    if re.findall("lekcija_", item2) and re.findall("pdf$", item2):
        # print("dzjaava 1    " + item)
        katDzjav.append(item)
        kategorizesana(kategorija, item)
        return
    elif re.findall("sagatave", item2) or re.findall("java", item2) or re.findall("dzjaava", item2):
        # print("dzjaava 2  " + item)
        katDzjav.append(item)
        kategorizesana(kategorija, item)
        return
    elif item and item[0].isdigit() and (re.findall("_st.pdf", item2)):       
        # print("djaava 3   " + item)
        katDzjav.append(item)
        kategorizesana(kategorija, item)
        return
    else: return

def datorgrafika(item):
    kategorija = katDat
    if re.findall(".ipynb$", item):
        # print("datorgrafika     " + item)
        katDat.append(item)
        kategorizesana(kategorija, item)
        return
    return

def filmas(item):
    kategorija = filmFold
    if (re.findall(r"\("+"20"+"\d"+"\d"+r"\)", item) or re.findall(r"\("+"20"+"\d"+"\d"+r"\)", item)):
        # print("filma 1: " + item)
        filmFold.append(item)
        kategorizesana(kategorija, item)
        return
    # elif re.findall(karogs, item):
    #     # print("filma: " + item)
    #     skaitKat +=1
    #     return
    else: return

def programmas(item):
    kategorija = progrFold
    for karogs in progrKarogi:
        if re.findall(progrKarogi[0], item):
            # print("zip fails    " + item)
            progrFold.append(item)
            kategorizesana(kategorija, item)
            return
        elif re.findall(karogs, item):
            # print("programma    " + item)
            progrFold.append(item)
            kategorizesana(kategorija, item)
            return
        else: continue
    return

def bildes(item):
    kategorija = bildFold
    for karogs in bildKarogi:
        if re.findall(bildKarogi[0], item) or re.findall("screeni", item):
            # print("screenshots  " + item)
            bildFold.append(item)
            kategorizesana(kategorija, item)
            return
        elif re.findall(bildKarogi[1], item) and re.findall(bildKarogi[4], item):
            # print("icloud vid  " + item)
            bildFold.append(item)
            kategorizesana(kategorija, item)
            return
        elif re.findall(karogs, item):
            # print("cita bilde  " + item)
            bildFold.append(item)
            kategorizesana(kategorija, item)
            return
        else:
            continue
    return

# faili kurus parskats() ielika nekategorizetajos tiks parlikti uz attiecigo kategoriju
# si funkcija tiek palaista tikai tad, ja kada no galapunktu funkcijam ir noteikusas ka
# fails pieder kadai kategorijai.
def kategorizesana(item, kategorija):
    if item in nekategorizeti:
        nekategorizeti.remove(item)
        kategorija.append(item)
        return
    return
    # elif item not in nekategorizeti:
    #     nekategorizeti.append(item)
    #     kategorija.remove(item)
    #     return

def nezinamie(item):
    if item in nekategorizeti:
        print("tika atstats down folderi:   " + item)
    else: return

def kartosana():
    for item in reversed(nekategorizeti):
        if item in nekategorizeti:
            filmas(item)
            matematika(item)
            dzjaava(item)
            datorgrafika(item)
            bildes(item)
            programmas(item)

    for item in dokFold:
        matematika(item)
        dzjaava(item)
        datorgrafika(item)