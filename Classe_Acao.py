class Acoes:

    def __init__(self, id, nome, tipo, categoria, dano, precisao, efeitos=None, bloqSeq=False):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.categoria = categoria
        self.dano = dano
        self.precisao = precisao

        self.efeitos = efeitos.copy() if efeitos is not None else []
        #atribuimos apenas a copia dos efeitos, para que o objeto original nao seja alterado, tambem pode ser None
        self.bloqSeq = bloqSeq

    def __str__(self):
        nomes_efeitos = [efeito.tipo for efeito in self.efeitos]

        return(
             f"Ação [ID: {self.id}, "
            f"Nome: {self.nome}, "
            f"Tipo: {self.tipo}, "
            f"Categoria: {self.categoria}, "
            f"Dano: {self.dano if self.dano is not None else 'ATQ do Pokémon'}, "
            f"Precisão: {self.precisao}%, "
            f"Efeitos: {', '.join(nomes_efeitos) if nomes_efeitos else 'Nenhum'}, "
            f"Bloqueia sequência: {self.bloqSeq}]"
        )

    def obterDanoBase(self, pokemon):
        if self.categoria == "BASICO":
            #se for um ataque tipo basico, retorna o atributo de ataque do pokemon, se nao, retorna o dano dele
            return pokemon.ataque
        else:
            return self.dano

        

    '''
    A classe Acoes representa os ataques disponíveis para os Pokémon. Ela armazena as características de cada ataque, mas não realiza o cálculo de dano nem modifica os Pokémon.
Minha proposta é manter essa classe simples, deixando a execução dos ataques para Combate e seus efeitos para Efeitos.
Atributos:

-id	int	Identificador único do ataque no catálogo.
-nome,str;Nome do ataque.
-tipo,str;Tipo do ataque: Água, Fogo, Grama, Lutador ou Elétrico.
-categoria,str;Básico, especial ou assinatura.
-dano,int ou None;Dano base do ataque.
-precisao,int;Probabilidade de acertar, de 0 a 100.
-efeito,Efeitos;Efeito associado ao ataque, quando existir.
-bloqueiaSequencia,bool;Indica se o ataque não pode ser usado em oportunidades consecutivas.

Métodos
__init__(...);Inicializa o ataque com suas características.
__str__();Retorna nome, categoria, dano, precisão e efeito.
obterDanoBase(pokemon);Retorna o dano fixo ou o atributo de ataque do Pokémon, conforme a categoria.

Exemplo de Acao:
hidro_bomba = Acoes(
    id=1,
    nome="Hidro Bomba",
    tipo="AGUA",
    categoria="ASSINATURA",
    dano=40,
    precisao=80

)
como nao tem efeitos nem bloqueio de sequencia, nao eh necessario coloca-los

cadeia_alimentar = Acoes(
    id=1,
    nome="Cadeia Alimentar",
    tipo="GRAMA",
    categoria="ESPECIAL",
    dano=30,
    precisao=80,
    efeitos=[dano_adicional, cura]
)
    '''
