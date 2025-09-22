# Pede a lista de números
numeros = input("Digite uma lista de números separados por espaço: ")
lista = [int(x) for x in numeros.split()]

# Pede o valor a ser procurado
valor = int(input("Digite o valor que deseja procurar: "))

# Cria uma lista vazia para guardar os índices
indices = []

# Percorre a lista procurando o valor
for i in range(len(lista)):
    if lista[i] == valor:
        indices.append(i)

# Mostra o resultado
if indices:
    print("O valor", valor, "aparece nos índices:", indices)
else:
    print("O valor", valor, "não aparece na lista.")
