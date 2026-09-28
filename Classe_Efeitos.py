import random

class Efeitos:

    def __init__(self,tipo, valor, prob= 100, cond=None, duracao="IMEDIATO", alvo="ATACANTE", invertCond = False):
        self.tipo = tipo
        self.valor = valor
        self.prob = prob
        self.cond = cond
        self.duracao = duracao
        self.alvo = alvo
        self.invertCond = invertCond
        #este atributo diz se o return de verificaCond deve ser invertido ou nao, para poupar linhas de codigo

    def __str__(self):
        return (
            f"Efeito [Tipo: {self.tipo}, "
            f"Valor: {self.valor}, "
            f"Probabilidade: {self.probab}%, "
            f"Condição: {self.cond}, "
            f"Duração: {self.duracao}, "
            f"Alvo: {self.alvo}]"
        )

    def verificaProb(self):
        return random.randint(1, 100) <= self.prob
        
    def verificaCond(self, contexto):
        atacante = contexto["atacante"]
        alvo = contexto["alvo"]
        #contexto guarda o estado atual dos dois pokemons que estao lutando, o atacante e o alvo. 
        #O estado atual contem todas as informacoes dos pokemon, sao obejtos da classe ESTADO_POKEMON
        if self.cond is None:
            result = True
            
 
        elif self.cond == "VIDA_ALTA":
            #verifica se a vida o pokemon atacante eh maior que a metade
            resultado = (
                atacante.vidaAtual > atacante.pokemon.vidaMax * 0.5
            )

        elif self.cond == "ALVO_LUTADOR":
            #verifica se o tipo do pokemon defensor eh lutador
            resultado = alvo.pokemon.tipo == "LUTADOR"

        elif self.cond == "INIMIGO_MAIS_RAPIDO":
            resultado =(
                alvo.pokemon.velocidade > atacante.pokemon.velocidade
            )

        elif self.cond == "ATACANTE_MAIS_RAPIDO":
            resultado =(
                atacante.pokemon.velocidade > alvo.pokemon.velocidade
            )

        elif self.cond == "VIDA_%_MENOR":
            resultado =(
                atacante.vidaAtual/atacante.pokemon.vidaMax < alvo.vidaAtual/alvo.pokemon.vidaMax
            )

        else: 
            raise ValueError(
                f"Condicao Desconhecida: {self.cond}"
            )
        else:
            raise ValueError(f"Condição desconhecida: {self.cond}")

        return not resultado if self.invertCond else resultado

        




''' 
Atributos 

-tipo,str;Identifica o efeito: cura, atordoamento, bônus de dano, redução de precisão etc.
-valor,float;Intensidade do efeito, como 25% ou 15 pontos de vida.
-probabilidade,int;Chance de ativação após o ataque acertar.
-condicao,str ou None;Condição necessária para ativar o efeito.
-duracao,str;Determina quando o efeito termina ou é consumido.
-alvo,str;Indica se o efeito é aplicado ao atacante ou ao adversário.

Esses atributos descrevem as regras fixas do efeito. Os dados temporários, como a quantidade de rodadas restantes, serão armazenados no estado do 
Pokémon durante o combate.

Métodos 

__init__(...);Inicializa a configuração do efeito.
__str__();Retorna uma descrição do efeito.
verificarCondicao(contexto);Verifica se as condições necessárias foram atendidas.
verificarProbabilidade();Sorteia a ativação do efeito, quando necessário.

exemplos:

dano_adicional = Efeitos(
    tipo="DANO_ADICIONAL",
    valor=10,
    cond="ALVO_LUTADOR",
    invertCond=False,
    alvo="ALVO"
)

cura = Efeitos(
    tipo="CURA",
    valor=15,
    cond="ALVO_LUTADOR",
    invertCond=True,
    alvo="ATACANTE"
)
'''
