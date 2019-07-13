"""
1. U datoteci `gradovi-region.txt` date su informacije o nekim gradovima u regionu.
Svaki red datoteke sadrži sledeće informacije: naziv grada, naziv teritorije
u kojoj se nalazi dati grad i broj stanovnika grada.
 Ispred svake grupe gradova iz jedne drzave nalazi se naziv drzave.
Linija bez teksta oznacava da je zavrsena jedna grupa drzava.

a) Napraviti funkciju Ucitaj1, koja iz datoteke čita podatke o gradovima
i kao rezultat vraće recnik, gde je kljuc trojka (naziv drzave, naziv teritorije, naziv grada),
a odgovoarajuca  vrednost je broj stanovnika.
Funkcija ima jedan argument - putanju do datoteke koja sadrži podatke o gradovima.

"""

def Ucitaj1 (fname):
    risultato = {}
    f = open(fname, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        if "\t" not in linea:
        #if len(linea)< 15:
            drzava = linea.strip()
        else:
            elementi = linea.split("\t")
            for i in range(len(elementi)):
                elementi[i] = elementi[i].strip()
            grad = elementi[0]
            teritorija = elementi[1]
            populacija = int(float(elementi[2])*1000)
            risultato[(drzava, teritorija, grad)] = populacija
    f.close()
    return risultato

"""
b) Napraviti funkciju Ucitaj2, koja iz datoteke čita podatke o gradovima
i kao rezultat vraće recnik, gde je kljuc naziv drzave, a vrednost koja odgovara nazivu drzave
je lista tupli (naziv teritorije, naziv grada, broj stanovnika)
Funkcija ima jedan argument - putanju do datoteke koja sadrži podatke o gradovima.
"""

def Ucitaj2(fname):
    risultato = {}
    f = open(fname, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        if "\t" not in linea:
            drzava = linea.strip()
        else:
            elementi = linea.split("\t")
            for i in range(len(elementi)):
                elementi[i] = elementi[i].strip()
            grad = elementi[0]
            teritorija = elementi[1]
            populacija = int(float(elementi[2])*1000)
            valore = risultato.get(drzava, [])
            valore = valore + [(teritorija, grad, populacija)]
            risultato[drzava] = valore
    f.close()
    return risultato

"""
c) Napraviti funkciju Ucitaj3, koja iz datoteke čita podatke o gradovima
i kao rezultat vraće recnik, gde je kljuc naziv drzave, a vrednost koja odgovara nazivu drzave
je recnik kod koga je kljuc naziv grada kome odgovara par (naziv teritorije, broj stanovnika)
Funkcija ima jedan argument - putanju do datoteke koja sadrži podatke o gradovima.
"""

def Ucitaj3(fname):
    risultato = {}
    f = open(fname, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        if "\t" not in linea:
            drzava = linea.strip()
        else:
            elementi = linea.split("\t")
            for i in range(len(elementi)):
                elementi[i] = elementi[i].strip()
            grad = elementi[0]
            teritorija = elementi[1]
            populacija = int(float(elementi[2])*1000)
            dizGradovi = risultato.get(drzava, {})
            dizGradovi[grad]= (teritorija, populacija)
            risultato[drzava] = dizGradovi
    f.close()
    return risultato

"""
d) Napraviti funkciju Ucitaj4, koja iz datoteke čita podatke o gradovima
i kao rezultat vraće recnik, gde je kljuc naziv drzave, a vrednost koja odgovara nazivu drzave
je recnik kod koga je kljuc naziv teritorije kojoj odgovara lista parova (naziv grada, broj stanovnika)
Funkcija ima jedan argument - putanju do datoteke koja sadrži podatke o gradovima.

"""

def Ucitaj4(fname):
    risultato = {}
    f = open(fname, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        if "\t" not in linea:
            drzava = linea.strip()
        else:
            elementi = linea.split("\t")
            for i in range(len(elementi)):
                elementi[i] = elementi[i].strip()
            grad = elementi[0]
            teritorija = elementi[1]
            populacija = int(float(elementi[2])*1000)
            dizTeritorije = risultato.get(drzava, {})
            listaParova = dizTeritorije.get(teritorija, [])
            listaParova = listaParova + [(grad, populacija)]
            dizTeritorije[teritorija] = listaParova
            risultato[drzava] = dizTeritorije
    f.close()
    return risultato

"""
e) Napraviti funkciju Ucitaj5, koja iz datoteke čita podatke o gradovima
i kao rezultat vraće recnik, gde je kljuc naziv drzave, a vrednost koja odgovara nazivu drzave
je recnik kod koga je kljuc naziv teritorije kojoj odgovara  recnik sa kljucem naziv grada i vrednoscu broj stanovnika
Funkcija ima jedan argument - putanju do datoteke koja sadrži podatke o gradovima.

"""

def Ucitaj5 (fname):
    risultato = {}
    f = open(fname, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        if "\t" not in linea:
            drzava = linea.strip()
        else:
            elementi = linea.split("\t")
            for i in range(len(elementi)):
                elementi[i] = elementi[i].strip()
            grad = elementi[0]
            teritorija = elementi[1]
            populacija = int(float(elementi[2])*1000)
            dizTeritorije = risultato.get(drzava, {})
            dizGradovi = dizTeritorije.get(teritorija, {})
            dizGradovi[grad] = populacija
            dizTeritorije[teritorija] = dizGradovi
            risultato[drzava] = dizTeritorije
    f.close()
    return risultato

"""
f) napraviti funkciju NajmanjeStanovnika, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje naziv grada koji ima najmanje stanovnika.
"""

def NajmanjeStanovnika (dizA):
    minPopulacija = 10000000
    minGrad = ""
    for chiave in dizA.keys():
        #print(chiave)
        populacija = dizA[chiave]
        grad = chiave[2]
        if populacija < minPopulacija:
            minPopulacija = populacija
            minGrad = grad
    return minGrad

"""
g) napraviti funkciju NajmanjeStanovnikaNaTeritoriji, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje naziv grada na datoj teritoriji koji ima najmanje stanovnika.

"""
def NajmanjeStanovnikaNaTeritoriji(dizA, teritorija):
    minPopulacija = 10000000
    minGrad = ""
    for chiave in dizA.keys():
        populacija = dizA[chiave]
        grad = chiave[2]
        podrucje = chiave[1]
        if teritorija == podrucje:
            if populacija < minPopulacija:
                minPopulacija = populacija
                minGrad = grad
    return minGrad

"""
g) napraviti funkciju NajmanjeStanovnikaUDrzavi, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje naziv grada u toj drzavi koji ima najmanje stanovnika.
"""

def NajmanjeStanovnikaUDrzavi(gradovi, drzava):
    minPopulacija = 100000000
    minGrad = ""
    for chiave in gradovi.keys():
        populacija = gradovi[chiave]
        drz = chiave[0]
        grad = chiave [2]
        if drzava == drz:
            if populacija < minPopulacija:
                minPopulacija = populacija
                minGrad = grad
    return minGrad

"""
h) napraviti funkciju NajviseStanovnika2, koja za recnik sa strukturom kao u
dijelu zadatka b), određuje naziv grada koji ima najvise stanovnika.

"""
def NajviseStanovnika2(gradovi):
    maxPopulacija = 0
    maxGrad = ""
    for chiave in gradovi.keys():
        listaValori = gradovi[chiave]
        for i in range(len(listaValori)):
            populacija = gradovi[chiave][i][2]
            grad = gradovi[chiave][i][1]
            if populacija > maxPopulacija:
                maxPopulacija = populacija
                maxGrad = grad
    return maxGrad

"""
i) napraviti funkciju NajviseStanovnikaNaTeritoriji2, koja za recnik sa strukturom kao u
dijelu zadatka b), određuje naziv grada na datoj teritoriji koji ima najvise stanovnika.

"""

def NajviseStanovnikaNaTeritoriji2(gradovi, teritorija):
    maxPopulacija = 0
    maxGrad = ""
    for chiave in gradovi.keys():
        listaValori = gradovi[chiave]
        for i in range(len(listaValori)):
            populacija = gradovi[chiave][i][2]
            grad = gradovi[chiave][i][1]
            podrucje = gradovi[chiave][i][0]
            if teritorija == podrucje:
                if populacija > maxPopulacija:
                    maxPopulacija = populacija
                    maxGrad = grad
    return maxGrad

"""
j) napraviti funkciju NajviseStanovnikaUDrzavi2, koja za recnik sa strukturom kao u
dijelu zadatka b), određuje naziv grada u toj drzavi koji ima najvise stanovnika.

"""

def NajviseStanovnikaUDrzavi2(gradovi, drzava):
    maxPopulacija = 0
    maxGrad = ""
    for drz in gradovi.keys():
        listaValori = gradovi[drz]
        for i in range(len(listaValori)):
            populacija = gradovi[drz][i][2]
            grad = gradovi[drz][i][1]
            if drzava == drz:
                if populacija > maxPopulacija:
                    maxPopulacija = populacija
                    maxGrad = grad
    return maxGrad

"""
k) napraviti funkciju ProsjecnoStanovnika3, koja za recnik sa strukturom kao u
dijelu zadatka c), određuje projecan broj stanovnika u gradu.

"""
def ProsjecnoStanovnika3(gradovi):
    i = 0
    ukupnaPopulacija = 0
    for drzava in gradovi.keys():
        dizGradovi = gradovi[drzava]
        for grad in dizGradovi.keys():
            populacija = dizGradovi[grad][1]
            ukupnaPopulacija = ukupnaPopulacija + populacija
            i = i + 1
        prosjek = ukupnaPopulacija/i
    return prosjek


"""
la) napraviti funkciju ProsjecnoStanovnikaPoTeritoriji3, koja za recnik sa strukturom kao u
dijelu zadatka c), određuje rjecnik gdje za svaku teritoriju upisuje
koliko grad na toj teritoriji prosjecno ima stanovnika.
"""

def  ProsjecnoStanovnikaPoTeritoriji3a(gradovi):
    risultato = {}
    dizTeritorije = {}
    for drzava in gradovi.keys():
        dizGradovi = gradovi[drzava]
        for grad in dizGradovi.keys():
            teritorija = dizGradovi[grad][0]
            populacija = dizGradovi[grad][1]
            valore = dizTeritorije.get(teritorija, [0.0,0])
            ukupnaPopulacija = valore[0]
            brojGradova = valore[1]
            ukupnaPopulacija = ukupnaPopulacija + populacija
            brojGradova = brojGradova + 1
            dizTeritorije[teritorija] = [ukupnaPopulacija, brojGradova]
    for teritorija in dizTeritorije.keys():
        prosjek = dizTeritorije[teritorija][0]/dizTeritorije[teritorija][1]
        risultato[teritorija] = prosjek
    return risultato

"""
lb) kao la samo struktura podataka iz a).
"""

def ProsjecnoStanovnikaPoTeritoriji3b(gradovi):
    risultato = {}
    dizTeritorije = {}
    for chiave in gradovi.keys():
        populacija = gradovi[chiave]
        teritorija = chiave[1]
        grad = chiave[2]
        valore = dizTeritorije.get(teritorija, [0.0, 0])
        valore[0] = valore[0] + populacija
        valore[1] = valore[1] + 1
        dizTeritorije[teritorija] = valore
    for teritorija in dizTeritorije.keys():
        prosjek = dizTeritorije[teritorija][0]/dizTeritorije[teritorija][1]
        risultato[teritorija] = prosjek
    return risultato

"""
lc) kao la samo struktura podataka iz b).

"""
def ProsjecnoStanovnikaPoTeritoriji3c(gradovi):
    risultato = {}
    dizTeritorije = {}
    for drzava in gradovi.keys():
        listaTupli = gradovi[drzava]
        for i in range(len(listaTupli)):
            teritorija = listaTupli[i][0]
            populacija = listaTupli[i][2]
            valore = dizTeritorije.get(teritorija, [0.0, 0])
            valore[0] = valore[0]+ populacija
            valore[1] = valore[1] + 1
            dizTeritorije[teritorija] = valore
    for teritorija in dizTeritorije.keys():
        prosjek = dizTeritorije[teritorija][0]/dizTeritorije[teritorija][1]
        risultato[teritorija]= prosjek
    return risultato

"""
m) napraviti funkciju ProsjecnoStanovnikaUDrzavi3, koja za recnik sa strukturom kao u
dijelu zadatka c), određuje rjecnik koji za datu drzavu odredjuje koliko
grad u toj drzavi prosjecno ima stanovnika.
"""
def ProsjecnoStanovnikaUDrzavi3(gradovi):
    risultato = {}
    for drzava in gradovi.keys():
        dizGradovi = gradovi[drzava]
        i = 0
        ukupnaPopulacija = 0
        for grad in dizGradovi.keys():
            populacija = dizGradovi[grad][1]
            ukupnaPopulacija = ukupnaPopulacija + populacija
            i = i + 1
        risultato[drzava] = ukupnaPopulacija/i
    return risultato
"""
n) napraviti funkciju StanovnikaUDrzavi4, koja za recnik sa strukturom kao u
dijelu zadatka d), vrace recnik gdje je za svaku drzavu daje broj stanovnika u njoj

"""

def StanovnikaUDrzavi4(gradovi):
    risultato = {}
    for drzava in gradovi.keys():
        dizTeritorije = gradovi[drzava]
        ukupnaPopulacija = 0
        for teritorija in dizTeritorije.keys():
            lista = dizTeritorije[teritorija]
            for i in range(len(lista)):
                populacija = lista[i][1]
                ukupnaPopulacija = ukupnaPopulacija + populacija
                risultato[drzava] = ukupnaPopulacija
    return risultato

"""
o) napraviti funkciju NajviseStanovnikaUDrzavi4, koja za recnik sa strukturom kao u
dijelu zadatka d), vraca recnik gdje je za svaku drzavu dat naziv teritorije,
naziv grada i broj stanovnika
za najveci grad u toj drzavi.
"""

def NajviseStanovnikaUDrzavi4(gradovi):
    risultato = {}
    for drzava in gradovi.keys():
        dizTeritorije = gradovi[drzava]
        maxPopulacija = 0
        maxGrad = ""
        maxTeritorija = ""
        for teritorija in dizTeritorije.keys():
            lista = dizTeritorije[teritorija]
            for i in range(len(lista)):
                grad = lista[i][0]
                populacija = lista[i][1]
                if populacija > maxPopulacija:
                    maxPopulacija = populacija
                    maxGrad = grad
                    maxTeritorija = teritorija
        risultato[drzava] = (maxTeritorija, maxGrad, maxPopulacija)
    return risultato

"""
p) napraviti funkciju NajblizeProsjekuDrzave4, koja za recnik sa strukturom kao u
dijelu zadatka d), vrace recnik gdje je za svaku drzavu dat
prosjecan broj stanovnika u gradu te drzave,
naziv teritorije, naziv grada i broj stanovnika
za grad u toj drzavi sa brojem stanovnika najblizi prosjecnoj velicini grada u toj drzavi.
"""
def ProsjecnoStanovnikaUDrzavi4 (gradovi):
    risultato = {}
    dizUkupno = {}
    for drzava in gradovi.keys():
        dizTeritorije = gradovi[drzava]
        for teritorija in dizTeritorije.keys():
            lista = dizTeritorije[teritorija]
            for i in range(len(lista)):
                grad = lista[i][0]
                populacija = lista[i][1]
                valore = dizUkupno.get(drzava, [0.0, 0])
                valore[0] = valore[0] + populacija
                valore[1] = valore[1] + 1
            dizUkupno[drzava] = valore
    for drzava in dizUkupno.keys():
        prosjek = dizUkupno[drzava][0]/dizUkupno[drzava][1]
        risultato[drzava] = prosjek
    return risultato

def NajblizeProsjekuDrzave4(gradovi):
    risultato = {}
    dizProsjek = ProsjecnoStanovnikaUDrzavi4(gradovi)
    for drzava in gradovi.keys():
        dizTeritorije = gradovi[drzava]
        minRazlika = 100000000
        minGrad = ""
        minTeritorija = ""
        minPopulacija = 0
        for teritorija in dizTeritorije.keys():
            lista = dizTeritorije[teritorija]
            for i in range(len(lista)):
                grad = lista[i][0]
                populacija = lista[i][1]
                if drzava in dizProsjek.keys():
                    prosjek = dizProsjek[drzava]
                    razlika = abs(populacija - prosjek)
                    if razlika < minRazlika:
                        minRazlika = razlika
                        minGrad = grad
                        minTeritorija = teritorija
                        minPopulacija = populacija
                        risultato[drzava] = (prosjek, minTeritorija, minGrad, minPopulacija)
    return risultato
"""
q) napraviti funkciju StatistikaUDrzavi1, koja za recnik sa strukturom kao u
dijelu zadatka a), vrace recnik gdje je za svaku drzavu odredjen broj stanovnika
 u njoj, broj gradova i broj teritorija
"""
def StatistikaUDrzavi1(gradovi):
    risultato = {}
    pomocna = {}
    for chiave in gradovi.keys():
        drzava = chiave[0]
        teritorija = chiave[1]
        grad = chiave[2]
        populacija = gradovi[chiave]
        valore = pomocna.get(drzava, [0, [],[]])
        valore[0] = valore[0] + populacija
        valore[1] = valore[1] + [grad]
        if teritorija not in valore [2]:
            valore[2] = valore[2] + [teritorija]
        pomocna[drzava] = valore
    #print (pomocna)
    for drzava in pomocna.keys():
        ukupnaPopulacija = pomocna[drzava][0]
        listaGradova = pomocna[drzava][1]
        listaTeritorija = pomocna[drzava][2]
        risultato[drzava] = [ukupnaPopulacija, len(listaGradova), len(listaTeritorija)]
    return risultato

"""
r) napraviti funkciju StatistikaUDrzavi2, koja za recnik sa strukturom kao u
dijelu zadatka b), vrace recnik gdje je za svaku drzavu odredjen broj stanovnika
 u njoj, broj gradova i broj teritorija
"""

def StatistikaUDrzavi2(gradovi):
    risultato = {}
    pomocna = {}
    for drzava in gradovi.keys():
        listaTupli = gradovi[drzava]
        for i in range(len(listaTupli)):
            teritorija = listaTupli[i][0]
            grad = listaTupli[i][1]
            populacija = listaTupli[i][2]
            valore = pomocna.get(drzava, [0, [], []])
            valore[0] = valore[0] + populacija
            valore[1] = valore[1] + [grad]
            if teritorija not in valore[2]:
                valore[2] = valore[2] + [teritorija]
            pomocna[drzava] = valore
    for drzava in pomocna.keys():
        ukupnaPopulacija = pomocna[drzava][0]
        listaGradova = pomocna[drzava][1]
        listaTeritorija = pomocna[drzava][2]
        risultato[drzava] = (ukupnaPopulacija, len(listaGradova), len(listaTeritorija))
    return risultato

"""
t) napraviti funkciju StatistikaUDrzavi3, koja za recnik sa strukturom kao u
dijelu zadatka c), vraca recnik gdje je za svaku drzavu odredjen broj stanovnika
 u njoj, broj gradova i broj teritorija.

 """

def StatistikaUDrzavi3(gradovi):
    risultato = {}
    pomocna = {}
    for drzava in gradovi.keys():
        dizGradovi = gradovi[drzava]
        for grad in dizGradovi.keys():
            teritorija = dizGradovi[grad][0]
            populacija = dizGradovi[grad][1]
            valore = pomocna.get(drzava, [0, [], []])
            valore[0] = valore[0] + populacija
            valore[1] = valore[1] + [grad]
            if teritorija not in valore[2]:
                valore[2] = valore[2] + [teritorija]
            pomocna[drzava] = valore
    for drzava in pomocna.keys():
        ukupnaPopulacija = pomocna[drzava][0]
        listaGradova = pomocna[drzava][1]
        listaTeritorija = pomocna[drzava][2]
        risultato[drzava] = (ukupnaPopulacija, len(listaGradova), len(listaTeritorija))
    return risultato

"""
u) napraviti funkciju StatistikaUDrzavi4, koja za recnik sa strukturom kao u
dijelu zadatka d), vraca recnik gdje je za svaku drzavu odredjen broj stanovnika
 u njoj, broj gradova i broj teritorija.

 """

def StatistikaUDrzavi4(gradovi):
    risultato = {}
    pomocna = {}
    for drzava in gradovi.keys():
        dizTeritorije = gradovi[drzava]
        for teritorija in dizTeritorije.keys():
            listaTupli = dizTeritorije[teritorija]
            for i in range(len(listaTupli)):
                grad = listaTupli[i][0]
                populacija = listaTupli[i][1]
                valore = pomocna.get(drzava, [0,[],[]])
                valore[0] = valore[0] + populacija
                valore[1] = valore[1] +[grad]
                if teritorija not in valore[2]:
                    valore[2] = valore[2] + [teritorija]
                pomocna[drzava] = valore
    for drzava in pomocna.keys():
        ukupnaPopulacija = pomocna[drzava][0]
        listaGradova = pomocna[drzava][1]
        listaTeritorija = pomocna[drzava][2]
        risultato[drzava] = (ukupnaPopulacija, len(listaGradova), len(listaTeritorija))
    return risultato
"""
v) napraviti funkciju StatistikaUDrzavi5, koja za recnik sa strukturom kao u
dijelu zadatka e), vrace recnik gdje je za svaku drzavu odredjen broj stanovnika
u njoj, broj gradova i broj teritorija

"""
def StatistikaUDrzavi5(gradovi):
    pomocna = {}
    risultato = {}
    for drzava in gradovi.keys():
        dizTeritorije = gradovi[drzava]
        for teritorija in dizTeritorije.keys():
            dizGradovi = dizTeritorije[teritorija]
            for grad in dizGradovi.keys():
                populacija = dizGradovi[grad]
                valore = pomocna.get(drzava, [0, [], []])
                valore[0] = valore[0] + populacija
                valore[1] = valore[1] + [grad]
                if teritorija not in valore[2]:
                    valore[2] = valore[2] + [teritorija]
                pomocna[drzava] = valore
    for drzava in pomocna.keys():
        ukupnaPopulacija = pomocna[drzava][0]
        listaGradova = pomocna[drzava][1]
        listaTeritorija = pomocna [drzava][2]
        risultato[drzava] = (ukupnaPopulacija, len(listaGradova), len(listaTeritorija))
    return risultato

"""
w) napraviti funkciju NajdaljeProjekuDrzave5, koja za recnik sa strukturom kao u
dijelu zadatka e), vrace recnik gdje je za svaku drzavu dat prosjecan broj stanovnika
 u gradu te drzave, naziv teritorije, naziv grada i broj stanovnika
za grad u toj drzavi sa brojem stanovnika najdalji od prosjecne velicine grada u toj drzavi.

"""
def ProsjecnoStanovnikaUDrzavi5(gradovi):
    pomocna = {}
    risultato = {}
    for drzava in gradovi.keys():
        dizTeritorije = gradovi[drzava]
        for teritorija in dizTeritorije.keys():
            dizGradovi = dizTeritorije[teritorija]
            for grad in dizGradovi.keys():
                populacija = dizGradovi[grad]
                valore = pomocna.get(drzava, [0, 0])
                valore[0] = valore[0] + populacija
                valore[1] = valore[1] + 1
                pomocna[drzava] = valore
    for drzava in pomocna.keys():
        ukupnaPopulacija = pomocna[drzava][0]
        brojGradova = pomocna[drzava][1]
        risultato[drzava] = (ukupnaPopulacija/brojGradova)
    return risultato

def NajdaljeProjekuDrzave5(gradovi):
    risultato = {}
    dizProsjek = ProsjecnoStanovnikaUDrzavi5(gradovi)
    for drzava in gradovi.keys():
        dizTeritorije = gradovi[drzava]
        maxTeritorija = ""
        maxGrad = ""
        maxRazlika = 0
        for teritorija in dizTeritorije.keys():
            dizGradovi = dizTeritorije[teritorija]
            for grad in dizGradovi.keys():
                populacija = dizGradovi[grad]
                prosjek= dizProsjek[drzava]
                razlika = abs(populacija - prosjek)
                if razlika > maxRazlika:
                    maxRazlika = razlika
                    maxGrad = grad
                    maxTeritorija = teritorija
                    maxPopulacija = populacija
                    risultato[drzava] = (prosjek, maxTeritorija, maxGrad, maxPopulacija)
    return risultato

dizA = Ucitaj1("gradovi-region.txt")
print(dizA)
dizB = Ucitaj2("gradovi-region.txt")
print(dizB)
dizC = Ucitaj3("gradovi-region.txt")
print(dizC)
dizD = Ucitaj4("gradovi-region.txt")
print()
print(dizD)
dizE = Ucitaj5 ("gradovi-region.txt")
print ("----")
print(dizE)
print(NajmanjeStanovnika(dizA))
print(NajmanjeStanovnikaNaTeritoriji(dizA, "Beograd"))
print(NajmanjeStanovnikaUDrzavi(dizA, "Crna Gora"))
print(NajviseStanovnika2(dizB))
print(NajviseStanovnikaNaTeritoriji2(dizB, "Herceg Novi"))
print(NajviseStanovnikaUDrzavi2(dizB, "Crna Gora"))
print()
print(ProsjecnoStanovnika3(dizC))
print(ProsjecnoStanovnikaPoTeritoriji3a(dizC))
print(ProsjecnoStanovnikaPoTeritoriji3b(dizA))
print(ProsjecnoStanovnikaPoTeritoriji3c(dizB))
print (ProsjecnoStanovnikaUDrzavi3(dizC))
print(StanovnikaUDrzavi4(dizD))
print(NajviseStanovnikaUDrzavi4(dizD))
print(ProsjecnoStanovnikaUDrzavi4(dizD))
print(NajblizeProsjekuDrzave4(dizD))
print(StatistikaUDrzavi1(dizA))
print(StatistikaUDrzavi2(dizB))
print()
print(StatistikaUDrzavi3(dizC))
print(StatistikaUDrzavi4(dizD))
print(StatistikaUDrzavi5(dizE))
print(ProsjecnoStanovnikaUDrzavi5(dizE))
print(NajdaljeProjekuDrzave5(dizE))
