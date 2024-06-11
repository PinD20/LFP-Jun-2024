from lexer import Lexer


if __name__ == "__main__":
    archivo = open("entrada.txt", "r", encoding="utf-8")
    texto = archivo.read()

    lexer = Lexer(texto)

    lexer.analizar()

    print("=================== TOKENS ===================")
    for token in lexer.tokens:
        print(token)

    print("================== ERRORES ===================")
    for error in lexer.errores:
        print(error)