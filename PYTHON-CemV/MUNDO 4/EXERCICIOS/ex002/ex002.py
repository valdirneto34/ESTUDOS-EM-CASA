class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, nome="vazio", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1
    
    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado -> Nome: {self.nome} ; Idade: {self.idade}"


g1 = Gafanhoto("Valdir", 21)
g1.aniversario()
print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)
