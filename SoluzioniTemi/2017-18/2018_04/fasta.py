# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = 'fasta'

##########################################################
# INTRODUZIONE
##########################################################

# Il programma che implementerete lavorerà sulle informazioni che caratterizzano
# il passaggio dal DNA all'RNA, e dall'RNA alle PROTEINE in una cellula vivente.
# Una sequenza di DNA è una sequenza di NUCLEOTIDI (chiamati anche BASI).
# che viene rappresentata come una stringa, es.
#        "CGTAACAAGGTTTCCGTAGGTGAACCTGCG"
# dove ogni lettera rappresenta un NUCLEOTIDE.
# Il passaggio da DNA ad RNA e poi a PROTEINE, avviene con le seguenti fasi:
# * TRASCRIZIONE. La sequenza che forma il DNA (basata sui nucleotidi {A,C,G,T})
#   viene trasformata in una sequenza RNA (basata sui  nucleotidi {A,C,G,U}).
#   Sia nel DNA sia nell'RNA possono essere presenti altri nucleotidi
#   diversi da quelli appena indicati.
#   Attenzione: durante la conversione da DNA a RNA,
#   ciascuna base 'T' nel DNA viene convertita in una base 'U' nell'RNA,
#   tutte le altre basi rimangono invariate. Per esempio
#      "CGTAACAAGGTTTCCGTAGGTGAACCTGCG"
#   viene convertito in
#      "CGUAACAAGGUUUCCGUAGGUGAACCUGCG".
# * TRADUZIONE. l'RNA viene 'letto' in TRIPLETTE (tre caratteri consecutivi)
#   chiamate anche CODONI.
#   A ciascuna tripletta viene associata il corrispondente AMINOACIDO
#   secondo un preciso dizionario. L'insieme degli AMINOACIDI
#   così composto (chiamato anche CATENA di aminoacidi) forma una PROTEINA.
# Il DNA di una cellula è una sequenza lunghissima. Non viene mai
# processato interamente con il metodo appena descritto,
# ma vengono processate delle sottostringhe
# chiamate SEQUENZE (conosciute anche come SEQUENZE GENOMICHE).


##########################################################
# DESCRIZIONE DEI FILE CON I DATI
##########################################################
#
# Nel file .zip troverete i seguenti file, oltre a questo script:
#
# - File 1) ls_orchid.fasta
#   Il file contiene DIVERSE sequenze genomiche di DNA codificate
#   nel formato FASTA.
#   In questo formato, ciascuna sequenza è composta da:
#   * una riga di intestazione (chiamata DEFLINE)
#     che inizia con il carattere '>' in cui vengono
#     memorizzate le informazioni che accompagnano la sequenza
#   * La sequenza di nucleotidi, rappresentata da
#     una stringa che si estende su una o più righe.
#   * Il termine di una sequenza è individuato da una riga vuota.
#     Vi invitiamo ad apre il file .fasta con un editor di testo
#     per verificare quanto sopra.
#   Per ogni sequenza la DEFLINE ha il seguente formato:
#   gi|numero-gi|emb|accession|locus commenti
#   dove:
#   * gi è una stringa che assieme a > identifica l'inizio della DEFLINE
#   * numuro-gi è il valore numerico associato alla sequenza nella base di dati
#   * emb è l'identificativo della base di dati da cui è stata recuperata l'informazione
#   * accession è un identificativo alternativo per la sequenza
#   * locus è la posizione sul genoma
#   * commenti sono le informazioni aggiuntive a corredo della sequenza
#   Un'intestazione di esempio è la seguente:
#   >gi|2765658|emb|Z78533.1|CIZ78533 C.irapeanum 5.8S rRNA gene and ITS1 and ITS2 DNA
#
#   Le righe che seguono la defline contengono la sequenza di nucleotidi, possono
#   avere lunghezza variabile e contenere caratteri diversi da {'A','C','G','T'}
#
# - File 2) codonTable.txt
#   Questo file contiene le informazioni sul mapping da nucleotidi
#   ad aminoacidi (i componenti delle proteine).
#   Ogni riga contiene due colonne separate dal simbolo di tabulazione '\t':
#   * tripletta di nucleotidi
#   * il corrispondente aminoacido associato
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

# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con contenente le sequenze in formato .FASTA.
#   La funzione deve restituire un dizionario di dizionari con
#   la seguente struttura (di seguito la spiegazione):
#   {
#     numeroGI_1:{'gi': numeroGI_1, 'emb': accessionGI_1, 'locus': locusECommenti_1,
#                 'seq': sequenzaNucleotidica_1},
#     ...,
#     numeroGI_N:{'gi': numeroGI_N, 'emb': accessionGI_N, 'locus': locusECommenti_N,
#                 'seq': sequenzaNucleotidica_N}
#   }
#   dove per ogni sequenza presente nel file, va inserita  nel dizionario esterno
#   una coppia chiave valore in cui:
#   * la chiave è numero_gi della sequenza (estratto dalla DEFLINE)
#   * il valore è a sua volta un dizionario di quattro elementi così strutturato:
#     {'gi': numeroGI, 'emb': accessionGI, 'locus': locusECommenti, 'seq': sequenzaNucleotidica}
#     dove numeroGI, accessionGI, locusECommenti sono contenuti nella defline di
#     ciascuna sequenza, mentre sequenzaNucleotidica è la stringa ottenuta dalla
#     concatenazione delle stringhe contenute nelle successive righe della sequenza.
#     Notate che l'informazione numeroGI è presente sia come chiave
#     sia come valore associato a 'gi' nel dizionario più interno.
#   Segue un esempio di coppia chiave valore che rappresenta una sequenza:
#   '2765658':{'gi':'2765658', 'emb':'Z78533.1', 'locus': 'CIZ78533 C.irapeanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'seq': 'CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGGAATAAACGATCGAGTGAATCCGGAGGACCGGTGTACTCAGCTCACCGGGGGCATTGCTCCCGTGGTGACCCTGATTTGTTGTTGGGCCGCCTCGGGAGCGTCCATGGCGGGTTTGAACCTCTAGCCCGGCGCAGTTTGGGCGCCAAGCCATATGAAAGCATCACCGGCGAATGGCATTGTCTTCCCCAAAACCCGGAGCGGCGGCGTGCTGTCGCGTGCCCAATGAATTTTGATGACTCTCGCAAACGGGAATCTTGGCTCTTTGCATCGGATGGAAGGACGCAGCGAAATGCGATAAGTGGTGTGAATTGCAAGATCCCGTGAACCATCGAGTCTTTTGAACGCAAGTTGCGCCCGAGGCCATCAGGCTAAGGGCACGCCTGCTTGGGCGTCGCGCTTCGTCTCTCTCCTGCCAATGCTTGCCCGGCATACAGCCAGGCCGGCGTGGTGCGGATGTGAAAGATTGGCCCCTTGTGCCTAGGTGCGGCGGGTCCAAGAGCTGGTGTTTTGATGGCCCGGAACCCGGCAAGAGGTGGACGGATGCTGGCAGCAGCTGCCGTGCGAATCCCCCATGTTGTCGTGCTTGTCGGACAGGCAGGAGAACCCTTCCGAACCCCAATGGAGGGCGGTTGACCGCCATTCGGATGTGACCCCAGGTCAGGCGGGGGCACCCGCTGAGTTTACGC'}
#
def caricaSeqs(filename):
    risultato = {}
    f = open(filename, "r")
    while 1:
        linea = f.readline ()
        if linea == "":
            break
        if linea[0] == ">":
            linea = linea.strip()
            elementi = linea.split("|")
            numeroGi = elementi [1]
            accessionGI = elementi[3]
            locusECommenti = elementi[4]
            risultato[numeroGi] = {"gi": numeroGi, "emb": accessionGI, "locus": locusECommenti, "seq": ""}
        else:
            linea = linea.strip()
            sequenza = risultato[numeroGi]["seq"]
            sequenza = sequenza + linea
            risultato[numeroGi]["seq"] = sequenza
    f.close()
    print(risultato)
    return risultato




# - La funzione seguente accetta come unico parametro in
#   ingresso una stringa con una sequenza di DNA (per esempio,
#   la stringa associata alla chiave 'seq' nella struttura dati
#    restituita dalla funzione precedente.
#   La funzione deve restituire una stringa con una sequenza di RNA,
#   identica alla stringa ricevuta come parametro in ingesso ma in cui a
#   ciascun carattere 'T' viene sostituito il carattere 'U'.
#
def trascrizione(dnaSeq):
    risultato = ""
    for i in range(len(dnaSeq)):
        if dnaSeq[i] == "T":
            risultato = risultato + "U"
        else:
           risultato = risultato + dnaSeq[i]
    return risultato



# - La funzione seguente accetta come unico parametro in
#   ingresso il nome del file con contenente la tabella di conversione
#   dai nucleotidi agli aminoacidi.
#   La funzione deve restituire un dizionario contenente una coppia chiave valore,
#   dove ogni chiave sarà una stringa
#   di tre caratteri contenente una tripletta di nucleotidi, mentre il valore
#   sarà la stringa dell'aminoacido corrispondente.
#   Se la stringa dell'aminoacido e' "STOP", nel dizionario dovra' essere inserito un *.
#   Segue a titolo esemplificativo una parte del dizionario:
#   {'GUC': 'V', 'AUA': 'I', ...,'UAA': '*', 'GAU': 'D', 'UUC': 'F'}
def caricaTabella(filename):
    risultato = {}
    f = open(filename, "r")
    while 1:
        linea = f.readline()
        if linea == "":
            break
        elementi = linea.split("\t")
        for i in range (len(elementi)):
            elementi[i] = elementi[i].strip()
        #print(elementi, len(elementi))
        tripletta = elementi [0]
        aminoAcido = elementi [1]
        if aminoAcido == 'STOP':
            risultato[tripletta] = '*'
        else:
            risultato[tripletta] = aminoAcido
    f.close()
    #print (risultato)
    return risultato




# - La funzione seguente accetta come parametri in
#   ingresso rispettivamente:
#   - la struttura dati con la sequenza di DNA restituita dalla
#     funzione caricaSeqs()
#   - la struttura dati restituita dalla funzione caricaTabella()
#     che permette di convertire le singole triplette di nucleotidi
#     in aminoacidi
#   La funzione deve convertire le sequenze di DNA presenti nel
#   primo parametro in sequenze di aminoacidi.
#   La funzione deve restituire un dizionario con la seguente
#   struttura:
#   { numeroGI_1:sequenza_aminoacidi_1,
#     numeroGI_2:sequenza_aminoacidi_2,
#     ...
#     numeroGI_N:sequenza_aminoacidi_N
#   }
#   dove a ciascuna sequenza di DNA memorizzata della strutura dati
#   in ingresso (dSeqs) corrisponde una coppia chiave:valore così
#   costituita:
#       * chiave è il numeroGI che identifica la sequenza di DNA
#         nella struttura dati in ingresso (dSeqs)
#       * valore è una sequenza di aminoacidi.
#   Il processo di conversione di una singola sequenza di DNA in una sequenza
#   di aminoacidi deve essere svolto nel modo seguente:
#   * La stringa contenente la sequenza di DNA deve essere convertita
#     in basi dell'RNA usando la funzione trascrizione().
#   * La stringa risultante dal punto precedente va suddivisa in triplette
#     (terne di lettere consecutive) es. 'CGUAACAAG' va diviso in 'CGU', 'AAC', 'AAG'.
#   * La traduzione di ciascuna tripletta in aminoacidi deve avvenire solo se:
#     - i caratteri che la compongono sono SOLO i caratteri 'AUCG'
#     - la tripletta è composta da esattamente 3 caratteri.
#     Le triplette che rispettano i criteri precedenti
#     vanno convertite 'utilizzando la "tabella di conversione"
#     passata come secondo parametro, mentre le triplette che non
#     rispettano i criteri vanno scartate.
#   Segue a titolo esemplificativo la coppia del dizionario associata alla sequenza
#   '2765658' che inizia con le basi 'CGTAACAAGGTTTCCGTAGGT...':
#   { '2765658':'RNKVSVG...', ...}

def TripletteCorrette (triplettaRNA):
    if len(triplettaRNA) != 3:
        return 0
    for i in range(len(triplettaRNA)):
        if triplettaRNA[i] not in "AUCG":
            return 0
    return 1



def seq2protein(dSeqs, dCT):
    risultato = {}
    for numeroGi in dSeqs.keys():
        sequenzaDNA = dSeqs[numeroGi]['seq']
        sequenzaRNA = trascrizione(sequenzaDNA)
        #print(sequenzaRNA)
        i = 0
        while i < len(sequenzaRNA):
            tripletta = sequenzaRNA[i:(i+3)]
            #print(tripletta)
            if TripletteCorrette (tripletta):
                aminoAcido = dCT.get (tripletta, "non esiste")
                if aminoAcido != "non esiste":
                    sequenzaAA = risultato.get(numeroGi,"")
                    sequenzaAA = sequenzaAA + aminoAcido
                    risultato[numeroGi] = sequenzaAA
            i = i + 3
    print (risultato)
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

print("1) Eseguo la funzione caricaSeqs('ls_orchid.fasta') ")
dizSequenze = caricaSeqs('ls_orchid.fasta')
if dizSequenze==None:
    print(dizSequenze)
else:
    print( 'numero sequenze caricate: ', len(dizSequenze) )
    print( dizSequenze['2765658'] )

print("2) Eseguo la funzione caricaTabella('codonTable.txt') ")
dizAN2AA = caricaTabella('codonTable.txt')
print(dizAN2AA)

print("3) Eseguo la funzione seq2protein(dizSequenze, dizAN2AA) ")
dizSeqsProteins = seq2protein(dizSequenze, dizAN2AA)
print(dizSeqsProteins)

print('Nome dello script eseguito')
print(__file__)  # Questa istruzione stampa il nome dello script, ignoratela.
