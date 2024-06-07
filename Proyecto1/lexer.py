class Lexer():
    def __init__(self, entrada) -> None:
        self.entrada = entrada

    def isCaracterValido(self, caracter):
        return caracter in [';', '[', ']', ':', ',', '{', '}', '>']

    def analizar(self):
        linea = 1
        columna = 1
        lexema = ""

        estado = 0

        for caracter in self.entrada:
            if estado == 0:
                if caracter.isalpha():
                    lexema += caracter
                    estado = 1
                elif caracter == "-":
                    lexema += caracter
                    estado = 2
                elif caracter == "'":
                    lexema += caracter
                    estado = 3
                elif self.isCaracterValido(caracter):
                    lexema += caracter
                    estado = 4
                else:
                    print(f'ERROR LÉXICO: {caracter} ({linea}, {columna})')
