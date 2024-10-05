from Areas import Circulo, Rectangulo, Cuadrado
from Validaciones import validar_numero_positivo

def menu():
    while True:
        print("\n---Menú---")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectangulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio= input("Ingresa el radio del círculo: ")
            valido, resultado = validar_numero_positivo(radio)
            if valido:
                circulo=Circulo(resultado)
                print(f"El área del círculo es: {circulo.calcular_area()}")
            else:
                print(resultado)
        
        elif opcion == "2":
            largo=input("Ingrese el lado del rectángulo: ")
            valido_largo, resultado_largo= validar_numero_positivo(largo)

            if valido_largo:
                ancho= input("Ingrese el ancho del rectángulo: ")
                valido_ancho, resultado_ancho = validar_numero_positivo(ancho)

                if valido_ancho:
                    rectangulo = Rectangulo(resultado_largo,resultado_ancho)
                    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
                
                else:
                    print(resultado_ancho)
            else:
                print(resultado_largo)
        

        elif opcion == "3":
            lado= input("Ingresa el lado del cuadrado: ")
            valido, resultado = validar_numero_positivo(lado)

            if valido:
                cuadrado=Cuadrado(resultado)
                print(f"El área del cuadrado es: {cuadrado.calcular_area()}")

            else:
                print(resultado)
        
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__=="__main__":
    menu()