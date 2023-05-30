#Formula:X_n+1 = (a * X_n) % m
#Instalar esto pip install pyautogui

from datetime import datetime
import pyautogui

def get_mouse_seed():
    # Obtener la posición actual del ratón
    x, y = pyautogui.position()

    # Convertir las coordenadas x e y en un número entero utilizando la función hash()
    seed = hash((x, y))

    # Devolver la semilla generada a partir de las coordenadas del ratón
    return seed

def mul_congruencia(semilla, n):
    # Lista vacía para almacenar la secuencia de números aleatorios
    num_aleatorios = []

    # Constantes del algoritmo multiplicativo de congruencia
    a = 16807
    m = 2**31 - 1

    # Se inicializa el número aleatorio x con la semilla proporcionada
    x = semilla

    # Generar n números aleatorios utilizando el algoritmo multiplicativo de congruencia
    for i in range(n):
        # Actualizar el valor de x utilizando la fórmula del algoritmo multiplicativo de congruencia
        x = (a * x) % m
        # Agregar el número aleatorio generado a la lista num_aleatorios
        num_aleatorios.append(x)
    # Devolver la lista con la secuencia de números aleatorios generados
    return num_aleatorios


semilla= int(input("Ingrese una semilla: "))
#semilla = int(datetime.now().timestamp()) #Toma los segundos que pasaron desde 1970 hasta hoy
#semilla = int(datetime.now().strftime("%Y%m%d")) #Toma la fecha actual
#semilla = get_mouse_seed()
numero2 = int(input("Ingrese la cantidad de numero aleatorios que quiere generar: "))
lista_num_aleatorios = mul_congruencia(semilla, numero2)
print("Tabla de números pseudoaleatorios generados:")
print("------------------------------")
print("|       Índice      |  Valor  |")
print("------------------------------")
for i in range(len(lista_num_aleatorios)):
    print(f"|        {i+1}         |  {lista_num_aleatorios[i]}  |")
print("------------------------------")
