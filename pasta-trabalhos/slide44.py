binario = input("Digite um número binário: ")
decimal = 0
expoente = len(binario)-1
for i in binario:
    decimal += int(i)*2**expoente
    visu = int(i)*2**expoente
    expoente -= 1
print("O número",binario,"equivale a",decimal,"no sistema decimal!")