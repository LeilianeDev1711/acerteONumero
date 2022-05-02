import random
from time import sleep

print("\033[1;30;45m------------------ACERTE O NÚMERO------------------\033[m")
sorteio = random.randint(1,5)

while True:
    try:
        escolha_usuario = int(input("Qual o seu palpite entre 1 e 5?"))
        break
    except:
        print("Entrada inválida")
        continue

while (escolha_usuario > 5) or (escolha_usuario < 1):
    print("----------------------")
    escolha_usuario = int(input("Você deve escolher entre 1 e 5:"))


if (escolha_usuario == sorteio):
    print("\033[1;30mMáquina: {}\033[m".format(sorteio))
    print("----------------------")
    print("\033[1;30mSeu palpite: {}\033[m".format(escolha_usuario))
    print("----------------------")
    print("\033[1;33mVOCÊ ACERTOU!\033[m")

else:
    print("Máquina: {}".format(sorteio))
    print("----------------------")
    print("Seu palpite: {}".format(escolha_usuario))
    print("----------------------")
    print("\033[1;33mVOCÊ ERROU!\033[m")






