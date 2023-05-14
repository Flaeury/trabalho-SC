endereco0 = endereco1 = endereco2 = endereco3 = endereco4 = endereco5 = endereco6 = endereco7 = endereco8 = endereco9 = endereco10 = endereco11 = endereco12 = endereco13 = endereco14 = endereco15 = '00000000'

while True:
    user = input(
        "Digite W para Escrever, L para listar os endereços e R para Ler e C para Limpar tudo: ")
    if user == 'W' or user == 'w':
        W_end = input("Qual endereço? (4 dígitos): ")
        if not all(c in '01' for c in W_end):
            print("A entrada contém caracteres inválidos.")
            exit()
        dado = (input(f"Digite um dado (8 bits): "))
        if not all(c in '01' for c in dado):
            print("A entrada contém caracteres inválidos.")
            exit()
        match W_end:
            case '0000':
                endereco0 = dado
            case '0001':
                endereco1 = dado
            case '0010':
                endereco2 = dado
            case '0011':
                endereco3 = dado
            case '0100':
                endereco4 = dado
            case '0101':
                endereco5 = dado
            case '0110':
                endereco6 = dado
            case '0111':
                endereco7 = dado
            case '1000':
                endereco8 = dado
            case '1001':
                endereco9 = dado
            case '1010':
                endereco10 = dado
            case '1011':
                endereco11 = dado
            case '1100':
                endereco12 = dado
            case '1101':
                endereco13 = dado
            case '1110':
                endereco14 = dado
            case '1111':
                endereco15 = dado
    elif user == 'L' or user == 'l':
        print(f"Endereço 0000: {endereco0}")
        print(f"Endereço 0001: {endereco1}")
        print(f"Endereço 0010: {endereco2}")
        print(f"Endereço 0011: {endereco3}")
        print(f"Endereço 0100: {endereco4}")
        print(f"Endereço 0101: {endereco5}")
        print(f"Endereço 0110: {endereco6}")
        print(f"Endereço 0111: {endereco7}")
        print(f"Endereço 1000: {endereco8}")
        print(f"Endereço 1001: {endereco9}")
        print(f"Endereço 1010: {endereco10}")
        print(f"Endereço 1011: {endereco11}")
        print(f"Endereço 1100: {endereco12}")
        print(f"Endereço 1101: {endereco13}")
        print(f"Endereço 1110: {endereco14}")
        print(f"Endereço 1111: {endereco15}")
    elif user == 'R' or user == 'r':
        R_end = input("Qual endereço? (4 dígitos): ")
        match R_end:
            case '0000':
                print(f"Endereco 0: {endereco0}")
            case '0001':
                print(f"Endereco 1: {endereco1}")
            case '0010':
                print(f"Endereco 2: {endereco2}")
            case '0011':
                print(f"Endereco 3: {endereco3}")
            case '0100':
                print(f"Endereco 4: {endereco4}")
            case '0101':
                print(f"Endereco 5: {endereco5}")
            case '0110':
                print(f"Endereco 6: {endereco6}")
            case '0111':
                print(f"Endereco 7: {endereco7}")
            case '1000':
                print(f"Endereco 8: {endereco8}")
            case '1001':
                print(f"Endereco 9: {endereco9}")
            case '1010':
                print(f"Endereco 10: {endereco10}")
            case '1011':
                print(f"Endereco 11: {endereco11}")
            case '1100':
                print(f"Endereco 12: {endereco12}")
            case '1101':
                print(f"Endereco 13: {endereco13}")
            case '1110':
                print(f"Endereco 14: {endereco14}")
            case '1111':
                print(f"Endereco 15: {endereco15}")
    elif user == 'C' or user == 'c':
        endereco0 = endereco1 = endereco2 = endereco3 = endereco4 = endereco5 = endereco6 = endereco7 = endereco8 = endereco9 = endereco10 = endereco11 = endereco12 = endereco13 = endereco14 = endereco15 = '00000000'
