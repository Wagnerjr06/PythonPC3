class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre= nombre
        self.numero_registro= numero_registro
        self.edad= None
        self.nota= None

    def display(self):
        """Muestra la información del estudiante."""
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        else:
            print("Edad: No asignada")
        if self.nota is not None:
            print(f"Nota: {self.nota}")
        else:
            print("Nota: No asignada")
    
    def setAge(self,edad):
        """Asigna la edad al estudiante."""
        self.edad=edad
    def setNota(self,nota):
        """Asigna las notas al estudiante."""
        self.nota=nota
    
alumno1 = Alumno("Juan Perez", "A00123")
alumno1.display()

alumno1.setAge(20)
alumno1.setNota(85)
alumno1.display()
