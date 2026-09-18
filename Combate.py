import Entidade.py

class Combate(Entidade):
    def __init__(self, pokemonA, pokemonB):
        self.pokemonA = pokemonA
        self.pokemonB = pokemonB

        self.vida_pokemonA = pokemonA.vida
        self.vida_pokemonB = pokemonB.vida

        self.vencedor = None

    def __str__(self):
        return f"Combate: {self.pokemonA.nome} x {self.pokemonB.nome} \nVencedor: {self.vencedor}"
        
    def duelar(self):
        if self.pokemonA.velocidade > self.pokemonB.velocidade:
            atacante = self.pokemonA
        else:
            atacante = self.pokemonB

        while self.nocauteado() is None:
            self.atacar(atacante)

            if self.nocauteado() is not None:
                break

            if atacante == self.pokemonA:
                atacante = self.pokemonB
            else: 
                atacante = self.pokemonA

        return self.vencedor()

    def atacar(self,atacante):
        Dano = 0
        AD = 0
        Crit = 1.5
        Frc = 0.75
        if atacante == self.pokemonA:
            #AD = dano de ataque antes da defesa
            AD = self.pokemonA.ataque
            #ataque critico
            if self.pokemonB.fraqueza == self.pokemonA.tipo:
                AD = AD * Crit
                #ataque fraco
            elif self.pokemonA.tipo == self.pokemonB.resistencia:
                AD = AD * Frc

            Dano = max(1, AD - self.pokemonB.defesa)

            self.defender(self.pokemonB, Dano)

        
        AD = self.pokemonB.ataque
        if self.pokemonA.fraqueza == self.pokemonB.tipo:
            AD = AD * Crit
        elif self.pokemonB.tipo == self.pokemonA.resistencia:
            AD = AD * Frc

        Dano = max(1, AD - self.pokemonA.defesa)
            
        self.defender(self.pokemonA, Dano)

    def defender (self,pokemon, dano):
        if pokemon == self.pokemonA:
            self.vida_pokemonA -= dano

            if self.vida_pokemonA < 0:
                self.vida_pokemonA = 0

        elif pokemon == self.pokemonB:
            self.vida_pokemonB -= dano

            if self.vida_pokemonB < 0:
                self.vida_pokemonB = 0
            
    def nocauteado(self):
        if self.pokemonA.vida == 0:
            return self.pokemonA

        if self.pokemonB.vida == 0:
            return self.pokemonB

        return None

    def vencedor(self):
        derrotado = self.nocauteado()

        if derrotado == self.pokemonA:
            self.vencedor= self.pokemonB

        elif derrotado == self.pokemonB:
            self.vencedor - self.pokemonA

        return self.vencedor
