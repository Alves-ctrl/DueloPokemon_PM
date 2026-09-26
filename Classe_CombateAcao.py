from Classe_Entidade import Entidade


class CombateAcao(Entidade):

    def __init__(self, id, atacante, acao, dano):
        super().__init__(id)

        self.atacante = atacante
        self.acao = acao
        self.dano = dano

    def __str__(self):

        nome_acao = self.acao.nome if self.acao else "Ataque básico"

        return (
            f"CombateAcao [ID: {self.id}, "
            f"Atacante: {self.atacante.nome}, "
            f"Ação: {nome_acao}, "
            f"Dano: {self.dano}]"
        )