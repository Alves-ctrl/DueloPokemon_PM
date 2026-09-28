
import random


class Efeitos:

    def __init__(self, tipo, valor, prob=100, cond=None,
                 duracao="IMEDIATO", alvo="ATACANTE", invertCond=False):
        self.tipo = tipo
        self.valor = valor
        self.prob = prob
        self.cond = cond
        self.duracao = duracao
        self.alvo = alvo
        self.invertCond = invertCond

    def __str__(self):
        return (
            f"Efeito [Tipo: {self.tipo}, "
            f"Valor: {self.valor}, "
            f"Probabilidade: {self.prob}%, "
            f"Condição: {self.cond}, "
            f"Condição invertida: {self.invertCond}, "
            f"Duração: {self.duracao}, "
            f"Alvo: {self.alvo}]"
        )

    def verificaProb(self):
        sorteio = random.randint(1, 100)
        return sorteio <= self.prob

    def verificaCond(self, contexto):
        atacante = contexto["atacante"]
        alvo = contexto["alvo"]

        if self.cond is None:
            resultado = True

        elif self.cond == "VIDA_ALTA":
            resultado = (
                atacante.vidaAtual > atacante.pokemon.vidaMaxima * 0.5
            )

        elif self.cond == "VIDA_BAIXA":
            resultado = (
                atacante.vidaAtual <= atacante.pokemon.vidaMaxima * 0.5
            )

        elif self.cond == "ALVO_LUTADOR":
            resultado = alvo.pokemon.tipo == "LUTADOR"

        elif self.cond == "INIMIGO_MAIS_RAPIDO":
            resultado = (
                alvo.pokemon.velocidade > atacante.pokemon.velocidade
            )

        elif self.cond == "ATACANTE_MAIS_RAPIDO":
            resultado = (
                atacante.pokemon.velocidade > alvo.pokemon.velocidade
            )

        elif self.cond == "VIDA_%_MENOR":
            resultado = (
                atacante.vidaAtual / atacante.pokemon.vidaMaxima
                < alvo.vidaAtual / alvo.pokemon.vidaMaxima
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
