def suma_enteros_positivos():
    suma = 0
    while True:
        numero = int(input("Ingresa un número entero positivo (o un número negativo para salir): "))
        if numero < 0:
            break
        suma += numero
    print("La suma de los números positivos ingresados es:", suma)

suma_enteros_positivos()
