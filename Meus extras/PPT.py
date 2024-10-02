#texto inicial 
print ("Seja bem vindo jogador, vamos jogar jokenpo? Lembre-se de colocar as respostas com a primeira letra maiuscula")

import random

# jogador = input("Digite o q vc quer jogar")
# list = ("Pedra","Papel","Tesoura")
# computador = random.choice(list)

# if jogador == computador:
#     print ("voce jogou",jogador, "e o computador escolheu"computador,"empatou")
# elif jogador:
#     print("voce jogou",jogador, "e o computador escolheu"computador,"empatou")

list = range(1,11)
jogador = int(input("Digite um numero"))
computador = random.choice(list)
calculo = jogador + computador

try:
    escolha = input("Par ou Impar? ").strip().upper()
    if escolha == ("PAR"):
        if calculo % 2 == 0: 
            print ("vc ganhou",calculo)
        else:
            print ("vc perdeu",calculo)
    elif escolha == ("IMPAR"):
        if calculo % 2 != 0: 
            print ("vc ganhou",calculo)
        else:
            print ("vc perdeu",calculo)

except NameError:
     print("Escolhe par ou impar seu burro")