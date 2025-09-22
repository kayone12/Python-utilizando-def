#exercicio 1
def presença():
    lista = []
    for i in range(3):
        nome = input('Coloque o seu nome para adicionar na lista:')
        lista.append(nome)

    pesquisa = input('Digite o seu nome e veja se está na lista:')

    if pesquisa in lista:
        print('Acesso autorizado')
    else:
       print('Acesso negado')


#exercicio2
def reverter():
 numeros = []

 for i in range(5):
    numero = int(input('Digite um numero:'))
    numeros.append(numero)
    numeros.sort(reverse=True)
 print(numeros)

#exercicio3

def positivos_negativos():
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


#exercicio4 MENU
def menulista():

    lista = []
    menu = 0

    while menu != 4:
     menu = int(input(
        "1 - Adicionar item\n"
        "2 - Remover item\n"
        "3 - Mostrar lista\n"
        "4 - Sair\n"
        "Escolha uma opção: "
    ))


     if menu == 1:
        adicionar = input("Digite o que deseja adicionar: ")
        lista.append(adicionar)

     elif menu == 2:
        remover = input("Digite o que deseja remover: ")
        if remover in lista:
         lista.remove(remover)
        else:
            print("Esse item não está na lista.")

     elif menu == 3:
         print("Lista atual:", lista)

    print("Os itens da sua lista foram:", lista)

 
#exercicio5
def numerorepitido():
 numeros = []

 for i in range(10):
    numero = int(input('Digite um numero:'))
    numeros.append(numero)

 for i in range(1):
    extra = int(input('Digite um numero extra e veja quantas vezes se repete:'))
    resultado = numeros.count(extra)
 print(f'Foram adicionados {numeros} e o numero {extra} se repete {resultado} vezes')


#exercicio6
def numeroporindice():

    numeros = input("Digite uma lista de números separados por espaço: ")
    lista = [int(x) for x in numeros.split()]

    valor = int(input("Digite o valor que deseja procurar: "))

    indices = []

    for i in range(len(lista)):
     if lista[i] == valor:
        indices.append(i)

    if indices:
     print("O valor", valor, "aparece nos índices:", indices)
    else:
     print("O valor", valor, "não aparece na lista.")

#exercicio7
def intercalada():
    listaA = []
    listaB = []

    print("Digite 5 números para a Lista A:")
    for i in range(5):
        num = int(input(f"Número {i+1}: "))
        listaA.append(num)

    print("Digite 5 números para a Lista B:")
    for i in range(5):
        num = int(input(f"Número {i+1}: "))
        listaB.append(num)

    listaC = []
    for i in range(5):
        listaC.append(listaA[i]) 
        listaC.append(listaB[i])  

    listaC.sort() 

    
    print("Lista A:", listaA)
    print("Lista B:", listaB)
    print("Lista Intercalada:", listaC)

#exercicio8
def nomesnalista():

    nome =[]

    quantidade = int(input('Quantos nome vai adicionar ?'))

    for i in range(quantidade):
     nomes = input(f'Digite o nome {i+1}:')
     nome.append(nomes)
    print('A lista tem os seguintes nomes :{}'.format(nome))



    antigo = input('Qual nome deseja mudar ?')
    novo = input('Digite o novo nome :')

    if antigo in nome:
     indice = nome.index(antigo)
     nome[indice]=novo
     print('Lista atualizada:', nome)
    else:
     print('esse nome não está na lista')







def main():
 presença()





if __name__ == '__main__':
   main()