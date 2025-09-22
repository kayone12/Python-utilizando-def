numeros = []

for i in range(5):
    numero = int(input('Digite um numero:'))
    numeros.append(numero)
    numeros.sort(reverse=True)
print(numeros)
