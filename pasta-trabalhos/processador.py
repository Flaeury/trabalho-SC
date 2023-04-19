print("Entradas A e B ligadas")
perguntaA = input("Escolha um valor para A (0,1): ")
perguntaB = input("Escolha um valor para B (0,1): ")

print("A e B = 00")
print("A ou B = 01")
print("A xnor B = 10")
print("A + B = 11")

pergunta = input("Qual operação você deseja: ")
if not all(c in '01' for c in pergunta):
    print("A entrada contém caracteres inválidos.")
    exit()
else:
    if perguntaA == '0' and perguntaB == '0':
        match pergunta:
            case "00":
                print("0 + 0 = 0")

            case "01":
                print("0 ou 0 = 1")

            case "10":
                print("0 xnor 0 = 1")

            case "11":
                print("0 + 0 = 1")

    elif perguntaA == '0' and perguntaB == '1':
        match pergunta:
            case "00":
                print("0 + 1 = 0")

            case "01":
                print("0 ou 1 = 1")

            case "10":
                print("0 xnor 1 = 0")

            case "11":
                print("0 + 1 = 1")

    elif perguntaA == '1' and perguntaB == '0':
        match pergunta:
            case "00":
                print("1 e 0 = 0")

            case "01":
                print("1 ou 0 = 1")

            case "10":
                print("1 xnor 0 = 0")

            case "11":
                print("1 + 0 = 1")

    elif perguntaA == '1' and perguntaB == '1':
        match pergunta:
            case "00":
                print("1 e 1 = 1")

            case "01":
                print("1 e 1 = 1")

            case "10":
                print("1 e 1 = 1")

            case "11":
                print("1 e 1 = 10 - Vai um")
