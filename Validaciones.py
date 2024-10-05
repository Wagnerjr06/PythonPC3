def validar_numero_positivo(valor):
    try:
        numero = float(valor)
        if numero <=0:
            return False, "Error: El número debe ser mayor a cero."
        return True, numero
    except ValueError:
        return False, "Error: Debes ingresar un valor numérico válido."