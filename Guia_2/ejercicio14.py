def sumar_numeros_en_cadena(cadena):
    return sum(int(char) for char in cadena if char.isdigit())

cadena=input("Ingrese un texto del tipo a1b2c3: ")
#cadena = "a1b2c3"
print("Suma de números en la cadena:", sumar_numeros_en_cadena(cadena))
