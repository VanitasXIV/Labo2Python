
temperaturas = []
for i in range(30):
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
    temperaturas.append(temp)


promedio_mensual = sum(temperaturas) / len(temperaturas)


dias_frios = 0
dias_calidos = 0
i = 0
while i < len(temperaturas):
    if temperaturas[i] < 20:
        dias_frios += 1
    elif temperaturas[i] > 30:
        dias_calidos += 1
    i += 1


promedios_semanales = []
for semana in range(0, len(temperaturas), 7):
    promedio_semana = sum(temperaturas[semana:semana+7]) / len(temperaturas[semana:semana+7])
    
    promedios_semanales.append(promedio_semana)

# Print
print(f"\nPromedio mensual: {promedio_mensual:.2f}°C")
print(f"Días fríos (menos de 20°C): {dias_frios}")
print(f"Días cálidos (más de 30°C): {dias_calidos}")
print(f"Promedios semanales: {promedios_semanales}")
