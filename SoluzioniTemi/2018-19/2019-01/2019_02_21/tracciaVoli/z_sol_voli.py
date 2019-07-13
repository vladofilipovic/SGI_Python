# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

from __future__ import print_function

nomeEsercizio = 'Voli'


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritto qua di seguito
#
# - File 1) 'dati_voli.csv'
#   Il file memorizza i dati raccolti sui viaggi svolti dai clienti di
#   una compagnia aerea.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#   Gli a capo (\r\n) sono stati omessi per semplicità.
#
#   Marcatore;Codice_volo;Nome;Cognome;Prezzo;Citta_partenza;Citta_arrivo;distanza_percorsa...
#   ***;AK032;Giorgia;Costa;747;Vienna;Lisbona;2236;***;AK004;Leonardo;Romano;311;Milano;Madrid;1250;***;AK020;Leonardo;Rinaldi;715;Londra;Parigi;559
#   ***;AK026;Lorenzo;Rinaldi;532;Londra;Zurigo;965
#   ***;AK033;Martina;Marino;471;Vienna;Zurigo;608;***;AK018;Andrea;Ferrari;531;Praga;Zurigo;570
#   ***;AK003;Andrea;Russo;7;Milano;Parigi;559
#   ***;AK029;Lorenzo;Ricci;767;Vienna;Barcellona;1250;***;AK037;Alessandro;Marino;205;Parigi;Berlino;901;***;AK005;Martina;Rossi;244;Milano;Barcellona;707
#   ***;AK013;Alice;Rossi;349;Praga;Madrid;1839;***;AK009;Gabriele;Gallo;423;Milano;Zurigo;180
#   ***;AK008;Martina;Ferrari;649;Milano;Lisbona;1677;***;AK014;Mattia;Esposito;640;Praga;Barcellona;1312
#   ***;AK020;Beatrice;Greco;356;Londra;Parigi;559;***;AK046;Lorenzo;Rizzo;424;Barcellona;Berlino;1457
#   ***;AK050;Beatrice;Colombo;760;Bruxelles;Lisbona;2126
#   ...
#
#   La prima riga contiene l'intestazione del file.
#   Il file contiene informazioni sui voli effettuati dai clienti di una compagnia aerea.
#   IMPORTANTE: in ogni riga ci possono essere le informazioni di uno o più voli, scritte di seguito sulla stessa riga.
#   Il marcatore *** aiuta ad individuare dove iniziano i dati di un volo. Vedi esempio qua sopra.
#   Per ogni volo sono memorizzate le seguenti informazioni
#   - Codice_volo. Un codice volo individua un volo che parte e arriva sempre nelle stesse citta'
#   - Nome (del cliente)
#   - Cognome (del cliente)
#   - Prezzo (pagato dal cliente per il biglietto)
#   - Citta_partenza. La citta' da dove il volo parte
#   - Citta_arrivo. La citta' dove il volo arriva
#   - Distanza_percorsa. La distanza percorsa in km
#   L'ordine con cui si ripetono le informazioni di un singolo volo rimane invariato nelle diverse righe.


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


# Vi forniamo un esempio di struttura dati,
# come dovrebbe risultare dopo il caricamento dei dati presenti nel file.
# La struttura dati caricata dal file potrebbe essere più lunga.
# Ogni tupla contiene rispettivamente
# (Codice_volo,Nome,Cognome,Prezzo,Citta_partenza,Citta_arrivo,distanza_percorsa)

volids=[
('AK015', 'Greta', 'Esposito', '261', 'Praga', 'Bruxelles', '291'), ('AK042', 'Tommaso', 'Romano', '446', 'Madrid', 'Berlino', '1952'), ('AK029', 'Emma', 'Rossi', '639', 'Vienna', 'Barcellona', '1250'), ('AK046', 'Francesco', 'Conti', '174', 'Barcellona', 'Berlino', '1457'), ('AK011', 'Emma', 'Costa', '596', 'Praga', 'Vienna', '291'), ('AK036', 'Greta', 'Romano', '820', 'Parigi', 'Bruxelles', '721'), ('AK040', 'Alice', 'Esposito', '374', 'Madrid', 'Barcellona', '559'), ('AK048', 'Gabriele', 'Rinaldi', '205', 'Barcellona', 'Zurigo', '763'), ('AK029', 'Mattia', 'Russo', '144', 'Vienna', 'Barcellona', '1250'), ('AK050', 'Ginevra', 'Conti', '479', 'Bruxelles', 'Lisbona', '2126'), ('AK042', 'Giorgia', 'Rinaldi', '560', 'Madrid', 'Berlino', '1952'), ('AK029', 'Beatrice', 'Moretti', '848', 'Vienna', 'Barcellona', '1250'), ('AK031', 'Francesco', 'Colombo', '528', 'Vienna', 'Berlino', '559'), ('AK019', 'Sofia', 'Fontana', '455', 'Londra', 'Vienna', '1520'), ('AK028', 'Leonardo', 'Moretti', '705', 'Vienna', 'Madrid', '1802'), ('AK036', 'Emma', 'Ferrari', '268', 'Parigi', 'Bruxelles', '721'), ('AK002', 'Aurora', 'Moretti', '937', 'Milano', 'Vienna', '559'), ('AK042', 'Mattia', 'Rossi', '681', 'Madrid', 'Berlino', '1952'), ('AK034', 'Mattia', 'Moretti', '933', 'Parigi', 'Madrid', '1118'), ('AK053', 'Giulia', 'Rossi', '160', 'Berlino', 'Zurigo', '694'), ('AK046', 'Giorgia', 'Esposito', '981', 'Barcellona', 'Berlino', '1457'), ('AK050', 'Aurora', 'Romano', '46', 'Bruxelles', 'Lisbona', '2126'), ('AK014', 'Andrea', 'Moretti', '253', 'Praga', 'Barcellona', '1312'), ('AK026', 'Gabriele', 'Rizzo', '553', 'Londra', 'Zurigo', '965'), ('AK032', 'Lorenzo', 'Rossi', '178', 'Vienna', 'Lisbona', '2236'), ('AK013', 'Riccardo', 'Rinaldi', '606', 'Praga', 'Madrid', '1839'), ('AK040', 'Giulia', 'Ricci', '949', 'Madrid', 'Barcellona', '559'), ('AK017', 'Alessandro', 'Ferrari', '139', 'Praga', 'Lisbona', '2232'), ('AK032', 'Beatrice', 'Ricci', '473', 'Vienna', 'Lisbona', '2236'), ('AK016', 'Giulia', 'Rinaldi', '774', 'Praga', 'Berlino', '269'), ('AK001', 'Ginevra', 'Marino', '74', 'Milano', 'Londra', '1118'), ('AK006', 'Francesco', 'Colombo', '175', 'Milano', 'Bruxelles', '657'), ('AK052', 'Alessandro', 'Gallo', '473', 'Berlino', 'Lisbona', '2304'), ('AK042', 'Alessandro', 'Bianchi', '952', 'Madrid', 'Berlino', '1952'), ('AK001', 'Giorgia', 'Fontana', '589', 'Milano', 'Londra', '1118'), ('AK044', 'Alessandro', 'Rossi', '231', 'Madrid', 'Zurigo', '1272'), ('AK006', 'Riccardo', 'Bianchi', '563', 'Milano', 'Bruxelles', '657'), ('AK018', 'Martina', 'Gallo', '622', 'Praga', 'Zurigo', '570'), ('AK054', 'Leonardo', 'Fontana', '359', 'Lisbona', 'Zurigo', '1664'), ('AK007', 'Mattia', 'Greco', '82', 'Milano', 'Berlino', '790'), ('AK006', 'Ginevra', 'Rossi', '572', 'Milano', 'Bruxelles', '657'), ('AK039', 'Emma', 'Romano', '853', 'Parigi', 'Zurigo', '412'), ('AK042', 'Emma', 'Romano', '891', 'Madrid', 'Berlino', '1952'), ('AK003', 'Matteo', 'Romano', '543', 'Milano', 'Parigi', '559'), ('AK050', 'Alessandro', 'Russo', '139', 'Bruxelles', 'Lisbona', '2126'), ('AK049', 'Andrea', 'Fontana', '991', 'Bruxelles', 'Berlino', '180'), ('AK034', 'Riccardo', 'Rossi', '163', 'Parigi', 'Madrid', '1118'), ('AK006', 'Lorenzo', 'Rossi', '223', 'Milano', 'Bruxelles', '657'), ('AK035', 'Aurora', 'Rizzo', '469', 'Parigi', 'Barcellona', '750'), ('AK042', 'Ginevra', 'Marino', '517', 'Madrid', 'Berlino', '1952')
]




##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso
#   il nome del file .csv contenente i dati sui voli
#   La funzione deve restituire una lista di tuple, come nell'esempio seguente
#        [ (Codice_volo,Nome,Cognome,Prezzo,Citta_partenza,Citta_arrivo,distanza_percorsa),
#          ...
#          (...),
#        ]
#   dove ogni tupla contiene i dati un volo.
#   NOTA BENE: il risultato di questa funzione e' utilizzato dalle funzioni successive,
#   se in via provvisoria volete far lavorare la funzione senza implementarla,
#   togliete il commento a return ..., la struttura dati così restituita e' una versione più corta ma analoga 
#   a quella che dovrebbe restituire la vostra implementazione.
#   OVVIAMENTE, se userete il return con la struttura dati gia' presente,
#   l'esercizio sara' considerato non svolto
def leggiDatiVoli(fn):
    pass
    #return volids
    li=[]
    f=open(fn, 'r')
    f.readline() # salto la prima riga di intestazione
    for line in f:
        line = line.strip('\r\n')
        recGroups = line.split('***')
        #print(recGroups) # es. ['', ';AK033;Martina;Marino;471;Vienna;Zurigo;608;', ';AK018;Andrea;Ferrari;531;Praga;Zurigo;570']
        for rec in recGroups:
            if rec!='':# il 1. elemento e' spesso una stringa vuota
                #print(rec)
                items = rec.split(';')
                codiceVolo=items[1] # dato che la stringa inizia con un ;, il 1. elemento e' una stringa vuota
                nome=items[2]
                cognome=items[3]
                prezzo=items[4]
                cittaPar=items[5]
                cittaAr=items[6]
                distanza=items[7]
                tu=(codiceVolo,nome,cognome,int(prezzo),cittaPar,cittaAr,int(distanza)) # anche se non richiesto esplicitamente, ho convertito prezzo e distanza in int. Si sarebbe potuto convertirli anche piu' tardi.
                li.append(tu)
    f.close()
    return li
    
# - La funzione seguente accetta come parametri in ingresso:
#   - ds: una struttura dati restituita dalla funzione leggiDatiVoli()
#   La funzione deve restituire una lista come la seguente
#       [codice_volo1, ... codice_voloN]
#   contenente i codici dei voli presenti nella struttura dati ricevuta in ingresso.
#   Nella lista restituita non ci dovranno essere ripetizioni, cioe' ogni
#   codice volo deve essere presente una e una sola volta, indipendentemente da quante
#   volte appare nella struttura dati ricevuta in ingresso.
def listaCodiciVolo(ds):
    pass # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    li = []
    for el in ds:
        codiceVolo = el[0]
        if codiceVolo not in li:
            li.append(codiceVolo)
    return li

    
# - La funzione seguente accetta come parametri in ingresso:
#   - ds: una struttura dati restituita dalla funzione leggiDatiVoli()
#   La funzione deve restituire una tupla cosi' formata:
#       (codice_volo, importo)
#   contenente le informazioni sul codice_volo che ha fatto incassare di piu'.
#   Nella tupla, importo e' il valore totale incassato per il codice_volo piu' redditizio.
def voloPiuRedditizio(ds):
    pass # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    # implementazione 2. Nelle correzioni di SSE, e' stata tenuta buona anche un'implementazione basata su una interpretazione diversa del testo: il volo piu' redditizio inteso come biglietto singolo piu' redditizio
    cod2pre={}
    for el in ds:
        codiceVolo = el[0]
        prezzo = el[3]
        if codiceVolo in cod2pre:
            cod2pre[codiceVolo] += prezzo
        else:
            cod2pre[codiceVolo] = prezzo
    # cerco chiave e valore del massimo
    codMax=''
    prezzoMax=-1
    for cod in cod2pre:
        if cod2pre[cod]>prezzoMax:
            codMax = cod
            prezzoMax = cod2pre[cod]
    return (codMax, prezzoMax)




# - La funzione seguente accetta come parametro in ingresso
#   - ds: una struttura dati restituita dalla funzione leggiDatiVoli()
#   Immaginate di individuare dei sottoinsiemi di clienti sulla base dei cognomi.
#   Per esempio tutte le persone che hanno 'Rossi' come cognome fanno parte dello stesso
#   sottoinsieme (che chiameremo sottoinsieme cognome da qui in avanti).
#   La funzione deve restituire una struttura dati come la seguente
#   { 'cognome1':(tot_km_percorsi1, tot_spesa_biglietti1),
#     'cognome2':(tot_km_percorsi2, tot_spesa_biglietti2),
#     ...
#     'cognomeN':(tot_km_percorsiN, tot_spesa_bigliettiN),
#   }  
#  Dove ogni chiave del dizionario e' uno dei cognomi, la tupla associata
#  alla chiave contiene il totale dei km percorsi e il totale speso in biglietti
#  per tutte le persone che hanno lo stesso cognome.
#  NOTA BENE: se nella struttura dati appaiono piu' tuple consecutive con lo stesso cognome,
#  solamente la prima tupla deve essere considerata. I dati delle tuple successive
#  alla prima (con lo stesso cognome) non devono essere considerati nei conteggi.
def analisiCognomi(ds):
    pass # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.
    cogPrec=''
    dip={}
    did={}
    diFinale={}
    for el in ds:
        # (codiceVolo,nome,cognome,int(prezzo),cittaPar,cittaAr,int(distanza))
        cognome=el[2]
        prezzo=el[3]
        dist=el[6]
        if cognome not in dip:
            dip[cognome]=prezzo
            did[cognome]=dist
        elif cognome in dip and cognome!=cogPrec:
            dip[cognome]+=prezzo
            did[cognome]+=dist
        cogPrec=cognome # aggiorno per l'iterazione successiva
    for cog in dip:
        diFinale[cog] = (did[cog], dip[cog]) # costruisco una struttura dati basata su una tupla
    return diFinale
        
    


##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################



print('Esercizio %s.' % (nomeEsercizio))

print('Ciao nome: %s, cognome: %s.' % (nome, cognome))


print('1) Eseguo la funzione leggiDatiVoli: ')
nomeFile='dati_voli.csv'
vds = leggiDatiVoli(nomeFile)
print(vds)

print('2) Eseguo la funzione listaCodiciVolo: ')
licv = listaCodiciVolo(vds)
print(licv)

print("3) Eseguo la funzione voloPiuRedditizio: ")
res = voloPiuRedditizio(vds)
print(res)

print("4) Eseguo la funzione analisiCognomi: ")
res2 = analisiCognomi(vds)
print(res2)



print('Nome e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s' % (nome, cognome))


