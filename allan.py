class Jogos:
    def __init__(self, ano=None, desenvolvedora=None, nome=None, genero=None, lista=None):
        self.ano = ano
        self.desenvolvedora = desenvolvedora
        self.nome = nome
        self.genero = genero
        self.lista = []

    def adicionar_jogo(self):
        self.ano=int(input("Qual o ano de lançamento?\nLançamento: "))
        self.desenvolvedora=input("Qual é a desenvolvedora?\nDesenvolvedora: ").capitalize()
        self.nome=input("Qual o nome do jogo?\nJogo: ").upper()
        self.genero=input("Qual o gênero do jogo?\nGênero: ").capitalize()
        self.lista.append(self.ano)
        self.lista.append(self.desenvolvedora)
        self.lista.append(self.nome)
        self.lista.append(self.genero)
        print("Jogo: '{}', Ano: '{}', Gênero: '{}', Desenvolvedora: '{}'".format(self.nome, self.ano, self.genero, self.desenvolvedora))

samuel=Jogos()
samuel.adicionar_jogo()

print()
print("~Feito por Samuel Brito Melo e Kauê Yuuki Yamamoto~")

print()
print("Questão 1 = É o programa que utilizamos para fazer nossos códigos, ex: CMD, Visual Studio, etc")
print("Questão 2 = Linus Linux")
print("Questão 3 = É utilizado para controlar versões da aplicação; Utilizamos quando queremos colocá-lo em um repositório; Importante para adicionar atualizações")

        
