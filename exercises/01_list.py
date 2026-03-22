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


