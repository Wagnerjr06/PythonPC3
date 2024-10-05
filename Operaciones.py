def suma (a,b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido. Asegúrate de ingresar números."

def resta (a,b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido. Asegúrate de ingresar números."

def producto (a,b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido. Asegúrate de ingresar números."

def division (a,b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero"
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido. Asegúrate de ingresar números."

