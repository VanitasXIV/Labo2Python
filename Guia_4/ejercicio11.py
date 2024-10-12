def estadisticas_notas(diccionario_notas):
    resultado = {}
    for estudiante, notas in diccionario_notas.items():
        promedio = sum(notas) / len(notas)
        max_nota = max(notas)
        resultado[estudiante] = (promedio, max_nota)
    return resultado

notas_estudiantes = {'Ana': [10, 9, 8], 'Luis': [7, 6, 8]}
print("Estadísticas de notas:", estadisticas_notas(notas_estudiantes))
