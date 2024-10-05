import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Eje Y"
        elif self.x != 0 and self.y == 0:
            return "Eje X"
        else:
            return "Origen"
        
    def vector(self,otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self,otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)
    
p1= Punto(3,4)
p2= Punto(-1,2)

print(f"Punto 1: {p1}")
print(f"Punto 2: {p2}")

print(f"Cuadrante de p1: {p1.cuadrante()}")
print(f"Cuadrante de p2: {p2.cuadrante()}")

print(f"Vector entre p1 y p2: {p1.vector(p2)}")
print(f"Distancia entre p1 y p2: {p1.distancia(p2)}")

    
        
        