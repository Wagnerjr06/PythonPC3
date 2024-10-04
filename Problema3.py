import math

class CIRCULO:
    def __init__(self,radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

circulo1 = CIRCULO(5)
circulo2 = CIRCULO(10)

print(f"El área del círculo 1 con radio {circulo1.radio} es: {circulo1.calcular_area():.2f}")
print(f"El área del círculo 2 con radio {circulo2.radio} es: {circulo2.calcular_area():.2f}")