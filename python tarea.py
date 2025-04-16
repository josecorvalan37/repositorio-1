def mostrar_menu():
    print("Menú de opciones:")
    print("1. Saludo")
    print("2. Despedida")
    print("3. Mostrar edad")
    print("4. Salir")

def saludo():
    print("¡Hola! ¿Cómo estás?")

def despedida():
    print("¡Hasta luego! Que tengas un buen día.")

def mostrar_edad():
    edad = int(input("Por favor, ingresa tu edad: "))
    print(f"Tienes {edad} años.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            saludo()
        elif opcion == "2":
            despedida()
        elif opcion == "3":
            mostrar_edad()
        elif opcion == "4":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, ingresa una opción entre 1 y 4.")

if __name__ == "__main__":
    main()