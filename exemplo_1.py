# ler um número n de pessoas
# cada pessoa tem um nome, ano que nasceu

limit = int(input("Número de pessoas: "))

pessoas = []

for i in range(limit):
    nome = input("Nome: ")
    ano = int(input("Ano de nascimento: "))
    pessoas.append((nome, ano))

for pessoa in pessoas:
    nome, idade = pessoa
    ano_atual = 2021
    if ano_atual - idade >= 18:
        print(f"Olá {nome}, você é maior de idade")
    else:
        print(f"Olá {nome}, você é menor de idade")
