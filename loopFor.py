# usado para travessia sequencial

for random in range(10):  # range gera uma lista de valores
    print(random)


for random in range(1, 11):  # começar de um range
    print(random)


for random in range(0, 101, 5):  # de 5 em 5
    print(random)


lista = ["Brasil", "Argentina", "Chile", "Equador", "Uruguai"]
for pais in lista:  # percorrendo a lista
    if pais == "Uruguai":
        print("O país é bi campeão da copa do mundo")
    ## print(pais.upper()[0:3])  # manipulações da lista
for x in range(10):
    print(x)


for loop in range(len(lista), 1):  # percorrendo pelo tamanho da lista
    print(lista[loop])  # exibindo valor da lista de acordo com a posição


for pais in enumerate(lista):  # antes do valor mostra o index
    print(pais)


print([numero for numero in range(0, 10, 2)])  # for dentro de uma lista

for loop in range(0, 10):
    lista.append(loop)
print(lista) 