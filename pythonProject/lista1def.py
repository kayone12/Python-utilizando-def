#exercicio1
def par_impar():
 num = int(input('Digite um numero:'))

 if num%2==0:
    print('Esse numero é par')
 else:
    print('Esse numero é ímpar')


#exercicio2
def maior_menor():
 n1 = int(input('Digite um numero: '))
 n2 = int(input('Digite outro numero: '))
 if n1 > n2:
    print('o numero {} é maior que o numero {}'.format(n1,n2))

 elif n1 < n2:
    print(f'o numero {n1} é menor que o numero {n2}')

 else:
    print('Os numeros são iguais')


#exercicio3
def tabuada():    
  n = int(input('Digite um numero e descubra a sua tabuada:'))

  for t in range(1,11):
    print(f'{n}x{t}={n*t}')


#exercicio4
def contador():


 contagem = 10
 while contagem >=0:
    print(contagem)
    contagem -=1

#exercicio5
def senhacorreta():
    senha = int(input('Digite a sua senha:'))
    senha2 = int(input('Repita a sua senha:'))

    while senha != senha2:
     print('Senha incorreta digite novamente:')
     senha2 = int(input('Repita a sua senha: '))

    if senha == senha2:
        print('Acesso permitido')
    elif senha != senha2:
        print('Senha incorreta digite novamente:')


#exercicio6
def somanumeros():
 n1 = float(input('Digite um numero:'))
 n2 = float(input('Digite outro numero:'))
 n3 = float(input('Digite outro numero:'))
 n4 = float(input('Digite outro numero:'))
 n5 = float(input('Digite o ultimo numero:'))

 soma = n1 + n2 + n3 + n4 + n5
 print('A soma dos numeros é = {:.0f}'.format(soma))

#exercicio7
def mediageral():
 nota1 = float(input('Digite a sua nota:'))
 nota2 = float(input('Digite a segunda nota:'))
 nota3 = float(input('Digite a terceira nota:'))

 media = (nota1 + nota2 + nota3 ) / 3
 print(' A sua média é = {:.1f}'.format(media))

 if media >=6:
    print('Aprovado')
 else:
    print('Reprovado')


#exercicio8
def numerosimpar():
    for x in range(1,51,2):
     print(x)

#exercicio9
def tamanho():
 n = int(input('Digite um numero inteiro :'))

 digitos = len(str(n))

 print('O numero {} possui {} digitos'.format(n,digitos))



#exercicio10
def segredo():
   
 secreto = 5

 tentativas = 0

 palpite = int(input('Adivinha um numero entre 1 e 10:'))


 while palpite != secreto:
    palpite = int(input('tente novamente:'))
    tentativas +=1

 print('Você acertou! Foram necessárias {} tentativas'.format(tentativas))





 

def main():
 tamanho()
 
   



 
 


 
 
 
if __name__=="__main__":
    main()


