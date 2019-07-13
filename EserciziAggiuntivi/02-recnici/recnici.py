"""
U datoteci `gradovi-cg.txt` date su informacije o nekim gradovima u Crnoj Gori.
Svaki red datoteke sadrži sledeće informacije: redni broj grada (cio broj),
naziv grada, naziv teritorije u kojoj se nalazi dati grad i broj stanovnika grada.

a) Napraviti funkciju UcitajGradovi, koja iz datoteke čita podatke o gradovima
i kao rezultat vraće recnik, gde je kljuc naziv grada, a odgovoarajuca  vrednost je
tupla koja sadrži redni broj grada, teritoriu u kojoj se nalazi dati grad i broj stanovnika.
Funkcija ima jedan argument - putanju do datoteke koja sadrži podatke o gradovima.

"""

def UcitajGradovi(gradovi):
    risultato = {}
    f = open(gradovi, "r")
    linea = f.readline()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split("\t")
        for i in range(len(elementi)):
            elementi[i] = elementi[i].strip()
        broj = elementi[0].split(".")
        rbr = int(broj[0])
        grad = elementi[1]
        teritorija = elementi[2]
        populacija = int(float(elementi[3])*1000)
        risultato[grad] = (rbr, teritorija, populacija)
    return risultato


"""
b) napraviti funkciju NajmanjeStanovnikaIma, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje naziv grada koji ima najmanje stanovnika.
"""

def NajmanjeStanovnikaIma(gradovi):
    minPopulacija = 10000000
    minGrad = ""
    for grad in gradovi.keys():
        populacija = gradovi[grad][2]
        if populacija < minPopulacija:
            minPopulacija = populacija
            minGrad = grad
    return minGrad

"""
c) napraviti funkciju NajviseStanovnikaIma, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje naziv grada koji ima najvise stanovnika.

"""

def NajviseStanovnikaIma(gradovi):
    maxPopulacija = 0
    maxGrad = ""
    for grad in gradovi.keys():
        populacija = gradovi[grad][2]
        if populacija > maxPopulacija:
            maxPopulacija = populacija
            maxGrad = grad
    return maxGrad

"""
d) napraviti funkciju NajbliziDatojVeliciniJe, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje naziv grada koji je po broju stanovnika najbliži zadatoj veličini.

"""

def NajbliziDatojVeliciniJe(gradovi, ciljnaVelicina):
    najmanjaRazlika = 100000000
    najbliziGrad = ""
    for grad in gradovi.keys():
        populacija = gradovi[grad][2]
        razlika = abs(ciljnaVelicina - populacija)
        if razlika < najmanjaRazlika:
            najmanjaRazlika = razlika
            najbliziGrad = grad
    return najbliziGrad

"""
e) napraviti funkciju RbrPoNazivu, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje redni broj grada koji ima dati naziv.
Ako takav grad ne postoji, funkcija treba da vrati -1.

"""

def RbrPoNazivu(gradovi, naziv):
    for grad in gradovi.keys():
        rbr = gradovi[grad][0]
        if naziv == grad:
            return rbr
    return -1

"""
f) napraviti funkciju RbrPoVelicini, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje redni broj grada koji ima datu velicinu.
Ako takav grad ne postoji, funkcija treba da vrati -1.

"""

def RbrPoVelicini(gradovi, velicina):
    for grad in gradovi.keys():
        rbr = gradovi[grad][0]
        populacija = gradovi[grad][2]
        if velicina == populacija:
            return rbr
    return -1

"""
g) napraviti funkciju TeritorijePopulacija, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje recnik sa informacijama o teritorijama, gde je
kljuc naziv teritorije, a vrednost je ukupan broj stanovnika na toj teritoriji.

"""

def TeritorijePopulacija(gradovi):
    risultato = {}
    for grad in gradovi.keys():
        teritorija = gradovi[grad][1]
        populacija = gradovi[grad][2]
        ukupnaPopulacija = risultato.get(teritorija, 0)
        ukupnaPopulacija = ukupnaPopulacija + populacija
        risultato[teritorija] = ukupnaPopulacija
    return risultato

"""
h) Napraviti funkciju TeritorijeGradovi, koja za recnik sa strukturom kao u
dijelu zadatka a), određuje recnik sa informacijama o teritorijama, gde je
kljuc naziv teritorije, a vrednost je lista svih gradova na toj teritoriji.
"""

def TeritorijeGradovi(gradovi):
    risultato = {}
    for grad in gradovi.keys():
        teritorija = gradovi[grad][1]
        listaGradovi = risultato.get(teritorija, [])
        listaGradovi = listaGradovi + [grad]
        risultato[teritorija] = listaGradovi
    return risultato

"""
i) Za rjecnik iz g) i napraviti funkciju koja racuna prosjecnu populaciju
po teritoriji.

"""

def ProsjecnaPopulacijaPoTeritoriji (dizPop):
    broj = 0
    ukupnaPopulacija = 0
    for teritorija in dizPop.keys():
        populacija = dizPop[teritorija]
        ukupnaPopulacija = ukupnaPopulacija + populacija
        broj = broj + 1
    prosjek = ukupnaPopulacija/broj
    return prosjek


x = UcitajGradovi("gradovi-cg.txt")
print(x)
print(NajmanjeStanovnikaIma(x))
print(NajviseStanovnikaIma(x))
print(NajbliziDatojVeliciniJe(x, 3000))
print(RbrPoNazivu(x,"Beograd"))
print(RbrPoVelicini(x,21377))
y = TeritorijePopulacija(x)
print(y)
print(TeritorijeGradovi(x))
print(ProsjecnaPopulacijaPoTeritoriji(y))
