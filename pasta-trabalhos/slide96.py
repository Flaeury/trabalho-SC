pergunta1 = input("Digite um número inteiro em binário: ")
pergunta2 = input("Digite outro número inteiro em binário: ")

# Verifica se a entrada é válida
if not all(c in '01' for c in pergunta1):
    print("A primeira entrada contém caracteres inválidos.")
    exit()
if not all(c in '01' for c in pergunta2):
    print("A segunda entrada contém caracteres inválidos.")
    exit()
else:
    # Converte os números em binário para decimal
    decimalde1 = 0
    decimalde2 = 0
    expoente1 = len(pergunta1)-1
    expoente2 = len(pergunta2)-1

    for i in pergunta1:
        decimalde1 += int(i)*2**expoente1
        expoente1 -= 1
    print(f"O primeiro número equivale a {decimalde1} no sistema decimal.")

    for a in pergunta2:
        decimalde2 += int(a)*2**expoente2
        expoente2 -= 1
    print(f"O segundo número equivale a {decimalde2} no sistema decimal.")

    # Realiza a operação de subtração em decimal
    subtracao = decimalde1 - decimalde2

    # Verifica se é necessário realizar o complemento de dois
    if subtracao < 0:
        # Calcula o complemento de dois do número a ser subtraído
        complemento = (1 << len(pergunta1)) - decimalde2
        # Realiza a soma com o complemento de dois
        soma = decimalde1 + complemento
        # Converte o resultado para binário
        final = bin(soma)[2:]
        # Inverte os bits do resultado
        final_invertido = ''
        for c in final:
            final_invertido += "0" if c == "1" else "1"
        # Converte o resultado invertido para decimal
        deci = 1
        expoente = len(final_invertido) - 1
        for d in final_invertido:
            deci += int(d)*2**expoente
            expoente -= 1
        # Exibe o resultado da subtração com o complemento de dois
        print(
            f"A subtração desses valores é: {final} e seu número em decimal é: -{deci}")
    else:
        # Converte o resultado para binário
        final = bin(subtracao)[2:]
        # Converte o resultado para decimal
        deci = 0
        expoente = len(final) - 1
        for b in final:
            deci += int(b)*2**expoente
            expoente -= 1
        # Exibe o resultado da subtração
        print(
            f"A subtração desses valores é: {final} e seu número em decimal é: {deci}")
