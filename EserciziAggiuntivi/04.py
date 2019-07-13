"""
Napisati progam koji za recenicu sa ulaza prikazuje koliko se
puta ponavljalo svako slovo u recenici.

"""

def NumOccorenze (stringa):
    diz = {}
    for i in range (len(stringa)):
        chiave = stringa [i]
        valore = diz.get (chiave, 0)
        valore = valore + 1
        diz [chiave] = valore
    return diz

frase  = input ("Inserisci una frase ")
print (NumOccorenze (frase))
