palavra = str(input('Digite uma palavra : '))

letras = 0
numeros = 0
espaco = 0

for texto in palavra:
    if texto.isalpha():
        letras +=1
    elif texto.isdigit():
        numeros +=1
    elif texto.isspace():
        espaco +=1
print(f'Quantidade de letras: {letras}')
print(f'Quantidade de numeros: {numeros}')
print(f'Quantidade de espacos: {espaco}')

