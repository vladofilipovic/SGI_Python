# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Raccolta Finanziamenti'

##########################################################
# INTRODUZIONE
##########################################################
#
# Un sito web permette di realizzare campagne di raccolta fondi.
# Le persone che hanno idee imprenditoriali ma che necessitano di denaro
# possono avviare una campagna di raccolta fondi utilizzando il sito web.
# Il proponente inserisce nel sito web una descrizione del progetto, una
# cifra obiettivo e le date di apertura e chiusura della raccolta fondi.
# I progetti possono avere cifre obiettivo diverse.
# I visitatori del sito possono effettuare delle donazioni ai progetti di
# loro preferenza.
# Se le donazioni ad un progetto raggiungono la cifra obiettivo, il progetto
# ha successo e i soldi vengono passati alle persone che hanno avviato la
# raccolta fondi. I progetti che invece non raggiungono la cifra obiettivo
# sono considerati insuccessi e i soldi raccolti vengono restituiti ai donatori.
# Ogni riferimento a fatti reali e' puramente casuale.

##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e alcuni file di dati.
# I file con i dati sono:
#
# - File 1) progetti.csv
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#   ID_Progetto;Nome_Progetto;CifraObiettivo;DataInizio;DataFine;Categoria\r\n
#   560;Progetto 1;640000;21/08/2020;25/05/2021;Categoria 5\r\n
#   758;Progetto 2;820000;15/01/2018;08/12/2018;Categoria 5\r\n
#   302;Progetto 3;690000;09/01/2018;04/02/2022;Categoria 3\r\n
#   984;Progetto 4;1140000;05/02/2019;27/11/2021;Categoria 8\r\n
#   ...
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo.
#   Le informazioni memorizzate sono le seguenti:
#   - ID_Progetto. Un valore numerico che identifica univocamente un progetto.
#   - Nome_Progetto. Il nome del progetto.
#   - CifraObiettivo. La cifra obiettivo che deve essere raccolta. Se le
#              donazioni risulteranno insufficienti il progetto non partira'.
#   - DataInizio. La data di inizio della raccolta.
#   - DataFine. La data di fine della raccolta.
#   - Categoria. La categoria in cui il progetto e' classificato.
#
#
# - File 2) sottoscrizioni.csv
#   Un esempio del contenuto del file e' il seguente.
#   Nella prima riga non c'e' intestazione del file.
#   Nell'esempio non considerate il simbolo di # e gli spazi.
#
#   >ID_Utente;200\r\n
#   461;7100;683;6800;398;9300\r\n
#   383;5800;619;7600;871;5300\r\n
#   845;6000;772;3900\r\n
#   331;8200\r\n
#   \r\n
#   >ID_Utente;201\r\n
#   874;3000;302;9700;19;2600\r\n
#   40;4100\r\n
#   \r\n
#   >ID_Utente;202\r\n
#   845;2000;755;2200\r\n
#   846;9200\r\n
#   \r\n
#
#   ...
#
#   Il gruppo di righe che iniziano con un > rappresentano
#   le donazioni fatte da un singolo utente. Es.,  >ID_Utente;200\r\n
#   segna l'inizio delle donazioni effettuate dall'utente con ID_Utente 200.
#   Le informazioni sulle donazioni effettuate dall'utente sono contenute nelle
#   righe successive e terminano quando si incontra una riga vuota
#   (cioe' una riga con la sola interlinea).
#   Le informazioni sulle donazioni sono rappresentate da coppie di numeri consecutivi,
#   i numeri sono separati tra loro da punti e virgola.
#   Le coppie di numeri vanno interpretate in questo modo:
#   - il primo numero della coppia e' l'id_progetto del progetto a cui si e' donato,
#   - il secondo numero e' l'importo donato (in genere e' un multiplo di 100).
#   Per esempio, la riga
#   461;7100;683;6800;398;9300\r\n
#   indica che all'id_progetto 461 sono stati donati 7100 euro,
#   all'id_progetto 683 sono stati donati 6800 euro e
#   all'id_progetto 398 sono stati donati 9300 euro.
#   Per vostra semplicita', potete assumere che:
#   - le informazioni su un donatore sono presenti una e una sola volta nel file.
#   - un donatore NON dona una seconda volta allo stesso progetto
#   - una coppia id_progetto e importo donato non è mai spezzata su righe diverse



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
#   ingresso il nome del file contenente i dati dei progetti
#   per i quali e' stata avviata la campagna di raccolta fondi.
#   La funzione restituisce una struttura dati come nell'esempio seguente:
#         {
#          id_progetto1:[Nome_Progetto1, CifraObiettivo1, DataInizio1, DataFine1, Categoria1],
#          id_progetto2:[Nome_Progetto2, CifraObiettivo2, DataInizio2, DataFine2, Categoria2],
#          ...
#         }
#   Per ogni progetto, nel dizionario restituito sara' presente una coppia chiave:lista di valori.
#   Per maggiori informazioni sui dati coinvolti si faccia riferimento all'intestazione del file progetti.csv.
#   Nell'esempio qua sopra
#   - id_progetto, CifraObiettivo devono assumere valori interi
#   - Nome_Progetto, DataInizio, DataFine, Categoria sono stringhe
#   Dai dati restituiti devono essere escluse le intestazioni del file.
#
def leggiProgetti(filename):
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
        idProgetto = int(elementi[0])
        nomeProgetto = elementi[1]
        cifraObiettivo = int(elementi[2])
        dataInizio = elementi[3]
        dataFine = elementi[4]
        categoria = elementi[5]
        valore = risultato.get(idProgetto, [0,0,0,0,0])
        valore[0] = nomeProgetto
        valore[1] = cifraObiettivo
        valore[2] = dataInizio
        valore[3] = dataFine
        valore[4] = categoria
        risultato[idProgetto] = valore
    f.close()
    print(risultato)
    return risultato





# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con le sottoscrizioni effettuate dagli utenti.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#              [ (id_utente, id_progetto, importo_finanziamento), ... ]
#   Ogni elemento della lista restituita e' una tupla che riporta rispettivamente
#   le informazioni su:
#   - id_utente del donatore (valore di tipo intero)
#   - id_progetto che identifica il progetto (valore di tipo intero)
#   - l'importo donato (valore di tipo intero)
#   Nota bene: le donazioni fatte dallo stesso utente a progetti diveresi
#   devono essere memorizzate su elementi diversi della lista.
#
def leggiSottoscrizioni(fname):
    risultato = []
    f = open(fname, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        if linea[0] == ">":
            #print(linea)
            elementi = linea.split(";")
            for i in range(len(elementi)):
                elementi[i] = elementi[i].strip()
            idUtente = int(elementi[1])
        else:
            elementi = linea.split(";")
            for i in range(len(elementi)):
                elementi[i] = elementi[i].strip()
            i = 0
            while i < len(elementi) - 1:
                idProgetto = int(elementi[i])
                importoFinzanziamento = int(elementi[i+1])
                risultato = risultato +[(idUtente,idProgetto, importoFinzanziamento)]
                i = i + 2
    f.close()
    #print(risultato)
    return(risultato)



# - La funzione seguente accetta come parametri in ingresso
#   le strutture dati restituite rispettivamente dalle funzioni
#   leggiProgetti() e leggiSottoscrizioni().
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#        {id_progetto:(cifra_raccolta, cifra_obiettivo), ...}
#   in cui devono essere inseriti solo i dati dei progetti che
#   NON SONO riusciti a raccogliere la cifra obiettivo.
#   Per vostra semplicita', nella ricerca dei progetti, considerate
#   solo i progetti per i quali esiste almeno una donazione.
#
def individuaIncompleti(progetti, sottoscrizioni):
    risultato = {}
    for idProgetto in progetti:
        cifraObiettivo = progetti[idProgetto][1]
        cifraRaccolta = 0
        for i in range(len(sottoscrizioni)):
            if sottoscrizioni[i][1] == idProgetto:
                cifraRaccolta = cifraRaccolta + sottoscrizioni[i][2]
        if cifraRaccolta < cifraObiettivo:
            risultato[idProgetto] = [(cifraRaccolta, cifraObiettivo)]
    print(risultato)
    return risultato




# - La funzione seguente restituisce una lista contenente
#   il numero dei giorni che compongono i mesi dell'anno.
#   La funzione non ha parametri in ingresso.
#   Per maggiori informazioni, vedi commento all'interno della funzione.
#
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, la dovete SOLO USARE negli
#   esercizi seguenti.
def lunghezzaMesi():
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Numero giorni rispettivamente nei mesi di Gen., Feb., ...


# - La funzione seguente accetta due parametri in ingresso
#   che rappresentano due date (chiamati rispettivamente data e partenza).
#   La funzione deve restituire il numero di giorni che intercorrono tra le 2 date.
#   Nel conteggio dei giorni, solo uno dei 2 estremi va considerato. Esempio:
#   - giorniDa('25/01/2018', '23/01/2018') deve restituire 2
#   - giorniDa('01/03/2018', '25/02/2018') deve restituire 4 # si ricorda che febbraio ha 28 giorni.
#   - giorniDa('01/03/2019', '25/02/2018') deve restituire 369 #
#   Per vostra semplicita' assumete che
#   - la data passata in "data" sara' sempre successiva alla data passata in "partenza".
#   - tutti gli anni hanno 365 giorni (cioe' non considerate gli anni bisestili).
#   - non saranno mai passate date precedenti allo 01/01/2000
def giorniDa(data, partenza):
    d = data.split("/")
    gD = int(d[0])
    mD = int(d[1])
    aD = int(d[2])
    p = partenza.split("/")
    gP = int(p[0])
    mP = int(p[1])
    aP = int(p[2])
    print(gD, mD, aD, gP, mP, aP)
    return 0






# - La funzione seguente accetta come parametri in ingresso
#   la struttura dati restituita da leggiProgetti().
#   La funzione deve calcorare per ogni progetto
#   l'indicatore dato dal rapporto tra
#   la cifra obiettivo della raccolta e il numero di
#   giorni in cui la raccolta e' rimasta aperta.
#   La funzione deve restituire, per il progetto che ha il valore piu' piccolo dell'indicatore,
#   una tupla contente l'id del progetto e il valore dell'indicatore, come nell'esempio seguente.
#        (id_progetto, valore_indicatore)
#   dove valore_indicatore deve essere di tipo float.
#   Suggeriamo di utilizzare la funzione giorniDa() per calcolare i giorni in cui la raccolta e'
#   rimasta aperta.
def statisticheProgetti(datiProgetti):
    pass  # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.






##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


print('Esercizio %s.' % (nomeEsercizio))

print('Ciao %s, %s .' % (nome, cognome))

print("1) Eseguo la funzione leggiProgetti: ")
fname1='progetti.csv'
datiProgetti = leggiProgetti(fname1)
print(datiProgetti)

print('2) Eseguo la funzione leggiSottoscrizioni: ')
fname2='sottoscrizioni.csv'
datiSottosc = leggiSottoscrizioni(fname2)
print(datiSottosc)

print('3) Eseguo la funzione individuaIncompleti: ')
incompleti = individuaIncompleti(datiProgetti, datiSottosc)
print(incompleti)

print('4) Eseguo la funzione giorniDa: ')
giorni = giorniDa('01/03/2019', '25/02/2018')
print(giorni)

print('5) Eseguo la funzione statisticheProgetti: ')
stat = statisticheProgetti(datiProgetti)
print(stat)

print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
