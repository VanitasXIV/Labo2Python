import math

def distancia(punto1, punto2):
    return math.sqrt((punto2[0] - punto1[0]) ** 2 + (punto2[1] - punto1[1]) ** 2)

punto1 = (0, 0)
punto2 = (3, 4)
print("Distancia entre puntos:", distancia(punto1, punto2))
