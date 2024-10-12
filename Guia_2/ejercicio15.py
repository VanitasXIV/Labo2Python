def multiplicar_elementos(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto


lista = [2, 3, 4]
print("Producto de los elementos de la lista:", multiplicar_elementos(lista))
