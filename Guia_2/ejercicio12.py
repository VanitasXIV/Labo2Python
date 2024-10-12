def rotar_lista(lista, posiciones):
    #slicing
    return lista[posiciones:] + lista[:posiciones]

lista = [1, 2, 3, 4, 5]
posiciones = int(input("¿Cuántas veces desea rotar la lista?: "));
print("Lista rotada:", rotar_lista(lista, posiciones))
