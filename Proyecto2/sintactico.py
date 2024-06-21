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
        if self.tokens[0].nombre == "$":
            return
        self.instruccion()
        self.instrucciones()

    #<instruccion> ::= <declaracion>
    #                | <instruccionID>
    def instruccion(self):
        if self.tokens[0].nombre == "tk_palabraArray":
            self.declaracion()
        else:
            self.instruccionID()

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
                                        print("ID: ", id.lexema)
                                        print("Lista: ")
                                        for e in elementos:
                                            print(e.lexema)
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

    #<listaElementos> ::= <elemento> <masElementos>
    #                   | epsilon
    def listaElementos(self):
        item = self.elemento()
        if item == None:
            return []
        lista = [item]
        masElementos = self.mas_elementos()
        lista.extend(masElementos)
        return lista
    
    #<masElementos> ::= tk_coma <tk_elemento> <masElementos>
    #                 | epsilon
    def mas_elementos(self):
        if self.tokens[0].nombre == "tk_coma":
            self.tokens.pop(0)
            item = self.elemento()
            if item == None:
                return []
            lista = [item]
            lista.extend(self.mas_elementos())
            return lista
        else:
            return []

    # <elemento> ::= tk_entero
    #              | tk_decimal
    def elemento(self):
        if self.tokens[0].nombre == "tk_entero":
            return self.tokens.pop(0)
        elif self.tokens[0].nombre == "tk_decimal":
            return self.tokens.pop(0)
        else:
            return None
        
    #<instruccionID> ::= tk_id tk_punto <accionArreglo>
    def instruccionID(self):
        if self.tokens[0].nombre == "tk_id":
            self.tokens.pop(0)
            if self.tokens[0].nombre == "tk_punto":
                self.tokens.pop(0)
                self.accionArreglo()
            else:
                print(f"Error sintactico: Se esperaba un . en la linea {self.tokens[0].linea}")
        else:
            print(f"Error sintactico: Se esperaba un id en la linea {self.tokens[0].linea}")
    
    #<accionArreglo> ::= ordenamiento>
    #                  | <guardar>
    def accionArreglo(self):
        if self.tokens[0].nombre == "tk_palabraSort":
            self.ordenamiento()
        else:
            self.guardar()

    #<ordenamiento> ::= tk_palabraSort tk_parentesisAbre tk_palabraAsc tk_igual tk_booleano tk_parentesisCierra tk_PyC
    def ordenamiento(self):
        if self.tokens[0].nombre == "tk_palabraSort":
            self.tokens.pop(0)
            if self.tokens[0].nombre == "tk_parentesisAbre":
                self.tokens.pop(0)
                if self.tokens[0].nombre == "tk_palabraAsc":
                    self.tokens.pop(0)
                    if self.tokens[0].nombre == "tk_igual":
                        self.tokens.pop(0)
                        if self.tokens[0].nombre == "tk_booleano":
                            asc = self.tokens.pop(0)
                            if self.tokens[0].nombre == "tk_parentesisCierra":
                                self.tokens.pop(0)
                                if self.tokens[0].nombre == "tk_PyC":
                                    self.tokens.pop(0)
                                    #Aquí se debe manejar la instruccion
                                    #Ya tenemos el id del arreglo y el valor booleano
                                else:
                                    print(f"Error sintactico: Se esperaba un ; en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
                            else:
                                print(f"Error sintactico: Se esperaba un ) en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")

                        else:
                            print(f"Error sintactico: Se esperaba TRUE/FALSE en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
                    else:
                        print(f"Error sintactico: Se esperaba un = en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
                else:
                    print(f"Error sintactico: Se esperaba ASC en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
            else:
                print(f"Error sintactico: Se esperaba un ( en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
        else:
            print(f"Error sintactico: Se esperaba SORT en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")

    #<guardar> ::= tk_palabraSave tk_parentesisAbre tk_string tk_parentesisCierra tk_PyC
    def guardar(self):
        if self.tokens[0].nombre == "tk_palabraSave":
            self.tokens.pop(0)
            if self.tokens[0].nombre == "tk_parentesisAbre":
                self.tokens.pop(0)
                if self.tokens[0].nombre == "tk_string":
                    path = self.tokens.pop(0)
                    if self.tokens[0].nombre == "tk_parentesisCierra":
                        self.tokens.pop(0)
                        if self.tokens[0].nombre == "tk_PyC":
                            self.tokens.pop(0)
                            #Aquí se debe manejar la instruccion
                        else:
                            print(f"Error sintactico: Se esperaba ; en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
                    else:
                        print(f"Error sintactico: Se esperaba ) en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
                else:
                    print(f"Error sintactico: Se esperaba un string en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
            else:
                print(f"Error sintactico: Se esperaba ( en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
        else:
            print(f"Error sintactico: Se esperaba SAVE en la linea {self.tokens[0].linea}, pero se obtuvo {self.tokens[0].lexema}")
                        
