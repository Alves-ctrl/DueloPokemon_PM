from Entidade import Entidade
from CombateAcao import CombateAcao

class Combate(Entidade):

    def __init__(self, id, pokemonA, pokemonB):
        super().__init__(id)
        self.pokemonA = pokemonA
        self.pokemonB = pokemonB

        self.vidaA = pokemonA.vida
        self.vidaB = pokemonB.vida

        self.movimentos = []
        self.vencedor = None

    def __str__(self):
         return (
            f"Combate [ID: {self.id}, "
            f"{self.pokemon_a.nome} x {self.pokemon_b.nome}, "
            f"Vida {self.pokemon_a.nome}: {self.vida_pokemon_a}, "
            f"Vida {self.pokemon_b.nome}: {self.vida_pokemon_b}, "
            f"Vencedor: {self.vencedor}]"
        )

    def addAcao(self,acao):
        self.movimentos.append(acao)

    def delAcao(self,acao):
        if acao in self.movimentos:
            self.movimento.remove(acao)

    def buscarAcao(self,indice):
        if 0 <= indice < len(self.movimentos):
            return self.movimentos[indice]
        return None

    def alterarAcao(self,movimento,indice):
        result = self.buscarAcao(indice)
        if result is not None:
            self.movimentos[result] = movimento
            return True
        return False

    def mostrarAcao(self):
        return self.movimentos


    def duelar(self):
        if self.pokemonA.velocidade > self.pokemonB.velocidade:
            atacante = self.pokemonA
            defensor = self.pokemonB
        else:
            atacante = self.pokemonB
            defensor = self.pokemonA

        while self.nocauteado() is None:
            acao = None

            self.atacar(atacante, defensor, acao)
            if self.nocauteado() is not None:
                break
            atacante,defensor = defensor, atacante

        return  self.vencedor()

    def atacar(self, atacante, defensor, acao):
        crit = 1.5
        fraco = 0,75

        dano = atacante.ataque
        if atacante.tipo == defensor.fraqueza:
            dano = dano * crit
        elif atacante.tipo == defensor.resistencia:
            dano = dano * fraco

        if dano < 0:
            dano = 0

        acao =  CombateAcao(atacante, acao, dano)

        self.addAcao(acao)

        self.defender(defensor, dano)

    def defender(self, defensor, dano):
        if defensor == self.pokemonA:
            self.vidaA -= dano

            if self.vidaA < 0:
                self.vidaA = 0
        if defensor == self.pokemonB:
            self.vidaB -= dano
        
            if self.vidaB < 0:
                self.vidaB = 0

    def nocauteado(self):

        if self.VidaA == 0:
            return self.pokemonA
        if self.VidaB == 0:
            return self.pokemonB

        return None

    def vencedor(self):
        derrotado = self.nocauteado()
        if derrotado == self.pokemonA:
            self.vencedor = self.pokemonA
        if derrotado == self.pokemonB:
            self.vencedor = self.pokemonB

            return self.vencedor
