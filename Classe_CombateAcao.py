class CombateAcao:
    """Registra uma ação executada durante um combate."""

    def __init__(self, id, rodada, atacante, alvo, ataque,
                 acertou=False, danoCausado=0,
                 efeitosAplicados=None, estadoAnterior=None):

        self.id = id
        self.rodada = rodada
        self.atacante = atacante
        self.alvo = alvo
        self.ataque = ataque
        self.acertou = acertou
        self.danoCausado = danoCausado

        # Copia a lista e os registros para preservar o histórico.
        self.efeitosAplicados = [
            registro.copy() if isinstance(registro, dict) else registro
            for registro in (
                efeitosAplicados if efeitosAplicados is not None else []
            )
        ]

        # Estado do combate antes da execução da ação.
        self.estadoAnterior = estadoAnterior

    def __str__(self):
        return self.obterResumo()

    def obterResumo(self):

        if self.ataque is None:
            return (
                f"Rodada {self.rodada}: "
                f"{self.atacante.pokemon.nome} estava atordoado "
                f"e perdeu seu turno."
            )

        if not self.acertou:
            return (
                f"Rodada {self.rodada}: "
                f"{self.atacante.pokemon.nome} usou "
                f"{self.ataque.nome}, mas errou!"
            )

        resumo = (
            f"Rodada {self.rodada}: "
            f"{self.atacante.pokemon.nome} usou "
            f"{self.ataque.nome} em "
            f"{self.alvo.pokemon.nome} e causou "
            f"{self.danoCausado} de dano."
        )

        if self.efeitosAplicados:
            nomes = ", ".join(
                registro["tipo"]
                if isinstance(registro, dict)
                else str(registro)
                for registro in self.efeitosAplicados
            )

            resumo += f" Efeitos ativados: {nomes}."

        return resumo
    '''
Atributos

-id,int	;Identificador da ação dentro do combate.
-rodada,int;Rodada em que a ação ocorreu.
-atacante,Pokemon;Pokémon que executou o ataque.
-alvo,Pokemon;Pokémon que recebeu o ataque.
-ataque,Acoes;Ataque escolhido.
-acertou,bool;Indica se o ataque acertou.
-danoCausado,int;Dano total efetivamente causado.
-efeitosAplicados,list;Efeitos que foram ativados.
-estadoAnterior,dict;Estado do combate antes da execução da ação.

Métodos 
__init__(...);Inicializa o registro da ação.
__str__();Retorna uma descrição do que aconteceu.
obterResumo();Retorna um resumo da ação para o histórico.
    '''
