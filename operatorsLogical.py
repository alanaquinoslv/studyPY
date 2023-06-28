# Operadores de Comparações - Parte 2
And = 'and'
Ou = 'or'
Negação = 'not'

print('8 é maior que 7 e 7 maior que 8:', 8 > 7 and 7 > 8 )
print('8 é maior que 7 e 7 menor que 8:', 8 > 7 and 7 < 8 )
print('8 é maior que 7 ou 7 menor que 8:', 8 == 7 or 7 == 8 )
print('8 é maior que 7 ou 7 menor que 8:', 8 > 7 or 7 > 8 )

print(20 > 2 and 30 > 15)
print(40 > 41.2 or 23.2 <= 23.1)

Lista = [1, 2, 3, 4]

print(10 not in Lista)