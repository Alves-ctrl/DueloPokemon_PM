import Entidade.py

class Treinador(Entidade):
    def __init__(self, id, nome):
        super().__init__(id)
        self.nome = nome

    def __str__(self):
        return f"Treinador\n [ID:{self.id}, Nome: {self.nome}]"