nota1 = float(input('Digite a sua nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))

media = (nota1 + nota2 + nota3 ) / 3
print(' A sua média é = {:.1f}'.format(media))

if media >=6:
    print('Aprovado')
else:
    print('Reprovado')