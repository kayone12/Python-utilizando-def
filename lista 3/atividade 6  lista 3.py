# Programa para contar palavras em uma frase

frase = input("Digite uma frase: ")

# O split() divide a frase em uma lista de palavras

palavras = frase.split()

# Conta a quantidade de palavras

quantidade = len(palavras)

print("Quantidade de palavras:", quantidade)
