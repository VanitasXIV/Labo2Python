def sumar_matrices(matriz1, matriz2):
    return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]


matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
print("Suma de matrices:", sumar_matrices(matriz1, matriz2))
