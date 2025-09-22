# Programa para extrair iniciais de um nome completo

nome = input("Digite seu nome completo: ")

# Remove espaços extras e divide em partes

partes = nome.strip().split()

iniciais = ""

for p in partes:

    # Pega a primeira letra de cada parte e deixa maiúscula

    iniciais += p[0].upper() + "."

print("Iniciais:", iniciais)
