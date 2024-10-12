def eliminar_elemento(A, n):
    A.discard(n)
    return A

A = {1, 2, 3, 4}
print(A)
n = int(input("Ingrese el numero a eliminar: "))
print("Conjunto después de eliminar:", eliminar_elemento(A, n))
