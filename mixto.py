# coding=utf-8
from datetime import datetime

# ejemplo valores a utilizar tratar de no usar 0
# Valor de a: 1548 usar valor de 4 cifras
# Valor de c: 4578 usar valor de 4 cifras que no se repita con a
# Valor de m: 7845 usar un valor de 4 cifras alto
#Función que recibe por parámtro la semilla, las dos constantes y la cantidad de números aleatorios que deseamos.
def lehmer(pSemilla, pA, pM, pC, pN):
    sequence = []  # Se crea una lista vacía para almacenar los números generados.
    for i in range(pN):  
        pSemilla = (pA * pSemilla + pC) % pM  
        sequence.append(pSemilla) 
    return sequence  # Se retorna la lista de números pseudoaleatorios generada.


a = int(input("Valor de a: "))  # Se solicita al usuario ingresar el valor de a.
c = int(input("Valor de c: "))  # Se solicita al usuario ingresar el valor de c.
m = int(input("Valor de m: "))  # Se solicita al usuario ingresar el valor de m.
n = int(input("Cantidad de numeros aleatorios: "))

#Se asigna a la semilla el valor transcurrido en segundos desde el 1 de enero de 1970 hasta la actualidad, por lo tanto, siempre cambia.
semilla = int(73619)
#datetime.now().timestamp()
# Se llama a la función lehmer enviando los valores ingresados por el usuario y la semilla generada a partir de la marca de tiempo.
generator = lehmer(semilla, a, m, c, n)

print(generator)  # Se imprime en pantalla la lista de números pseudoaleatorios generados.
 