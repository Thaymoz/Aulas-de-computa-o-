# Crie uma string com espaços extras e remova-os. Exemplo: texto = " Espaços extras "

text = input("digite o q vc quiser com quantos espaços quiser ")

#Tudo é meio parecido agora mas strip serve para remover os espaços tanto da frente e de tras 
# ele tem as funçoes ->rstrip q remove só os espaços da direita. ->lstrip remove só os espaços da esquerda
print(f"{text.strip()}")