class Estudiante:
    #Constructor
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años")
