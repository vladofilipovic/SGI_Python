"""
U datoteci `gradovi-cg.txt` date su informacije o nekim gradovima u Crnoj Gori.
Svaki red datoteke sadrži sledeće informacije: redni broj grada (cio broj),
naziv grada, naziv teritorije u kojoj se nalazi dati grad i broj stanovnika grada.

a) Napraviti funkciju UcitajPodatkeGradovi, koja iz datoteke čita podatke o gradovima
i kao rezultat vraće odgovarajuću listu tuplova, gde svaka tupla sadrži redni broj grada,
naziv grada, naziv teritorije u kojoj se nalazi dati grad i broj stanovnika grada.
Funkcija ima jedan argument - putanju do datoteke koja sadrži podatke o gradovima.
"""

def UcitajPodatkeGradovi (stringa):
    f = open (stringa, "r")
    risultato = []
    linea = f.readline()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split("\t")
        for i in range (len(elementi)):
            elementi[i] = elementi[i].strip()
        broj = elementi[0].split(".")
        rbr = int(broj[0])
        #rbr = int(broj[0:])
        grad = elementi[1]
        teritorija = elementi[2]
        populacija = int(float(elementi[3])*1000)
        risultato = risultato + [(rbr, grad, teritorija, populacija)]
    f.close()
    #print (risultato)
    return risultato


"""
b) napraviti funkciju GradSaNajmanjeStanovnika, koja za listu tuplova sa strukturom kao u
dijelu zadatka a), određuje naziv grada koji ima najmanje stanovnika.
"""

def GradSaNajmanjeStanovnika(gradovi):
    minPopulacija = 100000000
    minGrad = ""
    for i in range (len(gradovi)):
        grad = gradovi[i][1]
        populacija = gradovi[i][3]
        if populacija < minPopulacija:
            minPopulacija = populacija
            minGrad = grad
    return minGrad





"""
b) napraviti funkciju GradSaNajviseStanovnika, koja za listu tuplova sa strukturom kao u
dijelu zadatka a), određuje naziv grada koji ima najvise stanovnika.
"""
def GradSaNajviseStanovnika(gradovi):
    maxPopulacija = 0
    maxGrad = ""
    for i in range(len(gradovi)):
        grad = gradovi[i][1]
        populacija = gradovi[i][3]
        if populacija > maxPopulacija:
            maxPopulacija = populacija
            maxGrad = grad
    return maxGrad


"""
c) napraviti funkciju GradNajbliziDatojVelicini, koja za listu tuplova sa strukturom kao u
dijelu zadatka a), određuje naziv grada koji je po broju stanovnika najbliži zadatoj veličini.
Zadata veličina se takodje daje kao parametar funkcije.

"""

def GradNajbliziDatojVelicini(gradovi, ciljnaVelicina):
    minRazlika = 100000000
    najbliziGrad = ""
    for i in range(len(gradovi)):
        grad = gradovi[i][1]
        populacija = gradovi[i][3]
        razlika = abs(ciljnaVelicina - populacija)
        if razlika < minRazlika:
            minRazlika = razlika
            najbliziGrad = grad
    return najbliziGrad



"""
d) napraviti funkciju RbrPoNazivu, koja za listu tuplova sa strukturom kao u
dijelu zadatka a), određuje redni broj grada koji ima dati naziv.
Ako takav grad ne postoji, funkcija treba da vrati -1.

"""

def RbrPoNazivu(gradovi, naziv):
    for i in range(len(gradovi)):
        grad = gradovi[i][1]
        rbr = gradovi[i][0]
        if naziv == grad:
            return rbr
    return -1




"""
e) napraviti funkciju RbrPoVelicini, koja za listu tuplova sa strukturom kao u
dijelu zadatka a), određuje redni broj grada koji ima datu velicinu.
Ako takav grad ne postoji, funkcija treba da vrati -1.

"""
#Vlado je stavio u tekstu zadatka da je parametar naziv, a trazi se velicina!!!!!

def RbrPoVelicini(gradovi, velicina):
    for i in range(len(gradovi)):
        rbr = gradovi[i][0]
        populacija = gradovi[i][3]
        if velicina == populacija:
            return rbr
    return -1



"""
e) napraviti funkciju GradoviNaTeritoriji, koja za listu tuplova sa strukturom kao u
dijelu zadatka a), određuje listu tuplova sa gradovima na datoj teritoriji.
Ako takvi gradovi ne postoje, funkcija treba da vrati praznu listu.

"""

def GradoviNaTeritoriji(gradovi, teritorija):
    risultato = []
    for i in range(len(gradovi)):
        podrucje = gradovi[i][2]
        rbr = gradovi[i][0]
        populacija = gradovi[i][3]
        grad = gradovi[i][1]
        if teritorija == podrucje:
            risultato = risultato + [(rbr,grad,populacija)]
    return risultato



"""
f) napraviti funkciju UkupnaPopulacija koja za listu tuplova sa strukturom kao u
dijelu zadatka a), određuje ukupnu populaciju.

"""
def UkupnaPopulacija (gradovi):
    total = 0
    for i in range(len(gradovi)):
        populacija = gradovi[i][3]
        total = total + populacija
    return total



"""
g) napraviti funkciju UkupnaIProsjecnaPopulacija koja za listu tuplova sa strukturom kao u
dijelu zadatka a), određuje ukupnu i prosjecnu populaciju.
"""

def UkupnaIProsjecnaPopulacija (gradovi):
    total = 0
    broj = 0
    for i in range(len(gradovi)):
        populacija = gradovi[i][3]
        total = total + populacija
        broj = broj + 1
        prosjek = total/broj
        rezultat = (total, prosjek)
    return rezultat

"""
h) Napraviti funkciju koja za listu tuplova sa strukturom kao u dijelu zadatka a),
odredjuje naziv grada cija je velicina najbliza prosjecnoj.
"""

def NajbliziProsjeku (gradovi):
    razlikaProsjek = 100000000
    najbliziGradProsjeku = ""
    prosjek = UkupnaIProsjecnaPopulacija(gradovi)[1]
    for i in range(len(gradovi)):
        grad = gradovi[i][1]
        populacija = gradovi [i][3]
        razlika = abs(populacija-prosjek)
        if razlika < razlikaProsjek:
            razlikaProsjek = razlika
            najbliziGradProsjeku = grad
    return najbliziGradProsjeku

def NajbliziProsjeku2 (gradovi):
    prosjek = UkupnaIProsjecnaPopulacija(gradovi)[1]
    grad = GradNajbliziDatojVelicini(gradovi, prosjek)
    return grad

x = UcitajPodatkeGradovi("gradovi-cg.txt")
print(x)
print(GradSaNajmanjeStanovnika(x))
print(GradSaNajviseStanovnika(x))
print(GradNajbliziDatojVelicini(x, 100000))
print(RbrPoNazivu(x,"Beograd"))
print (RbrPoVelicini(x,12739))
print(GradoviNaTeritoriji(x,"Kotor"))
print(UkupnaPopulacija(x))
print (UkupnaIProsjecnaPopulacija(x))
print(NajbliziProsjeku(x))
print(NajbliziProsjeku2(x))
