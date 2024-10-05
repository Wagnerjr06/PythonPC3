import Operaciones

a = 10
b = 2
c = "tres"

print("Suma de", a, "y", b, Operaciones.suma(a,b))
print("Resta de", a, "y", b, Operaciones.resta(a,b))
print("Producto de", a, "y", b, Operaciones.producto(a,b))
print("División de", a, "y", b, Operaciones.division(a,b))

print("Suma de", a, "y", c, Operaciones.suma(a,c))
print("División de", a, "y 0:", Operaciones.division(a,0))
