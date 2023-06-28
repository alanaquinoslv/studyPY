# instruções de controle de loop

lista = ["Morango", "Uva", "Pera", "Abacaxi"]

for fruta in lista:
    print(fruta)
    if fruta == "Pera":
        break


for loop in range(0, 11):
    if loop == 5:
        continue  #ignora instrução
        print("Cheguei, mas vou ser ignorado")
    print(loop)
