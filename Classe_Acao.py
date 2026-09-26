from Classe_Entidade import Entidade


class Acoes(Entidade):

    def __init__(self, id, nome, poder):
        super().__init__(id)

        self.nome = nome
        self.poder = poder

    def __str__(self):
        return (
            f"Ação [ID: {self.id}, "
            f"Nome: {self.nome}, "
            f"Poder: {self.poder}]"
        )