# Comentario de una línea en Python

'''
Comentario de
varias líneas
'''

"""
Comentario de varias
líneas con comilla
doble
"""

#Imprimir en consola
print("Hola mundo!")

#Variables
cantidad = 15
print(cantidad)

#cantidad = "cantidad + 5"
#print(cantidad)

#Tipos de datos
entero = 1
decimal = 2.54564646
booleano = True
booleano2 = False

print(booleano, booleano2)


#Concatenar

#Forma 1, es necesario castear números a string
print("La cantidad es: " + str(cantidad))

#Forma 2
print("La cantidad es:", cantidad)

#Forma 3
print(f"La cantidad sin castear es: {cantidad}")


#División en Python, siempre da un float
print(10/5)
print(10.8/5.8)
print(10/6.5)
print(45.87/2)


# Listas
miLista = [True, 2, "hola", 4, 5.85, 78]

#Cambiar un valor de la lista
miLista[1] = 10

print(miLista)

#Imprimir un elemento de la lista
print(miLista[2])

#Imprimir el último elemento de la lista
print(miLista[-1])

#Imprimir un rango de elementos
print(miLista[1:4])

#Agregar elemento al final de la lista
miLista.append("nuevo elemento")

#Agregar elemento en posición específica
miLista.insert(2, "elemento en posición 2")

#Eliminar elemento según su valor
miLista.remove("elemento en posición 2")

#Eliminar elemento según índice
miLista.pop(4)

lista2 = [1, 2, 3, 4, 5]

#Agregar elementos de una lista a otra
miLista.extend(lista2)


#Tamaño de la lista
print("Tamaño de la lista:", len(miLista))



#Tuplas
#Las tuplas son inmutables (no pueden cambiar luego de ser creadas)
miTupla = (1, 2, 3, 4, 5)
#miTupla[0] = 10 <- Esto es un error
print(miTupla)
print(miTupla[2])


#Condicionales
 
#If
if 1 > 5:
    print("1 es mayor que 0")
else:
    #pass <- Si no se quiere colocar instrucciones
    print("Falso")

#if anidados
if 1 > 5:
    print("1 es mayor que 0")
elif 1 < 5:
    print("1 es menor que 5")
elif 1 == 5:
    print("1 es igual a 5")
else:
    print("no sé qué pasa")


#Ciclos
#Comienza en 0
for i in range(10):
    print("for:", i)

#Comienza en 5
print("Comienza en 5")
for i in range(5, 10):
    print("for:", i)

#For con paso 2
print("for con Paso 2")
for i in range(0, 10, 2):
    print("for:", i)

listaX = [5, 8, "hola", 80.58]
for i in listaX:
    print("elemento de lista:", i)

string = "Lenguajes formales"
for i in string:
    print("Caracter:", i)

#While
contador = 0
while contador < 10:
    print("Contador:", contador)
    contador += 1
    if contador == 5:
        break