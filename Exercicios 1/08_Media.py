# Peça 4 notas de um aluno. Tire a média e mostre se ele foi aprovado ou não (média 7).
#PULL
p1 = float(input("Nota da primeira prova"))
p2 = float(input("Nota da segunda prova"))
p3 = float(input("Nota da terceira prova"))
p4 = float(input("Nota da qurta prova"))
#List serve para criar uma lista
#sum server para somar os numeros da esquerda para direita
#len serve para pegar quantos numeros tem na lista (ali 4)
list = (p1,p2,p3,p4)
conta = sum(list)/len(list)

if conta > 7:
    print ("parabens vc passou com", conta)
else:
    print("Reprovado, nota",conta)