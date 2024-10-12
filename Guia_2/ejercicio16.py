def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]


n = int(input("Ingrese un numero para la secuencia Fibonacci: "))
print("Secuencia de Fibonacci:", fibonacci(n))
