from Pokemon import Pokemon


class DAO_pokemon:

    _banco_dados = {

        1: Pokemon(
            id=1,
            nome="Pikachu",
            tipo="Elétrico",
            fraqueza="Terrestre",
            resistencia="Elétrico",
            ataque=30,
            defesa=20,
            vida=100,
            velocidade=90
        ),

        2: Pokemon(
            id=2,
            nome="Charmander",
            tipo="Fogo",
            fraqueza="Água",
            resistencia="Fogo",
            ataque=28,
            defesa=18,
            vida=100,
            velocidade=80
        ),

        3: Pokemon(
            id=3,
            nome="Bulbasaur",
            tipo="Planta",
            fraqueza="Fogo",
            resistencia="Planta",
            ataque=25,
            defesa=22,
            vida=110,
            velocidade=60
        ),

        4: Pokemon(
            id=4,
            nome="Squirtle",
            tipo="Água",
            fraqueza="Elétrico",
            resistencia="Água",
            ataque=26,
            defesa=25,
            vida=105,
            velocidade=50
        ),

        5: Pokemon(
            id=5,
            nome="Pidgey",
            tipo="Normal",
            fraqueza="Elétrico",
            resistencia="Planta",
            ataque=20,
            defesa=15,
            vida=80,
            velocidade=75
        ),

        6: Pokemon(
            id=6,
            nome="Gengar",
            tipo="Fantasma",
            fraqueza="Fantasma",
            resistencia="Veneno",
            ataque=35,
            defesa=18,
            vida=90,
            velocidade=95
        )
    }

    @classmethod
    def buscar(cls, id_pokemon: int):
        #Busca e retorna o Pokemon correspondente ao ID .
        return cls._banco_dados.get(id_pokemon, None)

    @classmethod
    def listar_todos(cls):
        #Retorna a lista de todos os Pokemons cadastrados.
        return list(cls._banco_dados.values())

    @classmethod
    def inserir(cls, pokemon: Pokemon):
        #Adiciona um novo Pokemon ao banco de dados.
        cls._banco_dados[pokemon.id] = pokemon