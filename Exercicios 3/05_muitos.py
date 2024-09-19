# Dado a variável meuTexto = “Esta lista contém muitos nomes”, 
# utilize uma f-strig com if e else para dizer se a
# variável meuTexto contém a string “muitos”

text = "Esta lista contém muitos nomes"

#O dificil do exercicio foi entender o q ele queria mas basicamente ele quer q anuncie se tem a palavras
#muitos no texto SE tiver fale que tem POREM SE NAO tiver fale que nao ha muitos

print (f"Sim a muitos" if "muitos" in text else "nao ha muitos")
