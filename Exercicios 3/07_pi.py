# Crie uma variável com 10 dígitos de π (Pi) e formate os apenas os 2 primeiros dígitos,
#  com vírgula, utilizando um f-string.

import math
piGerado = math.pi
print (piGerado)

piManual = 3.141592653
print(f"O valor de Pi com dois dígitos é: {piManual:.2f}".replace('.', ','))