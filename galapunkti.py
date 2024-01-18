import re

# galapunktu mapes
pathMatematika = r"C:\Users\Rudolfs\testings\dokumenti\matematika"
pathDzjaava = r"C:\Users\Rudolfs\testings\dokumenti\dzjaava"
pathDatorgrafika = r"C:\Users\Rudolfs\testings\dokumenti\datorgrafika"
pathFilmas = r"C:\Users\Rudolfs\testings\filmas"
pathProgr = r"C:\Users\Rudolfs\testings\programmas"
pathBildes = r"C:\Users\Rudolfs\testings\bildes"
pathMusic = r"C:\Users\Rudolfs\testings\music"

# karogi, kadi var būt failu nosaukumiem
dokKarogi = [".xlsx",  ".pdf", ".doc", ".pptx"]
filmKarogi = ["1080p", "720p", "BluRay", "x264", "[5.1]", "DVD", ".mp4", ".srt",]
progrKarogi = [".zip", "installer",  'setup', ".exe",  ".msi",  ".iso", "indows", "driver", "win64"]
musicKarogi = [".mp3", ".flac"]
bildKarogi = ["creenshot", ".MOV", ".png", ".jpg", "IMG_", ".JPG", ".PNG"]

# V Failu kategorijas V
dokFold = []
filmFold = []
progrFold = []
musicFold = []
bildFold = []
nekategorizeti = []

katMat = []
katDzjav = []
katDat = []

# Saraksts kura tiek uzglabati tie faili kuriem mainiisies kategorijas piederība,
# pec parbaudes ar atslēgvardu kombinacijam. Tas vajadzigs lai varētu pec tam
# tos failus izdzest no tiem sarakstiem kuros tie sakotneji tika ielikti
tempFaili = []


# V funkcijas kas atpazist failus pēc atslēgvārdu kombinācijām V
def matematika(item):
    item2 = item.lower()
    if item2 and item2[0].isdigit() and re.search(r"lekcija.pptx", item2):       
        # print("matematika 1   " + item)
        katMat.append(item)
        tempFaili.append(item)
        return
    elif re.search(".m$", item2) or re.search(r"matlab", item2):       
        # print("matematika 2   " + item)
        katMat.append(item)
        tempFaili.append(item)
        return
    elif item2 and item2[0].isdigit() and (re.findall(r"jēdziens", item2) or re.findall(r"vienādoj", item2) or re.findall(r"plakn", item2) or re.findall(r"funkcij", item2) or re.findall(r"telp", item2) or re.findall(r"darbības ar", item2)):       
        # print("matematika 3   " + item)
        katMat.append(item)
        tempFaili.append(item)
        return
    elif re.search(r"formul", item2) or re.search(r"atematika", item2):
        # print("matematika 4   " + item)
        katMat.append(item)
        tempFaili.append(item)
        return
    else: return

def dzjaava(item): 
    kategorija = katDzjav
    item2 = item.lower()
    if re.findall(r"lekcija_", item2) and re.findall(r"pdf", item2):
        # print("dzjaava 1    " + item)
        katDzjav.append(item)
        tempFaili.append(item)
        return
    elif re.findall("sagatave", item2) or re.findall("java", item2) or re.findall("dzjaava", item2):
        # print("dzjaava 2  " + item)
        katDzjav.append(item)
        tempFaili.append(item)
        return
    elif item and item[0].isdigit() and (re.findall(r"_st.pdf", item2)):       
        # print("djaava 3   " + item)
        katDzjav.append(item)
        tempFaili.append(item)
        return
    else: return

def datorgrafika(item):
    kategorija = katDat
    if re.search(r".ipynb", item):
        # print("datorgrafika     " + item)
        katDat.append(item)
        tempFaili.append(item)
        return
    elif re.search(r"atorgrafika", item):
        katDat.append(item)
        tempFaili.append(item) 
    return

def filmas(item):
    kategorija = filmFold
    if (re.findall(r"\("+"20"+"\d"+"\d"+r"\)", item) or re.findall(r"\("+"19"+"\d"+"\d"+r"\)", item)):
        # print("filma 1: " + item)
        filmFold.append(item)
        tempFaili.append(item)       
        return
    else: return

def programmas(item):
    kategorija = progrFold
    for karogs in progrKarogi:
        if re.findall(progrKarogi[0], item):
            # print("zip fails    " + item)
            progrFold.append(item)  
            tempFaili.append(item)                    
            return
        elif re.findall(karogs, item):
            # print("programma    " + item)
            progrFold.append(item)
            tempFaili.append(item)            
            return
        else: continue
    return

def bildes(item):
    kategorija = bildFold
    for karogs in bildKarogi:
        if re.findall(bildKarogi[0], item) or re.findall(r"screeni", item):
            # print("screenshots  " + item)
            bildFold.append(item)  
            tempFaili.append(item)                    
            return
        elif re.findall(bildKarogi[1], item) and re.findall(bildKarogi[4], item):
            # print("icloud vid  " + item)
            bildFold.append(item) 
            tempFaili.append(item)
            return
        elif re.findall(karogs, item):
            # print("cita bilde  " + item)
            bildFold.append(item) 
            tempFaili.append(item)      
            return
        else:
            continue
    return

# funkcija parbauda dotaja mapee atrodas kads fails kas ari atrodas "tempFaili", 
# sarakstā. ja abos sarakstos fails tiek atrasts, tas tiek izdzests no padotās
# mapes
def salidzinajums(folderis):
    for ele in reversed(folderis):
        for checks in tempFaili:
            if ele == checks:
                folderis.remove(ele)

# atlikusie faili dokFold kategorija (tiem kuriem neatrada konkretas kategorijas),
# tiek parvietoti uz nekategorizeto kategoriju
def pazudusie():
    for item in reversed(dokFold):
        nekategorizeti.append(item)
        dokFold.remove(item)