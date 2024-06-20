from token import Token

class Parser():
    def __init__(self, tokens) -> None:
        self.tokens = tokens

        # Token fin de entrada
        self.tokens.append(Token('$', 'EOF', -1, -1))
        # End of File = EOF

    def parse(self):
        self.inicio()
    
    #<inicio> ::= <instrucciones>
    def inicio(self):
        self.instrucciones()

    #<instrucciones> ::= <instruccion> <instrucciones>
    #                  | ε
    def instrucciones(self):
        self.instruccion()
        self.instrucciones()

    #<instruccion> ::= <declaracion>
    #                | <ordenamiento>
    #                | <guardar>
    def instruccion(self):
        self.declaracion()
        self.ordenamiento()
        self.guardar()

    #<declaracion> ::= tk_palabraArray tk_id tk_igual tk_palabraNew tk_palabraArray tk_corcheteA <listaElementos> tk_corcheteC tk_PyC
    def declaracion(self):
        if self.tokens[0].nombre == "tk_palabraArray":
            self.tokens.pop(0)
            if self.tokens[0].nombre == "tk_id":
                id = self.tokens.pop(0)
                if self.tokens[0].nombre == "tk_igual":
                    self.tokens.pop(0)
                    if self.tokens[0].nombre == "tk_palabraNew":
                        self.tokens.pop(0)
                        if self.tokens[0].nombre == "tk_palabraArray":
                            self.tokens.pop(0)
                            if self.tokens[0].nombre == "tk_corcheteA":
                                self.tokens.pop(0)
                                elementos = self.listaElementos()
                                if self.tokens[0].nombre == "tk_corcheteC":
                                    self.tokens.pop(0)
                                    if self.tokens[0].nombre == "tk_PyC":
                                        self.tokens.pop(0)
                                        #Aquí se debe manejar la instruccion
                                        #Ya tenemos el id del nuevo arreglo y el valor (el arreglo como tal)
                                    else:
                                        print(f"Error sintactico: Se esperaba un ; en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
                                else:
                                    print(f"Error sintactico: Se esperaba un ] en la linea {self.tokens[0].linea}")
                            else:
                                print(f"Error sintactico: Se esperaba un [ en la linea {self.tokens[0].linea}")
                        else:
                            print(f"Error sintactico: Se esperaba la palabra Array en la linea {self.tokens[0].linea}")
                    else:
                        print(f"Error sintactico: Se esperaba la palabra New en la linea {self.tokens[0].linea}")
                else:
                    print(f"Error sintactico: Se esperaba un = en la linea {self.tokens[0].linea}")

    #<listaElementos> ::= <elemento> <listaElementos>
    #                   | epsilon
    def listaElementos(self):
        item = self.elemento()
        lista = [item]
        lista.extend(self.listaElementos())
        return lista

    # <elemento> ::= tk_entero
    #              | tk_decimal
    def elemento(self):
        if self.tokens[0].nombre == "tk_entero":
            return self.tokens.pop(0)
        elif self.tokens[0].nombre == "tk_decimal":
            return self.tokens.pop(0)
        else:
            print(f"Error sintactico: Se esperaba un valor en la linea {self.tokens[0].linea}")
            return None
        
