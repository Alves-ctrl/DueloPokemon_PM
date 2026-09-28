class EstadoPokemon:

    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.vidaAtual = pokemon.vidaMaxima
        self.defesaAtual = float(pokemon.defesa)

        # Histórico utilizado para validar ataques consecutivos.
        self.ultimoAtaque = None
        self.ultimoAtaqueTentado = None
        self.ultimoAtaqueTentadoAcertou = False

        # Registros dos efeitos temporários.
        self.efeitosAtivos = []

    def __str__(self):
        nomes_efeitos = []

        for registro in self.efeitosAtivos:
            nomes_efeitos.append(registro["efeito"].tipo)

        return (
            f"EstadoPokemon [Nome: {self.pokemon.nome}, "
            f"Vida: {self.vidaAtual}/{self.pokemon.vidaMaxima}, "
            f"Defesa: {self.defesaAtual}%, "
            f"Efeitos: {', '.join(nomes_efeitos) if nomes_efeitos else 'Nenhum'}]"
        )

    def receberDano(self, dano):
        if dano < 0:
            return False

        self.vidaAtual = max(0, self.vidaAtual - dano)
        return True

    def recuperarVida(self, valor):
        if valor < 0:
            return False

        self.vidaAtual = min(
            self.pokemon.vidaMaxima,
            self.vidaAtual + valor
        )
        return True

    def estaDerrotado(self):
        return self.vidaAtual <= 0

    def estaAtordoado(self):
        return self.buscarEfeito("ATORDOAMENTO") is not None

    def adicionarEfeito(self, efeito):
        if efeito is None:
            return False

        registro = self.buscarEfeito(efeito.tipo)

        restante = (
            efeito.duracao
            if type(efeito.duracao) is int
            else None
        )

        novoRegistro = {
            "efeito": efeito,
            "restante": restante
        }

        if registro is not None:
            # Renova o efeito, descartando os dados
            # temporários da aplicação anterior.
            registro.clear()
            registro.update(novoRegistro)
            return True

        self.efeitosAtivos.append(novoRegistro)
        return True


    def removerEfeito(self, tipo):
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
            "ultimoAtaque": self.ultimoAtaque,
            "ultimoAtaqueTentado": self.ultimoAtaqueTentado,
            "ultimoAtaqueTentadoAcertou": self.ultimoAtaqueTentadoAcertou,
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
        self.ultimoAtaqueTentadoAcertou = estado[
            "ultimoAtaqueTentadoAcertou"
        ]

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
