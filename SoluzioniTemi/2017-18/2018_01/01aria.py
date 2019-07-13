# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'rilevazioniAria'

# DESCRIZIONE DEL PROGRAMMA

# Il programma da implementare serve per analizzare i dati relativi
# all'inquinamento atmosferico in una zona prescelta verificando quante
# volte sono stati superate le soglie indicate dalla normativa.
# L'area d'interesse è l'intorno dell'università di Milano Bicocca (UniMiB) per
# un raggio di 10km. Le rilevazioni utilizzate provengono dagli open data messi
# a disposizione dalla Regione Lombardia e si riferiscono alle rilevazioni
# degli inquinanti atmosferici per l'anno 2017. I dati dei sensori contengono
# la posizione degli stessi espressa tramite Latitudine e Longitudine.
# Per il calolo della distanza vi viene fornita una funzione già implementata
# che dovrete sfruttare.

import math


# Nel file .zip trovate i seguenti file:
#
# - Stazioni_qualita_dell_aria.csv contenente i dati relativi ai sensori usati
#   per il rilevamento degli inquinanti nell'aria.
#   Ciascuna riga contiene le seguenti informazioni:
#    * Idsensore: Identificativo Univoco che distingue il sensore all’interno
#     della Rete di Qualità dell’Aria
#    * NomeTipoSensore: Tipologia inquinante. Nota bene: ogni sensore prende il
#      nome dalla specifica tipologia di inquinante che rileva.
#    * UnitaMisura: Unità di misura con cui viene restituito il valore del dato
#    * Idstazione: Identificativo Univoco che distingue la stazione all’interno
#     della Rete di Qualità dell’Aria
#    * NomeStazione: Località in cui è collocata la stazione
#    * Quota: Quota in metri slm a cui è collocata la stazione
#    * Provincia: Provincia in cui è collocata la stazione
#    * Comune: Comune in cui è collocata la stazione
#    * Indirizzo: Località in cui è collocata la stazione
#    * Storico: N = sensore attivo oppure S = sensore storico
#    * DataStart: Data inizio disponibilità dei dati
#    * DataStop: Data fine disponibilità dei dati (campo valorizzato solo se
#      il sensore è storico)
#    * UTM_Est: Coordinate UTM /zone 32N Est
#    * UTM_Nord: Coordinate UTM/zone 32N Nord
#    * Lat: Longitudine misurata in gradi
#    * Lng: Latitudine misurata in gradi
#    * location: (Latitudine in gradi; Longitudine in gradi)
#
# - 2017RilevazioniAria.csv contenente i dati relativi alle rilevazioni per
#   l'anno 2017.
#   Ciascuna riga contiene le seguenti informazioni:
#    * IDsensore: Identificativo Univoco che distingue il sensore
#    * Data:  Data e ora. L’orario del dato è "ora solare" e si riferisce alle
#       osservazioni ottenute fino all’orario indicato.
#    * Valore: se -9999 = dato mancante o invalido
#    * Stato: VA = dato valido, NA = dato invalido
#    * idOperatore: 1 = Valore medio
#
#   E' possibile associare una rilevazione ad un sensore tremite IDsensore.

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

# - grad2rad(gradi). La funzione accetta come unico parametro in ingresso
#   un valore espresso in gradi.
#   La funzione restituisce un valore espresso in radianti.
#   La funzione applica la conversione di un valore in gradi nel equivalente
#   in radianti. Per la conversione la funzione deve applicare la seguente
#   espressione matematica:
#       radianti = (gradi / 180) * pi_greco
#   Ad esempio, 45 gradi  sono equivalenti a 0.785398 radianti.
#   Per il valore di pi greco si ricorra alla costante math.pi della libreria math
#   Il valore restituito dalla funzione deve essere di tipo float.
def grad2rad(gradi):
    radianti = (gradi/180)*math.pi
    return radianti
print (grad2rad(45))



# NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
# NON DOVETE MODIFICARLA, la dovete SOLO USARE negli esercizi seguenti.
def latLonAB2km(aLat, aLong, bLat, bLong):
    """Calcola la distanza tra i punti a e b date le due latiduni e le due longitudini.
        aLat, aLong, bLat, bLong devono essere espressi in gradi (come nel dataset)
    """
    a_r = (grad2rad(aLat), grad2rad(aLong))
    b_r = (grad2rad(bLat), grad2rad(bLong))
    km = RQM * math.acos(math.sin(a_r[0]) * math.sin(b_r[0]) +
                         math.cos(a_r[0]) * math.cos(b_r[0]) *
                         math.cos(a_r[1] - b_r[1]))
    return km


# - dizIDSensoriInRange(filename, dist, inquinante).
#   La funzione accetta come parametri in ingresso la stringa contenente il
#   nome dele file con i dati relativi alle stazioni di monitoraggio, una
#   distanza espressa in chilometri ed una stringa che identifica il tipo di
#   inquinante.
#   Nota bene: il nome del file deve essere passato dal programma chiamante
#   come parametro.
#   La funzione restituisce un dizionario di dizionari con la seguente struttura:
#   {   'IDsensore': {'distanza': float, 'TipoSensore': stringa,
#                      'NomeStazione': stringa}, ...,
#       'IDsensore2': {'distanza': float, 'TipoSensore': stringa,
#                      'NomeStazione': stringa}, ...,
#       'IDsensoreN': {'distanza': float, 'TipoSensore': stringa,
#                      'NomeStazione': stringa}}
#   Ad esempio:
#   {'10320': {'distanza': 5.361145368313876, 'TipoSensore': 'PM10 (SM2005)',
#              'NomeStazione': 'Milano - via Senato'},
#    '10273': {'distanza': 4.582676630444521, 'TipoSensore': 'PM10 (SM2005)',
#              'NomeStazione': 'Milano - Pascal Citt\xc3\xa0 Studi'},...}
#   dove la chiave IDsensore è l'identificativo del sensore ed il dizionario
#   ad essa associato contiene un dizionario i cui elementi sono le coppie:
#       'distanza': valore della distanza in km tra il sensore stesso e la
#                   posizione di UniMiB ottenuta per mezzo della funzione
#                   latLonAB2km.
#       'TipoSensore': la stringa associata all'inquinante rilevato dal sensore,
#                       come compare nel file dei sensori.
#       'NomeStazione': la stringa contenente il nome della stazione.
#   Il dizionario di dizionari restituito dalla funzione deve contenere solo le
#   informazioni per i sensori che non distano più di dist da UniMiB e che
#   possano rilevare l'inquinante passato come parametro (nell'esempio PM10).
#   UniMiB è una tupla (Lat, Long) costante definita nel parte principale
#   del programma e che dovete utilizzare senza doverla ne' ridefinire
#   ne' passare come parametro.
def dizIDSensoriInRange(filename, dist, inquinante):
    risultato = {}
    f = open (filename, "r")
    linea = f.readline ()
    while 1:
        linea = f.readline ()
        if linea == "":
            break
        elementi = linea.split(",")
        for i in range (0, len(elementi)):
            elementi[i] = elementi[i].strip()
        #print(elementi)
        lat = float (elementi [13])
        lng = float (elementi [14])
        distanza = latLonAB2km (lat, lng, UniMiB[0], UniMiB[1])
        tipoSensore = elementi [1]
        #print (tipoSensore, inquinante)
        if inquinante in tipoSensore and distanza <= dist:
            idSensore = elementi [0]
            valore = {}
            valore["distanza"] = distanza
            valore["TipoSensore"] = tipoSensore
            valore["NomeStazione"] = elementi [4]
            risultato[idSensore] = valore
    f.close()
    #print (risultato)
    return risultato




# - SensoriAllarme(filename, dizIDsens, soglia).
#   La funzione accetta tre parametri in ingresso: la stringa contenente il
#   nome dele file con i dati relativi alle rilevazioni, una struttura dati
#   come quella restituita dalla funzione dizIDSensoriInRange ed un valore di
#   soglia numerico per l'inquinante.
#   Nota bene: il nome del file deve essere passato dal programma chiamante
#   come parametro.
#   La funzione restituisce un dizionario contente le informazioni dei sensori
#   che almeno una volta hanno superato il valore di soglia e che rientrano
#   nell'insieme dei sensori selezionati dalla funzione dizIDSensoriInRange().
#   Il dizionario deve avere la seguente
#   {'IDsensore1': conteggio1,
#       'IDsensore2': conteggio2, ...,
#       'IDsensoreN': conteggioN}
#   Ad esempio:
#   {'10320': 97, '9890': 87, '10273': 94, '6956': 84, '6908': 94}
#   Dove:
#       IDsensore: è l'identificativo del sensore e
#       conteggio: è il valore intero che corrisponde al numero di volte che
#                  il sensore ha superato la soglia.
def SensoriAllarme(filename, dizIDsens, soglia):
    risultato = {}
    f = open (filename, "r")
    linea = f.readline ()
    while 1:
        linea = f.readline ()
        if linea == "":
            break
        elementi = linea.split(",")
        for i in range (len(elementi)):
            elementi [i] = elementi[i].strip()
        valMisurato = float(elementi [2])
        if valMisurato > soglia:
            idSensore = elementi [0]
            if idSensore in dizIDsens.keys ():
                conteggio = risultato.get(idSensore,0)
                conteggio = conteggio + 1
                risultato[idSensore] = conteggio
    f.close()
    #print (risultato)
    return risultato




# - visualizza(dizSensori, dizAllarmi).
#   La funzione accetta due parametri in ingresso: la struttura dati restituita
#   dalla funzione SensoriAllarme e la struttura dati restituita dalla funzione
#   dizIDSensoriInRange.
#   Per ogni stazione che ha superato i valori di soglia, la funzione deve
#   stampare a video le seguenti informazioni: numero di volte che la soglia
#   e' stata oltrepassata, nome della stazione e distanza da UniMiB in km.
def visualizza(dizSensori, dizAllarmi):
    for idSensore in dizAllarmi.keys():
        conteggio = dizAllarmi[idSensore]
        nome = dizSensori[idSensore]["NomeStazione"]
        distanza = dizSensori[idSensore]["distanza"]
        print ("%s, %d, % f" % (nome, conteggio, distanza))



##########################################################
# Fine della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


RQM = 6372.795477598
UniMiB = (45.517309, 9.213865)
stazioniFile = 'Stazioni_qualita_dell_aria.csv'
rilevazioniFile = '2017RilevazioniAria.csv'

print('Esercizio %s.' % (nomeEsercizio))

print('Eseguo la funzione dizIDSensoriInRange')
dizIDSensori = dizIDSensoriInRange(stazioniFile, 10.0, 'PM10')
print (dizIDSensori)

print('Eseguo la funzione SensoriAllarme')
dizSensoriAllarmati = SensoriAllarme(rilevazioniFile,
                                     dizIDSensori, 50.0)
print('Eseguo la funzione visualizza')
visualizza(dizIDSensori, dizSensoriAllarmati)
# for el in dizSensoriAllarmati:
#     print el, dizSensoriAllarmati[el]
