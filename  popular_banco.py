
from DAO_pokemon import DAO_pokemon
from Pokemon import Pokemon


DAO_pokemon.criar_tabela()


pokemons = [

    Pokemon(
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

    Pokemon(
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

    Pokemon(
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

    Pokemon(
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

    Pokemon(
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

    Pokemon(
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
]


for pokemon in pokemons:

    if DAO_pokemon.buscar(pokemon.id) is None:
        DAO_pokemon.inserir(pokemon)


print("Banco de dados criado e populado!")

