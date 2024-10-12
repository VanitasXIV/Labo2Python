def agregar_elemento(A, n):
    A.add(n)
    return A

A = {1, 2, 3}
n = int(input("¿Qué número desea agregar?: "))
print("Conjunto después de agregar:", agregar_elemento(A, n))
