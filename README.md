Exigências do professor:
Entidade → construtores e toString (__str__).
Cada classe filha → deve implementar seus comportamentos necessários e ter associação com outra classe filha de Entidade.
Duelo (transação) → precisa ter métodos para adicionar e remover objetos de Combate.
Duelo → também terá os métodos necessários para montar times/iniciar o duelo.
Combate → precisa ter seus métodos para realizar um combate.
EntidadeDAO → precisa implementar salvar, atualizar, apagar, buscar, carregar, persistir e recuperar.


COMPONENTES:

Relacionamentos:
Duelo ->Treinador
Duelo ->Pokémon
Duelo ->Combate

Resumo das Funções de cada Classe:
Pokemon -> dados do Pokemon.
Treinador -> dados do treinador.
Duelo -> criação do time, informacoes do duelo e seus Combates.
Combate -> execucao da luta.

Descrição de cada Classe:
1-Entidade:
Classe abstrata que serve como base para todas as entidades que serao 
armazenadas pelo sistema.
-Atributos:
  id

-Metodos:
  Construtor com e sem id
__str__()

2-Treinador
-Atributos:
  id(herdado)
  nome

-Metodos:
__init__(herdado)
__str__(herdado):
  Retorna as informacoes do treinador, como ID e nome

3-Pokemon:
-Atributos:
  id(herdado)
  nome
  fraqueza
  resistencia
  ataque
  defesa
  vida
  velocidade

-Metodos:
__init__(herdado)
__str__(herdado)


4 - Duelo

Atributos:

  id (herdado)
  treinador_a
  treinador_b
  time_a → 3 Pokémon
  time_b → 3 Pokémon
  combates → lista dos combates realizados
  vencedor

Métodos:

__init__(herdado)

__str__(herdado):
  Exibe as informações do duelo

  iniciar_duelo():
    Seleciona o primeiro Pokémon de cada time.
    Cria o primeiro Combate.
    Adiciona o Combate à lista de combates.
    Inicia o combate.
    Quando o combate termina, verifica qual Pokémon foi derrotado.
    Reorganiza o time do treinador que perdeu o Pokémon.
    Cria o próximo Combate.
    Repete até que um dos times fique sem Pokémon.
    Define o vencedor do duelo.

  times()
  Escolhe 6 pokemons e os coloca em 2 times. 
  Acessa o DAO de Pokémon e pesquisa por um id e verifica se o id existe

5 - Combate

Atributos:

  pokemon1
  pokemon2
  vida_pokemon1
  vida_pokemon2
  vencedor

Métodos:

__init__()

__str__():
  Exibe as informações do combate, incluindo os Pokémon, suas vidas e o vencedor.

duelar():
  Coordena a execução de um único combate:
  atacar() → defender() → nocauteado() → ...
  
  Repete o processo até que um dos Pokémon seja derrotado.

  atacar():
    Realiza um ataque entre os Pokémon.
    Calcula o dano utilizando ataque e defesa.
    Aplica o dano ao Pokémon adversário.

  defender(dano):
    Reduz a vida do Pokémon de acordo com o dano recebido.
    A vida nunca poderá ficar abaixo de zero.

  nocauteado():
    Verifica se um Pokémon chegou a 0 de vida.
    Indica qual Pokémon foi derrotado.

  vencedor():
    Verifica qual Pokémon venceu o combate.
    Define o vencedor do combate.
    Retorna o vencedor.
