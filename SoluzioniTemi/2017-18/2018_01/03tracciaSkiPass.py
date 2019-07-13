# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Ski Pass'

##########################################################
# INTRODUZIONE
##########################################################
#
# Un'azienda gestisce le piste da sci di una stazione sciistica.
# Un insieme di utenti acquista gli ski pass giornalieri per
# usufruire delle piste da sci. Uno ski pass giornaliero da
# diritto all'utente che lo ha acquistato di usufruire di tutte le
# piste da sci della stazione sciistica per il giorno di acquisto.

##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete i seguenti file, oltre a questo script:
#
# - File 1) skiPiste.csv
#   Il file contiene informazioni sulle piste da sci disponibili
#   nella stazione sciistica.
#   La prima riga del file contiene l'intestazione:
#
#   ID_Pista;Nome_Pista;Lunghezza_Pista
#
#   Ogni riga successiva del file contiene informazioni su una
#   singola pista, i diversi valori sono separati da ; e i
#   \r\n rappresentano i caratteri di a capo.
#   * ID_Pista rappresenta l'identificatore numerico associato
#            alla pista,
#   * Nome_Pista e' il nome testuale della pista,
#   * Lunghezza_Pista e' la lunghezza in metri delle piste.
#
#
# - File 2) skiPassaggi.csv
#   Ogni volta che l'utente accede ad una pista, l'accesso viene
#   rilevato e memorizzato nel file skiPassaggi.csv.
#   La prima riga del file contiene l'intestazione:
#
#   ID_Cliente;Giorno;Ora:Minuti;id_Pista
#
#   Ogni riga rappresenta un accesso di un utente ad una pista,
#   i diversi valori sono separati da ; e i \r\n rappresentano
#   i caratteri di a capo.
#   ID_Cliente e' un valore numerico che identifica
#               il cliente,
#   * Giorno rappresenta il giorno del mese in cui e' avvenuto
#               l'accesso del cliente alla pista (nel file sono
#               presenti i dati di un solo mese),
#   * Ora:Minuti sono l'ora ed il minuto (separati  da : )
#              in cui l'utente e' entrato nella pista,
#   * ID_Pista rappresenta l'identificatore numerico associato
#            alla pista.
#
#
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

# - arrotondaDistanze(metri). La funzione accetta come unico parametro in
#   ingresso un numero intero che rappresenta una lunghezza in metri.
#   La funzione dovra' "arrotondare" le distanze secondo le seguenti modalita':
#   * Se lunghezza<=500 dovra' essere restituito 500
#   * Se 500<lunghezza<=1000 dovra' essere restituito 1000
#   * se lunghezza>1000, dovra' essere restituita la lunghezza arrotondata al
#     centinaio inferiore, cioe' con decine e centinaia pari a 0.
#   Per esempio 120 deve essere arrotondato a 500, 730 deve essere arrotondato
#   a 1000, 1199 deve essere arrotondato a 1100, 2410 deve essere arrotondato a
#   2400.
#   Il valore restituito dovra' essere di tipo intero.
def arrotondaDistanze(metri):
    if metri <= 500:
        return 500
    if metri <= 1000:
        return 1000
    else:
        return (int(metri/100))*100

#print(arrotondaDistanze(2410))



# - leggiPiste(filePiste). La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati sulle piste da sci (File 1).
#   La funzione dovra' restituire un dizionario come nell'esempio seguente:
#   [   idPista:(nomePista, lunghezza_arrotondata), ...    ] dove
#   * idPista rappresenta l'id della pista,
#   * nomePista rappresenta il nome testuale della pista e
#   * lunghezza_arrotondata e' ottenuta arrotondando la lunghezza della pista
#             utillizzando la funzione arrotondaDistanze() precedentemente
#             implementata.
def leggiPiste(filePiste):
    risultato = {}
    f = open (filePiste, "r")
    linea = f.readline ()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split (";")
        for i in range(len(elementi)):
            elementi[i] = elementi[i].strip()
        idPista = int(elementi[0])
        nomePista = elementi[1]
        lunghezzaArrotondata = arrotondaDistanze(int(elementi[2]))
        risultato[idPista]=(nomePista,lunghezzaArrotondata)
    f.close()
    #print(risultato)
    return risultato



# - puntiBonusPiste(g,h,m). L'utente riceve dei punti bonus ogni volta che accede ad una singola
#   pista. L'ammontare del bonus dipende dal giorno, ora e minuti in cui l'utente accede
#   alla pista. I parametri g, h ed m assumono valori interi e rappresentano rispettivamente
#   il giorno, l'ora e il minuto in cui l'utente ha avuto accesso alla pista.
#   I punti sono restituiti secondo l'algoritmo implementato qua sotto. Tendenzialmente,
#   si acquisiscono piu' punti accedendo alle piste al di fuori dei giorni e degli orari
#   di punta.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, la dovete SOLO USARE negli esercizi seguenti.
def puntiBonusPiste(g,h,m):
    if g%7<=5:
        return 2
    else:
        minuti=h*60+m
        if minuti<10*60+30  or minuti>14*60+30:
            return 1
        else:
            return 2

# - leggiPassaggi(nomeFilePassaggi).  La funzione accetta come unico parametro in
#   ingresso il nome del file con i dati sugli accessi alle piste da parte degli
#   utenti (File 2).
#   La funzione dovra' restituire una lista formata da tuple,
#   come nell'esempio seguente:
#   [   (idCli,id_pista, punti_bonus), ...    ] dove
#   * idCli rappresenta l'identificatore del cliente
#   * id_pista rappresenta la pista nel quale l'utente e' entrato.
#   * punti_bonus sono i punti bonus che il cliente acquisice con l'ingresso in una
#    pista e calcolati con la funzione puntiBonusPiste() presente qua sopra.
def leggiPassaggi(nomeFilePassaggi):
    risultato = []
    f = open (nomeFilePassaggi, "r")
    linea = f.readline()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range (len(elementi)):
            elementi[i] = elementi[i].strip()
        idCliente = int(elementi[0])
        idPista = int(elementi[3])
        giorno = int(elementi[1])
        oraEMinuti = elementi[2].split(":")
        ora = int(oraEMinuti[0])
        minuti = int(oraEMinuti[1])
        puntiBonus = puntiBonusPiste(giorno, ora, minuti)
        risultato = risultato + [(idCliente,idPista,puntiBonus)]
    f.close()
    #print (risultato)
    return risultato





# - calcolaClientiPiste(passaggi, datiPiste). Il parametro passaggi deve essere
#   la struttura dati restituita dalla funzione leggiPassaggi(), il parametro datiPiste
#   deve essere la struttura dati restituita dalla funzione leggiPiste().
#   La funzione deve restituire un dizionario di coppie chiave valore come nell'esempio seguente,
#        {id_cliente:[metri_percorsi, punti_bonus], ...}
#   dove  ogni chiave e' l'identificatore di un cliente, e il valore associato alla
#   chiave e' una lista di due elementi:
#   * il totale dei metri di pista percorsi dal cliente e
#   * il totale dei punti bonus conseguiti dal cliente.
def calcolaClientiPiste(passaggi, datiPiste):
    risultato = {}
    for i in range (len(passaggi)):
        idCliente = passaggi[i][0]
        idPista = passaggi[i][1]
        metriPercorsi = datiPiste[idPista][1]
        valore = risultato.get(idCliente, [0,0])
        valore[0] = valore[0] + metriPercorsi
        valore[1] = valore[1] + passaggi[i][2]
        risultato[idCliente] = valore
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

print('1) Eseguo la funzione arrotondaDistanze(2410): ')
da1 = arrotondaDistanze(2410)
print(da1)

print('2) Eseguo la funzione leggiPiste: ')
fPiste='skiPiste.csv'
dpis = leggiPiste(fPiste)
print(dpis)

print('3) Eseguo la funzione leggiPassaggi: ')
fPassaggi='skiPassaggi.csv'
dpas = leggiPassaggi(fPassaggi)
print(dpas)

print('4) Eseguo la funzione calcolaClientiPiste: ')
dati = calcolaClientiPiste(dpas, dpis)
print(dati)

print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
