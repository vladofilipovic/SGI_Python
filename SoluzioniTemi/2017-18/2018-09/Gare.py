# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'GareNuoto'


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file di dati, descritto qua di seguito
#
# - File 1) A28A2018.txt.csv
#   Il file memorizza le informazioni sui risultati di diverse gare di nuoto.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di #
#
#       400 stile libero  femminile  -  Categoria  Under 25
#----------------------------------------------------------------------------------------------
#       1   BAIGUERA  MARTA ISIDE          1994   Verolanuoto                 4'49"74  0,00
#       2   FERRARI  ALICE                 1997   Coopernuoto                 4'55"15  0,00
#
#        400 stile libero  femminile  -  Categoria  Master 25      Tempo Base :  4'23"38
#----------------------------------------------------------------------------------------------
#       1   GUARESCHI  MARTINA             1990   Coopernuoto                 4'33"59  962,68
#       2   FE`  ELEONORA                  1989   Prosport Acqua ssd          4'52"72  899,77
#       3   PASTORE  GIULIA                1991   Effetto Sport - Barzano`    4'56"77  887,49
#       4   MOTTADELLI  ANNA               1992   Nord Padania Nuoto - Vare   5'03"97  866,47
#       5   LOPPI  LAURA                   1989   Amici Nuoto Firenze         5'06"75  858,61
#       6   BIGIOGGERO GIORGIA             1993   NUOTO ALTO MILANESE         5'19"51  824,32
#       7   RICCARDI  FIORELLA             1989   Amici Nuoto Firenze         5'39"61  775,54
#
#        400 stile libero  femminile  -  Categoria  Master 30      Tempo Base :  4'22"11
#----------------------------------------------------------------------------------------------
#       1   LUGANO  DILETTA                1984   Derthona Nuoto              4'51"39  899,52
#       2   TAINI  RAFFAELLA               1984   Nuoto Master Brescia asd    5'05"49  858,00
#       3   COGO  MARTINA GAIA             1985   Effetto Sport - Barzano`    5'08"50  849,63
#       4   PELIZZARI  VALENTINA           1987   Aquatic Center ssd          5'26"82  802,00
#       5   LEONI  SARA                    1985   Prosport Acqua ssd          5'49"83  749,25
#       6   LEONARDI  CHIARA               1985   ASA asd - Cinisello Balsa   6'07"73  712,78
#       7   MAZZOLENI  ELISA               1987   Canottieri Baldesio         6'31"91  668,80
#
#   La prima riga sopra i ----- contiene informazioni sul nome della gara e
#   sul Tempo Base (quest'ultimo non e' sempre presente). Per esempio in
#            400 stile libero  femminile  -  Categoria  Master 30      Tempo Base :  4'22"11
#   il nome della gara e' "400 stile libero  femminile  -  Categoria  Master 30" e
#   il tempo base e' "Tempo Base :  4'22"11"
#   Sotto i ----- sono riportate le informazioni sui partecipanti alla gara e sui loro piazzamenti.
#   Per ogni partecipante sono riportate le informazioni descritte qua sotto. Per esempio,
#   la riga
#
#   1   GUARESCHI  MARTINA             1990   Coopernuoto                 4'33"59  962,68
#
#   contiene queste informazioni:
#   * Posizione di arrivo nella gara   1
#   * Cognome e nome   GUARESCHI  MARTINA
#   * Anno di nascita   1990
#   * Squadra di cui il partecipante fa parte   Coopernuoto
#   * Tempo impiegato per completare la gara   4'33"59 (4 minuti, 33 secondi, 59 centesimi)
#   * Punteggio ottenuto   962,68
#
#   Le informazioni sui partecipanti occupano sempre una posizione fissa all'interno della riga.
#   Una gara e' separata tramite una doppia interlinea dalla gara successiva.
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
#   ingresso una stringa contenente un tempo espresso in
#   minuti, secondi e centesimi, come nell'esempio seguente
#   1'01"24 (rispettivamente 1 minuto, 1 secondo, 24 centesimi).
#   La funzione deve convertire il tempo in centesimi
#   e restituire un valore di tipo intero.
#   Per esempio 1'01"24 deve essere convertito in
#   24 + 1*100 + 1*60*100 = 6124
#   centesimi.
#   Se la persona e' stata squalificata, deve essere restituito -1
def tStr2tCC(string):
    #print(string)
    if "Squalif." in string:
        return -1
    risultato = 0
    for i in range(len(string)):
        lstring1 = string.split("'")
        minuti = int(lstring1[0])
        lstring2 = lstring1[1].split('"')
        #print(string1, string2)
        secondi = int(lstring2[0])
        centesimi = int(lstring2[1])
        risultato = centesimi + secondi*100 + minuti*60*100
    return risultato

print(tStr2tCC(" 1'01\"24"))


# - La funzione seguente accetta come unico parametro in
#   ingresso una stringa contenente una riga del file A28A2018.txt con i dati
#   dei piazzamenti di un atleta.
#   Per esempio, passando come parametro la stringa seguente
#       1   GUARESCHI  MARTINA             1990   Coopernuoto                 4'33"59  962,68
#   la funzione deve restiture un dizionario, come nell'esempio seguente:
#         {'ordArrivo': 1,
#          'atleta': ' GUARESCHI  MARTINA',
#          'nascita': 1990,    # questo valore deve essere di tipo intero intero
#          'squadra': 'Coopernuoto',
#          'tempoCC': 27359,    # l'equivalente in centesimi di 4'33"59
#          'punti': 962.68  # questo valore deve essere di tipo float
#         }
#
def dizPrestazione(string):
    ordArrivo = int(string[0:8].strip())
    atleta = string[8:41].strip()
    nascita = int(string[41:46].strip())
    squadra = string[46:76].strip()
    tempoCC = tStr2tCC(string[76:85].strip())
    punti = float(string[85:].strip().replace(",","."))
    risultato = {"ordArrivo": ordArrivo, "atleta": atleta, "nascita": nascita, "squadra":squadra, "tempoCC":tempoCC, "punti" : punti}
    return risultato

print(dizPrestazione("       1   GUARESCHI  MARTINA             1990   Coopernuoto                 4'33\"59  962,68"))





# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file contenente i risultati
#   delle gare di nuoto.
#   La funzione deve restituire una struttura dati come la seguente:
#
#   {gara1:tBase1, gara2:tBase2, ...}
#
#   cioe' un dizionario dove
#   * gara... e' il nome della gara,
#   * tBase... e' un intero contenente il tempo base della gara, convertito in centesimi
#     attraverso la funzione tStr2tCC() precedentemente creata. Se il tempo base
#     non e' indicato nella gara, allora deve essere inserito lo 0
#   Per esempio, se il file contenesse le seguenti righe
#
#       400 stile libero  femminile  -  Categoria  Under 25
#----------------------------------------------------------------------------------------------
#       1   BAIGUERA  MARTA ISIDE          1994   Verolanuoto                 4'49"74  0,00
#       2   FERRARI  ALICE                 1997   Coopernuoto                 4'55"15  0,00
#
#        400 stile libero  femminile  -  Categoria  Master 25      Tempo Base :  4'23"38
#----------------------------------------------------------------------------------------------
#       1   GUARESCHI  MARTINA             1990   Coopernuoto                 4'33"59  962,68
#       2   FE`  ELEONORA                  1989   Prosport Acqua ssd          4'52"72  899,77
#
#   la funzione dovrebbe restituire
#
#   {
#    '400 stile libero  femminile  -  Categoria  Under 25':0,
#    '400 stile libero  femminile  -  Categoria  Master 25':26338   # 26338 e' l'equivalente in centesimi di 4'23"38
#   }
#
def leggiGare(fn):
    risultato = {}
    f = open (fn, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        if "Categoria" in linea:
            nomeGara = linea[7:58].strip()
            if "Tempo" not in linea:
                tempoBase = 0
            else:
                strTempoBase = linea[80:].strip()
                #print (strTempoBase)
                tempoBase = tStr2tCC(strTempoBase)
            risultato[nomeGara] = tempoBase
    f.close()
    #print(risultato)
    return risultato







# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file contenente i risultati
#   delle gare di nuoto.
#   La funzione deve restituire una struttura dati come la seguente:
#
#   {
#      'nome_squadra1':{'nAtleti':10, 'punti':5340.32 },
#      'nome_squadra2':{'nAtleti':14, 'punti':8470.69 },
#       ...
#    }
#
#   cioe' un dizionario dove le chiavi sono i nomi delle squadre
#   e ad ogni nome di squadra e' a sua volta associato
#   un dizionario con le seguenti informazioni:
#   * 'nAtleti' il n. di volte che gli atleti della squadra sono presenti
#      nei piazzamenti contenuti all'interno del file. Se uno stesso atleta si
#      e' piazzato in piu' gare, questi piazzamenti vanno contati tutti
#   * 'punti' il totale dei punti conseguiti dalla squadra
#
def leggiRisultati(fn):
    risultato = {}
    f = open(fn, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        if len(linea)>7:
            if "Categoria" not in linea:
                if "Squalif." not in linea:
                    if "-----------" not in linea:
                        dataPerLinea = dizPrestazione(linea)
                        #print(dataPerLinea)
                        nomeSquadra = dataPerLinea["squadra"]
                        valore = risultato.get(nomeSquadra, {"numeroAtleti":0, "totPunti":0})
                        valore["numeroAtleti"] = valore["numeroAtleti"] + 1
                        valore["totPunti"] = valore["totPunti"] + dataPerLinea["punti"]
                        risultato[nomeSquadra] = valore
    f.close()
    print(risultato)
    return risultato




# - La funzione seguente accetta come parametri in ingresso:
#   la struttura dati restituita dalla funzione leggiRisultati(). /* Nel testo originale era erroneamente scritto leggiSquadre() */
#   La funzione deve restituire una struttura dati simile a quella ricevuta in ingresso,
#   in cui nel dizionario associato ad ogni squadra e' presente anche
#   una coppia chiave valore come mostrato nell'esempio seguente
#   (la nuova coppia e' l'ultima delle 3):
#   {
#      'nome_squadra1':{'nAtleti':10, 'punti':5340.32,  'muPuntiPrest': 53.432 },
#      'nome_squadra2':{'nAtleti':14, 'punti':8470.69,  'muPuntiPrest': 605.0492 },
#       ...
#   }
#   Il valore associato a 'muPuntiPrest' e', per ogni squadra, il rapporto tra il valore
#   associato alla chiave 'punti' e il valore associato alla chiave 'nAtleti'
def aggiungiMedia(dizSquadre):
    risultato = {}
    for nomeSquadra in dizSquadre.keys():
        numeroAtleti = dizSquadre[nomeSquadra]["numeroAtleti"]
        totPunti = dizSquadre[nomeSquadra]["totPunti"]
        muPuntiPrest = totPunti/numeroAtleti
        risultato[nomeSquadra] = {"numeroAtleti": numeroAtleti, "totPunti":totPunti, "muPuntiPrest" : muPuntiPrest}
    #print(risultato)
    return risultato



# - La funzione seguente accetta come parametri in ingresso:
#   la struttura dati restituita dalla funzione aggiungiMedia()
#   e restituisce una tupla contenente il nome della squadra che ha ottenuto
#   il punteggio massimo su 'muPuntiPrest' (la media dei punteggi per atleta),
#   assieme al punteggio stesso.
#   Se piu' squadre raggiungono lo stesso punteggio massimo,
#   sceglietene una sola come meglio preferite.
def squadraMediaMax(dizSquadre):
    maxMu = 0
    maxMuKey = 0
    for nomeSquadra in dizSquadre.keys():
        muPuntiPrest = dizSquadre[nomeSquadra]["muPuntiPrest"]
        if muPuntiPrest > maxMu:
            maxMu = muPuntiPrest
            maxMuKey = nomeSquadra
    risultato = (maxMuKey, maxMu)
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

print("1) Eseguo la funzione tStr2tCC: ")
te='''4'33"59'''
dp = tStr2tCC(te)
print(dp)

print("2) Eseguo la funzione dizPrestazione: ")
st='''       1   GUARESCHI  MARTINA             1990   Coopernuoto                 4'33"59  962,68'''
dp = dizPrestazione(st)
print(dp)

fname='A28A2018.txt'
print('3) Eseguo la funzione leggiGare: ')
gare = leggiGare(fname)
print(gare)

print('4) Eseguo la funzione leggiRisultati: ')
ris = leggiRisultati(fname)
print(ris)

print('5) Eseguo la funzione aggiungiMedia: ')
ris2 = aggiungiMedia(ris)
print(ris2)

print('6) Eseguo la funzione squadraMediaMax: ')
sMeMax = squadraMediaMax(ris2)
print(sMeMax)

print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
