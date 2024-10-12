def filtrar_palabras_cortas(palabras, longitud_minima):
    return [palabra for palabra in palabras if len(palabra) > longitud_minima]


#Variable palabras y longitud minima se pueden cambiar a input, lo importante es la función definida arriba
palabras = ["sol", "programación", "código", "red"]
longitud_minima = 3
print("Palabras más largas que", longitud_minima, "caracteres:", filtrar_palabras_cortas(palabras, longitud_minima))
