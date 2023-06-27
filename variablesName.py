#pode declarar de diversas formas

#nomeando(em vez de fazer uma por uma)
Laranja, Melao, Limao = 1, 2, 3
print(Laranja, Melao, Limao)

# essa sequencia vao receber o mesmo valor
Morango = Uva = Kiwi = 100
print(Morango, Uva, Kiwi)

#nomear com listas
Lista_carros = ['Renault', 'Tesla', 'Mercedes-Benz']
Marca_01, Marca_02, Marca_03 = Lista_carros
# cada marca recebeu o nome da lista de acordo com a posiçõa
print(Marca_01, Marca_02, Marca_03)

#combinar variaveis
Nome = 'Alan'
Sobrenome = 'Aquino'
Nome_Completo = Nome + ' ' + Sobrenome
print(Nome_Completo)


#experimento
#pra concatenar 
Idade = str(21)
print(Nome + " " + Idade)

Investimento = 1000
Taxa_Juros = float('0.2')
print(Investimento * Taxa_Juros)

Valor_Ganho = ((Investimento * Taxa_Juros) + Investimento)
print(Valor_Ganho)