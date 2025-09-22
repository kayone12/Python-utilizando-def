from time import sleep

nome =[]

quantidade = int(input('Quantos nome vai adicionar ?'))

for i in range(quantidade):
    nomes = input(f'Digite o nome {i+1}:')
    nome.append(nomes)
print('A lista tem os seguintes nomes :{}'.format(nome))

sleep(2)

antigo = input('Qual nome deseja mudar ?')
novo = input('Digite o novo nome :')

if antigo in nome:
    indice = nome.index(antigo)
    nome[indice]=novo
    print('Lista atualizada:', nome)
else:
    print('esse nome não está na lista')

