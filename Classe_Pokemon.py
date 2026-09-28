class Pokemon:

    def __init__(
        self, id, nome, tipo, fraqueza, resistencia,
        ataque, defesa, vidaMaxima, velocidade, ataques=None
    ):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.fraqueza = fraqueza
        self.resistencia = resistencia
        self.ataque = ataque
        self.defesa = defesa
        self.vidaMaxima = vidaMaxima
        self.velocidade = velocidade

        # Copia a lista, mantendo os objetos Acoes compartilhados.
        self.ataques = ataques.copy() if ataques is not None else []

    def __str__(self):
        nomes_ataques = [ataque.nome for ataque in self.ataques]

        return (
            f"Pokemon [ID: {self.id}, "
            f"Nome: {self.nome}, "
            f"Tipo: {self.tipo}, "
            f"Vida Máxima: {self.vidaMaxima}, "
            f"Ataque: {self.ataque}, "
            f"Defesa: {self.defesa}%, "
            f"Velocidade: {self.velocidade}, "
            f"Fraqueza: {self.fraqueza}, "
            f"Resistência: {self.resistencia}, "
            f"Ataques: {', '.join(nomes_ataques)}]"
        )

    def obterAtaque(self, nome):
        for ataque in self.ataques:
            if ataque.nome == nome:
                return ataque

        return None

    def listarAtaques(self):
        return self.ataques.copy()



'''
A classe Pokemon representará os dados originais de cada Pokémon. Ela não herdará de Entidade, pois os Pokémon serão predefinidos e não terão um cadastro próprio na interface.
Mesmo assim, cada Pokémon terá um id para ser identificado e selecionado pelo usuário.
Atributos:
-id,int:Identificador único do Pokémon no catálogo.
-nome,str:Nome do Pokémon.
-tipo,str:Água, Fogo, Grama, Lutador ou Elétrico.
-vidaMaxima, int:Quantidade de vida com que começa cada combate.
-ataque,int;Dano base do ataque básico.
-defesa,int	;Capacidade de reduzir o dano recebido.
-velocidade,int	;Determina a ordem de ataque.
-fraqueza,str;Tipo contra o qual recebe dano aumentado.
-resistencia,str;Tipo contra o qual recebe dano reduzido.
-ataques,list[Acoes];Seus três ataques predefinidos.


Método:
__init__(...)	Inicializa todos os atributos originais do Pokémon.
__str__()	Retorna seus dados para exibição.
obterAtaque(nome)	Busca um dos seus três ataques.
listarAtaques()	Retorna os três ataques disponíveis.
'''
