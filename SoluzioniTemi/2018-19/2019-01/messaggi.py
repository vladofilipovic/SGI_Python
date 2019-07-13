# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

dMessaggi = {
'cnCvh2949675':  {'tags': ['13'], 'msgID': 'cnCvh2949675', '+': 388, '-': 361, 'data': '2018:06:20', 'userID': 'FIW3720E'} ,
'MHWNK7996901':  {'tags': ['13', '17', '7', '9', '5'], 'msgID': 'MHWNK7996901', '+': 865, '-': 470, 'data': '2018:02:19', 'userID': 'WBC1361E'} ,
'puvBz0876489':  {'tags': ['18', '24'], 'msgID': 'puvBz0876489', '+': 561, '-': 141, 'data': '2018:03:29', 'userID': 'sEF0091T'} ,
'FFQdn6934145':  {'tags': ['26'], 'msgID': 'FFQdn6934145', '+': 634, '-': 758, 'data': '2018:02:24', 'userID': 'gtL2090M'} ,
'HlULW3493990':  {'tags': ['20', '13'], 'msgID': 'HlULW3493990', '+': 482, '-': 662, 'data': '2018:01:05', 'userID': 'XHk7709T'} ,
'tzipE0863408':  {'tags': ['7', '28', '22', '25'], 'msgID': 'tzipE0863408', '+': 633, '-': 800, 'data': '2018:09:17', 'userID': 'xrX7336E'} ,
'uPpSr0868368':  {'tags': ['4', '17', '28', '10', '8', '13'], 'msgID': 'uPpSr0868368', '+': 667, '-': 373, 'data': '2018:12:02', 'userID': 'cPr8884T'} ,
'kYnqG5818534':  {'tags': ['10', '21', '7', '23'], 'msgID': 'kYnqG5818534', '+': 549, '-': 840, 'data': '2018:09:10', 'userID': 'PeD5602T'} ,
'cKRvi2458293':  {'tags': ['7', '4', '6'], 'msgID': 'cKRvi2458293', '+': 460, '-': 42, 'data': '2018:11:03', 'userID': 'LdW6206E'} ,
'LLjFw3074114':  {'tags': ['14', '10', '15', '16'], 'msgID': 'LLjFw3074114', '+': 249, '-': 871, 'data': '2018:02:20', 'userID': 'DRU7015E'} ,
'nEPIh9111009':  {'tags': ['25', '6', '14', '20', '9'], 'msgID': 'nEPIh9111009', '+': 390, '-': 985, 'data': '2018:12:12', 'userID': 'KzY0689E'} ,
'zjvyD4252722':  {'tags': ['17', '15', '14'], 'msgID': 'zjvyD4252722', '+': 323, '-': 275, 'data': '2018:12:28', 'userID': 'xrX7336E'} ,
'JxSPe2784207':  {'tags': ['23'], 'msgID': 'JxSPe2784207', '+': 598, '-': 248, 'data': '2018:05:13', 'userID': 'cwX5570M'} ,
'Dxifh8134474':  {'tags': ['28', '24', '21'], 'msgID': 'Dxifh8134474', '+': 425, '-': 238, 'data': '2018:05:27', 'userID': 'GGS8172E'} ,
'dTrXA5236433':  {'tags': ['21', '7', '19', '27'], 'msgID': 'dTrXA5236433', '+': 386, '-': 904, 'data': '2018:10:28', 'userID': 'QnP1531M'} ,
'bFYSr8218545':  {'tags': ['1'], 'msgID': 'bFYSr8218545', '+': 881, '-': 747, 'data': '2018:08:30', 'userID': 'tWU8731T'} ,
'pKkns6143656':  {'tags': ['27', '8', '21', '10'], 'msgID': 'pKkns6143656', '+': 510, '-': 325, 'data': '2018:06:11', 'userID': 'VgZ2427M'} ,
'GZUjQ7847592':  {'tags': ['6', '24', '25', '28', '22', '20'], 'msgID': 'GZUjQ7847592', '+': 116, '-': 122, 'data': '2018:11:10', 'userID': 'LdW6206E'} ,
'mYwvS0541169':  {'tags': ['23', '22', '3', '21', '25'], 'msgID': 'mYwvS0541169', '+': 823, '-': 774, 'data': '2018:10:27', 'userID': 'zSN2923T'} ,
'Rtmjm1968558':  {'tags': ['12', '6', '10', '15'], 'msgID': 'Rtmjm1968558', '+': 215, '-': 872, 'data': '2018:01:15', 'userID': 'HWJ8620E'}
}


nomeEsercizio = 'messagesReport'

##########################################################
# INTRODUZIONE
##########################################################
#
# Una sito web desidera analizzare i messaggi che vengono scambiati dai propri
# utenti e decide di sfruttare il file di log 'messages.log' ad essi associato.
#
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete il seguente file, oltre a questo script:
#
# - File 1) messages.log.
#       Il file contiene le informazioni da analizzare per ciascun messaggio
#       che è transitato sulla piattaforma.
#       I blocchi di informazione associati ai messaggi sono separati da una
#       riga vuota e ciascuna riga contiene al più 80 caratteri.
#       Il formato in cui sono salvate le informazioni di ogni messaggio è il
#       seguente:
#
# usrID @ msgID
# data++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++-------------------------------------------------------
# ---------------------------|T24T4T11
#
#  - usrID è l'identificativo unico dell'utente. Ciascun utente può postare
#          più messaggi
#  - msgID è l'identificativo unico del messaggio.
#  - data  è la data in cui è stato postato il messaggio. La data può comparire
#          in due formati: aaaa:mm:gg oppure gg:mm:aaaa
#  - '+'   il carattere '+' indica un parere positivo espresso per il messaggio
#  - '-'   il carattere '-' indica un parere negativo espresso per il messaggio
#  - |T24... il carattere '|' indica che seguno le etichette associate al
#             messaggio. Ciascuna è formata dal carattere 'T' seguito da un
#             numero. Il numero di etichette per ciascun messagio è variabile.
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


# - uniformaData(data). La funzione accetta come unico parametro in ingresso
# una stringa contenente una data in uno dei due formati possibili nel file:
# aaaa:mm:gg oppure gg:mm:aaaa. La funzione deve restituire una stringa che
# contenga la data nel formato aaaa:mm:gg.
# Esempio:
# '07:09:2018' -> '2018:09:07'
# '2018:02:18' -> '2018:02:18'
def uniformaData(data):
    elementi = data.split(":")
    if len(elementi[0]) == 2:
        giorno = elementi[0]
        mese = elementi[1]
        anno = elementi[2]
        return anno + ":" + mese + ":" + giorno
    return data


# - caricaMessaggi(filename). La funzione accetta come unico parametro in
# ingresso una stringa contenente il nome del file da processare.
# La funzione deve restituire il dizionario dei messaggi che è un dizionario di
# dizionari che contiene le informazioni associate a ciascun messaggio.
# Per ogni messaggio le informazioni ad esso associate saranno contenute in un
# dizionario con la seguente struttura:
# {'msgID': stringa, 'userID': stringa, 'data': stringa,
#  'tags': [stringa, stringa, ...],  '+': intero, '-': intero }
# Dove i valori associati alle seguenti chiavi sono:
#   'msgID' è il codice associato al messaggio
#   'userID' è il codice associato all'utente
#   'data' è la data nel formato aaaa:mm:gg
#   'tags' lista di stringhe, una per ogni etichetta '|T21' diventa ['21']
#   '+': numero di valutazioni favorevoli ottenibile come conteggio dei '+'
#   '-': numero di valutazioni negative ottenibile come conteggio dei '-'
# Il dizionario dei messaggi deve avere come chiavi i codici dei messaggi
# presenti nel file e come valori i dizionari con la struttura appena descritta.
# Esempio
# {'cnCvh2949675': {'tags': ['13'], 'msgID': 'cnCvh2949675', '+': 388, '-': 361, 'data': '2018:06:20', 'userID': 'FIW3720E'},
# 'MHWNK7996901': {'tags': ['13', '17', '7', '9', '5'], 'msgID': 'MHWNK7996901', '+': 865, '-': 470, 'data': '2018:02:19', 'userID': 'WBC1361E'},
# 'puvBz0876489': {'tags': ['18', '24'], 'msgID': 'puvBz0876489', '+': 561, '-': 141, 'data': '2018:03:29', 'userID': 'sEF0091T'}, ...}
def caricaMessaggi(filename):
    risultato = {}
    f = open(filename, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        if "@" in linea:
            userId = linea.split("@")[0]
            msgId = linea.split("@")[1]
        elif ":" in linea:
            sData = linea[0:10]
            data = sData.split(":")
            if len(data[0])==2:
                data = uniformaData(sData)
            primaRigaPiuMeno = linea[10:]
            nPiu = primaRigaPiuMeno.count("+")
            nMeno = primaRigaPiuMeno.count("-")
        elif "+" == linea[0] or "-" == linea[0]:
            nPiu = nPiu + linea.count("+")
            nMeno = nMeno + linea.count("-")
            if "|" in linea:
                posizione = linea.find("|")
                strTags = linea[posizione+1:]
                lTags = strTags.split("T")
                risultato[msgId] = {"tags" : lTags, "msgID": msgId, "userID" : userId, "data" : data, "+": nPiu, "-" : nMeno}
    return risultato







# - generaRepUtenti(dizMessaggi). La funzione accetta come unico parametro in
#   ingresso la struttura dati restituita dalla funzione caricaMessaggi.
#   La funzione deve restituire un dizionario contenente il report delle
#   informazioni per ciascun utente presente nel file. Di ciascun utente il
#   dizionario deve avere la seguente struttura:
#   {'nMessaggi': intero, 'nPlus': intero, 'nMinus': intero, 'meanPlus': float, 'meanMinus': float}
#   e contenere le seguenti informazioni:
#   - 'nMessaggi' numero totale dei messaggi postati dall'utente,
#   - 'nPlus': numero totale dei pareri favorevoli,
#   - 'nMinus': numero totale dei pareri sfavorevoli,
#   - 'meanPlus': numero medio di pareri favorevoli per messaggio,
#   - 'meanMinus': numero medio di pareri sfavorevoli per messaggio
# Il dizionario dei report per utente deve avere come chiavi il codice degli utenti
# presenti nel file e come valori i dizionari con la struttura appena descritta.
# Esempio:
# {'VeP4436E': {'meanMinus': 573.5806451612904, 'nMessaggi': 31, 'nMinus': 17781, 'meanPlus': 619.741935483871, 'nPlus': 19212},
# 'gtE1535M': {'meanMinus': 536.2758620689655, 'nMessaggi': 29, 'nMinus': 15552, 'meanPlus': 522.0344827586207, 'nPlus': 15139},
# 'XFD8832E': {'meanMinus': 530.6363636363636, 'nMessaggi': 33, 'nMinus': 17511, 'meanPlus': 614.3333333333334, 'nPlus': 20273}, ... }
def generaRepUtenti(dizMessaggi):
    risultato = {}
    dizCalcolo = {}
    for msgId in dizMessaggi.keys():
        idUtente = dizMessaggi[msgId]["userID"]
        nPlus = dizMessaggi[msgId]["+"]
        nMinus = dizMessaggi[msgId]["-"]
        valore = dizCalcolo.get(idUtente, {"nMessaggi": 0, "nPlus" : 0, "nMinus": 0})
        valore["nMessaggi"] = valore["nMessaggi"] + 1
        valore["nPlus"] = valore["nPlus"] + nPlus
        valore["nMinus"] = valore["nMessaggi"] + nMinus
        dizCalcolo[idUtente] = valore
    for idUtente in dizCalcolo.keys():
        nMessaggi = dizCalcolo[idUtente]["nMessaggi"]
        nPlus = dizCalcolo[idUtente]["nPlus"]
        nMinus = dizCalcolo[idUtente]["nMinus"]
        meanPlus = nPlus/nMessaggi
        meanMinus = nMinus/nMessaggi
        risultato[idUtente] = {"nMessaggi": nMessaggi, "nPlus" : nPlus, "nMinus": nMinus, "meanPlus": meanPlus, "meanMinus" : meanMinus}
    print (risultato)
    return risultato


# - trovaMinMax(dizRepUsrs). La funzione accetta come unico parametro in
#   ingresso la struttura dati restituita dalla funzione generaRepUtenti.
#   La funzione deve stampare a video il massimo valore medio di conteggi di '+'
#   ottenuto tra tutti gli utenti ed il codice dell'utente che lo ha ottenuto
#   insieme al più piccolo valor medio dei conteggi di '-' ed il codice
#   dell'utente che lo ha ottenuto
# Esempio:
# max mean pluses 681.03030303 utente xrX7336E
# min mean minuses 359.172413793 utente Ozf5583T
def trovaMinMax(dizRepUsrs):
    minMinus = 1e8
    idMinMinus = ""
    maxPlus = -1
    idMaxPlus = ""
    for idUtente in dizRepUsrs.keys():
        meanPlus = dizRepUsrs[idUtente]["meanPlus"]
        meanMinus = dizRepUsrs[idUtente]["meanMinus"]
        if meanMinus < minMinus :
            minMinus = meanMinus
            idMinMinus = idUtente
        if meanPlus > maxPlus:
            maxPlus = meanPlus
            idMaxPlus = idUtente
    print(minMinus, idMinMinus, maxPlus, idMaxPlus)
    return (minMinus, idMinMinus, maxPlus, idMaxPlus)

##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('Ciao %s, %s .' % (nome, cognome))

print("1) Eseguo la funzione uniformaData(data) ")
print(uniformaData("07:09:2018"))

print("2) Eseguo la funzione caricaMessaggi('messages.log') ")
dMessaggi = caricaMessaggi('messages.log') # commenta questa riga se vuoi usare la struttura dati precaricata
print('numero messaggi caricati: ', len(dMessaggi))

print("3) Eseguo la funzione generaRepUtenti(dMessaggi) ")
dUtenti = generaRepUtenti(dMessaggi)
print('numero utenti/report generati: ', len(dUtenti))

print("4) Eseguo la funzione trovaMinMax(dUtenti) ")
trovaMinMax(dUtenti)

print('Nome dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
