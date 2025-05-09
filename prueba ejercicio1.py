def calcular_descuento_arancel(promedio, quintil):
    
    if promedio > 6.0:
        if quintil == 1 or quintil == 2:
            return 0.20  
        elif quintil == 3 or quintil == 4:
            return 0.15 
    elif 5.0 < promedio <= 6.0:
        if quintil == 1 or quintil == 2:
            return 0.13 
        elif quintil == 3 or quintil == 4:
            return 0.10  
    return 0  # Sin descuento

def calcular_descuento_matricula(quintil, promedio):
    # Descuento en matrícula basado en el quintil
    descuento = 0
    if quintil == 1 or quintil == 2 or quintil == 3:
        descuento = 0.10  # 10% descuento en matrícula
        if promedio >= 5.5:
            descuento += 0.05  # 5% adicional si promedio >= 5.5
    return descuento

def calcular_valores():
    # Valores base
    valor_arancel = 1800000
    valor_matricula = 90000
    
    # Obtener los datos de entrada del usuario
    promedio = float(input("Ingrese su promedio: "))
    quintil = int(input("Ingrese el quintil (1, 2, 3, 4 o 5): "))
    
    # Calcular descuentos
    descuento_arancel = calcular_descuento_arancel(promedio, quintil)
    descuento_matricula = calcular_descuento_matricula(quintil, promedio)
    
    # Aplicar descuentos
    arancel_final = valor_arancel * (1 - descuento_arancel)
    matricula_final = valor_matricula * (1 - descuento_matricula)
    
    # Mostrar resultados
    print(f"El valor del arancel es: {int(arancel_final)}")
    print(f"El valor de la matrícula es: {int(matricula_final)}")

# Ejecutar el programa
calcular_valores()