# Crie um programa que solicite um número ao usuário e informe se o número é par ou ímpar. 
# Dica: Use o operador % para verificar a divisão inteira

num1 = float(input("Escolha um numero"))


if num1 % 2 != 0:
    print ("Seu numero é impar")
else:
    print ("Seu numero é par")