from Entidade import Entidade


class Combate(Entidade):

    def __init__(self, pokemonA, pokemonB):

        self.pokemonA = pokemonA
        self.pokemonB = pokemonB


        self.vida_pokemonA = pokemonA.vida
        self.vida_pokemonB = pokemonB.vida


        self.pokemon_vencedor = None

    def __str__(self):

        return (
            f"Combate: {self.pokemonA.nome} x {self.pokemonB.nome}\n"
            f"Vencedor: {self.pokemon_vencedor}"
        )

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

    def atacar(self, atacante):

        Crit = 1.5
        Frc = 0.75

 
        if atacante == self.pokemonA:

            AD = self.pokemonA.ataque


            if self.pokemonB.fraqueza == self.pokemonA.tipo:
                AD = AD * Crit

  
            elif self.pokemonA.tipo == self.pokemonB.resistencia:
                AD = AD * Frc

            dano = max(1, AD - self.pokemonB.defesa)

            self.defender(self.pokemonB, dano)

            print(
                f"{self.pokemonA.nome} atacou "
                f"{self.pokemonB.nome} causando {dano} de dano."
            )

    
        else:

            AD = self.pokemonB.ataque


            if self.pokemonA.fraqueza == self.pokemonB.tipo:
                AD = AD * Crit


            elif self.pokemonB.tipo == self.pokemonA.resistencia:
                AD = AD * Frc

            dano = max(1, AD - self.pokemonA.defesa)

            self.defender(self.pokemonA, dano)

            print(
                f"{self.pokemonB.nome} atacou "
                f"{self.pokemonA.nome} causando {dano} de dano."
            )

    def defender(self, pokemon, dano):

        if pokemon == self.pokemonA:

            self.vida_pokemonA -= dano

            if self.vida_pokemonA < 0:
                self.vida_pokemonA = 0

        elif pokemon == self.pokemonB:

            self.vida_pokemonB -= dano

            if self.vida_pokemonB < 0:
                self.vida_pokemonB = 0

    def nocauteado(self):

        if self.vida_pokemonA == 0:
            return self.pokemonA

        if self.vida_pokemonB == 0:
            return self.pokemonB

        return None

    def vencedor(self):

        derrotado = self.nocauteado()

        if derrotado == self.pokemonA:

            self.pokemon_vencedor = self.pokemonB

        elif derrotado == self.pokemonB:

            self.pokemon_vencedor = self.pokemonA

        return self.pokemon_vencedor