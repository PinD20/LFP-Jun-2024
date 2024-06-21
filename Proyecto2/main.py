from sintactico import Parser
from token import Token

'''
Array variable = new Array [15, 564];
variable.sort(asc=FALSE);
'''

def crearTokens():
    tokens = []
    tokens.append(Token("tk_palabraArray", "Array", 1, 1))
    tokens.append(Token("tk_id", "arreglo1", 2, 1))
    tokens.append(Token("tk_igual", "Array", 3, 1))
    tokens.append(Token("tk_palabraNew", "Array", 4, 1))
    tokens.append(Token("tk_palabraArray", "Array", 5, 1))
    tokens.append(Token("tk_corcheteA", "Array", 6, 1))
    tokens.append(Token("tk_entero", "3", 7, 1))
    tokens.append(Token("tk_coma", "Array", 8, 1))
    tokens.append(Token("tk_entero", "40", 9, 1))
    tokens.append(Token("tk_corcheteC", "Array", 10, 1))
    tokens.append(Token("tk_PyC", "Array", 11, 1))

    tokens.append(Token("tk_id", "Array", 12, 1))
    tokens.append(Token("tk_punto", "Array", 13, 1))
    tokens.append(Token("tk_palabraSort", "Array", 14, 1))
    tokens.append(Token("tk_parentesisAbre", "Array", 15, 1))
    tokens.append(Token("tk_palabraAsc", "Array", 16, 1))
    tokens.append(Token("tk_igual", "Array", 17, 1))
    tokens.append(Token("tk_booleano", "TRUE", 18, 1))
    tokens.append(Token("tk_parentesisCierra", "Array", 19, 1))
    tokens.append(Token("tk_PyC", "Array", 20, 1))

   

    return tokens

if __name__ == "__main__":

    parser = Parser(crearTokens())
    parser.parse()