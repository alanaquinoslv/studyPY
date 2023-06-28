# gerador de numeros pseudo-aleatorios

import random

lista = [1, 2, 3, 4, 5, 6, 7, 8]

# sorteio com numeros da lista
print(random.choice(lista))

palavra = 'Alan'
print(random.choice(palavra))

# numero entre 0 e 1
print(random.random())

# dentro de um range
print(random.randint(0, 100))

