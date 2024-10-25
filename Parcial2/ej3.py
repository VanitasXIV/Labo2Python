def comparar_sets(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    comunes = conjunto1 & conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2
    return (comunes, diferencia_simetrica)


lista1 = [1, 2, 3, 4]
print(lista1)
lista2 = [3, 4, 5, 6]
print(lista2)
print(comparar_sets(lista1, lista2)) 
