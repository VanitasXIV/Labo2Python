def calculadora_basica():
    while True:
        print("\nCalculadora básica:")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operacion = input("Ingresa la operación (+, -, *, /) o 'salir' para terminar: ")
        
        if operacion == "+":
            print(f"Resultado: {num1 + num2}")
        elif operacion == "-":
            print(f"Resultado: {num1 - num2}")
        elif operacion == "*":
            print(f"Resultado: {num1 * num2}")
        elif operacion == "/":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
        elif operacion.lower() == "salir":
            print("Saliendo de la calculadora.")
            break
        else:
            print("Operación inválida, intenta nuevamente.")

calculadora_basica()
