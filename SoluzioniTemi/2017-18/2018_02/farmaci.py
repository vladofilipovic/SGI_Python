# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Farmaci'

##########################################################
# INTRODUZIONE
##########################################################
#
# Il ministero della sanita' ha deciso di monitorare le vendite
# di farmaci a pazienti, per avere una stima dei momenti di maggior
# manifestazione delle malattie.

##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete i seguenti file, oltre a questo script:
#
# - File 1) venditaFarmaci.csv
#   Il file contiene informazioni su clienti e farmaci venduti.
#   La prima riga del file contiene l'intestazione:
#
#   ID_Farmaco;ID_Persona;Numero_scatole;PrezzoScatola;gg/mm/aaaa\r\n
#
#   Ogni riga successiva del file contiene informazioni su una
#   singola vendita, i diversi valori sono separati da ; e i
#   \r\n rappresentano i caratteri di a capo.
#   * ID_Farmaco rappresenta l'identificatore numerico associato
#     al farmaco venduto.
#   * ID_Persona rappresenta l'identificatore numerico associato
#     al cliente che ha acquistato il farmaco.
#   * Numero_scatole rappresenta il numero di scatole di farmaco
#     acquistate dal cliente.
#     Se il numero e' negativo si tratta di un reso,
#     se e' positivo si tratta di un acquisto.
#   * PrezzoScatola rappresenta il prezzo al quale e' stata venduta
#     una singola scatola. Il prezzo e' un valore in euro che puo'
#     avere due cifre decimali. Tenete presente che il prezzo di una
#     stessa scatola di farmaco puo' variare da una riga all'altra.
#   * gg/mm/aaaa rappresenta la data in cui e' avvenuta la vendita.
#     gg, mm ed aaaa sono numeri separati da / che rappresentano il giorno,
#     il mese e l'anno in cui e' avvenuta la vendita.
#
# - File 2) acquirentiFarmaci.csv
#   In questo file sono presenti le informazioni anagrafiche sulle
#   persone che hanno acquistato farmaci. Ogni singola persona
#   e' presente una volta solo nel file ed e' identificata da
#   un valore numerico.
#   La prima riga del file contiene l'intestazione:
#
#   ID_Persona;gg/mm/aaaa;genere\r\n
#
#   Ogni riga contiene informazioni su un acquirente, ogni
#   acquirente e' presente una volta solo nel file, i diversi valori
#   sono separati da ; e i \r\n rappresentano i caratteri di a capo.
#   * ID_Persona e' un valore numerico che identifica univocamente
#     un cliente.
#   * gg,mm ed aaaa sono numeri separati da / che rappresentano il giorno,
#     il mese e l'anno di nascita della persona.
#   * genere rappresenta il genere della persona e puo' assumere come
#     valori solo M oppure F.
#
# Provate ad aprire i file con un editor di testi.
# State attenti, se aprirete il file con Excel o con il
# notepad di windows, alcune informazioni potrebbero essere
# VISUALIZZATE in MANIERA DISTORTA rispetto al contenuto del file.


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

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome

# - calcolaPrezzoTotale(qt, prezzoUnitario). La funzione
#   accetta due parametri in ingresso, rispettivamente
#   una quantita' di scatole acquistate e il prezzo di
#   una singola scatola. La funzione deve restituire il
#   prezzo totale pagato per l'acquisto.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, la dovete SOLO USARE negli
#   esercizi seguenti.


def calcolaPrezzoTotale(qt, prezzoUnitario):
    return qt * prezzoUnitario

# - convertiInMesi(stdata, strAnno). La funzione accetta in ingresso due
#   parametri. Il primo parametro di tipo stringa contenente una data, nel
#   formato gg/mm/aaaa. Il secondo e' un parametro opzionale e contiene
#   una stringa nel formato aaaa.
#   La funzione deve restituire un intero corrispondente al numero di mesi
#   trascorsi dall'1 gennaio dell'anno presente nel parametro opzionale strAnno.
#   Nel calcolo dei mesi dovete trascurare la cifra dei giorni
#   e focalizzarvi solo sui valori mm e aaaa.
#   Per esempio, se strAnno='1900' allora:
#   - fino al ../01/1900 sono trascorsi 0 mesi,
#   - fino al ../02/1900 sono trascorsi 1 mese,
#   - fino al ../03/1900 sono trascorsi 2 mesi,
#   - fino al ../01/1901 sono trascorsi 12 mesi.
#   La funzione deve poter funzionare anche quando l'utente modifica
#   il valore del parametro opzionale strAnno.
#   L'utente che richiama questa funzione, se vuole puo' modificare
#   il parametro opzionale, tuttavia questo dovra' sempre assumere
#   valori di anni nel formato 'aaaa', non serve effettuare controlli.


def convertiInMesi(stdata, strAnno='1900'):
    mese = int(stdata.split("/")[1])
    anno = int(stdata.split("/")[2])
    strAnno = int(strAnno)
    return ((anno-strAnno)*12 + (mese-1))

print (convertiInMesi("01/01/1901"))



# - caricaVenditeFarmaci(fname). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati sulle vendite dei farmaci.
#   La funzione deve restituire una tupla composta da due liste: la prima contenente
#   informazioni sui farmaci acquistati, la seconda contenente informazioni
#   sui farmaci resi.
#   La lista delle vendite deve contenere tuple come nell'esempio seguente:
#   [   (ID_Farmaco, ID_Persona, prezzo_scatole, mesi_trascorsi), ...]
#   La lista dei resi deve contenere tuple come nell'esempio seguente:
#   [   (ID_Farmaco, ID_Persona, Numero_scatole, mesi_trascorsi), ...]
#   Ad ogni riga di dati del file dovra' corrispondere una tupla di una delle
#   due strutture dati.
#   * ID_Farmaco rappresenta l'identificatore del farmaco,
#   * ID_Persona rappresenta l'identificatore della persona,
#   * prezzo_scatole rappresenta il prezzo speso dall'acquirente per
#     le scatole di farmaco acquistate. Questo valore e' ottenuto
#     moltiplicando la quantita' di scatole per il prezzo unitario.
#   * mesi_trascorsi rappresenta i mesi trascorsi dall'1/1/1900 fino alla data
#     di acquisto dei farmaci, calcolati utilizzando la funzione convertiInMesi()
#     precedentemente definita. Invocando convertiInMesi() non occorre modificare il
#     parametro opzionale strAnno.
#   * Numero_scatole rappresenta il numero di scatole rese dal cliente

def caricaVenditeFarmaci(fname):
    listaVendite = []
    listaResi = []
    f = open (fname, "r")
    linea = f.readline()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range (len(elementi)):
            elementi[i] = elementi[i].strip()
        idFarmaco = int (elementi[0])
        idPersona = int (elementi[1])
        numeroScatole = int(elementi[2])
        prezzoTot = int(elementi[2])*float(elementi[3])
        mesiTrascorsi = convertiInMesi(elementi[4])
        if  numeroScatole >= 0:
            listaVendite = listaVendite + [(idFarmaco, idPersona, prezzoTot, mesiTrascorsi)]
        else:
            listaResi = listaResi + [(idFarmaco, idPersona, numeroScatole, mesiTrascorsi)]
    f.close()
    risultato = (listaVendite,listaResi)
    print(risultato)
    return (risultato)



# - caricaDatiClienti(fname). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati anagrafici delle persone che hanno
#   acquistato farmaci.
#   La funzione deve restituire un dizionario con la struttura rappresentata
#   nell'esempio seguente:
#              {  ID_Persona:[genere, numero_mesi_trascorsi], ...}
#   dove ad ogni riga di dati del file corrisponde una coppia
#   chiave:valore (valore in realta' e' una lista) composta dagli elementi seguenti:
#   * ID_Persona rappresenta l'identificatore della persona,
#   * Genere e' una stringa che puo' assumere i valori 'M' o 'F' e che rappresenta
#     il genere della persona.
#   * numero_mesi_trascorsi rappresenta i mesi trascorsi dall'1/1/1900 fino alla data
#     di nascita della persona, calcolati utilizzando la funzione convertiInMesi()
#     precedentemente definita.
def caricaDatiClienti(fname):
    risultato = {}
    f = open (fname, "r")
    linea = f.readline ()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range(len(elementi)):
            elementi[i] = elementi[i].strip()
            idPersona = int(elementi[0])
            valore = risultato.get(idPersona, [0,0])
            valore[0] = elementi[2]
            valore[1] = convertiInMesi(elementi[1])
            risultato[idPersona] = valore
    f.close()
    #print(risultato)
    return risultato



# - spesePerMese(datiFarmaci, datiClienti). La funzione accetta come parametri in ingresso
#   le strutture dati restituite rispettivamente dalla funzione caricaVenditeFarmaci() e
#   caricaDatiClienti().
#   I dati restituiti dalla funzione servono per capire se c'e' un mese dell'anno in cui
#   si concentrano maggiormente le spese per farmaci.
#   La funzione deve restituire un dizionario con la struttura rappresentata nell'esempio
#   seguente:
#           {numero_mese_dell_anno:[spese_maschi,spese_femmine, totResi], ...}
#   dove ogni chiave del dizionario rappresenta un generico mese dell'anno (quindi nel dizionario
#   ci saranno 12 chiavi) e ogni valore associato ad una chiave e' una lista contenente le spese
#   per farmaci ed i farmaci resi nello specifico mese. Per esempio, al mese di gennaio dovranno essere
#   associate tutte le spese fatte a gennaio nei diversi anni.
#   Le spese devono essere divise per genere, i resi no.
#   I valori presenti nell'esempio di struttura dati da restituire sono:
#   * numero_mese_dell_anno e' un valore intero che va da 0 a 11. 0 rappresenta il mese di gennaio
#     1 rappresenta il mese di febbraio, ... 11 rappresenta il mese di dicembre.
#   * spese_maschi rappresenta il totale delle spese per farmaci effettuate da persone di
#     genere maschile nel mese dell'anno.
#   * spese_femmine rappresenta il totale delle spese per farmaci effettuate da persone di
#     genere femminile nel mese dell'anno corrispondente.
#   * num_resi rappresenta la somma delle confezioni, indipendentemte dal genere, rese nel mese
#     dell'anno corrispondente.
#   Fate attenzione, nei dati di vendita potrebbero essere presenti identificativi di persone non presenti
#   in datiClienti (quindi non presenti nel file acquirentiFarmaci.csv). I dati di tali persone
#   non devono essere considerati dai calcoli svolti da questa funzione.
def spesePerMese(datiVendite, datiClienti):
    risultato = {}
    listaVendite = datiVendite[0]
    listaResi = datiVendite[1]
    #print(listaResi)
    for i in range (len(listaVendite)):
        idPersona = listaVendite[i][1]
        prezzoTot = listaVendite[i][2]
        mesiTrascorsi = listaVendite[i][3]
        genere = datiClienti[idPersona][0]
        meseDelAnno = mesiTrascorsi%12
        valore = risultato.get(meseDelAnno,[0,0,0])
        speseMaschi = valore[0]
        speseFemmine = valore[1]
        numeroResi = valore[2]
        if genere == "M":
            speseMaschi = speseMaschi + prezzoTot
        else:
            speseFemmine = speseFemmine + prezzoTot
        risultato[meseDelAnno] = [speseMaschi, speseFemmine, numeroResi]
    for i in range (len(listaResi)):
        numeroScatole = listaResi[i][2]
        mesiTrascorsi = listaResi[i][3]
        meseDelAnno = mesiTrascorsi%12
        valore = risultato.get(meseDelAnno,[0,0,0])
        speseMaschi = valore[0]
        speseFemmine = valore[1]
        numeroResi = valore[2]
        numeroResi = numeroResi + numeroScatole
        risultato[meseDelAnno] = [speseMaschi, speseFemmine, numeroResi]
    print(risultato)
    return (risultato)




##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('Ciao %s, %s .' % (nome, cognome))

print("1) Eseguo la funzione convertiInMesi('12/12/1921') ")
m1 = convertiInMesi('12/12/1921')
print(m1)

print('2) Eseguo la funzione caricaVenditeFarmaci: ')
fven = 'venditaFarmaci.csv'
res = caricaVenditeFarmaci(fven)
print(res)

print('3) Eseguo la funzione caricaDatiClienti: ')
fpers = 'acquirentiFarmaci.csv'
dpers = caricaDatiClienti(fpers)
print(dpers)

print('4) Eseguo la funzione spesePerMese: ')
dati = spesePerMese(res, dpers)
print(dati)

print('Nome dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
