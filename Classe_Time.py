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
            #a funcao join juntar os elementos de uma lista em uma única string, separando-os por vírgula e espaço.
        )
    
    def addPokemon(self, pokemon):
        if pokemon is None:
            #se o pokemon nao existir
            return False
       
        if len(self.pokemons)>3:
            print(" O time ja esta completo")
            #se ja existir 3 pokemons no time
            return False
        
        if self.buscarPokemon(pokemon.id) is not None:
            #se o pokemon ja existir no time
            return False

        self.pokemons.append(pokemon)

    def removePokemon(self, id_pokemon):
        pokemon = self.buscarPokemon(id_pokemon)

        if pokemon is None:
            #se o pokemon nao existir
            return False

        self.pokemons.remove(pokemon)
        return True

    def editarOrdem(self, id_pokemon, nova_posicao):
        pokemon = self.buscarPokemon(id_pokemon)

        if pokemon is None:
            return False

        if nova_posicao < 1 and nova_posicao >len(self.pokemon):
            #se for menor q 1 ou maior q o tamanho do time
            return False

        self.pokemon.remove(pokemon)
        #remove o pokemon
        self.pokemon.insert(nova_posicao - 1, pokemon)
        #coloca na posicao deseja, e empura os outros pokemons em 1 posição.
        # A funcao insert insere um elemento na posição indicada, deslocando os demais elementos para a direita.

        return True

    def buscarPokemon(self, id_pokemon):
        for pokemon in self.pokemons:
            #porcura dentro do time um pokemon com o mesmo id e o retorna
            if pokemon.id == id_pokemon:
                return pokemon
        return None

    def listPokemons(self):
        return self.pokemons.copy()

    def estaCompleto(self):
        #retorne True se o tamanho do time eh 3
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