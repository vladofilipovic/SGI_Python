# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe


nomeEsercizio = 'Turbine'


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file di dati, descritto qua di seguito
#
# - File 1) turbine.csv
#   Il file memorizza i dati raccolti sul funzionamento di alcune
#   turbine per il pompaggio d'acqua.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#   ID_Machine;Failure(S/N);flow_1;rpm_1;hz_1;flow_...;rpm_...;hz_...;flow_N;rpm_N;hz_N\r\n
#   0;S;180;2880;31680;150;2700;29700;130;2210;24310;90;1530;16830\r\n
#   1;N;50;900;10800;180;3060;36720;210;3780;45360;50;850;1700;150;2400;4800;210;3780;7560\r\n
#   2;N;140;2380;28560;140;2380;28560\r\n
#   3;S;80;1280;15360;180;3240;38880;170;2720;5440;120;2040;4080;100;1600;3200\r\n
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo. Seguono alcune precisazioni sulle informazioni
#   contenute nel file.
#   - ID_Machine: e' un intero che identifica univocamente la turbina
#   - Rottura(S/N) e' la colonna che riporta se la turbina si e'
#     rotta alla fine delle rilevazioni (S) oppure no (N).
#   - flow_...;rpm_...;hz_... sono 3 valori, rispettivamente
#     * la portata d'acqua,
#     * il numero di giri per minuto e
#     * le vibrazioni in hertz
#     rilevate sulla turbina all'inizio di ogni ora.
#     Per ogni turbina le rilevazioni vengono svolte coprendo un numero variabile N di ore di
#     funzionamento, dove N varia da turbina a turbina. Quindi il numero di rilevazioni
#     varia di riga in riga.
#     In ogni ora vengono sempre registrati 3 valori, quindi il numero di rilevazioni
#     presenti in una riga e' sempre multiplo di 3.
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
#   ingresso il nome del file contenente l'elenco delle rilevazioni sulle turbine.
#   La funzione deve restituire le informazioni sulle rotture delle turbine,
#   sotto forma di un dizionario con la struttura descritta nell'esempio seguente:
#         { id_turbina1:rottura, id_turbina2:rottura, ... }
#   dove id_turbina e' di tipo intero, mentre rottura e' una stringa che puo'
#   assumere il valore 'S' o 'N'.
def leggiRotture(filename):
    risultato = {}
    f = open (filename, "r")
    linea = f.readline ()
    while 1:
        linea = f.readline ()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range(len(elementi)):
            elementi[i] = elementi[i].strip()
        idTurbina = int(elementi[0])
        rottura = elementi[1]
        risultato[idTurbina] = rottura
    f.close()
    print (risultato)
    return risultato




# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file contenente l'elenco delle rilevazioni sulle turbine
#   (lo stesso file della funzione precedente).
#   La funzione deve restituire i dati raccolti sulle turbine,
#   sotto forma di un dizionario con la struttura descritta nell'esempio seguente:
#         { id_turbina1:(lista_flow, lista_rpm, lista_hz),
#         { id_turbina2:(...),
#         ... }
#   dove id_turbina e' una chiave associata ad una tupla e
#   la tupla è composta a suo volta da tre liste
#   * lista_flow contiene le rilevazioni dei flow,
#   * lista_rpm contiene le rilevazioni degli rpm,
#   * lista_hz conteiene le rilevazioni degli hz
#   Le rilevazioni fatte nella prima ora occupano i primi elementi delle tre liste,
#   le rilevazioni fatte nella seconda ora occupano le seconde posizioni delle liste, ...
def leggiRilevazioni(filename):
    risultato = {}
    f = open (filename, "r")
    linea = f.readline ()
    while 1:
        linea = f.readline ()
        if linea == "":
            break
        elementi = linea.split(";")
        for i in range(len(elementi)):
            elementi[i] = elementi[i].strip()
        idTurbina = int(elementi[0])
        listaFlow = []
        listaRpm = []
        listaHz = []
        i = 2
        while i < len(elementi)-2:
            listaFlow = listaFlow + [int(elementi[i])]
            listaRpm = listaRpm + [int(elementi[i+1])]
            listaHz = listaHz + [int(elementi[i+2])]
            i = i + 3
        risultato[idTurbina] = (listaFlow, listaRpm, listaHz)
    f.close()
    print(risultato)
    return risultato


# - La funzione seguente restituisce una lista contenente
#   un insieme di turbine.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, dovete SOLO USARLA negli
#   esercizi seguenti.
def listaATurbineSpeciali():
    return [1, 5, 10, 12, 34, 33, 40, 51]


# - La funzione seguente accetta come parametri in ingresso
#   la struttura dati restituita dalla funzione leggiRotture()
#   e deve restituire una tupla come nell'esempio seguente.
#
#        (n_turbine_rotte, n_turbine_sane)
#
#   contenente due numeri interi, rispettivamente il numero di turbine rotte
#   e il numero di turbine sane, il conteggio deve essere limitato solamente
#   al sottoinsieme di turbine, i cui id_turbina sono restituiti dalla funzione
#   listaATurbineSpeciali().
#   Il sottoinsieme di turbine non e' passato come parametro ma deve
#   essere ottenuto richiamando la funzione listaATurbineSpeciali().
#   Se non sono presenti turbine rotte, n_turbine_rotte deve essere pari a 0,
#   se non sono presenti turbine sane, n_turbine_sane deve essere pari a 0.
def statisticheTurbineSpeciali(rot):
    listaTS = listaATurbineSpeciali ()
    #for i in range(len(listaTS)):
        #idTurbinaSpeciale = listaTS[i]
    nRotte = 0
    nSane = 0
    for idTurbina in rot.keys():
        if idTurbina in listaTS:
            valore = rot.get(idTurbina,0)
            if valore =="N":
                nSane = nSane + 1
            else:
                nRotte = nRotte + 1
    print (nSane,nRotte)
    return (nSane, nRotte)




# - La funzione seguente accetta come parametri in ingresso:
#   la struttura dati restituita dalla funzione leggiRilevazioni()
#   e deve restituire una struttura dati come nell'esempio seguente:
#        { id_turbina1:indiceA1,
#          id_turbina2:indiceA2,
#         ...
#          id_turnina_n:indiceA_n
#        }
#   Dove indiceA e' cosi' definito:
#  * indiceA:  per ogni rilevazione si calcoli il rapporto tra le vibrazioni e i flow.
#     Si ricorda che per ogni turbina ci sono un numero (variabile) di rilevazioni orarie
#     Se il valore di un rapporto è maggiore del rapporto ottenuto per la rilevazione dell'ora
#     precedente, si incrementa un contatore. L'indiceA di una turbina e' pari
#     al valore di questo contatore al termine del confronto della sequenza delle rilevazioni orarie
#     fatte sulla turbina.
#     Se non ci sono incrementi indiceA deve essere posto a 0.
#     Ad esempio, se nei confronti tra i rapporti ottenuti dalle rilevazioni, per 6 volte la rilevazione
#     di un'ora restituisce un valore maggiore rispetto all'ora precedente, indiceA varrà 6.
def calcolaIndiceA(rilev):
    risultato = {}
    for idTurbina in rilev.keys():
        listaVib = rilev[idTurbina][2]
        listaFlow = rilev[idTurbina][0]
        indiceA = 0
        rapportoPrecedente = 0
        for i in range(len(listaVib)):
            rapporto = listaVib[i]/listaFlow[i]
            if rapporto > rapportoPrecedente:
                indiceA = indiceA + 1
            rapportoPrecedente = rapporto
        risultato[idTurbina] = indiceA - 1 
    print(risultato)
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

print("1) Eseguo la funzione leggiRotture: ")
fname='turbine.csv'
rotture = leggiRotture(fname)
print(rotture)

print('2) Eseguo la funzione leggiRilevazioni: ')
rilevazioni = leggiRilevazioni(fname)
print(rilevazioni)

print('3) Eseguo la funzione listaATurbineSpeciali: ')
lts = listaATurbineSpeciali()
print(lts)

print('4) Eseguo la funzione statisticheTurbineSpeciali: ')
sts = statisticheTurbineSpeciali(rotture)
print(sts)

print('5) Eseguo la funzione calcolaIndiceA: ')
isa = calcolaIndiceA(rilevazioni)
print(isa)

print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
