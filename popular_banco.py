from DAO_Entidade import EntidadeDAO
from Classe_Pokemon import Pokemon
from Classe_Acao import Acao


dao_pokemon = EntidadeDAO.get_instancia(Pokemon)
dao_acao = EntidadeDAO.get_instancia(Acao)
dao_pokemon.recuperar()
dao_acao.recuperar()


#Ações (criadas primeiro, para serem usadas pelos Pokémon)

ataque_basico_eletrico = Acao(id=1, nome="Choque", tipo="Elétrico", categoria="BASICO", dano=None, precisao=100)
choque_trovao = Acao(id=2, nome="Choque do Trovão", tipo="Elétrico", categoria="ESPECIAL", dano=40, precisao=90)

ataque_basico_fogo = Acao(id=3, nome="Arranhão", tipo="Fogo", categoria="BASICO", dano=None, precisao=100)
lancachamas = Acao(id=4, nome="Lança-Chamas", tipo="Fogo", categoria="ESPECIAL", dano=38, precisao=90)

ataque_basico_planta = Acao(id=5, nome="Chicote", tipo="Planta", categoria="BASICO", dano=None, precisao=100)
folha_navalha = Acao(id=6, nome="Folha Navalha", tipo="Planta", categoria="ESPECIAL", dano=35, precisao=95)

ataque_basico_agua = Acao(id=7, nome="Investida", tipo="Água", categoria="BASICO", dano=None, precisao=100)
hidro_bomba = Acao(id=8, nome="Hidro Bomba", tipo="Água", categoria="ASSINATURA", dano=40, precisao=80)

ataque_basico_normal = Acao(id=9, nome="Investida", tipo="Normal", categoria="BASICO", dano=None, precisao=100)
bico_ferino = Acao(id=10, nome="Bico Ferino", tipo="Normal", categoria="ESPECIAL", dano=30, precisao=95)

ataque_basico_fantasma = Acao(id=11, nome="Lambida", tipo="Fantasma", categoria="BASICO", dano=None, precisao=100)
sombra_negra = Acao(id=12, nome="Sombra Negra", tipo="Fantasma", categoria="ASSINATURA", dano=45, precisao=75)

acoes = [
    ataque_basico_eletrico, choque_trovao,
    ataque_basico_fogo, lancachamas,
    ataque_basico_planta, folha_navalha,
    ataque_basico_agua, hidro_bomba,
    ataque_basico_normal, bico_ferino,
    ataque_basico_fantasma, sombra_negra,
]

for a in acoes:
    dao_acao.salvar(a)

pokemons = [

    Pokemon(
        id=1,
        nome="Pikachu",
        tipo="Elétrico",
        fraqueza="Terrestre",
        resistencia="Elétrico",
        ataque=30,
        defesa=20,
        vidaMaxima=100,
        velocidade=90,
        ataques=[ataque_basico_eletrico, choque_trovao]
    ),

    Pokemon(
        id=2,
        nome="Charmander",
        tipo="Fogo",
        fraqueza="Água",
        resistencia="Fogo",
        ataque=28,
        defesa=18,
        vidaMaxima=100,
        velocidade=80,
        ataques=[ataque_basico_fogo, lancachamas]
    ),

    Pokemon(
        id=3,
        nome="Bulbasaur",
        tipo="Planta",
        fraqueza="Fogo",
        resistencia="Planta",
        ataque=25,
        defesa=22,
        vidaMaxima=110,
        velocidade=60,
        ataques=[ataque_basico_planta, folha_navalha]
    ),

    Pokemon(
        id=4,
        nome="Squirtle",
        tipo="Água",
        fraqueza="Elétrico",
        resistencia="Água",
        ataque=26,
        defesa=25,
        vidaMaxima=105,
        velocidade=50,
        ataques=[ataque_basico_agua, hidro_bomba]
    ),

    Pokemon(
        id=5,
        nome="Pidgey",
        tipo="Normal",
        fraqueza="Elétrico",
        resistencia="Planta",
        ataque=20,
        defesa=15,
        vidaMaxima=80,
        velocidade=75,
        ataques=[ataque_basico_normal, bico_ferino]
    ),

    Pokemon(
        id=6,
        nome="Gengar",
        tipo="Fantasma",
        fraqueza="Fantasma",
        resistencia="Veneno",
        ataque=35,
        defesa=18,
        vidaMaxima=90,
        velocidade=95,
        ataques=[ataque_basico_fantasma, sombra_negra]
    )
]

for p in pokemons:
    dao_pokemon.salvar(p)

dao_acao.persistir()
dao_pokemon.persistir()
print(f"Banco de dados populado com {len(dao_pokemon.carregar())} Pokemon(s)!")
