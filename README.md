1-EXIGENCIAS DO PROFESSOR

Entidade deve possuir construtores com e sem id e o método __str__().
Cada classe filha de Entidade deve possuir associação com outra classe filha de Entidade.
Deve existir uma classe de transação com uma quantidade indefinida de objetos intermediários.
A transação deve possuir métodos para:

adicionar objetos intermediários;
remover objetos intermediários;
alterar objetos intermediários;
buscar objetos intermediários;
carregar objetos intermediários.

Os objetos intermediários devem ser armazenados junto com a transação.
EntidadeDAO deve implementar:

salvar();
atualizar();
apagar();
buscar();
carregar();
persistir();
recuperar().

2-COMPONENTES DO PROJETO:
Entidades
Pokemon
Acao
Combate
CombateAcao


3-RELACIONAMENTOS:
Pokemon ─────── Acao
   │              │
   └── CombateAcao┘
          │
          ▼
       Combate

4-RESUMO DAS CLASSES:

Entidade:	Classe abstrata base para as entidades armazenadas
Pokemon	:Armazenar os dados de um Pokémon
Acao:	Representar as ações disponíveis, como ataques e defesas
Combate:	Controlar a execução de uma luta e armazenar suas ações
CombateAcao:	Registrar uma ação específica realizada durante um combate
EntidadeDAO:	Armazenar, consultar, alterar, excluir e persistir entidades

5-DESCRIÇÃO DAS CLASSES:
5.1. Entidade
Classe abstrata que serve como base para todas as entidades que serão armazenadas pelo sistema.

-Atributos:
id
-Métodos:
__init__() — construtor sem id;
__init__(id) — construtor com id;
__str__() — retorna a representação textual da entidade.

5.2. Pokemon
Representa um Pokémon e armazena suas características básicas.

-Atributos:
id — herdado de Entidade;
nome;
fraqueza;
resistencia;
ataque;
defesa;
vida;
velocidade.

-Métodos:
__init__() — inicializa os atributos do Pokémon;
__str__() — retorna informações do Pokémon, como seu ID, nome, ataque, defesa e vida.


Pikachu
 ├── Choque do Trovão
 ├── Investida
 └── Defesa Elétrica

5.3. Acao
Representa uma ação que pode ser realizada por um Pokémon. Uma ação pode ser um ataque ou uma defesa.

-Atributos:
id — herdado de Entidade;
nome;
tipo — identifica se a ação é um ataque ou uma defesa;

-Métodos:
__init__() — inicializa os atributos da ação;
__str__() — retorna as informações da ação.


5.4. Combate
Combate é a classe de transação do projeto. Representa uma luta específica entre dois Pokémon e possui uma quantidade indefinida de objetos CombateAcao.

-Atributos:
id — herdado de Entidade;
pokemon_a;
pokemon_b;
vida_pokemon_a;
vida_pokemon_b;
combate_acoes — lista de ações realizadas durante o combate;
vencedor.

-Métodos:
__init__()
__str__()

adicionar_acao(combate_acao):Adiciona uma nova CombateAcao à lista de ações do combate.

remover_acao(combate_acao):Remove uma CombateAcao da lista de ações do combate.

alterar_acao(combate_acao):Altera os dados de uma ação já registrada no combate, quando necessário.

buscar_acao(...):Busca uma ação específica entre as ações registradas no combate.

carregar_acoes():Retorna as ações registradas no combate.

atacar():Realiza um ataque entre os Pokémon.Calcula o dano utilizando os atributos de ataque e defesa e registra a ação realizada por meio de uma CombateAcao.

defender(dano):Reduz a vida do Pokémon de acordo com o dano recebido.A vida nunca poderá ficar abaixo de zero.

nocauteado():Verifica se algum Pokémon chegou a zero de vida.

vencedor():Verifica qual Pokémon venceu o combate, define o vencedor e retorna esse Pokémon.

duelar():Coordena a execução de uma luta:

atacar()
   ↓
defender()
   ↓
nocauteado()
   ↓
atacar()
   ↓
defender()
   ↓
...


5.5 CombateAcao
É a classe intermediária entre Combate, Pokemon e Acao.Representa uma ação específica realizada por um Pokémon em um combate.

Por exemplo:
Pikachu utilizou Choque do Trovão com intensidade 80 durante o Combate 1.

-Atributos:
pokemon — Pokémon que realizou a ação;
acao — ação utilizada;

-Métodos:
__init__() — inicializa os dados da ação realizada;
__str__() — retorna as informações da ação realizada.

6.ESTRUTURA DAS CLASSES:
Entidade
│
├── Pokemon
├── Acao
└── Combate
       │
       └── CombateAcao

A classe Combate será responsável pela lógica da luta, enquanto CombateAcao apenas representará cada ação realizada durante essa luta.

7.EntidadeDAO
A classe EntidadeDAO será responsável pelo acesso e pela persistência das entidades.
Cada entidade deverá possuir um DAO próprio, evitando conflitos entre objetos de tipos diferentes.

