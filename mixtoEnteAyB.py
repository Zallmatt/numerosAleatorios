from datetime import datetime
a=1
b=0

#Función que recibe por parámtro la semilla, las dos constantes 
#y la cantidad de números aleatorios que deseamos.
def mixtoCongruencial(pSemilla, pA, pB, pC, pM, pN):
    sequence = []  # Se crea una lista vacía para almacenar los números generados.
    for i in range(pN):  
        pSemilla = (pA * pSemilla + pC) % pM  
        num_aleatorio = pA + (pB - pA) * (pSemilla / m) # Se escala el resultado al intervalo [a, b]
        sequence.append(num_aleatorio)
    return sequence  # Se retorna la lista de números pseudoaleatorios generada.

while a>b:
    a = float(input("Intervalo a: ")) #Se solicita al usuario el minimo valor
    b = float(input("Intervalo b (mayor que a): ")) #Se solicita al usuario el maximo valor
c = float(input("Valor de c: "))  # Se solicita al usuario ingresar el valor de c.
m = float(input("Valor de m: "))  # Se solicita al usuario ingresar el valor de m.


n = int(input("Cantidad de numeros pseudoaleatorios: "))

#Se asigna a la semilla el valor transcurrido en segundos desde el 1 de enero de 1970 hasta la actualidad
#por lo tanto, siempre cambia.
#semilla = datetime.now().timestamp()
semilla = float(input("Agregar semilla: "))

# Se llama a la función mixtoCongruencial enviando los valores ingresados 
# por el usuario y la semilla generada a partir de la marca de tiempo.
generator = mixtoCongruencial(semilla, a, b, c, m, n)

print("Valor de la semilla generada: ", semilla)
print("Tabla de números pseudoaleatorios generados:")
print("------------------------------")
print("|       Índice      |  Valor  |")
print("------------------------------")
for i in range(len(generator)):
    print(f"|        {i+1}         |  {format(generator[i], '.3f')}  |")
print("------------------------------")
