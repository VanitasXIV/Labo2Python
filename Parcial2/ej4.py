
def multiplicar_resultado(factor):
    def decorador(func):
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * factor
        return wrapper
    return decorador

@multiplicar_resultado(3)
def suma(a, b):
    return a + b

@multiplicar_resultado(2)
def resta(a, b):
    return a - b


print(suma(2, 3))
print(resta(5, 2))
