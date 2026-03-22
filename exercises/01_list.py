# 01. cos'e' una sequenza?

response = "una sequenza e' ..."

# 02. cos'e' una lista/array?

response = "una lista e' ..."

# 03. qual'e' la differenza fra un'array di caratteri e una stringa?
# hint: mutable vs immutable

response = "la differenza ..."

# 04. quanto spazio in memoria RAM occupa una stringa?
# [ ] A. 1Byte
# [ ] B. 1Byte per ogni carattere
# [ ] C. 1KiloByte per ogni carattere

# 05. misura quanto spazio occupano in memoria RAM le stringhe `s1`, `s2`, ... usando la funzione sys.getsizeof

import sys
s1 = ""
s2 = "a"
s3 = "1"
s4 = "ab"
s5 = "12"
s6 = "abcdefghij"
s7 = "1234567890"

# 06. inizializza una lista x vuota, y contentente la stringa "abc", z contentente i caratteri "abc"

x = ...
y = ...
z = ...

# 07. misura quanto spazio occupano x, y, z 

ram_space = ...

# 08. misura quanto spazio occupa ["a","b","c","de"] senza usare variabili di appoggio

ram_space = ...

# 09. e' possibile ispezionare l'identificativo dell'indirizzo di memoria di 
# ogni variabile tramite la funzione id, controlla l'id delle seguenti variabili/valori

"abc"
x = "abc"
x
x = "abc"
x = "abcd"
x
y = []
y
y = []
y.append("a")
y
y.append("b")
y

# 09.bis come mai secondo te succede questa cosa?

print(sys.getsizeof(  []                ))  # 56
print(sys.getsizeof(  [[], []]          ))  # 72
print(sys.getsizeof(  [[[]], []]        ))  # 72
print(sys.getsizeof(  [[[[]]], []]      ))  # 72
print(sys.getsizeof(  [[[[], []]], []]  ))  # 72

# 10. operazioni sulle liste
# - inizializza una lista di stringhe vuota x
# - misura lo spazio in memoria occupato dal valore in x
# - leggi l'identificativo dello spazio in memoria occupato dal valore di x
# - sovrascrivi x con una nuova lista contentente una solo valore "a"
# - controlla l'id di x (dovrebbe essere cambiato)
# - aggiungi ad x un nuovo valore "b" (senza reinizializzare la lista)
# - modifica l'ultimo valore in x aggiungendo i caratteri "cd"
# - leggi il primo e l'ultimo valore in x
# - rimuovi l'ultimo valore in x (tramite indice)
# - aggiungi ad x l'array ["e", "f", ["g", "h"]]
# - conta il numero di elementi in x
# - ordina gli elementi in x in ordine alfabetico ascendente
# - ordina gli elementi in x in ordine alfabetico discendente
# - rovescia x
# - pulisci x (clear)

...


# 11. inizializza una lista x contenente questi valori eterogenei "a", "1", 1, True, 3.14

...

# 12. inizializza una matrice bidimensionale contenente questi valori
#
#   1 0 0
#   0 1 0
#   0 0 1
#
# stampa i valori in posizione (0,0), (1,1), (-1, -1)

...

# 13. salva in una matrice i valori di questa tabella
#
# titolo_libro, costo, disponibile_in_magazzino, anno_pubblicazione
# -----------------------------------------------------------------
# aaa,          1.50,   si,                      2015
# bbb,          23.0,   no,                      2016
# ccc,          4.12,   si,                      1997

...

# 14. crea un programma che fa operazioni di CRUD sul database dell'esercizio 13
# CRUD = Create, Read, Update, Delete
# mi aspetto di avere i 4 metodi 
# e un workflow che iterativamente mi chiede che azione fare, parametri e alla fine stampa anche il contenuto del database

...

# 15. crea un programma che gestisce il CRUD su 2 tabelle libro, casa_editrice
# 
# id, titolo_libro, costo, disponibile_in_magazzino, id_casa_editrice
# -----------------------------------------------------------------
# 1,  aaa,          1.50,   si,                      2
# 2,  bbb,          23.0,   no,                      1
# 3,  ccc,          4.12,   si,                      1
#
# id, nome
# -----------------------------------------------------------------
# 1,  einaudi
# 2,  feltrinelli

...

# 15.bis 
# il programma parte con database vuoto
# crea una nuova casa editrice einaudi
# crea una nuova casa editrice hoepli
# elimina hoepli
# crea un nuova casa editrice feltrinelli
# stampa le case editrici
# stampa le case editrici che contengono nel nome "elli"
# crea un nuovo libro aaa ... assegnato a feltrinelli
# crea un nuovo libro e prova ad assegnarlo all'editore 4 che non esiste (mi aspetto un errore)
# crea bbb, ccc, ddd
# elimina ddd
# stampa tutti i libri che costano meno di 10 euro (con li nome della casa editrice)
# stampa tutti i libri presenti in magazzino
# stampa tutti i libri della casa editrice einaudi
# elimina tutto dal database