def descuento_matricula():
    nombre = input("ingresa tu nombre")
    print(f"bienvenido: {nombre}")

    calificacion = float(input("ingresa tu calificacion:"))
    if calificacion >=6:
        print("felicitaciones, tienes un descuento del 20% para la matricula")
    elif calificacion >= 5:
        print("tienes una calificacion buena, te damos un descuento del 15%")
    elif calificacion >= 4:
        print("puedes mejorar,tienes un descuento del 10%")
    else:
        print("reprobado")

        descuento_matricula()