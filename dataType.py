# listas - []
# tuplas - ()
# dicionarios(json) - {} 

#recebem qualquer tipo de informação

#listas
lista_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_02 = ['Nome', 'Sobrenome', 1, 6 ]

lista_03 = [1, 'text', True, [1, 2, 4]]
print(lista_01, lista_03)

#tuplas são imutáveis
tupla_01 = (1, 2, 4, 5)
tupla_02 = ('nome', 'sobrenome', False, 1.99)
print(tupla_01, tupla_02)

# dicionarios
dicionario = {
    'index' : 'valor',
    'id' : 1,
    'nome' : 'Alan',
    'Lista' : lista_03,
    'Tupla' : tupla_02
}
print(dicionario)

