def generateMatrix(n, m):

    matrix = {}
    counter = 1
    for i in range(n):
        for j in range(m):
            matrix[(i, j)] = counter
            counter += 1
    return matrix

print("Generar una matriz n x m")
n=int(input("Ingrese valor n: "))
m=int(input("Ingrese valor m: "))
print(generateMatrix(n, m))
