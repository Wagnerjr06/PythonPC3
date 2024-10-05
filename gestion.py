class GestionBiblioteca:
    def __init__(self):
        self.libros=[]

    def agregar_libro(self,libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado exitosamente.")

    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("Listado de libros en la biblioteca: ")
            for libro in self.libros:
                print(libro)
    
    def buscar_por_titulo(self,titulo):
        encontrados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        if encontrados:
            print("Libros encontrados por titulo: ")
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")
    
    def buscar_por_autor(self,autor):
        encontrados = [libro for libro in self.libros if autor.lower() in libro.autor.lower()]
        if encontrados:
            print("Libros encontrados por autor: ")
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros con el título '{autor}'.") 