# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem de aumento. Mostre o valor do aumento, do salário atual e quanto a mais este
# aumento vai resultar em 1 ano.

salario = float(input("Quanto vc recebe?"))
aumento = float(input("Quanto % vc quer de aumento?"))

conversor = (aumento/100) + 1
conta = salario*conversor

print("Seu salario atual é", conta,"e em um ano vc vai ter ganhado",conta*12)