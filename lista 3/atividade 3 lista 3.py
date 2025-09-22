# Programa que imprime uma palavra de trás para frente

palavra = input("Digite uma palavra: ")

invertida = ""

# Percorre a palavra de trás para frente usando range

for i in range(len(palavra) - 1, -1, -1):
    invertida += palavra[i]

print("Palavra invertida:", invertida)
