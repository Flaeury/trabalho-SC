from tqdm import tqdm
import time
# ATIV 1

pergunta = (input("Digite 1 para ligar a válvula do tanque: "))
if pergunta == "1":
    print("Tanque enchendo: ")
    for i in tqdm(range(100)):
        time.sleep(0.1)
    print("O tanque está cheio, iniciando esvaziamento...")
    for i in tqdm(range(50)):
        time.sleep(0.1)
    print("O tanque está vazio.")

else:
    print("Ligue a válvula do tanque!")


# ATIV 2
chave1 = int(input("Digite 0 para desligar ou 1 para ligar a chave 1: "))
chave2 = int(input("Digite 0 para desligar ou 1 para ligar a chave 2: "))
chave3 = int(input("Digite 0 para desligar ou 1 para ligar a chave 3: "))

num_chaves_ligadas = chave1 + chave2 + chave3

if num_chaves_ligadas % 2 == 0:
    print("Você ligou a saída")
else:
    print("Você desligou a saída")
