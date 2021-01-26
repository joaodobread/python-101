from pprint import pprint

# 0 -> n-1
# array = [1, 2, 3, 4, 5]
# array[0] = "Marcio!"

# print(array)
# print(type(array))
# print(array[0])

# array.append(123123)
# array.pop(0)
# print(array)

# array = [12, 3, 234, -12, 234]
# print(array.sort())
# print(array)
# array.clear()
# print(array)

# array_2 = array.copy()
# array_3 = array[:]

# array_2[0] = "dfkasdfk"

# print(array, array_2, array_3)

# array.sort()
# print(array)
# array.reverse()
# print(array)
# print(array[-2])

nomes = ["João", "Mácio", "Pedro", "Marcos"]
idades = [21, 30, 14, 20]
sobrenomes = ["Santana", "Belo", "Fernandes", "Silva"]

pprint(list(zip(nomes, idades, sobrenomes)))

for nome, idade, sobrenome in zip(nomes, idades, sobrenomes):
    # print(nome, idade, sobrenome)
    print(f"Olá, {nome} {sobrenome}, você tem {idade} anos de idade")

# for var in enumerate(idades):
#     print(var[0], var[1], len(var))

# for index, value in enumerate(idades):
#     print(index, value)
