senha = int(input('Digite a sua senha:'))
senha2 = int(input('Repita a sua senha:'))

while senha != senha2:
    print('Senha incorreta digite novamente:')

if senha == senha2:
    print('Acesso permitido')
elif senha != senha2:
    print('Senha incorreta digite novamente:')







