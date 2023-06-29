# python é OO
# quase tudo é um objeto
# classe é construtor de objetos


class pessoa:
    # construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def boas_vindas(self):
        print("olá, seja bem vindo ", self.nome)

    def recusado(self):
        print("seu acesso foi recusado")

    # metodo
    def maior_idade(self):
        if self.idade >= 18:
            print("usuário é maior de idade")
            self.boas_vindas()
        else:
            print("usuário é menor de idade")
            self.recusado()


dados = pessoa("Alan", 21)
dados.maior_idade()