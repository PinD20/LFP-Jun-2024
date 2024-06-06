'''
from tkinter import filedialog, Tk

#Abrir un archivo con el explorador
Tk().withdraw()

path = filedialog.askopenfilename(
    title= "Seleccione un archivo",
    initialdir= "C:/",
    filetypes= [
        ("Archivo de excel", "*.txt")
    ]
)

if path != "":
    archivo = open(path, "r", encoding="utf-8")

    print(archivo.read())
'''


from tkinter import filedialog, Tk, Label, Button, Text


def escribir():
    print("Hola, estoy escribiendo")

def imprimir(txt):
    print(txt)

def abrirArchivo():
    path = filedialog.askopenfilename(
        title= "Seleccione un archivo",
        initialdir= "C:/",
        filetypes= [
            ("Archivo de entrada", "*.code")
        ]
    )

    if path != "" and path is not None:
        archivo = open(path, "r", encoding="utf-8")
        print(archivo.read())
    else:
        print("No se seleccionó ningún archivo")


#Crear ventana
main = Tk()

label = Label(main, text="Hola, soy una etiqueta")

#Colocar objeto centrado horizontalmente
#label.pack()

#Colocar objeto en posicion específica
label.place(x=200, y=100)

#Crear un botón, y asignarle una función sin parámetros
button = Button(main, text="Escribir", command=escribir)

#Crear un botón y asignarle una función pasándole un parámetro	
button2 = Button(main, text="Imprimir", command= lambda: imprimir("Imprimiendo..."))
button.place(x=200, y=250)
button2.place(x=200, y=300)

botonAbrir = Button(main, text="Abrir archivo", command=abrirArchivo)
botonAbrir.place(x=200, y=350)

consola = Text(main, width=50, height=10)
consola.place(x=100, y=400)


ancho_ventana = 1000
alto_ventana = 600
#Tamaño de la ventana
#main.geometry(f"{ancho_ventana}x{alto_ventana}")

#Cambiar título de la ventana
main.title("Grafos Guatemala")

#Evitar redimensión de la ventana
main.resizable(False, False)


#Centrar ventana
window_x = main.winfo_screenwidth() // 2 - ancho_ventana // 2
window_y = main.winfo_screenheight() // 2 - alto_ventana // 2

main.geometry(f"{ancho_ventana}x{alto_ventana}+{window_x}+{window_y}")


#Mantener ventana abierta
main.mainloop()