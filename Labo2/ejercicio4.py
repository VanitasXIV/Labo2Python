letra = input("Ingrese una letra: ").lower() #uso lower para realizar la comparacion más fácil
    
if len(letra) != 1:
    print("Debe ingresar un solo carácter.")
elif letra in 'aeiou':
    print("Es vocal.")
else:
    print("No es vocal.")
