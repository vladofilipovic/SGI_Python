"""
Napisati program koji ucitava listu, odredjuje koliko ima duplikata u datoj
listi i na izlaz prikazuje one elemente koji se ponavljaju tri ili vise puta.


"""

def Duplicati (lista):
    diz = {}
    for i in range (len (lista)):
        chiave = lista [i]
        valore = diz.get (chiave, 0)
        valore = valore + 1
        diz [chiave] = valore
    return diz

n = int (input ( "Quanti elementi ha la lista "))
l = []
i = 0
while i < n:
    x = int (input ("Inserisci un numero "))
    l = l + [x]
    i = i + 1
print (l)
print (Duplicati (l))
