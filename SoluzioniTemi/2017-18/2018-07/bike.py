# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'Bici02'

##########################################################
# INTRODUZIONE
##########################################################
#
# I file descritti qua di seguito contengono informazioni sull'utilizzo
# di biciclette che possono essere noleggiate dalle persone e lasciate
# in un qualsiasi punto della citta.
##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete uno script .py da compilare e alcuni file di dati.
# I file con i dati sono:
#
#
# - File 1) spostamenti.csv
#   Questo file memorizza le informazioni sulla strada percorsa
#   dalle biciclette durante l'erogazione del servizio.
#   Un esempio del contenuto del file e' il seguente. Nell'esempio
#   non considerate il simbolo di # e gli spazi.
#
#       ID_Noleggio;ID_Bici;ID_Utente;Data;MetriPercorsi;TempoImpiegato(secondi)\r\n
#       0;39;69;26/04/2010;450;45\r\n
#       1;41;93;26/02/2010;4550;455\r\n
#       2;23;73;11/04/2010;1250;156\r\n
#       3;1;6;07/12/2010;1800;450\r\n
#       4;29;24;26/07/2010;1950;487\r\n
#
#   La prima riga contiene l'intestazione delle colonne.
#   In tute le righe le informazioni sono separati da ; (punto e virgola) e
#   i \r\n rappresentano i caratteri di a capo. Seguono alcune precisazioni
#   sulle informazioni contenute nel file.
#   Ogni riga del file contiene informazioni su un noleggio effettuato.
#   Le informazioni sono:
#   * ID_Noleggio identifica univocamente un noleggio effettuato da un cliente
#   * ID_Bici identifica la bici noleggiata
#   * ID_Utente identifica l'utente che ha usufruito della bici
#   * Data identifica la data in cui e' iniziato il noleggio
#   * MetriPercorsi indica i metri percorsi
#   * TempoImpiegato indicata il tempo del noleggio in secondi


#
# - File 2) danni.csv
#   Il file memorizza le informazioni sui danni subiti dalle biciclette.
#   Un esempio del contenuto del file e' il seguente.
#   Nella prima riga c'e' intestazione del file.
#   Nell'esempio non considerate il simbolo di # e gli spazi.
#       ID_Bici;ModelloBicicletta;TipoDanno1;TipoDanno2;...;TipoDannoN;CostoRiparazione1;CostoRiparazione2;...;CostoRiparazioneN\r\n
#       0;B;2;3;18;3;8;22\r\n
#       1;D;11;7;16;18;18;20;1;17\r\n
#       2;B;18;13;9;19;2;17\r\n
#       3;D;16;7;15;7\r\n
#       4;D;17;1;15;15\r\n
#       5;D;14;7\r\n
#
#   Ogni riga del file riporta informazioni su una singola bicicletta.
#   Per esempio la prima riga di dati fornisce le seguenti informazioni:
#   * la bicicletta ha ID_Bici 0,
#   * il ModelloBicicletta e' B,
#   * la bici ha subito 3 danni, rispettivamente TipoDanno pari a 2, 3 e 18,
#     questi danni sono costati rispettivamente 3, 8 e 22 euro.
#     I costi dei danni sono sempre numeri interi.
#     In altre parole, considerando i numeri dopo ModelloBicicletta, la prima meta'
#     sono gli identificatori che individuano la tipologia di danno, la seconda meta'
#     sono i corrispondenti costi di riparazione.
#
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
#   ingresso il nome del file con le informazioni sui tragitti percorsi dagli utenti.
#   La funzione deve restituire una struttura dati come nell'esempio seguente.
#       [ (ID_Noleggio, ID_Bici, ID_Utente, data, metri_percorsi, tempo_impiegato),
#               ...
#       ]
#
#   Per esempio, la funzione leggendo le seguenti righe del file (i \r\n sono stati omessi)
#       ID_Noleggio;ID_Bici;ID_Utente;Data;MetriPercorsi;TempoImpiegato(secondi)\r\n
#       0;39;69;26/04/2010;450;45
#       1;41;93;26/02/2010;4550;455
#       2;23;73;11/04/2010;1250;156
#
#   dovrebbe restituire la seguente struttura dati:
#        [ (0, 39, 69, '26/04/2010', 450, 45),
#          (1, 41, 93, '26/02/2010', 4550, 455),
#          (2, 23, 73, '11/04/2010', 1250, 156)
#        ]
def caricaSpostamenti(fname):
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
        idNoleggio = int(elementi[0])
        idBici = int(elementi[1])
        idUtente = int(elementi[2])
        data = elementi[3]
        metriPercorsi = int(elementi[4])
        tempo = int(elementi[5])
        risultato = risultato + [(idNoleggio, idBici, idUtente, data, metriPercorsi, tempo)]
    f.close()
    return risultato



# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file contenente i dati sui danneggiamenti delle biciclette.
#   La funzione deve restituire le informazioni sulle biciclette,
#   sotto forma di un dizionario con la struttura descritta nell'esempio seguente:
#         {
#          id_bici1:(modello_bici1, totale_costi_riparazione_bici1),
#          id_bici2:(modello_bici2, totale_costi_riparazione_bici2),
#          ...,
#          id_biciN:(modello_biciN, totale_costi_riparazione_biciN)
#         }
#
#   Dove totale_costi_riparazione_bici... e' il totale della somma spesa
#   per le riparazioni di una singola bicicletta.
#   Per maggiori informazioni sui dati si faccia riferimento
#   alla descrizione del file contenente i dati.
#
#   Vi suggeriamo di implementare anche una funzione accessoria
#   che riceva come parametro in ingresso la stringa (oppure una lista di elementi)
#   corrispondenti ad una riga del file. La funzione accessoria dovrebbe
#   calcolare il totale dei costi di riparazione presenti in una riga.
#   Esempio di funzione accessoria: # se volete potete togliere i commenti qua sotto
#
#def calcolaTotaleCosti(...):
#    pass
#
def caricaDatiBici(filename):
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
        idBici = int(elementi[0])
        modello = elementi[1]
        posInDanni = 2
        numeroDanni = int((len(elementi)-2)/2)
        posInCosti = 2 + numeroDanni
        i = 0
        while (posInCosti + i) < len(elementi):
            costo = int(elementi[posInCosti + i])
            tupla = risultato.get(idBici,("",0))
            totCosto = tupla[1] + costo
            risultato[idBici] = (modello, totCosto)
            i = i + 1
    return risultato


# - La funzione seguente calcola la tariffa per un noleggio,
#   sulla base dei metri percorsi e dei minuti di utilizzo della bicicletta.
#   NOTA BENE: questa funzione e' GIA' IMPLEMENTATA,
#   NON DOVETE MODIFICARLA, dovete SOLO USARLA negli
#   esercizi seguenti.
def tariffazione(metri, secondi): # NB: nel testo originale il parametro secondi era stato erroneamente chiamato minuti. Nella correzione sono state considerate valide entrambe le possibilita' (valore passato in minuti, valore passato in secondi)
    imp=metri/1000.0*0.20 + secondi/60.0*0.10
    if imp < 0.5:
        return 0.0
    else:
        return imp

# - La funzione seguente accetta come parametro in ingresso la struttura
#   dati restituita dalla funzione caricaSpostamenti()
#   La funzione deve restituire una struttura dati come la seguente:
#       { id_bicicletta1:totale_noleggi1,  id_bicicletta2:totale_noleggi2, ...}
#   dove per esempio totale_noleggi1 e' il totale dei soldi che la bicicletta1
#    ha fatto guadagnare con i noleggi.
def calcolaAddebiti(spost):
    risultato = {}
    for i in range (len(spost)):
        idBici = spost[i][1]
        metri = spost[i][4]
        secondi = spost[i][5]
        guadagno = tariffazione(metri, secondi)
        totGuadagno = risultato.get(idBici,0)
        totGuadagno = totGuadagno + guadagno
        risultato[idBici] = totGuadagno
    return risultato


# - La funzione seguente accetta come parametri in ingresso:
#   * spost: la struttura dati restituita dalla funzione caricaSpostamenti()
#   * danni: la struttura dati restituita dalla funzione caricaDatiBici().
#   La funzione deve restituire una struttura dati come nell'esempio seguente:
#   { ModelloBicicletta1:rapporto1, ModelloBicicletta2:rapporto2, ...
#       ModelloBiciclettaN:rapportoN}
#   dove "rapporto..." e' il rapporto tra i soldi incassati con i noleggi della bici
#   appartenenti ad una certa categoria (identificata da ModelloBicicletta)
#   e i soldi spesi per riparazioni delle biciclette della categoria.
#   Nota bene1: il rapporto deve essere calcolato per modello di bicicletta,
#               non sulle singole biciclette.
#   Nota bene2: nel dato fornito, tutte le biciclette hanno avuto una spesa per danni.
def rapportoRedditivita(spost, danni):
    risultato = {}
    dizCalcoloPerModello = {}
    for i in range(len(spost)):
        idBici = spost[i][1]
        metri = spost[i][4]
        secondi = spost[i][5]
        guadagno = tariffazione(metri, secondi)
        if idBici in danni.keys():
            modello = danni[idBici][0]
            totCosti = danni[idBici][1]
            valore = dizCalcoloPerModello.get(modello, [0, 0])
            valore[0] = valore[0] + guadagno
            valore[1] = valore[1] + totCosti
            dizCalcoloPerModello[modello] = valore
    for modello in dizCalcoloPerModello.keys():
        totGuadagno = dizCalcoloPerModello[modello][0]
        totCosto = dizCalcoloPerModello[modello][1]
        rapporto = totGuadagno/totCosto
        risultato[modello] = rapporto
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

print("1) Eseguo la funzione caricaSpostamenti: ")
fname1='spostamenti.csv'
spost = caricaSpostamenti(fname1)
print(spost)

print('2) Eseguo la funzione caricaDatiBici: ')
fname2='danni.csv'
danni = caricaDatiBici(fname2)
print(danni)

print('Eseguo la funzione tariffazione: ')
tar = tariffazione(3000,25)
print(tar)

print('3) Eseguo la funzione calcolaAddebiti: ')
ad = calcolaAddebiti(spost)
print(ad)

print('4) Eseguo la funzione rapportoRedditivita: ')
rap = rapportoRedditivita(spost, danni)
print(rap)

print('Nome dello script eseguito')
print(__file__) # Questa istruzione stampa il nome dello script, ignoratela.
