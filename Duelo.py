import Entidade.py
import Combate.py
import Pokemon.py

class Duelo(Entidade):
    def __init__(self, id, treinadorA, treinadorB):
        super().__init__(id)

        self.treinadorA = treinadorA
        self.treinadorB = treinadorB
        self.timeA = []
        self.timeB = []

        self.combates = []
        self.vencedor = None

    def __str__(self):
        return(
            f"Duelo [ID:{self.id},"
            f"{self.treinadorA.nome} x {self.treinadorB.nome},"
            f"Time A:{self.timeA[0].nome}, {self.timeA[1].nome}, {self.timeA[2].nome},"
            f"Time B:{self.timeB[0].nome}, {self.timeB[1].nome}, {self.timeB[2].nome},"
            f"Vencedor: {self.vencedor}]"
        )
    def iniciar(self):

        while len(self.timeA) > 0 and len(self.timeA) > 0:
            pokemonA = self.timeA[0]
            pokemonB = self.timeB[0]

            combate = Combate(pokemonA, pokemonB)

            self.combates.append(combate)

            vencedor_combate = combate.duelar()

            if vencedor_combate == pokemonA:
                self.timeB.pop(0)
            else:
                self.timeA.pop(0)

        if len(self.timeA) == 0:
            self.vencedor = self.treinadorB
        else:
            self.vencedor = self.treinadorA

            return self.vencedor

    def times(self):
        print(f"Escolha os Pokemons do {self.treinadorA.nome}:")

        for i in range(3):
            id_pokemon = int(input(f"{i+1}° Pokemon:"))
            #procura no banco de dados o id do pokemon
            pokemon  = DAO_pokemon.buscar(id_pokemon)

            while id_pokemon is None:
                print(f"O id: {id_pokemon} nao foi encontrado, digite outro")
                id_pokemon = int(input(f"{i+1}° Pokemon:"))
                pokemon  = DAO_pokemon.buscar(id_pokemon)

            self.timeA.append(pokemon)
        f"Escolha os Pokemons do(a) {self.treinadorB.nome}:"
        
        for i in range(3):
            id_pokemon = int(input(f"{i+1}° Pokemon:"))
            
            pokemon  = DAO_pokemon.buscar(id_pokemon)
            
            while id_pokemon is None:
                print(f"O id: {id_pokemon} nao foi encontrado, digite outro")
                id_pokemon = int(input(f"{i+1}° Pokemon:"))
                pokemon  = DAO_pokemon.buscar(id_pokemon)
        
            self.timeB.append(pokemon)
                
                
            
