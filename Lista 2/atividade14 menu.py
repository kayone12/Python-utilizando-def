from time import sleep
from unittest import removeResult

lista = []
menu = 0

while menu != 4:
    sleep(1)
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



