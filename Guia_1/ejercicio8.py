ahorro_mensual = float(input("Ingrese la cantidad que desea ahorrar mensualmente: "))
total_ahorro = ahorro_mensual
for _ in range(12):
    total_ahorro += total_ahorro * 0.50
print(f"El total de ahorro acumulado en un año es: {total_ahorro:.2f}")