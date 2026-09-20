from Entidade import Entidade

class Acoes(Entidade):

    def __init__(self, id, nome, tipo):
        super().__init__(id)
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return f" Açaõ: {self.id}\nNome: {self.nome}\nTipo: {self.tipo}\n"

    
