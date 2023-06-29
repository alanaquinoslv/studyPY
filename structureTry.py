# permite testar um bloco quanto a erros
# except permite lidar com o erro
# else executar quando não há erro
# finally sempre será executado, independentemente do que acontecer

# erro
#0 / 0


# teste
try:
    0 / 0
    print('deu certo')
except:
    print("não deu certo")

finally: 
    print('sempre é executada')