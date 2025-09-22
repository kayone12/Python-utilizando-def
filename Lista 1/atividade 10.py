secreto = 5

tentativas = 0


palpite = int(input('Adivinha um numero entre 1 e 10:'))
tentativas +=1

while palpite != secreto:
    palpite = int(input('tente novamente:'))
    tentativas +=1

print('Você acertou! Foram necessárias {} tentativas'.format(tentativas))
