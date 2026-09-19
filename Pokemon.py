from Entidade import Entidade

class Pokemon(Entidade):
    def __init__(self, id, nome,tipo, fraqueza, resistencia, ataque, defesa, vida, velocidade):
        super().__init__(id)
        self.nome = nome
        self.tipo = tipo
        self.fraqueza = fraqueza
        self.resistencia = resistencia
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida
        self.velocidade = velocidade

    def __str__(self):
        return(
            f"Pokemon [ID:{self.id}, Nome:{self.nome},"
            f" Vida:{self.vida}, Tipo:{self.tipo},"
            f" Fraqueza:{self.fraqueza}, Resistencia:{self.resistencia},"
            f" Ataque:{self.ataque}, Defesa:{self.defesa}, Valocidade:{self.velocidade}]"
        )

    