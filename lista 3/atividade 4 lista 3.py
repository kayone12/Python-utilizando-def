# Programa para verificar se uma palavra é palíndromo

palavra = input("Digite uma palavra: ")

# Deixar tudo em minúsculo para não diferenciar maiúsculas/minúsculas

palavra_normalizada = palavra.lower()

# Inverter a palavra usando loop (sem slicing)

invertida = ""
for i in range(len(palavra_normalizada) - 1, -1, -1):
    invertida += palavra_normalizada[i]

# Comparar

if palavra_normalizada == invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra NÃO é um palíndromo.")
