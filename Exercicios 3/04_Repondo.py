# Utilize a função replace() e troque azul por nublado da variável texto = "O céu está azul".
#  Formate com a função
# dentro de uma f-string.

text = " O céu está azul."
p1= input("Digite q o cor o céu deveria ter")

#Aqui vc podia criar uma variavel e colocar o text.replace("n sei", "n sei 2") -> primeira palavra é
#a do texto a segunda é pela qual vc quer trocar 
#e dps printar n sei pq nao foi dentro das chaves o replace mas desse jeito foi 

print(f"Agora{text}".replace("azul",p1))