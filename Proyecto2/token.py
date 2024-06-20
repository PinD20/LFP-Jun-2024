class Token():
    def __init__ (self, nombre, lexema, linea, columna):
        self.nombre = nombre
        self.lexema = lexema
        self.linea = linea
        self.columna = columna

    def __str__(self):
        return f'{self.nombre} {self.lexema} ({self.linea}, {self.columna})'