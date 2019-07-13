"""
Napisati program koji sortira sve znake unesene recenice

"""

f = input ("Inserisci una frase ")
l = sorted (f)
for i in range (len(l)):
    risultato = l [i]
    print (risultato, end = " ")
