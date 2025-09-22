letras = str(input('Digite uma palavra: '))

caracter=len(letras)

maiusculas = letras.upper()
minusculas = letras.lower()

if len(letras)>0:
    print(f'Primeira letra = {letras[0]}')
    print(f'Última letra = {letras[-1]}')

else:
    print('Você não digitou nada')



print(f'Numeros de caracteres = {caracter} ')
print(f'Em maisculas = {maiusculas}')
print(f'Em minusculas = {minusculas}')


