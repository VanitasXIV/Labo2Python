from collections import deque

def simulacion_colas():
    cola = deque()
    while True:
        print("\nMenú:")
        print("1. Agregar persona a la cola")
        print("2. Atender persona (eliminar de la cola)")
        print("3. Mostrar estado de la cola")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            persona = input("Ingresa el nombre de la persona: ")
            cola.append(persona)
        elif opcion == '2':
            if cola:
                atendido = cola.popleft()
                print(f"Se atendió a {atendido}")
            else:
                print("No hay personas en la cola.")
        elif opcion == '3':
            print("Estado actual de la cola:", list(cola))
        elif opcion == '4':
            print("Saliendo de la simulación de colas.")
            break
        else:
            print("Opción inválida, intenta nuevamente.")

simulacion_colas()
