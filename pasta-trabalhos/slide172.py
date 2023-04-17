from tqdm import tqdm
import time
# ATIV 1

pergunta = (input("Digite 1 para ligar a válvula do tanque: "))
if pergunta == "1":
    for i in tqdm(range(100)):
        time.sleep(0.1)
    print("Tanque cheio!")

    pergunta2 = (
        input("Digite 2 para desligar a válvula e escoar a água do tanque: "))
    for i in tqdm(range(10)):
        time.sleep(0.1)
    print("O tanque está vazio.")

else:
    print("Ligue a válvula do tanque!")


# ATIV 2
