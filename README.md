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


5.ESTRUTURA DAS CLASSES:
Entidade
│
├── Pokemon
├── Acao
└── Combate
       │
       └── CombateAcao

A classe Combate será responsável pela lógica da luta, enquanto CombateAcao apenas representará cada ação realizada durante essa luta.

6.EntidadeDAO
A classe EntidadeDAO será responsável pelo acesso e pela persistência das entidades.
Cada entidade deverá possuir um DAO próprio, evitando conflitos entre objetos de tipos diferentes.

