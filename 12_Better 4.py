# Melhore o exercício 4 com o módulo Time e a função sleep()

#import para trazer a biblioteca de funçao de tempo
import time
#Como no exercicio 4 ou 10 criamos um loop simples com uma condiçao simples 

#O diferencial é colocar time.sleep q como o nome diz ele da uma "dormidinha" com base no tempo q vc 
#colocar ou seja ao printar o numero "n" subtrair 1 ele fara a pausa de meio segundo e ent vai reptir o 
#ciclo

#Coloquei o print n , antes da subtraçao para aparecer o primeiro numero

n = 100
while n>0:
    print(n)
    n -= 1
    time.sleep(0.5)
print("Cabo")