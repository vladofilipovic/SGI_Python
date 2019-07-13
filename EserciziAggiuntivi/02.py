#Napraviti funkciju koja sabira dva brojaself.
# Napraviti program koji ucitava dva cijela broja i kroiscenjem prethodno napravljene
#funkcije prikazuje njihov zbir.


def Somma (x,y):
    return x+y

a = float(input ("Inserire il primo numero "))
b = float(input ("Inserire il secondo numero "))
print("%.2f" %Somma (a,b))
