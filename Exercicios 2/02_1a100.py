# Crie uma lista com os números de 1 a 100. A seguir, escolha um número desta lista e imprima-o.
# Utilize a função
# choice() do módulo random

import random

list = range(1,100)
d100 = random.choice(list)

print (d100)