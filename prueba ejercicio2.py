from random import randint

limite_menor = int(input("ingresa el limite menor"))
limite_mayor = int(input("ingresa el limite mayor"))

while limite_menor >= limite_mayor:
    print("el limite menor debe ser menor al limite mayor.")
    limite_menor = int(input("ingrese el limite menor"))
    limite_mayor = int(input("ingresa el limite mayor"))

numero_secreto = randint(limite_menor, limite_mayor)

for intento in range(1, 4):
    intento_usuario = int(input(f"intento (intento): adivina el numero: "))

    if intento_usuario == numero_secreto:
        print("felicitaciones, pudiste adivinar el numero")
        break
    else:
        if intento < 3:
            if intento_usuario < numero_secreto:
               print("pista el numero es mayor. ")
            else:
                print("pista el numero es menor. ")
        else:
            print(f"perdiste. el numero era {numero_secreto}.")

            