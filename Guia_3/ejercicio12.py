def encontrar_pares(A):
    return {x for x in A if x % 2 == 0}

A = {1, 2, 3, 4, 5, 6}
print("Números pares en el conjunto:", encontrar_pares(A))
