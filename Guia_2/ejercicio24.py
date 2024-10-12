def menu_interactivo():
    lista = []
    while True:
        print("\nMenú:")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar lista")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            elemento = input("Ingresa un elemento: ")
            lista.append(elemento)
        elif opcion == '2':
            elemento = input("Ingresa el elemento a eliminar: ")
            if elemento in lista:
                lista.remove(elemento)
            else:
                print("El elemento no está en la lista.")
        elif opcion == '3':
            print("Lista actual:", lista)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intenta nuevamente.")


menu_interactivo()
