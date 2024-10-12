def promedio_numeros():
    suma = 0
    count = 0
    while True:
        numero = int(input("Ingresa un número (o 0 para terminar): "))
        if numero == 0:
            break
        suma += numero
        count += 1
    if count > 0:
        print("Promedio de los números ingresados:", suma / count)
    else:
        print("No se ingresaron números.")

promedio_numeros()
