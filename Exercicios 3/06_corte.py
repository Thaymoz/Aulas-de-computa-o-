# Dada a variável texto = "Python é incrível", 
# utilize uma f-string para cortar o texto e imprimir somente a primeira
# palavra da frase

text = "Python é incrivel"

#Bem como todas as outras funçoes upper, strip precisa de um parentesses vazio dps dele e 
#no caso do spli se coloca um colchete para decidir qual palavra ele vai escolher 
#neste caso python é 0 / é é 1 / incrivel é 2

print (f"{text.split()[0].upper()}")