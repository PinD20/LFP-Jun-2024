class Error():
    def __init__(self, token, lexema, linea, columna, caracter) -> None:
        self.token = token
        self.lexema = lexema
        self.linea = linea
        self.columna = columna

        if caracter == " ":
            self.caracter = "Espacio en blanco"
        else:
            self.caracter = caracter

    def __str__(self):
        return f'Error: {self.token} {self.lexema} ({self.linea}, {self.columna}) {self.caracter}'