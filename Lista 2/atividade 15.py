

numeros = []

for i in range(10):
    numero = int(input('Digite um numero:'))
    numeros.append(numero)

for i in range(1):
    extra = int(input('Digite um numero extra e veja quantas vezes se repete:'))
    resultado = numeros.count(extra)
print(f'Foram adicionados {numeros} e o numero {extra} se repete {resultado} vezes')




