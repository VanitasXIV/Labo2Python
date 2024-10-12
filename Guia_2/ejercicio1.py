def transponer_matriz(matriz):
    return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz transpuesta:", transponer_matriz(matriz))