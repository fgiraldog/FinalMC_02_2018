print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 1 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

# Ejercicio1
# Tiene dos arreglos A y B. Su codigo debe:
# 1) Imprima el mensaje "A es menor que B" si todos los elementos del arreglo A son menores que los elementos del arreglo B.
# 2) Imprima "A NO es menor que b" si al menos uno de los elementos de A es mayor que alguno de los elementos de B.

import numpy as np
N=10
A=(np.random.random((N,1))*10.0)-5.0
B=(np.random.random((N,1))*10.0)-3.0
print (A)
print (B)

C = B - A

contador = 0

for element in C:
     if element > 0:
            contandor = contador + 1
     else:
        print ('A NO es menor que B')
        break
        
if contador == 9:
    print ('A es mayor que B')










