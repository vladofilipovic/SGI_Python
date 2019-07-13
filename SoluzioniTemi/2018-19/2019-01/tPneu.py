# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe


import random
nomeEsercizio = 'Pneumatici'


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e un
# file dati, descritti qua di seguito
#
# - File 1) 'pneumatici.csv'
#   Il file memorizza i dati raccolti sulla durata (in termini di km percorsi)
#   dei pneumatici utilizzati da una flotta di autoveicoli.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi. Gli a capo (\r\n) sono stati omessi per semplicità.
#
#   *Marca
#   *Modello
#   *Misura
#   *Km_percorsi
#
#   Goodyear
#   G070
#   205
#   21485
#
#   Hankook
#   H056
#   195
#   33749
#
#   Nokian
#   N039
#   195
#   23736
#
#   Pirelli
#   P008
#   175
#   25401
#
#   ...
#
#   Ogni volta che un pneumatico viene sostituito vengono raccolte le informazioni
#   sul pneumatico e su quanti km sono stati percorsi prima della sostituzione.
#   I dati di un pneumatico sono sempre spezzati su 4 righe (un dato per riga),
#   contenenti, nell'ordine, le seguenti informazioni:
#   - Marca: il nome del fabbricante di pneumatici.
#   - Modello: un codice con cui è possibile identificare il modello di pneumatico.
#              Ogni fabbricante produce diversi modelli di pneumatico
#   - Misura: la dimensione in mm della larghezza del pneumatico.
#             Uno stesso modello di pneumatico può essere prodotto con misure diverse.
#   - Km_percorsi: la quantità di km percorsi dal pneumatico prima della sostituzione.
#
#   Nel file
#   - l'ordine delle informazioni è sempre lo stesso,
#   - le prime righe (quelle che iniziano con un *) costituiscono un esempio
#   - una riga vuota (contenente cioè solo gli a capo)
#     separa i dati di un pneumatico dal successivo.
#

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


# Per evitarvi di dover leggere fin da subito il contenuto del file,
# vi forniamo la struttura dati seguente che contiene un estratto
# delle informazioni presenti nel file.
# Nei primi esercizi che dovrete svolgere userete questa struttura dati,
# successivamente caricherete i dati dal file.
# Leggete la spiegazione dopo questa struttura dati.
sdp = [(0, 'Goodyear', 'G070', 205, 21485), (1, 'Hankook', 'H054', 185, 37523), (2, 'Hankook', 'H056', 195, 33749), (3, 'Nokian', 'N039', 195, 23736), (4, 'Pirelli', 'P008', 175, 25401), (5, 'Pirelli', 'P096', 165, 20757), (6, 'Goodyear', 'G063', 165, 32033), (7, 'Pirelli', 'P008', 185, 47303), (8, 'Goodyear', 'G077', 205, 47396), (9, 'Pirelli', 'P062', 205, 41174), (10, 'Nokian', 'N049', 175, 35676), (11, 'Goodyear', 'G063', 195, 31959), (12, 'Nokian', 'N094', 195, 39414), (13, 'Goodyear', 'G095', 185, 43674), (14, 'Michelin', 'M009', 195, 44096), (15, 'Goodyear', 'G053', 175, 21094), (16, 'Hankook', 'H038', 205, 48228), (17, 'Dunlop', 'D061', 185, 36414), (18, 'Nokian', 'N081', 185, 29179), (19, 'Bridgestone', 'B074', 195, 22214), (20, 'Bridgestone', 'B097', 185, 23221), (21, 'Bridgestone', 'B019', 165, 36107), (22, 'Bridgestone', 'B047', 175, 20954), (23, 'Dunlop', 'D092', 195, 20530), (24, 'Goodyear', 'G089', 185, 31428),
       (25, 'Goodyear', 'G053', 165, 38234), (26, 'Goodyear', 'G089', 205, 26472), (27, 'Nokian', 'N061', 185, 20332), (28, 'Dunlop', 'D077', 205, 37617), (29, 'Hankook', 'H038', 185, 34696), (30, 'Pirelli', 'P023', 175, 28668), (31, 'Goodyear', 'G095', 195, 43593), (32, 'Bridgestone', 'B043', 185, 49375), (33, 'Nokian', 'N049', 165, 24578), (34, 'Goodyear', 'G063', 185, 43088), (35, 'Continental', 'C095', 195, 36513), (36, 'Dunlop', 'D012', 205, 37112), (37, 'Goodyear', 'G070', 205, 29614), (38, 'Goodyear', 'G099', 205, 33390), (39, 'Goodyear', 'G053', 205, 43334), (40, 'Pirelli', 'P011', 195, 35991), (41, 'Dunlop', 'D083', 165, 21404), (42, 'Continental', 'C068', 195, 44741), (43, 'Dunlop', 'D020', 165, 32263), (44, 'Bridgestone', 'B019', 205, 39141), (45, 'Continental', 'C095', 185, 23916), (46, 'Nokian', 'N081', 205, 38803), (47, 'Hankook', 'H038', 165, 20428), (48, 'Goodyear', 'G099', 165, 26217), (49, 'Nokian', 'N027', 175, 40980)]
# La struttura dati qua sopra rappresenta lista di tuple come descritto nell'esempio seguente:
#         [
#            (Numero_progressivo1, Marca1,Modello1,Misura1,Km_percorsi1),
#            (Numero_progressivo2, Marca2,Modello2,Misura2,Km_percorsi2),
#            ...
#         ]
# Ogni tupla contiene i dati di un pneumatico.
# Numero_progressivo assume valore 0 nella prima tupla
# ed è incrementato di 1 ogni volta che si passa alla tupla successiva.
# Oltre a Numero_progressivo i dati presenti in una tupla
# sono rispettivamente Marca, Modello, Misura del pneumatico e i km percorsi.

##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = 'Sostituiscimi con il cognome'  # inserisci qua il tuo cognome
nome = 'Sostituiscimi con il nome'  # inserisci qua il tuo nome


# - La funzione seguente accetta come parametro in ingresso
#   - ds: una struttura dati analoga a sdp (descritta
#         qua sopra)
#   La funzione deve restituire un dizionario come nell'esempio seguente.
#        {marca_modello:media_km, ...}
#   dove per ogni combinazione di marca e modello di pneumatico
#   (per esempio se la marca è 'Pirelli' e il modello è 'P01',
#   marca_modello deve essere 'Pirelli#P01') viene associata la
#   percorrenza media in km che il modello di pneumatico ha avuto.
#   Dal calcolo della media vanno esclusi i pneumatici difettati,
#   cioè i pneumatici che hanno percorso meno di 10'000 km.
#   Nel calcolo della media non occorre differenzia sulla base delle
#   Misure del pneumatico.
#
#   Nota bene: nella funzione lavorate utilizzando il parametro formale,
#   e non direttamente sulla variabile globale sdp, in seguito la funzione
#   che implementerete sarà utilizzata per lavorare
#   sull'intero contenuto del file e non solo sull'estratto contenuto in sdp.
def mediaPercorrenza(ds):
    risultato = {}
    dizCalcolo = {}
    for i in range(len(ds)):
        marca = ds[i][1]
        modello = ds[i][2]
        marcaModello = marca + "#" + modello
        km = ds[i][4]
        if km >= 10000:
            somma = dizCalcolo.get(marcaModello, [0,0])
            somma[0] = somma[0] + km
            somma[1] = somma[0] + 1
            dizCalcolo[marcaModello] = somma
    for marcaModello in dizCalcolo.keys():
        totKm = dizCalcolo[marcaModello][0]
        numero = dizCalcolo[marcaModello][1]
        media = totKm/numero
        risultato[marcaModello] = media
    return risultato



# - La funzione seguente accetta come parametri in ingresso:
#   - ds: una struttura dati analoga a sdp (descritta sopra)
#   - produttore: una stringa contenente il nome di un produttore
#   La funzione deve individuare il momento in cui per la prima volta avviene il
#   "completamento dell'osservazione" dei modelli di un produttore.
#   Il "completamento ... " è il sottoinsieme delle prime tuple in ds in cui
#   ogni modello di pneumatico del produttore selezionato è apparso almeno una volta.
#   In questo esercizio non considerate le misure del pneumatico come fattore di differenziazione.
#   La funzione deve restituire il numero_progressivo associato alla tupla in cui
#   si raggiunge per la prima volta il "completamento dell'osservazione" per il
#   produttore passato come parametro.
#   Si ribadisce che l'ordine tra le tuple è dato dal numero_progressivo.
#   Dato che l'insieme dei modelli di un produttore non è noto a priori,
#   si consigli come prima fase di individuare l'insieme dei modelli prodotti dal produttore,
#   successivamente si può procedere a determinare qual è il numero progressivo
#   della tupla in cui avviene il completamento del produttore.
def calcolaCompletamento(ds, produttore):
    dizModelli = {}
    for i in range(len(ds)):
        marca = ds[i][1]
        modello = ds[i][2]
        if marca == produttore:
            dizModelli[modello] = 0
    print(dizModelli)
    for i in range(len(ds)):
        nProgressivo = ds[i][0]
        marca = ds[i][1]
        modello = ds[i][2]
        if marca == produttore:
            dizModelli[modello] = 1
            lista = dizModelli.values()
            if 0 not in lista:
                return nProgressivo
    return nProgressivo


# - La funzione seguente accetta come parametri in
#   ingresso due  parametri:
#   modello che è la stringa associata al modello di pneumatico
#   marca che rappresenta il produttore del pneumatico
#   La funzione deve restituire il valore True se il primo carattere delle due
#   stringhe coincide altrimenti False.
def controlloModelloMarca(modello, marca):
    if modello[0] == marca[0]:
        return True
    else:
        return False

# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file contenente i dati sui pneumatici.
#   La funzione deve restituire una struttura dati analoga a
#   sdp (vedi descrizione precedente) contenente TUTTI i dati del file.
#   Si faccia riferimento alla descrizione della variabile globale sdp
#    per maggiori dettagli.
#   Sui dati di ogni pneumatico utilizzate la funzione precedente per effettuare
#   un controllo: solo i pneumatici che superano il controllo devono essere
#   inseriti nella struttura dati restituita.


def leggiPneumatici(filename):
    risultato = []
    f = open(filename, "r")
    for i in range(5):
        linea = f.readline()
    while 1:
        linea = f.readlines()
        if linea == []:
            break
        j = 0
        nProgressivo = -1
        while j < len(linea):
            marca = linea[0].strip()
            modello = linea[1].strip()
            misura = int(linea[2].strip())
            km = int(linea[3].strip())
            lineaVuota = linea[4].strip()
            nProgressivo = nProgressivo + 1
            j = j + 5
            if controlloModelloMarca(modello, marca):
                risultato = risultato + [(nProgressivo, marca, modello, misura, km)]
    return risultato




##########################################################
# Fine del compito e della parte da editare obbligatoriamente
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################

print('Esercizio %s.' % (nomeEsercizio))

print('Ciao nome: %s, cognome: %s.' % (nome, cognome))


print('1) Eseguo la funzione mediaPercorrenza: ')
mp = mediaPercorrenza(sdp)
print(mp)

print('2) Eseguo la funzione calcolaCompletamento: ')
cmp = calcolaCompletamento(sdp, 'Dunlop')
print(cmp)

print("3) Eseguo la funzione leggiPneumatici: ")
fname = 'pneumatici.csv'
dataset = leggiPneumatici(fname)
print(dataset)

# se vuoi puoi provare ad eseguire le funzioni 1) e 2) sul dataset letto dal file


print('Nome e autore dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
print('Autore: %s, %s .' % (nome, cognome))


### cancellami

sep = ';'
newLine = '\r\n'


def generaDati():
    fn = 'pneumatici_semplice.csv'
    fn2 = 'pneumatici.csv'
    marchePneumatici = 'Bridgestone,Continental,Dunlop,Goodyear,Hankook,Michelin,Nokian,Pirelli'.split(
        ',')
    dimensioniPneumatici = [165, 175, 185, 195, 205]
    modelli = {k: [k[0] + ("%3d" % i).replace(' ', '0')
                   for i in random.sample(range(100), 10)] for k in marchePneumatici}
    #print(modelli)

    f = open(fn, 'w')
    intestazione = 'Marca,Modello,Misura,Km_percorsi'.split(',')
    f.write(sep.join(intestazione) + newLine)

    f2 = open(fn2, 'w')
    for si in intestazione:
        f2.write('*' + si + newLine)
    f2.write(newLine)

    marcamod = []
    for marca in modelli:
        for modello in modelli[marca]:
            marcamod.append((marca, modello))
    for i in range(1000):
        (marca, modello) = marcamod[random.randint(0, len(marcamod) - 1)]
        dimensione = str(dimensioniPneumatici[random.randint(
            0, len(dimensioniPneumatici) - 1)])
        kmpercorsi = str(random.randint(20000, 50000))
        li = [marca, modello, dimensione, kmpercorsi]
        f.write(sep.join(li) + newLine)

        for el in li:
            f2.write(el + newLine)
        f2.write(newLine)

    f.close()
    f2.close()
    print('Files %s %s written' % (fn, fn2))

#generaDati()
