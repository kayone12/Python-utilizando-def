#exercicio3
def palavra():

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

#exercicio2
def vogais():
 palavra = str(input('Digite uma palavra: '))

 vogais = 'aeiouAEIOU'
 contador = 0
 for letra in palavra:
    if letra in vogais:
        contador +=1
 print(f'Quantidade de vogais = {contador}')

#exercicio3
def palavrainvertida():
   
 palavra = input("Digite uma palavra: ")

 invertida = ""

 for i in range(len(palavra) - 1, -1, -1):
    invertida += palavra[i]

 print("Palavra invertida:", invertida)


#exercicio4
def escritaigualreverse():

 palavra = input("Digite uma palavra: ")


 palavra_normalizada = palavra.lower()


 invertida = ""
 for i in range(len(palavra_normalizada) - 1, -1, -1):
    invertida += palavra_normalizada[i]


 if palavra_normalizada == invertida:
    print("A palavra é um palíndromo!")
 else:
    print("A palavra NÃO é um palíndromo.")

#exercicio5 
def frasemodificada():

 frase = input("Digite uma frase: ")

 nova_frase = frase.replace('a','@')

 print("Frase modificada:", nova_frase)

#exercicio6
def quantidadedepalavra():
  
 frase = input("Digite uma frase: ")

 palavras = frase.split()

 quantidade = len(palavras)

 print("Quantidade de palavras:", quantidade)

#exercicio7
def letramaiuscula():

 nome = str(input('Digite o seu nome : '))

 nomeformatado = nome.title()

 print(f'O nome formatado é {nomeformatado}')

#exercicio8
def textosemespaço():

 texto = input("Digite uma frase: ")

 sem_espacos = texto.replace(" ", "")

 print("String original:", texto)
 print("String sem espaços:", sem_espacos)

#exercicio9
def palavradetalhada():
   
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

#exercicio10
def iniciaisdonome():

 nome = input("Digite seu nome completo: ")

 partes = nome.strip().split()

 iniciais = ""

 for p in partes:

    iniciais += p[0].upper() + "."

 print("Iniciais:", iniciais)






def main():
   iniciaisdonome()
   


if __name__ == "__main__":
    main()