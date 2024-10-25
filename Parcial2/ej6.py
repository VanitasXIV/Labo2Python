from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"

# ¿Cómo se implementa la abstracción en este código?¿Qué ventajas ofrece?
    #Se declara una clase/objeto llamada animal la cual es abstracta y sirve como
    #template para futuras clases hijas.
    #Ser una clase abstracta nos da la ventaja de forzar a las clases hijas a definir
    #su propios métodos sobreescribiendo aquellos de su padre

# ¿Qué ventaja tiene el polimorfismo en este caso?
    #Nos ofrece una flexibilización y la posibilidad de escalar el tamaño de nuestros
    #proyectos. El método sonido() se llama de manera igual para todos los objetos que hereden
    # de animal, desligandonos de su implementación.
    
#Explica cómo se podría aplicar la herencia en este ejemplo para extender
#la funcionalidad a otros animales.
    #La herencia nos sirve para poder definir otros animales y que estos tengan de base los métodos y atributos
    #de la clase animal. Pero además, al ser abstracto, forzamos a que cada clase implemente su propio método
    #sonido(). Si no fuese abstracto podríamos tener animales con los mismos sonidos en caso de que definamos
    #el método en animal, y eso no sería conveniente.