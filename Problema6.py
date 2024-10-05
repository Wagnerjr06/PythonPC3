class Producto:
    def __init__(self,nombre,precio,anio,categoria):
        """Inicia un producto con nombre, precio, anio y categoria"""
        self.nombre = nombre
        self.precio = precio
        self.anio = anio  
        self.categoria = categoria

    def __str__(self):
        """Representa el producto en forma de cadena."""
        return f"{self.nombre} - Precio: ${self.precio} - Año: {self.anio} - Categoria: {self.categoria}"

class Catalago:
    def __init__(self):
        """Inicializa el catalogo con una lista vacía de productos"""
        self.productos= []

    def agregar_producto(self, producto):
        """Agrega un producto al catalogo."""
        self.productos.append(producto)

    def mostrar_productos(self):
        """Muestra todos los productos del catálogo."""
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            print("Lista de productos en el catálogo:")
            for producto in self.productos:
                print(producto)

    def filtrar_por_anio(self,anio):
        """Muestra productos fabricados en un anio en específico."""
        print(f"Productos del anio {anio}:")
        productos_filtrados = [p for p in self.productos if p.anio == anio]
        if productos_filtrados:
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No se encontraron productos del anio {anio}.")

    def filtrar_por_categoria(self,categoria):
        """Muestra productos que pertenecen a una categoría específica"""
        print(f"Productos en la categoría '{categoria}': ")
        productos_filtrados= [p for p in self.productos if p.categoria.lower() == categoria.lower()]
        if productos_filtrados:
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No se encontraron productos en la categoría '{categoria}'.")

producto1= Producto("Filtro de aire", 35, 2022, "Motor")
producto2= Producto("Aceite del motor", 20, 2023, "Líquidos")
producto3= Producto("Bujía", 15,2022, "Encendido")

catalogo=Catalago()

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

catalogo.mostrar_productos()

catalogo.filtrar_por_anio(2022)

catalogo.filtrar_por_categoria("Motor")









