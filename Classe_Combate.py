from Classe_Entidade import Entidade
from DAO_pokemon import DAO_pokemon
from Classe_CombateAcao import CombateAcao


class Combate(Entidade):

    def __init__(self, id):

        super().__init__(id)

        self.vidas = {}
        self.movimentos = []
        self.vencedor = None

        self.timeA = []
        self.timeB = []

        self.pokemonA = None
        self.pokemonB = None

    def __str__(self):

        if self.pokemonA is None or self.pokemonB is None:

            return (
                f"Combate [ID: {self.id}, "
                f"Combate ainda não iniciado, "
                f"Vencedor: {self.vencedor}]"
            )

        return (
            f"Combate [ID: {self.id}, "
            f"{self.pokemonA.nome} x {self.pokemonB.nome}, "
            f"Vida {self.pokemonA.nome}: "
            f"{self.vidas[self.pokemonA]}, "
            f"Vida {self.pokemonB.nome}: "
            f"{self.vidas[self.pokemonB]}, "
            f"Vencedor: {self.vencedor}]"
        )


    def addAcao(self, acao):
        self.movimentos.append(acao)

    def delAcao(self, acao):

        if acao in self.movimentos:
            self.movimentos.remove(acao)
            return True

        return False

    def buscarAcao(self, indice):

        if 0 <= indice < len(self.movimentos):
            return self.movimentos[indice]

        return None

    def alterarAcao(self, movimento, indice):

        if 0 <= indice < len(self.movimentos):

            self.movimentos[indice] = movimento

            return True

        return False

    def mostrarAcao(self):
        return self.movimentos


    def draft(self):

        print("\nEscolha os 3 Pokémons do Time A:")

        for i in range(3):

            id_pokemon = int(
                input(f"{i + 1}º Pokémon: ")
            )

            pokemon = DAO_pokemon.buscar(id_pokemon)

            while pokemon is None:

                print(
                    f"O ID {id_pokemon} não foi encontrado."
                )

                id_pokemon = int(
                    input(f"{i + 1}º Pokémon: ")
                )

                pokemon = DAO_pokemon.buscar(id_pokemon)

            self.timeA.append(pokemon)
            self.vidas[pokemon] = pokemon.vida

        print("\nEscolha os 3 Pokémons do Time B:")

        for i in range(3):

            id_pokemon = int(
                input(f"{i + 1}º Pokémon: ")
            )

            pokemon = DAO_pokemon.buscar(id_pokemon)

            while pokemon is None:

                print(
                    f"O ID {id_pokemon} não foi encontrado."
                )

                id_pokemon = int(
                    input(f"{i + 1}º Pokémon: ")
                )

                pokemon = DAO_pokemon.buscar(id_pokemon)

            self.timeB.append(pokemon)
            self.vidas[pokemon] = pokemon.vida


    def duelar(self):

        self.draft()

        while len(self.timeA) > 0 and len(self.timeB) > 0:

            self.pokemonA = self.timeA[0]
            self.pokemonB = self.timeB[0]

            vencedor = self.dueloPokemon(
                self.pokemonA,
                self.pokemonB
            )

            if vencedor == self.pokemonA:

                self.timeB.pop(0)

            else:

                self.timeA.pop(0)

        if len(self.timeA) == 0:

            self.vencedor = "Time B"

        else:

            self.vencedor = "Time A"

        return self.vencedor


    def dueloPokemon(self, pokemonA, pokemonB):

        if pokemonA.velocidade > pokemonB.velocidade:

            atacante = pokemonA
            defensor = pokemonB

        else:

            atacante = pokemonB
            defensor = pokemonA

        while self.nocauteado() is None:

            self.atacar(
                atacante,
                defensor
            )

            if self.nocauteado() is not None:
                break

            atacante, defensor = defensor, atacante

        return self.winner()


    def atacar(self, atacante, defensor):

        crit = 1.5
        fraco = 0.75

        AD = atacante.ataque

        if atacante.tipo == defensor.fraqueza:

            AD = AD * crit

        elif atacante.tipo == defensor.resistencia:

            AD = AD * fraco

        dano = AD - defensor.defesa

        if dano < 0:
            dano = 0

        acao = CombateAcao(
            len(self.movimentos) + 1,
            atacante,
            None,
            dano
        )

        self.addAcao(acao)

        self.defender(
            defensor,
            dano
        )


    def defender(self, defensor, dano):

        self.vidas[defensor] -= dano

        if self.vidas[defensor] < 0:

            self.vidas[defensor] = 0



    def nocauteado(self):

        if self.pokemonA is not None:

            if self.vidas[self.pokemonA] == 0:
                return self.pokemonA

        if self.pokemonB is not None:

            if self.vidas[self.pokemonB] == 0:
                return self.pokemonB

        return None



    def winner(self):

        derrotado = self.nocauteado()

        if derrotado == self.pokemonA:

            self.vencedor = self.pokemonB

        elif derrotado == self.pokemonB:

            self.vencedor = self.pokemonA

        return self.vencedor