class EstadoPokemon:
    def __init__(self,pokemon):
        self.pokemon = pokemon
        self.vidaAtual = pokemon.vidaMax
        self.defesaAtual = float(pokemon.defesa)

        self.ultimoAtk= None
        self.ultimoAtkTentado = None

        self.efeitosAtivos = []

    def __str__(self):
        nomes_efeitos = [r["efeito"].tipo for r in self.efeitosAtivos]

        return(
            f"EstadoPokemon [Nome: {self.pokemon.nome}, "
            f"Vida: {self.vidaAtual}/{self.pokemon.vidaMax}, "
            f"Defesa: {self.defesaAtual}%, "
            f"Efeitos: {', '.join(nomes_efeitos) if nomes_efeitos else 'Nenhum'}]"
            #a funcao join juntar os elementos de uma lista em uma única string, separando-os por vírgula e espaço
        )

    def recebeDano(self, dano):
        if dano < 0:
            return False
        self.vidaAtual = max(0, self.vidaAtual - dano)
        #pega o menor valor entre zero e o dano, pois o dano nao pode ser menor que zero
        return True

    def recuperarVida(self,valor):
        if valor < 0:
            return False

       self.vidaAtual = min(self.pokemon.vidaMax, self.vidaAtual + valor)
    #pega o menor valor entre vida maxima e vida atual, pois a cura nao pode utrapassar a vida maxima
        return True

    def derrotado(self):
        return self.vidaAtual <= 0

    def atordoado(self):
        return self.buscarEfeito("ATORDOAMENTO") is not None
        #verifica se o pokemon esta com o efeito atordoamento ativo

    def addEfeito(self, efeito):
        if efeito is None:
            #verifica se existe efeito
            return False

        registro = self.buscarEfeito(efeito.tipo)

        if registro is not None:
            #verifica se o efeito ja esta ativo e o atualiza
            registro["efeito"] = efeito
            #adicionar que a duracao do efeito eh renovada
            return True

    #adiciona em efeitosAtivos o efeito e sua duracao
        self.efeitosAtivos.append({
            "efeito": efeito,
            "restante": None
        })

        return True

    def removerEfeito(self,tipo):
        registro = self.buscarEfeito(tipo)

        if registro is None:
            return False

        self.efeitosAtivos.remove(registro)
        return True

    def buscarEfeito(self, tipo):
        for registro in self.efeitosAtivos:
            if registro["efeito"].tipo == tipo:
                return registro
        return None

    def salvarEstado(self):
        return {
            "vidaAtual": self.vidaAtual,
            "defesaAtual": self.defesaAtual,
            "ultimoAtaque": self.ultimoAtk,
            "ultimoAtaqueTentado": self.ultimoAtkTentado,
            "efeitosAtivos": [
                registro.copy()
                for registro in self.efeitosAtivos
            ]
        }

    def restaurarEstado(self, estado):
        self.vidaAtual = estado["vidaAtual"]
        self.defesaAtual = estado["defesaAtual"]

        self.ultimoAtaque = estado["ultimoAtaque"]
        self.ultimoAtaqueTentado = estado["ultimoAtaqueTentado"]

        self.efeitosAtivos = [
            registro.copy()
            for registro in estado["efeitosAtivos"]
        ]
'''

Surge para diminuir a quantidade de codigo dentro de combate
Atributos;
pokemon	Pokemon	Referência ao Pokémon original.
vidaAtual	int	Vida restante durante o combate.
defesaAtual	float	Defesa percentual atual.
ultimoAtaque	Acoes \| None	Último ataque que acertou.
ultimoAtaqueTentado	Acoes \| None	Último ataque que o Pokémon tentou utilizar.
efeitosAtivos	list[dict]	Registros dos efeitos temporários ativos.
 Métodos;
__init__(pokemon)	;Inicializa os atributos temporários a partir do Pokémon original.
__str__()	;Retorna o nome, a vida atual e os efeitos ativos.
receberDano(dano)	;Reduz a vida atual, sem permitir valores negativos.
recuperarVida(valor)	;Recupera vida sem ultrapassar a vida máxima.
estaDerrotado()	;Retorna True se a vida atual for zero.
adicionarEfeito(efeito)	;Adiciona ou renova um efeito temporário.
removerEfeito(tipo)	;Remove um efeito ativo.
buscarEfeito(tipo)	;Busca um efeito ativo pelo seu tipo.
restaurarEstado(estado)	;Restaura os atributos temporários a partir de um estado salvo.
'''
