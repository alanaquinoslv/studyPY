# executa bloco de instruções até que uma determinada condição seja satisfeita.
import random

parar = 0

while parar <= 10:
    print(parar)
    parar += 1

loop = 0
while loop <= 10:
    print(loop)

    if loop == 5:
        for x in range(10):
            print(x)

    loop += 1

# jogo
while True:
    eu = random.randint(0, 10)
    voce = random.randint(0, 10)

    if eu > voce:
        print("ganhei!!")
        break

print('\n')
