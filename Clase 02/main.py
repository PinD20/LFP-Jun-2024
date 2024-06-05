#Diccionarios

#Estructuras que funcionan como clave-valor
diccionario = {"nombre": "Juan", "apellido": "Perez", "edad": 25, 15: "Quince"}

#Las claves pueden ser de cualquier tipo de dato


#Obtener un valor por su clave
print(diccionario["nombre"])

#Agregar o actualizar un valor
diccionario["nacionalidad"] = "Argentina"
diccionario["nombre"] = "Pedro"
diccionario["lista"] = [1, 2, 3, 4, 5]

print(diccionario)


del(diccionario["apellido"])
print(diccionario)


#Funciones
def pruebaFuncion():
    return "Hola mundo"

def funcionParametros(numero1, numero2):
    return numero1 + numero2

def funcionFormal(n1: int, n2: int) -> int:
    return n1 + n2
    

#Llamar a la funcion
print(funcionFormal(15, 68))


#OBJETOS

#Clase
class Estudiante:
    #Constructor
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años")


#Instanciar un objeto
estudiante1 = Estudiante("José", "Perez", 25)
estudiante1.presentarse()

#Obtener un atributo del objeto
print(estudiante1.nombre)

#Modificar un atributo del objeto
estudiante1.apellido = "Quiñonez"

estudiante1.presentarse()

print("=====================================")




#ARCHIVOS

archivo = open("archivo.txt", "r", encoding="utf-8")
#Permisos de apertura de archivos:
#r: Sólo lectura
#r+: Lectura y escritura
#w: Sólo escritura
#a: Escribir al final del archivo
#a+: Lectura y escritura al final del archivo


# lineas = archivo.readlines()
# for linea in lineas:
#     if linea[-1] == "\n":
#         print(linea[:-1])
#     else:
#         print(linea)


#Leer todo el texto del archivo
txt = archivo.read()

for caracter in txt:
    #Aquí va el análisis de su proyecto
    print(caracter)

archivo.close()


#Escritura de archivos
reporte = open("reporte.html", "w", encoding="utf-8")
texto = """
<!DOCTYPE html>
<html>
    <body>
        <h1>Clase 02</h1>
    </body>
</html>
"""

#Escribir en archivo
reporte.write(texto)

reporte.close()