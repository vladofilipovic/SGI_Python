# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Review01'

##########################################################
# INTRODUZIONE
##########################################################
#
# I file descritti qua di seguito contengono informazioni sulle review (valutazioni)
# che i clienti di alcuni ristoranti hanno scritto sul servizio ricevuto.
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e alcuni file di dati.
# I file con i dati sono:
#
#
# - File 1) fastfood.csv
#   Il file memorizza le informazioni sui locali oggetto delle valutazioni.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#        ID_FastFood;NomeFastFood;Citta;MetriQuadrati\r\n
#        0;PiadineriaRivazzurra;Lecce;640\r\n
#        1;Caffe600;Roma;640\r\n
#        2;Caffe600;Firenze;480\r\n
#        3;Panzer8;Bari;80\r\n
#        4;Farinata;Milano;80\r\n
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo. Seguono alcune precisazioni sulle informazioni
#   contenute nel file.
#   - ID_FastFood e' un intero che identifica univocamente il locale
#   - NomeFastFood e' il nome del fast food. Nota bene: lo stesso nome puo'
#     essere usato da locali diversi, sia nella stessa citta' sia in citta' diverse.
#     E' l'ID_FastFood che permette di distinguere locali diversi che pero'
#     hanno lo stesso nome.
#   - Citta e' il luogo in cui il fast food e' situato
#   - MetriQuadrati rappresenta la superficie del fast food
#
#
# - File 2) valutazioni.csv
#   Questo file memorizza le valutazioni date dagli utenti al servizio
#   ricevuto nel fast food.
#   Un esempio del contenuto del file e' il seguente.
#   Nella prima riga c'e' intestazione del file.
#   Nell'esempio non considerate il simbolo di # e gli spazi.
#
#      ID_Valutazione;ID_FastFood;ID_Utente;Data;Valutazioni...\r\n
#      0;25;143;11/09/2010;Atmosfera;Parcheggio;4.5;0.5\r\n
#      1;12;179;28/02/2010;Parcheggio;1.0\r\n
#      2;8;216;26/09/2010;Cibo;Costi;AccessoDisabili;5.0;4.0;2.5\r\n
#      3;14;5;07/08/2010;Cibo;3.0\r\n
#
#   Ogni riga contiene la valutazione fatta da un utente su un fast food.
#   Per esempio, la prima riga di dati
#   0;25;143;11/09/2010;Atmosfera;Parcheggio;4.5;0.5
#   contiene una valutazione (ID_Valutazione pari a 0) sull'ID_FastFood 25,
#   fatta dall'ID_Utente 143 nel giorno 11/09/2010. L'utente ha valutato
#   solo 2 "aspetti", Atmosfera e Parcheggio con voti rispettivamente pari a 4.5 e 0.5.
#   Ogni valutazione puo' contenere un numero variabile di voti, ognuno dato ad un
#   "aspetto" diverso. Per esempio nella riga successiva (ID_Valutazione pari a 1) e'
#   stato valutato solamente il "Parcheggio".
#   Gli "aspetti" valutabili sono: 'Parcheggio,AccessoDisabili,Atmosfera,Cibo,Costi'.
#   In ogni riga sono prima elencati gli "aspetti" valutati e poi i voti corrispondenti.
#   Ogni riga può contenere da 1 a 5 voti diversi.

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
#   ingresso il nome del file contenente l'elenco dei fast food.
#   La funzione deve restituire le informazioni sui fast food,
#   sotto forma di un dizionario con la struttura descritta nell'esempio seguente:
#         {
#          id_fast_food:[NomeFastFood, Citta, MetriQuadrati]
#          ...
#         }
#
#   Per maggiori informazioni sui dati coinvolti si faccia riferimento
#   alla descrizione del file contenente i dati.
#   Nell'esempio qua sopra id_fast_food e MetriQuadrati devono essere valori interi
def leggiFastFood(filename):
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
        idFastFood = int(elementi[0])
        nome = elementi[1]
        citta = elementi[2]
        mQuadri = int(elementi[3])
        risultato[idFastFood] = [nome, citta, mQuadri]
    f.close()
    print(risultato)
    return risultato




# - La funzione seguente restituisce una lista contenente
#   l'elenco degli aspetti valutati dagli utenti.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, dovete SOLO USARLA negli
#   esercizi seguenti.
def listaAspetti():
    return ['Parcheggio','AccessoDisabili','Atmosfera','Cibo','Costi']


# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con le informazioni sulle valutazioni effettuate dagli utenti.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#        [ (ID_Valutazione, ID_FastFood, ID_Utente, {aspetto1:voto1, aspetto2:voto2,... }),
#        ...
#        ]
#   Per esempio, la funzione leggendo le seguenti righe del file (i \r\n sono stati omessi)
#      ID_Valutazione;ID_FastFood;ID_Utente;Data;Valutazioni...
#      0;25;143;11/09/2010;Atmosfera;Parcheggio;4.5;0.5
#      1;12;179;28/02/2010;Parcheggio;1.0
#        ...
#   deve restituire la seguente struttura dati:
#        [ (0, 25, 143, {'Atmosfera'4.5, 'Parcheggio':0.5}),
#          (1, 12, 179, {'Parcheggio':1.0}),
#          ...
#        ]
#   Il dizionario contenuto in ogni tupla ha come chiavi gli aspetti valutati e come
#   valori i voti corrispondenti attribuiti dall'utente.
#   L'elenco dei possibili aspetti valutati e' quello restituito dalla funzione listaAspetti().
def leggiValutazioni(fname):
    risultato = []
    f = open(fname, "r")
    linea = f.readline()
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range(len(elementi)):
            elementi[i] = elementi[i].strip()
        idValutazione = int(elementi[0])
        idFastFood = int(elementi[1])
        idUtente = int(elementi[2])
        dizAspetti = {}
        j = 4
        numeroVoti = int((len(elementi)-4)/2)
        while j < (len(elementi)-numeroVoti):
            aspetto = elementi[j]
            voto = float(elementi[j+numeroVoti])
            dizAspetti[aspetto] = voto
            risultato = risultato + [(idValutazione, idFastFood,idUtente, dizAspetti)]
            j = j + 1
    f.close()
    return (risultato)



# - La funzione seguente accetta come parametri in ingresso
#   * la struttura dati restituita dalla funzione leggiValutazioni()
#   * il nome di un "aspetto" oggetto di valutazione.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#
#        {id_fast_food1:media_score1, id_fast_food2:media2, ...}
#
#   dove per ogni fast_food deve essere calcolato il punteggio medio ottenuto
#   rispetto all'aspetto passato come parametro.
#   Il parametro "aspetto" sara' una stringa con uno dei seguenti
#   valori (non occorre fare verifiche):
#   'Parcheggio', 'AccessoDisabili', 'Atmosfera', 'Cibo', 'Costi'
#   Se un fast food non riceve mai valutazioni sullo specifico aspetto,
#   allora non deve essere presente nella struttura dati restituita.
def valutazioneMediaAspetto(valutaz, aspetto):
    risultato = {}
    dizCalcolo = {}
    for i in range (len(valutaz)):
        idValutazione = valutaz[i][0]
        idFastFood = valutaz[i][1]
        idUtente = valutaz[i][2]
        dizAspetti = valutaz[i][3]
        if aspetto in dizAspetti.keys():
            valutazione = dizAspetti[aspetto]
            valore = dizCalcolo.get(idFastFood,[0.0,0])
            valore[0] = valore[0] + valutazione
            valore[1] = valore[1] + 1
            dizCalcolo[idFastFood] = valore
    for idFF in dizCalcolo.keys():
        sommaVoti = dizCalcolo[idFF][0]
        nVoti = dizCalcolo[idFF][1]
        media = sommaVoti/nVoti
        risultato[idFF] = media
    return risultato



# - La funzione seguente accetta come parametri in ingresso:
#   * valutaz: la struttura dati restituita dalla funzione leggiValutazioni()
#   * listaID_FastFood: una lista di id_fast_food, es. [0, 5, 6, 8, 12]
#   La funzione deve restituire una struttura dati come nell'esempio seguente:
#        { if_fast_food1:[media_aspetto_parcheggio, media_aspetto_accessodisabili,
#                         media_aspetto_atmosfera', media_aspetto_cibo, media_aspetto_costi],
#         ...}
#   Dove ogni chiave del dizionario restituita e' un id_fast_food,
#   ad ogni id_fast_food e' associata una lista con dentro le medie dei giudizi
#   dati dagli utenti ai diversi aspetti oggetto di valutazione.
#   L'ordine dei valori nelle liste deve essere quello dell'esempio qua sopra,
#   ed e' lo stesso con cui gli "aspetti" sono elencati nella lista restituita
#   dalla funzione listaAspetti().
#   Si suggerisce di sfruttare la precedebte funzione valutazioneMediaAspetto()
#   nell'implementare questa funzione.
#   Decidete voi come gestire l'eventuale caso di un fast food non ha valutazioni
#   su un singolo aspetto.
#   Nel dizionario restituito, devono essere presenti solo i fast food
#   i cui ID sono stati passati nel parametro in ingresso listaID_FastFood.
def generaRapporto(valutaz, listaID_FastFood):
    risultato = {}
    for i in range (len(valutaz)):
        idFastFood = valutaz[i][1]
        dizAspetti = valutaz[i][3]
        if idFastFood in listaID_FastFood:
            lAspetti = listaAspetti()
            for i in range(len(lAspetti)):
                if lAspetti[i] in dizAspetti.keys():
                    mediaPerAspetto = valutazioneMediaAspetto (valutaz, lAspetti[i])
                    risultato[idFastFood] = mediaPerAspetto
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

print("1) Eseguo la funzione leggiFastFood: ")
fname1='fastfood.csv'
ffood = leggiFastFood(fname1)
print(ffood)

print('2) Eseguo la funzione leggiValutazioni: ')
fname2='valutazioni.csv'
valut = leggiValutazioni(fname2)
print(valut)

print('3) Eseguo la funzione valutazioneMediaAspetto: ')
vma = valutazioneMediaAspetto(valut, 'Cibo')
print(vma)

print('Eseguo la funzione listaAspetti: ')
ris = listaAspetti()
print(ris)

print('4) Eseguo la funzione generaRapporto: ')
ffli=[0, 5, 6,8,12]
rap = generaRapporto(valut, ffli)
print(rap)

print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
