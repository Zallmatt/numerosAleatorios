from datetime import datetime

#Función que recibe por parámtro la semilla, las dos constantes 
#y la cantidad de números aleatorios que deseamos.
def mixtoCongruencial(pSemilla, pA, pC, pN):
    sequence = []  # Se crea una lista vacía para almacenar los números generados.
    for i in range(pN):  
        pSemilla = (pA * pSemilla + pC) % 1  
        sequence.append(pSemilla)
    return sequence  # Se retorna la lista de números pseudoaleatorios generada.


a = float(input("Valor de a (que sea decimal): "))  # Se solicita al usuario ingresar el valor de a.
c = float(input("Valor de c (que sea decimal): "))  # Se solicita al usuario ingresar el valor de c.
n = int(input("Cantidad de numeros pseudoaleatorios: "))

#Se asigna a la semilla el valor transcurrido en segundos desde el 1 de enero de 1970 hasta la actualidad
#por lo tanto, siempre cambia.
#semilla = datetime.now().timestamp()
semilla = float(input("Ingrese la semilla (que sea decimal): "))

# Se llama a la función mixtoCongruencial enviando los valores ingresados 
# por el usuario y la semilla generada a partir de la marca de tiempo.
generator = mixtoCongruencial(semilla, a, c, n)

print("Valor de la semilla generada: ", semilla)
print("Tabla de números pseudoaleatorios generados:")
print("------------------------------")
print("|       Índice      |  Valor  |")
print("------------------------------")
for i in range(len(generator)):
    print(f"|        {i+1}         |  {format(generator[i], '.3f')}  |")
print("------------------------------")
