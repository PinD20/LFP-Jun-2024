from token import Token
from error import Error

class Lexer():
    def __init__(self, entrada) -> None:
        self.entrada = entrada
        self.tokens = []
        self.errores = []

    def isCaracterValido(self, caracter):
        return caracter in [';', '[', ']', ':', ',', '{', '}', '>']

    def estado0(self, caracter, linea, columna):
        if caracter.isalpha():
            return 1
        elif caracter == "-":
            return 2
        elif caracter == "'":
            return 3
        elif self.isCaracterValido(caracter):
            return 4
        else:
            if ord(caracter) == 32 or ord(caracter) == 10 or ord(caracter) == 9:
                pass
            else:
                self.errores.append(Error("N/A", "N/A", linea, columna, caracter))
            return 0

    def analizar(self):
        linea = 1
        columna = 1
        lexema = ""

        estado = 0
        estado_anterior = 0

        for caracter in self.entrada:
            if estado == 0:
                estado = self.estado0(caracter, linea, columna)
                if estado == 0:
                    #Reiniciar lexema
                    lexema = ""
                else:
                    lexema += caracter

            elif estado == 1:
                if caracter.isalpha():
                    lexema += caracter
                else:
                    if lexema in ["nombre", "nodos", "conexiones"]:
                        #Es un estado de aceptación, se guarda el token
                        self.tokens.append(Token("Palabra reservada", lexema, linea, columna - len(lexema)))
                    else:
                        self.errores.append(Error("Palabra Reservada", lexema, linea, columna, "N/A"))

                    lexema = ""

                    #Operar como si estuviéramos en el estado 0
                    estado = self.estado0(caracter, linea, columna)
                    if estado != 0:
                        lexema += caracter
                    
            elif estado == 2:
                if caracter == ">":
                    lexema += caracter
                    estado = 20
                    estado_anterior = 2
                else:
                    self.errores.append(Error("Asignación", lexema, linea, columna, caracter))
                    estado = 0
                    lexema = ""

            elif estado == 3:
                if caracter == "'":
                    lexema += caracter
                    estado = 20
                    estado_anterior = 3
                elif caracter == "\n":
                    self.errores.append(Error("String", lexema, linea, columna, caracter))
                    estado = 0
                    lexema = ""
                else:
                    estado = 3
                    lexema += caracter

            elif estado == 4:
                #Es un estado de aceptación, se guarda el token
                self.tokens.append(Token("Signo", lexema, linea, columna - len(lexema)))

                lexema = ""

                #Operar como si estuviéramos en el estado 0
                estado = self.estado0(caracter, linea, columna)
                if estado != 0:
                    lexema += caracter
                
            elif estado == 20:
                #Estado de aceptación
                #Guardar el token
                if estado_anterior == 2:
                    self.tokens.append(Token("Asignación", lexema, linea, columna - len(lexema)))
                elif estado_anterior == 3:
                    self.tokens.append(Token("String", lexema, linea, columna - len(lexema)))
                estado_anterior = 0

                #Reiniciar lexema
                lexema = ""

                #Operar como si estuviéramos en el estado 0
                estado = self.estado0(caracter, linea, columna)
                if estado != 0:
                    lexema += caracter

            #Control de fila y columna
            if ord(caracter) == 10:
                linea += 1
                columna = 1
            elif ord(caracter) == 9:
                columna += 4
            else:
                columna += 1