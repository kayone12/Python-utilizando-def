numerospositivo = []

numerosnegativo = []

for i in range(6):
    numeros = int(input('Digite os numeros para adicionar na lista:'))
    if numeros >0:
     numerospositivo.append(numeros)

    elif numeros <0:
        numerosnegativo.append(numeros)

print('Lista de numeros positivos',numerospositivo)

print('Lista de numeros negativos',numerosnegativo)
