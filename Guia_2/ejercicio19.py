def suma_indices_pares(lista):
    return sum(lista[i] for i in range(0, len(lista), 2))

lista = [10, 20, 30, 40, 50]
print("Suma de elementos en índices pares:", suma_indices_pares(lista))
