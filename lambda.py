# é função anonima
# pode receber qualquer numero de argumento, mas apenas uma expressao


funcao_soma = lambda valor: valor + 10

print(funcao_soma(1))


funcao_soma_02 = lambda valor_1, valor_2: valor_1 + valor_2
print(funcao_soma_02(10, 10))


exemplo = lambda valor : 'verdadeiro' if valor % 2 == 0 else 'falso'
print(exemplo(4))