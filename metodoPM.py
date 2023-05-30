#Formula:X_n+1 = (a * X_n) % m
#Instalar esto pip install pyautogui
#https://stackoverflow.com/questions/35689869/park-miller-algorithm-python-3

from datetime import datetime
import pyautogui

def get_mouse_seed():
    # Obtener la posición actual del ratón
    x, y = pyautogui.position()

    # Convertir las coordenadas x e y en un número entero utilizando la función hash()
    seed = hash((x, y))

    # Devolver la semilla generada a partir de las coordenadas del ratón
    return seed

def park_miller(semilla, n):
    # Constantes del algoritmo Park-Miller
    a = 16807
    m = 2**31 - 1

    # Lista vacía para almacenar la secuencia de números aleatorios
    sequence = []

    # Se inicializa el número aleatorio x con la semilla proporcionada
    x = semilla

    # Generar n números aleatorios utilizando el algoritmo Park-Miller
    for i in range(n):
        # Actualizar el valor de x utilizando la fórmula del algoritmo Park-Miller
        x = (a * x) % m
        # Agregar el número aleatorio generado a la lista sequence
        sequence.append(x)
    # Devolver la lista con la secuencia de números aleatorios generados
    return sequence


#semilla= int(input("Ingrese una semilla: "))
#semilla = int(datetime.now().timestamp()) #Toma los segundos que pasaron desde 1970 hasta hoy
#semilla = int(datetime.now().strftime("%Y%m%d")) #Toma la fecha actual
semilla = get_mouse_seed()
numero2 = int(input("Ingrese la cantidad de numero aleatorios que quiere generar: "))
print (semilla)
random_numbers = park_miller(semilla, numero2)
print(random_numbers)
