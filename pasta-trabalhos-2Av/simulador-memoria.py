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
         if W_end == '0000':
            endereco0 = dado
         elif W_end == '0001':
            endereco1 = dado
         elif W_end == '0010':
            endereco2 = dado
         elif W_end == '0011':
            endereco3 = dado
         elif W_end == '0100':
            endereco4 = dado
         elif W_end == '0101':
             endereco5 = dado
         elif W_end == '0110':
             endereco6 = dado
         elif W_end == '0111':
             endereco7 = dado
         elif W_end == '1000':
             endereco8 = dado
         elif W_end == '1001':
             endereco9 = dado
         elif W_end == '1010':
             endereco10 = dado
         elif W_end == '1011':
             endereco11 = dado
         elif W_end == '1100':
             endereco12 = dado
         elif W_end == '1101':
             endereco13 = dado
         elif W_end == '1110':
             endereco14 = dado
         elif W_end ==  '1111':
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
         if R_end == '0000':
            print(f"Endereco 0: {endereco0}")
         elif R_end == '0001':
            print(f"Endereco 1: {endereco1}")
         elif R_end == '0010':
            print(f"Endereco 2: {endereco2}")
         elif R_end == '0011':
            print(f"Endereco 3: {endereco3}")
         elif R_end == '0100':
            print(f"Endereco 4: {endereco4}")
         elif R_end == '0101':
            print(f"Endereco 5: {endereco5}")
         elif R_end ==  '0110':
            print(f"Endereco 6: {endereco6}")
         elif R_end == '0111':
            print(f"Endereco 7: {endereco7}")
         elif R_end == '1000':
            print(f"Endereco 8: {endereco8}")
         elif R_end == '1001':
            print(f"Endereco 9: {endereco9}")
         elif R_end == '1010':
            print(f"Endereco 10: {endereco10}")
         elif R_end == '1011':
            print(f"Endereco 11: {endereco11}")
         elif R_end == '1100':
            print(f"Endereco 12: {endereco12}")
         elif R_end == '1101':
            print(f"Endereco 13: {endereco13}")
         elif R_end == '1110':
            print(f"Endereco 14: {endereco14}")
         elif R_end == '1111':
            print(f"Endereco 15: {endereco15}")
    elif user == 'C' or user == 'c':
        endereco0 = endereco1 = endereco2 = endereco3 = endereco4 = endereco5 = endereco6 = endereco7 = endereco8 = endereco9 = endereco10 = endereco11 = endereco12 = endereco13 = endereco14 = endereco15 = '00000000'
