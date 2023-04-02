deci = int(input("Digite um número inteiro e veja seu equivalente em binário: "))
bin = ''

while deci > 0:
    bin = str(deci % 2) + bin
    deci //= 2
    
print(f"O número {deci} em binário é {bin}")