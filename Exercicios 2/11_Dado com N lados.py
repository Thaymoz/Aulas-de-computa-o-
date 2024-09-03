# Melhore o exercício 1 solicitando um número ao usuário. Adicione uma checagem de erro caso ele não digite um
# número

import random

#Try é uma funçao que pede para rodar o codigo, porem se em algum EXCETO momento acontecer (Nesse caso
#o valor inserrido der erro) ele fara outra coisa.

try:
    lados = float(input("Digite o numero de lados: "))
    dn = random.randint(1,lados)
    print(dn)
except ValueError:
    print("Lados, invalidos escreva um numero real")
