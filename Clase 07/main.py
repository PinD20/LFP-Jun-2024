import graphviz

from graphviz import Source

# ============== FORMA 1 ==============

#Crear grafo
dot = graphviz.Digraph(comment='The Round Table')


#Agregar nodos
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')


#Agregar varias conexiones
dot.edges(['AB', 'AL'])

#Agregar una conexión
dot.edge('B', 'L')


#Imprimir el código DOT
print(dot.source)


#Crear imagen en PDF
#dot.render('salida.gv', view=True).replace('\\', '/')



# ============== FORMA 2 ==============
codigo_dot = """
digraph Hola {
    node[style="filled", fillcolor="blue"]
    
    label="Hola soy un grafo"
    
    
    nodo[label="Inicio", fontcolor="red"]
    nodo2[label="Fin", fillcolor="#57D959"]
    nodo3[label="Intermedio"]
    
    nodo2 -> nodo
    nodo2 -> nodo3
}
"""

#Forma A
source = Source(codigo_dot, filename="imagen", format="svg")
#source.view() #Renderiza y abre la imagen

#Forma B
source2 = Source(codigo_dot, filename="imagen")
source2.render(format="pdf")#Renderiza la imagen