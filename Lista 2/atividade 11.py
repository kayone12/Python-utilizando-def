lista = []

for i in range(3):
    nome = input('Coloque o seu nome para adicionar na lista:')
    lista.append(nome)

pesquisa = input('Digite o seu nome e veja se está na lista:')

if pesquisa in lista:
    print('Acesso autorizado')
else:
    print('Acesso negado')
