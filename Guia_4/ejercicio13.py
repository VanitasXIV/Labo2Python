def sumar_diccionarios(dic1, dic2):
    return {k: dic1[k] + dic2[k] for k in dic1}

dic1 = {'a': 1, 'b': 2}
dic2 = {'a': 3, 'b': 4}
print("Diccionario sumado:", sumar_diccionarios(dic1, dic2))
