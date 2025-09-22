# Cria as duas listas
listaA = []
listaB = []

print("Digite 5 números para a Lista A:")
for i in range(5):
    num = int(input(f"Número {i+1}: "))
    listaA.append(num)

print("Digite 5 números para a Lista B:")
for i in range(5):
    num = int(input(f"Número {i+1}: "))
    listaB.append(num)

# Cria a lista intercalada
listaC = []

for i in range(5):
    listaC.append(listaA[i])  # adiciona da lista A
    listaC.append(listaB[i])  # adiciona da lista B
    listaC.sort()

# Mostra as listas
print("Lista A:", listaA)
print("Lista B:", listaB)
print("Lista Intercalada:", listaC)

