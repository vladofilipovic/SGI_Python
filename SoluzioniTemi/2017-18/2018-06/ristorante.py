# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Ristorante02'

##########################################################
# INTRODUZIONE
##########################################################
#
# I file descritti qua di seguito contengono informazioni sulle
# consumazioni vendute da un ristorante.
#
#
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e alcuni
# file di dati.
# I file con i dati sono:
#
# - File 1) prezzi.csv
#   Il file contiene i prezzi di listino delle pietanze e delle
#   bevande vendute dal ristorante.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#      ID_Pietanza;Nome;PrezzoUnitario\r\n
#      0;Gnocco Fritto;12\r\n
#      1;Cheese burger;10\r\n
#      2;Chicken burger;9\r\n
#      3;Gligliata mista;16\r\n
#      ...
#      22;Grappa;8\r\n
#      23;Caffe;1\r\n
#      24;Succo di frutta;3\r\n
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo.
#   Le informazioni memorizzate sono le seguenti:
#   - ID_Pietanza. Un valore numerico che identifica univocamente la pietanza.
#     Per comodita', sono presenti anche le bevande in coda ai cibi.
#   - Prezzo_Unitario. Il prezzo di una unita' venduta (una unita'
#     e' un piatto per un cibo o un bicchiere per una bevanda).
#
#
# - File 2) consumazioni.csv
#   Il file contiene l'elenco delle pietanze e delle
#   bevande acquistate dai clienti.
#   Un esempio del contenuto del file e' il seguente.
#   Nella prima riga c'e' intestazione del file.
#   Nell'esempio non considerate il simbolo di # e gli spazi.
#
#      Data;ID_Cliente;Cod_Prodotto1;QT1;Cod_Prodotto2;QT2;...\r\n
#      25/01/2010;214;p13;q2\r\n
#      25/01/2010;289;p23;q4\r\n
#      25/01/2010;103;p21;q3\r\n
#      25/01/2010;406;p7;q2;p16;q3\r\n
#      25/01/2010;411;p3;q4;p19;q4\r\n
#      ...
#
#   Ogni riga contiene informazioni sui cibi acquistati da un cliente in uno specifico giorno.
#   Il primo elemento di una riga e' il giorno in cui e' avvenuto il pasto,
#   il secondo elemento e' l'id numerico che identifica univocamente un cliente.
#   Seguono poi un numero variabile di informazioni sui cibi acquistati.
#   Le informazioni sui cibi acquistati sono rappresentate da coppie di dati consecutivi,
#   dove ogni coppia e' formata da Cod_Prodotto e Quantita' del prodotto acquistato.
#   Il numero dei dati varia di riga in riga perche' clienti diversi possono acquistare diverse
#   tipologie di cibi. Ricapitolando, in una riga, i dati presenti sono:
#   - La data della consumazione
#   - L'id del cliente che ha acquistato il cibo.
#   - Seguono delle coppie di dati cosi' formate
#     * Identificatore univoco del prodotto venduto (preceduto dalla lettera p)
#     * Quantita' di prodotto acquistata (preceduto dalla lettera q). Una unita'
#       e' un piatto per un cibo o un bicchiere per una bevanda.
#


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
#   ingresso il nome del file contenente i prezzi dei cibi e delle bevante vendute dal ristorante
#   La funzione deve restituire un dizionario con la struttura descritta nell'esempio seguente:
#         {
#          id_pietanza1:prezzo_unitario_pietanza1,
#          id_pietanza2:prezzo_unitario_pietanza2,
#          ...
#         }
#   Per ogni cibo o bevanda, nel dizionario restituito sara' presente una coppia chiave:valore.
#   Per maggiori informazioni sui dati coinvolti si faccia riferimento alla descrizione del file
#   contenente i dati elaborati da questa funzione.
#   Nell'esempio qua sopra id_pietanza e prezzo_unitario_pietanza devono essere valori interi.
#   I prezzi nel file di partenza sono sempre arrotondati all'unita'.
#   Dai dati restituiti devono essere escluse le intestazioni del file.
def leggiPrezzi(filename):
    risultato = {}
    f = open(filename, "r")
    linea = f.readline()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range(len(elementi)):
            elementi[i] = elementi[i].strip()
        #print(elementi)
        idPietanza = int(elementi[0])
        prezzoUnitario = int(elementi[2])
        risultato[idPietanza] = prezzoUnitario
    f.close()
    return risultato


# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con le informazioni sulle consumazioni effettuate dagli utenti.
#   La funzione deve restituire un dizionario di stringhe e liste come nell'esempio seguente.
#              { 'clienti':[],     # questa lista deve contenere solo numeri
#                'cibibevande':[], # questa lista deve contenere solo numeri
#                'quantita':[]     # questa lista deve contenere solo numeri
#              }
#   Per esempio, le seguenti righe del file (i \r\n sono stati omessi)
#      Data;ID_Cliente;Cod_Prodotto1;QT1;Cod_Prodotto2;QT2;...
#      25/01/2010;214;p13;q2;p61;q3
#      25/01/2010;289;p23;q4
#      25/01/2010;411;p3;q1;p19;q2
#   danno origine alla seguente struttura dati
#              { 'cibibevande':[13,61,23,3,19],
#                'quantita':[2,3,4,1,2]
#                'clienti':[214,214,289,411,411],
#              }
#   dove nella lista associata a 'cibibevande' devono essere inseriti i codici dei prodotti
#   acquistati dai clienti (l'ordine e' dalla prima riga all'ultima, da sinistra verso destra
#   all'interno della stessa riga). Nella lista associata a 'quantita' ci devono essere le
#   quantita' di cibo del corrispondente elemento presente in 'cibibevande'. Nella lista
#   associata a 'clienti' ci deve essere il codice del cliente che ha acquistato il
#   corrispondente elemento presente in 'cibibevande'. Se un utente nella stessa riga del file
#   acquista piu' cibi, l'id del cliente dovra' apparire piu' volte consecutivamente nella
#    lista clienti.
def leggiConsumazioni(fname):
    risultato = {}
    listaClienti = []
    listaCibiBevande = []
    listaQuantita = []
    f = open(fname, "r")
    linea = f.readline ()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range (len(elementi)):
            elementi[i] = elementi[i].strip()
        idCliente = int(elementi[1])
        j = 2
        while j < len(elementi)-1:
            ciboBevanda = int(elementi[j][1:])
            quantita = int(elementi[j+1][1:])
            listaClienti = listaClienti +[idCliente]
            listaCibiBevande = listaCibiBevande + [ciboBevanda]
            listaQuantita = listaQuantita + [quantita]
            j = j + 2
        risultato["ciboBevanda"] = listaCibiBevande
        risultato["quantita"] = listaQuantita
        risultato["clienti"] = listaClienti
    f.close()
    return risultato


# - La funzione seguente accetta come parametri in ingresso
#   le strutture dati restituite rispettivamente dalle funzioni
#   leggiPrezzi() e leggiConsumazioni().
#   La funzione deve restituire una struttura dati come nell'esempio
#   seguente.
#        {id_cliente1:totale_cifra_spesa_dal_cliente1,
#           ...
#         id_clienteN:totale_cifra_spesa_dal_clienteN}
#   dove ad ogni id_cliente viene associato il totale delle spese effettuate
#   dal cliente per tutte le sue consumazioni.
#   Attenzione, i prezzi unitari dei cibi (e delle bevande) devono essere
#   moltiplicati per le quantita' acquistate.
def calcolaIncassi(dizPrezzi, dizConsumazioni):
    risultato = {}
    listaClienti = dizConsumazioni["clienti"]
    listaQuantita = dizConsumazioni["quantita"]
    listaCibiBevande = dizConsumazioni["ciboBevanda"]
    for i in range(len(listaClienti)):
        idCliente = listaClienti[i]
        ciboBevanda = listaCibiBevande[i]
        quantita = listaQuantita[i]
        prezzoUnitario = dizPrezzi[ciboBevanda]
        totPrezzo = quantita*prezzoUnitario
        totCifraSpesaCliente = risultato.get(idCliente,0)
        totCifraSpesaCliente = totCifraSpesaCliente + totPrezzo
        risultato[idCliente] = totCifraSpesaCliente
    #print(len(listaClienti))
    return risultato



# - La funzione seguente classifica una cifra spesa in scaglioni.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, la dovete SOLO USARE negli
#   esercizi seguenti.
def individuaScaglione(cifra):
    if cifra < 10:
        return 'A'
    elif cifra <100:
        return 'B'
    elif cifra <500:
        return 'C'
    else:
        return 'D'


# - La funzione seguente accetta in ingresso la struttura dati restituita
#   dalla funzione calcolaIncassi().
#   La funzione deve classificare le spese totali effettuate dai clienti in
#   scaglioni utilizzando la funzione dichiarata qua sopra.
#   La funzione deve restituire la seguente struttura dati
#   { 'A':[id_utente, somma_spesa], 'B':[id_utente, somma_spesa], ...}
#   dove 'A', 'B', ... sono gli scaglioni, inoltre per ogni scaglione
#   devono essere riportati i dati del cliente (appartenente allo scaglione)
#   che ha speso di piu'.
def individua(speseClienti):
    risultato = {"A":[0,0],"B":[0,0], "C":[0,0], "D":[0,0]}
    for idCliente in speseClienti.keys():
        sommaSpesa = speseClienti[idCliente]
        scaglione = individuaScaglione(sommaSpesa)
        if sommaSpesa > risultato[scaglione][1]:
            risultato[scaglione][1] = sommaSpesa
            risultato[scaglione][0] = idCliente
    return risultato




# - La funzione seguente accetta in ingresso la struttura dati restituita
#   dalla funzione calcolaIncassi().
#   Come primo passaggio individuate il valore minimo e il valore massimo
#   tra le spese dei clienti.
#   La funzione deve individuare 10 intervalli di spesa (di dimensioni uguali)
#   tra il valore massimo e il valore minimo di cui sopra e contare quanti
#   clienti giaciono in ciascun intervallo, sulla base delle loro spese.
#   La funzione deve restituire la seguente struttura dati
#   [nClienti1, nClienti2, ..., nClienti10]
#   In cui nClienti1 e' il numero di clienti che giaciono nel primo intervallo,
#   nClienti2 e' il numero di clienti che giaciono nel secondo intervallo e cosi' via.
def CalcolaMinMax(spesaClienti):
    maxSpesa = 0
    minSpesa = 10000000
    for cliente in spesaClienti.keys():
        spesa = spesaClienti[cliente]
        if spesa < minSpesa:
            minSpesa = spesa
        if spesa > maxSpesa:
            maxSpesa = spesa
        larghezzaIntervallo = (maxSpesa - minSpesa)/10.0
    print(minSpesa, maxSpesa, larghezzaIntervallo)
    return (minSpesa, maxSpesa, larghezzaIntervallo)

def istogramma (speseClienti):
    risultato = [0,0,0,0,0,0,0,0,0,0]
    x = CalcolaMinMax(speseClienti)
    print (x)
    min = x[0]
    max = x[1]
    l = x[2]
    for cliente in speseClienti.keys():
        spesa = speseClienti[cliente]
        nIntervallo = int((spesa-min)/l)
        if nIntervallo == 10:
            nIntervallo = nIntervallo-1
        risultato[nIntervallo] = risultato[nIntervallo] + 1
    return risultato





##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('Ciao %s, %s .' % (nome, cognome))

print("1) Eseguo la funzione leggiPrezzi: ")
fname1='prezzi.csv'
datiPrezzi = leggiPrezzi(fname1)
print(datiPrezzi)

print('2) Eseguo la funzione leggiConsumazioni: ')
fname2='consumazioni.csv'
datiConsumazioni = leggiConsumazioni(fname2)
print(datiConsumazioni)

print('3) Eseguo la funzione calcolaIncassi: ')
datiIncassi = calcolaIncassi(datiPrezzi, datiConsumazioni)
print(datiIncassi)

# Se volete potete togliere i commenti qua sotto
# print('Eseguo la funzione individuaScaglione: ')
# scaglione = individuaScaglione(5500)
# print(scaglione)

print('4) Eseguo la funzione individua: ')
ris = individua(datiIncassi)
print(ris)

print('5) Eseguo la funzione istogramma: ')
minMax = CalcolaMinMax(datiIncassi)
print(minMax)
ris = istogramma(datiIncassi)
print(ris)


print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
