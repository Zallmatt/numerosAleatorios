# Instalar esto pip install pyautogui
# X = X^2 (Se toman la poscion de 3-6) Teniendo que poseer 8 posiciones obligatoriamente
# Semilla de 4 digitos

import pyautogui


def get_mouse_seed():
    # Obtener la posición actual del ratón
    x, y = pyautogui.position()

    # Convertir las coordenadas x e y en un número entero utilizando la función hash()
    seed = hash((x, y))

    # Devolver la semilla generada a partir de las coordenadas del ratón
    return seed


def validar_semilla(semilla):  # Validar tamaño de semilla
    if semilla <= 9999:
        return semilla
    else:
        semilla_acortada = str(semilla)[:4]
        return int(semilla_acortada)


def validar_numAleatorio(num_aleatorio):
    x = str(num_aleatorio)
    while len(x) < 8: 
        x = "0" + x 
    return x


def von_Neumann(semilla, cantidad):
    lista = []
    x = semilla
    for i in range(cantidad):
        x = x ** 2
        valor_ale= validar_numAleatorio(x)
        x = int(valor_ale[2:6])
        lista.append(x)
    return print(lista)



#semilla = get_mouse_seed()
semilla = int(input("Ingresar semilla: "))
cantidad = int(input("Ingrese la cantidad de numeros aleatorios que necesita: "))
semilla = validar_semilla(semilla)
von_Neumann(semilla, cantidad)
