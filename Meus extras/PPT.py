#texto inicial 
print ("Seja bem vindo jogador, vamos jogar Par ou Impar?")

import random

escolha = input("Par ou Impar? ").strip().upper()

list = range(1,11)
jogador = int(input("Digite um numero"))
computador = random.choice(list)
calculo = jogador + computador

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
