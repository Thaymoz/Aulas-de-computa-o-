# Crie uma lista com os números de 1 a 100. A seguir, escolha um número desta lista e imprima-o.
# Utilize a função
# choice() do módulo random

import random
#Quando colocado o range ele cria uma "lista" de numeros, ou seja ali ele vai criar os numeros de 1 a 100
#Random.choice serve para escolher um numero aleatorio de uma lista q VC definiu
list = range(1,100)
d100 = random.choice(list)

print (d100)