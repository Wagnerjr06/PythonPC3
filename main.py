from libro import Libro
from gestion import GestionBiblioteca


def mostrar_menu():
    print("\n---Menú Biblioteca---")
    print("1.Agregar un libro")
    print("2.Listar todos los libros")
    print("3. Buscar un libro por título")
    print("4. Buscar un libro por autor")
    print("5. Salir")

def main():
    gestion = GestionBiblioteca()

    while True:
        mostrar_menu()
        opcion=input("Selecciona una opcion: ")

        if opcion == "1":
            titulo = input("Introduce el titulo del libro: ")
            autor = input("Introduce el autor del libro: ")
            isbn = input("Introduce el ISBN del libro: ")
            libro= Libro(titulo,autor,isbn)
            gestion.agregar_libro(libro)

        elif opcion == "2":
            gestion.listar_libros()

        elif opcion == "3":
            titulo = input("Introduce el título a buscar: ")
            gestion.buscar_por_titulo(titulo)

        elif opcion == "4":
            autor = input("Introduce el autor a buscar: ")
            gestion.buscar_por_autor(autor)

        elif opcion == "5":
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()

