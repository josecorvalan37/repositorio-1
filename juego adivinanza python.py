import random

def redondear_al_mas_cercano_multiplo_de_4(numero):
    return round(numero / 4) * 4

def juego_adivinanza():
    print("Bienvenido al juego de adivinanza.")

    # Solicitar el rango al usuario
    while True:
        try:
            rango_inicio = int(input("Ingrese el primer número del rango (entero): "))
            rango_fin = int(input("Ingrese el segundo número del rango (entero): "))
            if rango_inicio < rango_fin:
                break
            else:
                print("Error: El primer número debe ser menor que el segundo.")
        except ValueError:
            print("Por favor, ingrese solo números enteros.")

    # Generar número aleatorio y ajustarlo
    numero_original = random.randint(rango_inicio, rango_fin)
    numero_objetivo = redondear_al_mas_cercano_multiplo_de_4(numero_original)

    # Intentos del usuario
    intentos = 3
    for intento in range(1, intentos + 1):
        try:
            adivinanza = int(input(f"Intento {intento}: Adivina el número ajustado: "))
            if adivinanza == numero_objetivo:
                print("¡Felicidades! Adivinaste el número.")
                return
            else:
                if adivinanza < numero_objetivo:
                    print("Pista: El número es mayor.")
                else:
                    print("Pista: El número es menor.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    print(f"Perdiste. El número era: {numero_objetivo}")

# Ejecutar el juego
juego_adivinanza()
