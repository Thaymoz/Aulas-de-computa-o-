# Crie um programa que solicite um número ao usuário e informe se o número é par ou ímpar. 
# Dica: Use o operador % para verificar a divisão inteira

num1 = float(input("Escolha um numero"))

#Aqui para determinar se o numero é par ou impar a gente cria uma condiçao SE o numero q a pessoa 
#escolher for dividido e o resto desta conta for diferente de zero ele é impar. O simbolo de % serve
#para falar o resto da divisao q der. != serve para falar q é diferente
if num1 % 2 != 0:
    print ("Seu numero é impar")
else:
    print ("Seu numero é par")