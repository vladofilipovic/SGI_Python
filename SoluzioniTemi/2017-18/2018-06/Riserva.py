# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Riserva01'

##########################################################
# INTRODUZIONE
##########################################################
#
# I file descritti qua di seguito contengono informazioni sui movimenti
# di una popolazione di orsi che vivono in un parco naturale.
# Il rilevamento della posizione di un orso non e' continuo ma avviene solamente
# quando l'orso passa vicino a certi punti (chiamati postazioni di rilevazione).
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e alcuni file di dati.
# I file con i dati sono:
#
# - File 1) distanze.csv
#   Il file memorizza le distanze tra le postazioni di rilevazione.
#   Una postazione di rilevazione e' identificata da una lettera
#   maiuscola dell'alfabeto.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#        Postazione1;Postazione2;Distanza
#        A;B;211\r\n
#        A;C;470\r\n
#        A;D;275\r\n
#        A;E;229\r\n
#        A;F;290\r\n
#        A;G;299\r\n
#        A;H;348\r\n
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo.
#   Nell'esempio qua sopra, la prima riga di dati ci dice la
#   postazione A dista 211 metri dalla postazione B.
#   Nota bene: se nel file e' presente la distanza tra A e B (come
#   nell'esempio qua sopra), per risparmiare spazio non viene memorizzata
#   la distanza tra B ed A, visto che e' identica.
#
#
# - File 2) percorsi.csv
#   Questo file memorizza lo spostamento fatto dagli orsi
#   nelle giornate di osservazione.
#   Un esempio del contenuto del file e' il seguente.
#   Nella prima riga c'e' intestazione del file.
#   Nell'esempio non considerate il simbolo di # e gli spazi.
#
#      id_orso;data;Postazione1;Postazione2;...;PostazioneN\r\n
#      0;01/03/2010;J;Y;W\r\n
#      1;01/03/2010;U;Q\r\n
#      2;01/03/2010;V;A;J;Z;I;Q\r\n
#      ...
#
#   Ogni riga contiene informazioni sul percorso svolto da un orso in uno specifico giorno.
#   Per esempio, la prima riga di dati
#   0;01/03/2010;J;Y;W
#   ci dice che l'orso 0 il giorno 01/03/2010 ha svolto un percorso che e' passato per le
#   postazioni di rilevamento J, Y e W (nell'ordine con cui sono elencate).
#   Le postazioni di rilevamento sono identifiate con le
#   Lettere dell'alfabeto. I percorsi svolti dagli orsi possono toccare un
#   numero variabile di postazioni, per questo motivo il numero di postazioni toccate
#   puo' variare da una riga all'altra.


##########################################################
# DESCRIZIONE DEL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spieghera' cosa fare in dettaglio.
# Controllate nel corpo principale del programma (in fondo
# allo script), come vengono invocate le funzioni che
# implementerete.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
# Se volete potete implementare delle funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.

##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome='Sostituiscimi con il cognome' # inserisci qua il tuo cognome
nome='Sostituiscimi con il nome' # inserisci qua il tuo nome


# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file contenente le distanze tra le postazioni.
#   La funzione deve restituire le informazioni sulle distanze tra postazioni,
#   sotto forma di un dizionario con la struttura descritta nell'esempio seguente:
#         {
#          'AB':518, 'BC':231,
#          ...
#         }
#   La prima coppia chiave valore nell'esempio qua sopra indica che la distanza tra
#   la postazione A e la postazione B e' di 518 metri, la seconda coppia chiave
#   valore indica che la distanza tra la postazione B e la postazione C e' 231 metri.
#   Si ricorda che ogni singola postazione e' contraddistinta da un'unica lettera dell'alfabeto.
#   Per maggiori informazioni sui dati coinvolti si faccia riferimento
#   alla descrizione del file contenente i dati.
#   Nell'esempio qua sopra le distanze devono essere valori interi, mentre la chiave
#   deve essere una stringa formata dalle due postazioni coinvolte.
def leggiDistanzePostazioni(filename):
    risultato = {}
    f = open (filename, "r")
    linea = f.readline()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range(len(elementi)):
            elementi[i] = elementi[i].strip()
        daA = elementi[0] + elementi[1]
        distanza = int(elementi[2])
        risultato[daA] = distanza
    f.close()
    #print(risultato)
    return risultato





# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con le informazioni sulle postazioni raggiunte
#   dagli orsi durante gli spostamenti.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#              [ (id_orso, giorno, stringa_percorso), (id_orso, giorno, stringa_percorso), ...   ]
#   Per esempio, la funzione leggendo le seguenti righe del file (i \r\n sono stati omessi)
#        id_orso;data;Postazione1;Postazione2;...
#        0;01/03/2010;J;Y;W
#        2;01/03/2010;V;A;J;Z;I;Q
#        ...
#   dovrebbe restituire la seguente struttura dati:
#        [ (0,'01/03/2010', 'JYW'),  (2,'01/03/2010', 'VAJZIQ'), ... ]
#   Ogni elemento della lista e' una tupla che contiene, l'id dell'orso, la data in cui l'orso
#   ha svolto il suo percorso e una stringa formata dalle lettere delle Postazioni toccate dall'orso.
def caricaPercorsi(fname):
    risultato = []
    f = open (fname, "r")
    linea = f.readline()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range(len(elementi)):
            elementi[i] = elementi[i].strip()
        idOrso = int(elementi[0])
        giorno = elementi[1]
        i = 2
        stringaPercorso = ""
        while i < len(elementi):
            stringaPercorso = stringaPercorso + elementi[i]
            i = i + 1
        risultato = risultato + [(idOrso, giorno, stringaPercorso)]
    f.close()
    #print(risultato)
    return risultato

    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


# - La funzione seguente accetta come parametri in ingresso
#   le strutture dati restituite rispettivamente dalle funzioni
#   leggiDistanzePostazioni() e caricaPercorsi().
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#        {id_orso1:totale_strada_percorsa1, id_orso2:totale_strada_percorsa2, ...}
#           ...
#   dove per ogni orso deve essere calcolato il totale dello spazio percorso sulla
#   base dei dati ricevuti in ingresso.
def calcolaLunghezzaCammini(distanze, percorsi):
    risultato = {}
    for i in range (len(percorsi)):
        idOrso = percorsi[i][0]
        stringaPercorso = percorsi[i][2]
        totPercorso = 0
        for i in range(len(stringaPercorso)-1):
            daA = stringaPercorso[i]+stringaPercorso[i+1]
            if daA in distanze.keys():
                totPercorso = totPercorso + distanze[daA]
            daA2 = stringaPercorso[i+1] + stringaPercorso[i]
            if daA2 in distanze.keys():
                totPercorso = totPercorso + distanze[daA2]
        risultato[idOrso] = totPercorso
    print(risultato)
    return risultato




# - La funzione seguente classifica una distanza percorsa in scaglioni.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, dovete SOLO USARLA negli
#   esercizi seguenti.
def categoriaOrso(distanza):
    if distanza < 300:
        return 'Ammalato'
    elif distanza <500:
        return 'Pigro'
    elif distanza <1000:
        return 'Ok'
    else:
        return 'Iperattivo'


# - La funzione seguente accetta in ingresso la struttura dati restituita dalla funzione calcolaLunghezzaCammini().
#   La funzione deve classificare le distane totali percorse dagli orsi in scaglioni utilizzando la funzione dichiarata qua sopra.
#   La funzione deve restituire la seguente struttura dati
#   { 'Ammalato':[id_orso, metri_percorsi], 'Pigro':[id_orso, metri_percorsi], ...}
#   In cui per ogni categoria vengono riportati i dati dell'orso (appartenente alla categoria) che ha percorso piu' strada.
def individua(lunghezza):
    risultato={"Ammalato": [0,0], "Pigro":[0,0], "Ok":[0,0], "Iperattivo":[0,0]}
    for item in lunghezza.items():
        idOrso = item[0]
        totPercorso = item[1]
        categoria = categoriaOrso(totPercorso)
        if totPercorso > risultato[categoria][1]:
            risultato[categoria][1] = totPercorso
            risultato[categoria][0] = idOrso
    print(risultato)
    return risultato



# - La funzione seguente accetta in ingresso la struttura dati
#   restituita dalla funzione caricaPercorsi().
#   La funzione deve individuare l'id dell'orso che per primo arriva a visitare
#   tutte le stazioni A, B, C, D, E, F, G, H, I in un qualsiasi ordine.
#   Considerate i dati ottenuti dalla funzione caricaPercorsi()
#   come se fossero ordinati temporalmente.
def Tutto1 (dizTappa):
    for i in dizTappa.keys():
        if dizTappa[i] == 0:
            return 0
    return 1

def giramondo(percorsi):
    stazioniVisitate = {}
    for i in range(len(percorsi)):
        idOrso = percorsi[i][0]
        tappa = percorsi[i][2]
        dizTappa = stazioniVisitate.get(idOrso, {"A":0, "B": 0, "C": 0, "D": 0, "E":0, "F": 0, "G":0, "H":0, "I":0} )
        for j in range(len(tappa)):
            if tappa[j] in ["A","B","C", "D", "E", "F", "G", "H", "I"]:
                dizTappa[tappa[j]] = 1
        stazioniVisitate[idOrso] = dizTappa
        #print(dizTappa)
        if Tutto1(dizTappa):
            return idOrso
    return -1




##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('Ciao %s, %s .' % (nome, cognome))

print("1) Eseguo la funzione leggiDistanzePostazioni: ")
fname1='distanze.csv'
dist = leggiDistanzePostazioni(fname1)
print(dist)

print('2) Eseguo la funzione caricaPercorsi: ')
fname2='percorsi.csv'
perc = caricaPercorsi(fname2)
print(perc)

print('3) Eseguo la funzione calcolaLunghezzaCammini: ')
lung = calcolaLunghezzaCammini(dist, perc)
print(lung)

print('4) Eseguo la funzione categoriaOrso: ')
categoria = categoriaOrso(5500)
print(categoria)

print('Eseguo la funzione individua: ')
ris = individua(lung)
print(ris)

print('5) Eseguo la funzione giramondo: ')
ris = giramondo(perc)
print(ris)


print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
