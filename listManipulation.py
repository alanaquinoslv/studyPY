# As listas são um dos 4 tipos de dados internos do Python usados ​​para armazenar coleções de dados, os outros 3 são Tuple , Set e Dictionary , todos com qualidades e usos diferentes.

# Comandos mais utilizados:

# append() - Para adicionar um item ao final da lista
# len() - Calcular o tamanho da lista
# [ ] - Acessar posições
# del() - Exlcuir um elemtno
# clear() - Limpar a lista
# insert() - Para inserir um item de lista em um índice especificado
# extend() - Anexar elementos de outra lista à lista atual
# remove() - Remove o item especificado
# pop() - Remove o índice especificado.
# sort() - Ordenar os valores
# copy() - Faz uma copia da Lista
# index() - Retorna o index do elemento da lista


from operator import truediv


Lista_Vazia = []
# adicionando valores a ultima posicao
Lista_Vazia.append(1)
Lista_Vazia.append(3)
Lista_Vazia.append(8)
Lista_Vazia.append(22)
print(Lista_Vazia)

# tamanho lista
print(len(Lista_Vazia))

# acessar
print(Lista_Vazia[0])
print(Lista_Vazia[-1])  # ultimo valor
print(Lista_Vazia[0:2])  # 0 ate o 2

# limpar
print(Lista_Vazia)
#Lista_Vazia.clear()
print(Lista_Vazia)

#insert - voce define a posição para inserir valor 
Lista_Vazia.insert(0, 0)
Lista_Vazia.insert(3, 89)
print(Lista_Vazia)

#extend - lista dentro de outra lista
Lista_01 = [1, 2, 3]
Lista_02 = [4, 5, 6]
Lista_01.extend(Lista_02)
print(Lista_01)

# remove
Lista_01.remove(5)
print(Lista_01)

# pop - remover pela posição
Lista_01.pop(0)
print(Lista_01)

Lista_ABC = ['F', 'B', 'a', 'd', 'K']
# sort - ordenar lista
Lista_ABC.sort()
print(Lista_ABC)

Lista_ABC.sort( reverse= True )
print(Lista_ABC)

# copy - copia a lista
Lista_Nova = Lista_ABC.copy()
print(Lista_Nova)

# index - retorna a posição
print(Lista_Nova.index('K'))