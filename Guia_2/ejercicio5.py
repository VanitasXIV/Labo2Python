def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]


cadena = "nEuQuEn"
print("¿Es palíndromo?", es_palindromo(cadena))
