# Crie um programa que gere e exiba os primeiros 10 números da sequência de Fibonacci. Dica: use uma estrutura
# de loop para gerar a sequência

#Como funciona fibonacci: ele pega o numero anterior dele e soma 

#Seguindo essa logica vamos pensar 0+1=1 -> 1+1=2 -> 1+2=3 .....

#Agr vamos pensar nesses numeros em termos matematicos, como seria a funçao pense no primeiro numero
#como "a", o segundo numero "b", e o resultado como "c", assim apos resultarmos a conta devemos atualizar 
#os numeros anteriores, ou seja, "a" vira "b" e "b" vira "c"

#Ok estruturando como funciona fibonachi precisamos q a conta se repita 10 vezes e para isso precisamos 
#criar um loop q ocorra 10 vezes. Desta forma criamos uma terceira variavel q chamamos de "d", porem
#poderia ser algo mais simples para entender como "ciclos ou loops", mas tanto faz so precisamos criar
#uma variavel e dar um valor (zero) e dizemos q esse loop vai ocorrer enquanto for menos q zero
#e q para toda vez q ele fizer a conta ele deve somar 1 ao valor "d", assim em algum momento "d" vai valer 
#10 e acabar com o ciclo
a=0
b=1
d=0

while d<10:
    c=a+b
    print(c)
    d+=1
    a=b
    b=c
