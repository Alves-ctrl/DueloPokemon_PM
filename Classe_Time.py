from Classe_Entidade import Entidade


class Time(Entidade):

    def __init__(self, id=None, nome="", treinador=None):
        super().__init__(id)
        self.nome = nome
        self.treinador = treinador
        self.pokemons = []

    def __str__(self):
        nomes = [pokemon.nome for pokemon in self.pokemons]

        return (
            f"Time [{super().__str__()}, "
            f"Nome: {self.nome}, "
            f"Treinador: {self.treinador.nome if self.treinador else 'Nenhum'}, "
            f"Pokémons: {', '.join(nomes)}]"
        )

    def addPokemon(self, pokemon):
        if pokemon is None:
            return False

        if len(self.pokemons) >= 3:
            return False

        if self.buscarPokemon(pokemon.id) is not None:
            return False

        self.pokemons.append(pokemon)
        return True

    def removerPokemon(self, id_pokemon):
        pokemon = self.buscarPokemon(id_pokemon)

        if pokemon is None:
            return False

        self.pokemons.remove(pokemon)
        return True

    def alterarOrdem(self, id_pokemon, nova_posicao):
        pokemon = self.buscarPokemon(id_pokemon)

        if pokemon is None:
            return False

        # As posições começam em 1.
        if type(nova_posicao) is not int:
            return False

        if nova_posicao < 1 or nova_posicao > len(self.pokemons):
            return False

        self.pokemons.remove(pokemon)
        self.pokemons.insert(nova_posicao - 1, pokemon)
        return True

    def buscarPokemon(self, id_pokemon):
        for pokemon in self.pokemons:
            if pokemon.id == id_pokemon:
                return pokemon

        return None

    def listarPokemons(self):
        return self.pokemons.copy()

    def estaCompleto(self):
        return len(self.pokemons) == 3











'''
A classe Time será responsável por organizar os Pokémon selecionados pelo treinador. Ela controla quais Pokémon pertencem ao time e a ordem em que entrarão no combate.
O Time não controla a vida dos Pokémon, não executa ataques e não determina o vencedor. Essas responsabilidades continuam com Combate.

regras fundamentais: um time pode conter no máximo três Pokémon, sem repetições, e só poderá ser cadastrado quando estiver completo, com exatamente três Pokémon.
Atributos:

-id,int	
Identificador herdado de Entidade.
-nome,str	
Nome escolhido para o time.
-treinador,Treinador	
Treinador ao qual o time pertence.
-pokemons,list[Pokemon]	
Pokémon selecionados, na ordem em que entrarão na batalha.

Métodos:

__init__(id=None, nome="", treinador=None): Inicializa o time com uma lista vazia de Pokémon.
__str__():Retorna as informações do time e de seus integrantes.
adicionarPokemon(pokemon):	Adiciona um Pokémon ao final do time, respeitando o limite de três.
removerPokemon(id_pokemon):	Remove um Pokémon do time pelo ID.
alterarOrdem(id_pokemon, nova_posicao):	Altera a posição de um Pokémon no time.
buscarPokemon(id_pokemon):	Retorna um Pokémon do time pelo ID.
listarPokemons():	Retorna os Pokémon na ordem em que estão organizados.

O construtor e o __str__() utilizarão super(), como fizemos na classe Treinador.

'''
