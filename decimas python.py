import random

def obtener_rango():
    while True:
        try:
            # Solicitar los dos números al usuario
            num1 = int(input("Ingresa el primer número del rango (menor): "))
            num2 = int(input("Ingresa el segundo número del rango (mayor): "))
            if num1 < num2:
                return num1, num2
            else:
                print("El primer número debe ser menor que el segundo.")
        except ValueError:
            print("Por favor ingresa números enteros válidos.")

def generar_numero_aleatorio(num1, num2):
    # Generar un número aleatorio en el rango definido
    numero = random.randint(num1, num2)
    return numero

def ajustar_numero(numero):
    # Dividir el número entre 4 y redondear al múltiplo de 4 más cercano
    return round(numero / 4) * 4

def obtener_intentos(numero_ajustado):
    intentos = 0
    while intentos < 3:
        intento = int(input(f"Intento {intentos + 1}/3: Ingresa un número para adivinar el resultado (ajustado a múltiplos de 4): "))
        intentos += 1
        
        if intento == numero_ajustado:
            print("¡Felicidades, has acertado!")
            return True
        elif intento < numero_ajustado:
            print("El número es mayor. Intenta nuevamente.")
        else:
            print("El número es menor. Intenta nuevamente.")
    
    print(f"Lo siento, no has acertado. El número correcto era {numero_ajustado}. ¡Game over!")
    return False

def main():
    print("Bienvenido al juego de adivinar el número ajustado entre 4.")
    
    # Obtener el rango
    num1, num2 = obtener_rango()
    
    # Generar un número aleatorio dentro del rango
    numero_aleatorio = generar_numero_aleatorio(num1, num2)
    
    # Ajustar el número generado dividiéndolo entre 4
    numero_ajustado = ajustar_numero(numero_aleatorio)
    
    # Adivinar el número ajustado
    obtener_intentos(numero_ajustado)

if __name__ == "__main__":
    main()