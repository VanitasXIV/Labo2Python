def es_numero_perfecto(numero):
    divisores = [i for i in range(1, numero) if numero % i == 0]
    return sum(divisores) == numero

def numeros_perfectos(rango):
    return [num for num in range(1, rango+1) if es_numero_perfecto(num)]


rango = int(input("Ingrese un rango. Por ej. 1000: "))
print("Números perfectos hasta", rango, ":", numeros_perfectos(rango))
