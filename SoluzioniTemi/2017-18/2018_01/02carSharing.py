# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Car Sharing'

##########################################################
# INTRODUZIONE
##########################################################
#
# Un'azienda di car sharing noleggia automobili ad un insieme di clienti che
# le utilizzano per muoversi all'interno di una citta'.
# Il cliente preleva l'automobile da una via qualsiasi della citta' e al
# termine del suo utilizzo la parcheggia nella stessa citta', non
# necessariamente nella stessa via da cui l'auto e' stata prelevata.

##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete i seguenti file, oltre a questo script:
#
# - File 1) carsharingNol.csv
#   Il file contiene informazioni sui noleggi effettuati dai clienti.
#   La prima riga del file contiene l'intestazione:
#
#   ID_Cliente;ID_Via_Inizio;ID_Via_Fine;Minuti_Noleggio\r\n
#
#   Ogni riga successiva del file riporta le informazioni su un noleggio
#   svolto dal cliente, i diversi valori sono separati da ; e i \r\n
#   rappresentano i caratteri di a capo.
#   * ID_Cliente e' un valore numerico che identifica univocamente
#         il cliente che ha effettuato il noleggio,
#   * ID_Via_Inizio e ID_Via_Fine sono valori numerici che identificano
#         le vie in cui un noleggio inizia e finisce,
#   * Minuti_Noleggio indica la durata in minuti del noleggio
#
#
# - File 2) carsharingVie.csv
#   Il file contiene le distanze in km tra le vie della citta'.
#   La prima riga del file contiene l'intestazione:
#
#   ID_via1;Via1;ID_via2;Via2;Distanza
#
#   Ogni riga successiva del file contiene i dati di due vie e la loro
#   distanza in km (per ogni via e' riportato sia l'identificatore numerico
#   sia il nome).
#   In una riga, ogni volta che appare il nome di una via (ViaX...),
#   appare sempre il corrispondente identificatore numerico (ID_viaX).
#   ATTENZIONE, la distanza tra due vie e' presente un'unica volta nel file
#   quindi se nel file e' presente
#   ID_viaA;ViaA;ID_viaB;ViaB;Distanza
#   allora non e' presente una riga con
#   ID_viaB;ViaB;ID_viaA;ViaA;Distanza
#   o viceversa.
#   In ogni riga, i diversi valori sono separati da ; e i \r\n
#   rappresentano i caratteri di a capo.
#
# Provate ad aprire i file con un editor di testi.
# State attenti, se aprirete il file con Excel o con il
# notepad di windows, alcune informazioni potrebbero essere
# VISUALIZZATE in MANIERA DISTORTA rispetto al contenuto del file.


##########################################################
# DESCRIZIONE DEL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede ogni funzione vi
# spieghera' cosa fare in dettaglio.
# Controllate nel corpo principale del programma (in fondo allo script), come
# vengono invocate le funzioni che implementerete.
# Per favore NON USATE le istruzioni input() o raw_input() nel codice che scriverete.
# Se volete potete implementare delle funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.

##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

# - def metri2miglia(metri). La funzione accetta come unico parametro in
#   ingresso un numero intero che rappresenta una lunghezza in metri.
#   La funzione dovra' restituire il numero di miglia corrispondenti.
#   Si ricorda che un miglio e' lungo 1609 metri.
#   Il valore restituito dovra' essere di tipo float e dovra' avere parte
#   decimale nulla. Per esempio, 3000 metri corrispondono a 1.86 miglia
#   e la funzione dovra' restituire 1.0 ; 400 metri corrispondono a
#   0.24 miglia e la funzione dovra' restituire 0.0
def metri2miglia(metri):
    miglia = float (int (metri/1609))
    return miglia

print (metri2miglia(3000))


# - leggiVie(nomeFileVie). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati sulle distanze tra le vie (File 2).
#   La funzione dovra' restituire una lista formata da tuple,
#   come nell'esempio seguente:
#   [   (idv1,idv2,miglia), ...    ]
#   dove idv1 e idv2 sono gli ID identificatori di 2 vie e miglia e' la
#   distanza in miglia di tipo float.
#   Per convertire le distanze in miglia (nel file le distanze sono
#   memorizzate in km), dovete utilizzare la funzione
#   metri2miglia precedentemente creata.
def leggiVie(nomeFileVie):
    risultato = []
    f = open (nomeFileVie, "r")
    linea = f.readline ()
    while 1:
        linea = f.readline ()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range (len(elementi)):
            elementi[i] = elementi[i].strip()
        #print (elementi)
        idv1 = int (elementi [0])
        idv2 = int (elementi [2])
        miglia = metri2miglia(int(elementi[4])*1000)
        risultato = risultato + [(idv1, idv2, miglia)]
    f.close()
    #print(risultato)
    return risultato



# - distanza(idVia1, idVia2, ds). I parametri idVia1 e idVia2
#   contengono gli identificatori di due vie. Il parametro
#   ds e' invece la struttura dati restituita dalla funzione leggiVie().
#   La funzione deve restituire la distanza in miglia tra le due vie.
#   Se i valori di idVia1 o idVia2 non sono presenti in ds, allora deve
#   essere restituito 100.0 come valore di distanza.
#   Nota bene, siano 5 e 8 gli identificatori di due vie, la funzione
#   distanza(5, 8, ds) deve restituire lo stesso valore di
#   distanza(8, 5, ds).
#   Attenzione, vi ricordiamo che nel file a partire dal quale
#   e' stata creata la struttura dati passata in ds,
#   l'informazione sulla distanza tra una coppia di vie e'
#   presente una sola volta.
def distanza(idVia1, idVia2, ds):
    for i in range (len(ds)):
        tuple = ds[i]
        id1 = tuple [0]
        id2 = tuple [1]
        if id1 == idVia1 and id2 == idVia2:
            return tuple[2]
        if id1 == idVia2 and id2 == idVia1:
            return tuple [2]
    return 100.0




# - calcolaPuntiBonus(miglia, minuti). Il parametri miglia e minuti
#   rappresentano rispettivamente le miglia percorse e i minuti
#   impiegati per un singolo noleggio. Durante ogni noleggio
#   il cliente acquisisce dei punti bonus calcolati sulla base delle
#   miglia percorse e dei minuti impiegati. La funzione restituisce
#   i punti di bonus conseguiti da un utente, secondo l'algoritmo
#   che trovate implementato qua sotto.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, la dovete SOLO USARE negli esercizi seguenti.
def calcolaPuntiBonus(miglia, minuti):
    if miglia < 5.0:
        return int(miglia)
    else:
        return 2*minuti


# - calcolaDatiClienti(nomeFileNoleggi, ds). Il parametro nomeFileNoleggi
#   contiene il nome del file con le informazioni sui noleggi effettuati dai
#   clienti (File 1), il parametro ds e' la struttura dati restituita dalla
#   funzione leggiVie() precedentemente implementata.
#   La funzione deve leggere il contenuto del file il cui nome e' passato come
#   parametro e deve restituire un dizionario di coppie chiave valore come
#   nell'esempio seguente,
#        {id_cliente:[tot_minuti, tot_miglia, tot_punti_bonus], ...}
#   dove ogni chiave e' l'identificatore di un cliente, e il valore associato
#   alla chiave e' una lista di tre elementi:
#   * il totale dei minuti di noleggio effettuati dal cliente,
#   * il totale delle miglia percorse dal cliente e
#   * il totale dei punti bonus acquisiti dal cliente.
def calcolaDatiClienti(nomeFileNoleggi, ds):
    risultato = {}
    f = open (nomeFileNoleggi, "r")
    linea = f.readline ()
    while 1:
        linea = f.readline ()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range (len(elementi)):
            elementi [i] = elementi[i].strip()
        idCliente = int (elementi[0])
        id1 = int(elementi[1])
        id2 = int(elementi[2])
        miglia = distanza (id1, id2,ds)
        minuti = int(elementi[3])
        valore = risultato.get (idCliente, [0,0,0])
        valore[0] = valore[0] + minuti
        valore[1] = valore[1] + miglia
        valore[2] = valore [2] + calcolaPuntiBonus (miglia,minuti)
        risultato[idCliente] = valore
    f.close ()
    #print(risultato)
    return risultato





##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('1) Eseguo la funzione metri2miglia(3000): ')
mi = metri2miglia(3000)
print(mi)

print('2) Eseguo la funzione leggiVie: ')
fVie='carsharingVie.csv'
ds = leggiVie(fVie)
print(ds)

#print (distanza(13,14,ds))
#print (distanza(14,13,ds))

print('3) Eseguo la funzione calcolaDatiClienti: ')
fNoleggi='carsharingNol.csv'
datiCli = calcolaDatiClienti(fNoleggi, ds)
print(datiCli)

print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
