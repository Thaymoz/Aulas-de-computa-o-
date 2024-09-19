# Faça dois scripts (A e B). Crie uma função no scriptA, importe-o como um módulo no scriptB
#  e ative a função de
# A, a partir de valores no scriptB;


import modulo

n1 = float(input ("digite o primeiro numero "))
n2 = float(input ("digite o segundo numero "))

#quando colocado f"" vc cria uma f string ou seja ele formata o seu texto diretamente inves de criar uma
#conta, como normalmente eu criaria uma terceira variavel para realizar a mudança e ent colocar no print
#mas com ela eu posso fazer direto 

#Proximo ponto apos vc der IMPORT no arquivo q vc quiser vc tem acesso as informaçoes e as funçoes q vc
#criou ai vc precisa colocar um ponto e declarar o que vc quer qual deles vc deseja

print (f"A soma dos dois numeros q vc escolheu é {modulo.soma(n1,n2)}")