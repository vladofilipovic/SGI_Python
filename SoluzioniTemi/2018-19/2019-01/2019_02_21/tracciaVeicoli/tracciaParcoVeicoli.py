# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'ParcoVeicoliCircolanti'

# di seguito sara' spiegato come usare questa struttura dati 
dicDest = {
    '7': 'AUTOVEICOLO IN SERVIZIO PUBBLICO DI LINEA INTEGRATIVO',
    '8': 'AUTOVEICOLO USO ESCLUSIVO DI POLIZIA',
    'A': 'AUTOVETTURA PER TRASPORTO DI PERSONE',
    'B': 'AUTOBUS PER TRASPORTO DI PERSONE',
    'C': 'AUTOCARRO PER TRASPORTO DI COSE',
    'I': 'AUTOCARAVAN',
    'L': 'AUTOVEICOLO PER USO SPECIALE',
    'O': 'TRAS.SPECIFICO PERSONE PART.CONDIZIONI',
    'P': 'AUTOVEIC.TRASP.PROMISCUO PERSONE/COSE',
    'S': 'TRATTORE STRADALE PER RIMORCHIO',
    'T': 'TRATTORE PER SEMIRIMORCHIO',
    'V': 'AUTOVEICOLO PER TRASPORTO SPECIFICO',
    '3': 'QUADRICICLO PER TRASP. DI PERSONE',
    '4': 'QUADRICICLO PER TRASP.DI COSE',
    '5': 'QUADRICICLO PER USO SPECIALE',
    '6': 'QUADRICICLO TRASP. SPECIFICO',
    '9': 'MOTOVEICOLO USO ESCLUSIVO DI POLIZIA',
    'D': 'TRICICLO PER TRASPORTO PROMISCUO',
    'F': 'TRICICLO PER USO SPECIALE',
    'G': 'TRICICLO PER TRASPORTO SPECIFICO',
    'M': 'MOTOCICLO PER TRASPORTO PERSONE',
    'N': 'TRICICLO PER TRASPORTO COSE',
    'Z': 'TRICICLO PER TRASPORTO DI PERSONE',
    'E': 'SEMIRIMORCHIO PER TRASPORTO SPECIFICO',
    'H': 'SEMIRIMORCHIO PER TRASPORTO COSE',
    'J': 'RIMORCHIO PER TRASPORTO ATTREZZATURE TURISTICHE E SPORTIVE',
    'K': 'RIMORCHIO PER TRASPORTI SPECIFICI',
    'Q': 'SEMIRIMORCHIO PER TRASPORTO PERSONE',
    'R': 'RIMORCHIO PER TRASPORTO COSE',
    'U': 'CARAVAN',
    'W': 'RIMORCHIO PER TRASPORTO PERSONE',
    'X': 'RIMORCHIO PER USO SPECIALE',
    'Y': 'SEMIRIMORCHIO PER USO SPECIALE'}

##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e dei
# file dati, descritti qua di seguito
#
# - File 1) 'ParcoVeicoliCircolantiLombardia2018.csv'
#   Il file memorizza i dati del parco veicoli viaggianti in Lombardia.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
# PROG,USO,DESTINAZIONE,PORTATA,FLAG_ANN_MASSA_RIMORC,CILINDRATA,ALIMENTAZIONE,MASSA_RIMORCHIABILE,NUMERO_POSTI,TIPO_ALIMENTAZIONE_IMPIANTO,KW,DT_PRIMA_IMMATRICOLAZIONE,NUMERO_ASSI,COD_SIGLA_EURO,EMISSIONI_CO2,PESO_COMPLESSIVO,COD_ISTAT_COMUNE,COD_ISTAT_PROVINCIA
# 4607724,4,J,1000,A, , ,,, ,,1989,1,EURO0,0,1300,029,017
# 710077,0,A,0,,01570,B,,5,,0,,0,,,0,133,013
# 3292399,0,M,139,A,"600,00",B,0,2,,57,2000,2,EURO1,0,440,073,017
# 14536586,0,A,405,P,"1242,00",B,800,4,,51,2015,2,EURO6,1150,1345,216,016
# 7627294,0,M,125,A,01064,B,,2,,55,2006,2,EURO2,0,470,012,108
# 7375619,0,A,485,P,01242,B,900,4,,48,2006,2,EURO4,1400,1575,144,017
# 1792720,0,A,434,P,01968,G,1400,5,,103,2004,2,EURO4,1490,1910,029,017
# 3475439,0,A,475,P,01870,G,1300,5,,72,2000,2,EURO2,1570,1840,027,108
# 8812536,0,A,398,P,01124,B,920,5,,44.1,2007,2,EURO4,1400,1483,143,013
# ...
#   La prima riga contiene l'intestazione del file.
#   Nelle righe successive, per ogni veicolo/riga ci sono 18 colonne il cui significato
#   e' descritto qua di seguito:
#    0, PROG: numero Progressivo associato al veicolo
#    1, USO: Uso del veicolo
#    2, DESTINAZIONE: Tipologia del veicolo.
#    3, PORTATA: La portata del veicolo in Kg.
#    4, FLAG_ANN_MASSA_RIMORC: Flag indicante se il veicolo può rimorchiare o meno.
#    5, CILINDRATA: Numero della cilindrata del veicolo.
#    6, ALIMENTAZIONE: Tipo dell'alimentazione del veicolo.
#    7, MASSA_RIMORCHIABILE: La massa massima rimorchiabile in Kg.
#    8, NUMERO_POSTI: Numero di posti possibile del veicolo.
#    9, TIPO_ALIMENTAZIONE_IMPIANTO: Impianto di alimentazione se installato successivamente.
#   10, KW: Potenza Kilowatt del veicolo.
#   11, DT_PRIMA_IMMATRICOLAZIONE: Anno dell'immatricolazione del veicolo.
#   12, NUMERO_ASSI: Numero degli assi del veicolo.
#   13, COD_SIGLA_EURO: Classificazione euro del veicolo.
#   14, EMISSIONI_CO2: EMISSIONI_CO2 in gr/Km.
#   15, PESO_COMPLESSIVO: Peso complessivo del veicolo senza la portata in Kg.
#   16, COD_ISTAT_COMUNE: Codice Istat del comune d'appartenenza del veicolo lombardo.
#   17, COD_ISTAT_PROVINCIA: Codice Istat della provincia d'appartenenza del veicolo lombardo.
#
# - File 2) 'Parco_Veicoli_Circolanti_Campi.txt'
#   Il file fornisce i dettagli per ciascuna delle
#   colonne/campi del file 'ParcoVeicoliCircolantiLombardia2018.csv', ivi
#   compresi i valori ammissibili.


##########################################################
# DESCRIZIONE DEL LAVORO DA SVOLGERE
##########################################################
#
# Implementate le seguenti funzioni, il commento che precede
# ogni funzione vi spiegherà cosa fare in dettaglio.
# Controllate nel corpo principale del programma (in fondo
# allo script), come vengono invocate le funzioni che
# implementerete.
# Per favore NON USATE le istruzioni input() o raw_input()
# nel codice che scriverete.
# Se volete potete implementare delle funzioni aggiuntive
# rispetto a quelle gia' presenti qua sotto.

# Vi forniamo un esempio della struttura dati come dovrebbe risultare dopo il
# caricamento dei dati presenti nel file e che potete utilizzare
# alternativamente a quella restituita dalla funzione che caricherà i dati.
# In caso non riusciate a caricare i dati dal file potrete utilizzarla.
# La struttura dati caricata dal file potrebbe essere più lunga.
#



##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso due stringhe, rispettivamente
#   destinazione e siglaEuro. La funzione deve restituire il valore booleano True
#   se entrambe le stringhe hanno valori ammissibili per (rispettivamente) i campi DESTINAZIONE e COD_SIGLA_EURO.
#   In caso contrario la funzione deve restituire False.
#   La descrizione dei valori ammissibili per ognuno dei due campi e' presente nel file
#   'Parco_Veicoli_Circolanti_Campi.txt'.
#   Per il campo DESTINAZIONE potete sfruttare la struttura dati
#   dicDEST presente all'inizio di questo script.
def valida(destinazione, siglaEuro):
    pass


# - La funzione seguente accetta come parametro in ingresso
#   il nome del file .csv contenente i dati sui veicoli.
#   La funzione deve restituire una lista di tuple come nell'esempio seguente:
#        [ [(PROGR, DT_PRIMA_IMMATRICOLAZIONE, ALIMENTAZIONE, COD_SIGLA_EURO, EMISSIONI_CO2, DESTINAZIONE),
#          ...
#          (...),
#        ]
#   dove ogni tupla contiene i dati un veicolo e le sole colonne di interesse sono:
#   PROGR
#   DT_PRIMA_IMMATRICOLAZIONE
#   ALIMENTAZIONE
#   COD_SIGLA_EURO
#   EMISSIONI_CO2
#   DESTINAZIONE
#
#   Inoltre, dovete escludere dal caricamento i dati delle righe in cui
#   DESTINAZIONE e COD_SIGLA_EURO non superano il controllo effettuato dalla funzione valida().
#
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete far lavorare la funzione senza tuttavia implementarla,
#   togliete il commento a return ..., la struttura dati restituita e' analoga
#   a quella che dovrebbe restituire la vostra implementazione.
#   OVVIAMENTE, se userete il return con la struttura dati gia' presente,
#   l'esercizio sara' considerato non svolto
def leggiDatiParco(fn):
    pass
    #return volids


# - La funzione seguente accetta come parametro in ingresso
#   la struttura dati ds restituita dalla funzione leggiDatiParco.
#   La funzione deve restituire una lista di liste cosi' formata:
#       [[anno,numVeicoliImm], [1999,9302190], ...]
#   in cui *numVeicoliImm* e' il numero di immatricolazioni effettuate  in *anno*.
#   Per esempio nell'anno 1999, ci sono state 9302190 immatricolazioni. 
def immatricolazioniAnno(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass


# - La funzione seguente accetta come parametro in ingresso
#   la struttura dati ds restituita dalla funzione leggiDatiParco.
#   La funzione deve restituire una dizionario di dizionari dove per
#   ciascun COD_SIGLA_EURO sia immagazzinato il valore numero totale dei
#   veicoli immatricolati e l'emissione media di CO2 per quel codice.
#   La funzione deve restituire una struttura dati come la seguente
#   {'EURO0':{numVeicoliImm:num, 'emissioneMedia':num },
#    'EURO1':{numVeicoliImm:num, 'emissioneMedia':num },
#   ...
#   }
#  Dove ogni chiave del dizionario esterno è un codice di COD_SIGLA_EURO, e
#  ciascun dizionario interno, ha la seguenti coppie chiavi:valori :
#  numVeicoliImm ha associato il numero totale dei veicoli immatricolati,
#  emissioneMedia ha associato il valor medio dell'emissione per quel codice calcolata
#  sulla base dei valori in EMISSIONI_CO2.
def analisiEcoEmissioni(ds):
    # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    pass


##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('Ciao nome: %s, cognome: %s.' % (nome, cognome))

print('1) Eseguo la funzione valida: ')
print(valida('2', 'EURO9'))

print('2) Eseguo la funzione leggiDatiParco: ')
nomeFile = 'ParcoVeicoliCircolantiLombardia2018.csv'
pvc = leggiDatiParco(nomeFile)
print(pvc)

print('3) Eseguo la funzione immatricolazioniAnno: ')
lIA = immatricolazioniAnno(pvc)
print(lIA)

print("4) Eseguo la funzione analisiEcoEmissioni: ")
res = analisiEcoEmissioni(pvc)
print(res)



print('Nome e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))
