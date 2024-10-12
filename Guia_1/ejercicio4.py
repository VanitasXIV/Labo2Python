letra = input("Ingrese una letra: ").lower()
if len(letra) != 1:
    print("Debe ingresar un solo carácter.")
elif letra in 'aeiou':
    print("Es vocal.")
else:
    print("No es vocal.")