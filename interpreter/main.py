from lexer import tokenize


if __name__ == "__main__":
    with open("examples/ex1.txt") as f:
        code = f.read()

    tokens = tokenize(code)
    print(tokens)
    # parser = Parser(tokens)
    # program = parser.parse_program()

    # interp = Interpreter()
    # interp.eval(program)

    # print("Variables:", interp.vars)