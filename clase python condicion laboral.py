quintil = int(input("ingresa tu quintil: "))
condicion_la = input("ingresa tu condicion laboral: ").strip().lower()
edad = int(input("dime tu edad:"))

subsidio = 0
bono = 0

if quintil in [1, 2]:
    if condicion_la == "desempleado":
        subsidio = 15.000
    elif condicion_la == "empleado":
        subsidio = 10.000
elif quintil == 3:
    if condicion_la == "desempleado":
        subsidio= 8.000
    elif condicion_la == "empleado":
        subsidio = 6.000

if quintil in [1,2]:
    bono += 2000

if edad >= 60:
    bono += 3000

total = subsidio + bono

