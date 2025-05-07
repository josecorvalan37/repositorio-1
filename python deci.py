import random

def adivina_numero():
    # Solicitar los números del rango
    while True:
        try:
            # Ingresar el primer número (menor)
            num1 = int(input("Ingresa el primer número (menor): "))
            # Ingresar el segundo número (mayor)
            num2 = int(input("Ingresa el segundo número (mayor): "))
            
            if num1 < num2:
                break
            else:
                print("El primer número debe ser menor que el segundo. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa números enteros válidos.")
    
    # Generar un número aleatorio dentro del rango
    numero_aleatorio = random.randint(num1 + 1, num2 - 1)
    
    print(f"Intenta adivinar el número entre {num1 + 1} y {num2 - 1}. Tienes 3 intentos.")
    
    # Intentos de adivinanza
    for intento in range(1, 4):
        while True:
            try:
                # Ingresar el intento del usuario
                intento_usuario = int(input(f"Intento {intento}: Ingresa tu número: "))
                break
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        
        if intento_usuario == numero_aleatorio:
            print(f"Felicitaciones, adivinaste en el {intento} intento.")
            break
        else:
            if intento < 3:
                if intento_usuario < numero_aleatorio:
                    print("El número es mayor que tu intento.")
                else:
                    print("El número es menor que tu intento.")
            else:
                print(f"Perdiste, el número era {numero_aleatorio}.")
                break

# Llamada a la función para iniciar el juego
adivina_numero()