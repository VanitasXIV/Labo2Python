def invertir_palabras(oracion):
    return ' '.join([palabra[::-1] for palabra in oracion.split()])

oracion = input("Ingrese un textito: ")
print("Oración invertida:", invertir_palabras(oracion))
