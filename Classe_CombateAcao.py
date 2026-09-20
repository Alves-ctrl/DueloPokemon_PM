from Entidade import Entidade

class CombateAcao:

    def __init__(self, pokemon, acao):
        self.pokemon = pokemon
        self.acao = acao


    def __str__(self):
        return (
            f"Pokemon: {self.pokemon.nome} | "
            f"Acao: {self.acao.nome} | "
            
        )
   
