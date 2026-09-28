from copy import copy
import random
import math

if __package__:
    from .Classe_Entidade import Entidade
    from .Classe_EstadoPokemon import EstadoPokemon
    from .Classe_CombateAcao import CombateAcao
else:
    from Classe_Entidade import Entidade
    from Classe_EstadoPokemon import EstadoPokemon
    from Classe_CombateAcao import CombateAcao


class Combate(Entidade):

    def __init__(self, id, timeA, timeB):
        super().__init__(id)

        if timeA is timeB or (
            timeA.id is not None and timeA.id == timeB.id
        ):
            raise ValueError("Os times participantes devem ser diferentes.")

        if not timeA.estaCompleto() or not timeB.estaCompleto():
            raise ValueError("Os dois times precisam ter 3 Pokémon.")

        # Preserva a composição dos times no momento da criação do combate.
        self.timeA = copy(timeA)
        self.timeB = copy(timeB)

        # Cada cópia possui sua própria lista de Pokémon.
        self.timeA.pokemons = timeA.listarPokemons()
        self.timeB.pokemons = timeB.listarPokemons()

        # Histórico das ações.
        self.acoes = []

        # Informações gerais da batalha.
        self.rodada = 0
        self.status = "AGUARDANDO"
        self.vencedor = None

        # Estados temporários dos seis Pokémon.
        self.estadosPokemon = {}

        # Posições dos Pokémon ativos.
        self.indiceAtivoA = 0
        self.indiceAtivoB = 0

        # Controle dos turnos.
        self.vezAtual = None
        self.turnosNaRodada = 0

    def __str__(self):
        return (
            f"Combate [{super().__str__()}, "
            f"Time A: {self.timeA.nome}, "
            f"Time B: {self.timeB.nome}, "
            f"Rodada: {self.rodada}, "
            f"Status: {self.status}, "
            f"Vencedor: "
            f"{self.vencedor.nome if self.vencedor else 'Nenhum'}]"
        )

    # ================== Estrutura e Gerenciamento ==================

    def obterResumo(self):
        return str(self)

    def iniciarCombate(self):

        if self.status != "AGUARDANDO":
            return False

        # Cria os estados temporários dos Pokémon do Time A.
        for i, pokemon in enumerate(self.timeA.pokemons):
            self.estadosPokemon[("A", i)] = EstadoPokemon(pokemon)

        # Cria os estados temporários dos Pokémon do Time B.
        for i, pokemon in enumerate(self.timeB.pokemons):
            self.estadosPokemon[("B", i)] = EstadoPokemon(pokemon)

        self.status = "EM_ANDAMENTO"

        self.iniciarRodada()

        return True

    def obterEstado(self, time, pokemon):

        if pokemon is None:
            return None

        if time == "A":
            equipe = self.timeA

        elif time == "B":
            equipe = self.timeB

        else:
            return None

        # Procura o Pokémon dentro do time informado.
        for i, integrante in enumerate(equipe.pokemons):

            if integrante.id == pokemon.id:
                return self.estadosPokemon.get((time, i))

        return None

    def obterPokemonAtivo(self, time):

        if time == "A":
            indice = self.indiceAtivoA

        elif time == "B":
            indice = self.indiceAtivoB

        else:
            return None

        return self.estadosPokemon.get((time, indice))

    def iniciarRodada(self, _interna=False):

        if self.status != "EM_ANDAMENTO":
            return False

        # Depois da primeira rodada, somente finalizarRodada pode avançar.
        if self.rodada > 0 and not _interna:
            return False

        atacanteA = self.obterPokemonAtivo("A")
        atacanteB = self.obterPokemonAtivo("B")

        if atacanteA is None or atacanteB is None:
            return False

        # Um Pokémon derrotado deve ser substituído antes da nova rodada.
        if atacanteA.estaDerrotado() or atacanteB.estaDerrotado():
            return False

        self.rodada += 1

        # Ativa ou encerra os efeitos vinculados à rodada.
        self.atualizarEfeitos()

        velocidadeA = atacanteA.pokemon.velocidade
        velocidadeB = atacanteB.pokemon.velocidade

        if velocidadeA > velocidadeB:
            self.vezAtual = "A"
        else:
            # Em caso de empate, o Time B começa.
            self.vezAtual = "B"

        self.turnosNaRodada = 0

        return True


    # ================== Gerenciamento das Ações e Rodadas ==================

    def addAcao(self, acao):

        if self.status != "EM_ANDAMENTO":
            return False

        if not isinstance(acao, CombateAcao):
            return False

        if type(acao.id) is not int or acao.id <= 0:
            return False

        # Impede duas ações com o mesmo ID dentro do combate.
        if self.buscarAcao(acao.id) is not None:
            return False

        self.acoes.append(acao)
        return True

    def buscarAcao(self, id_acao):

        for acao in self.acoes:
            if acao.id == id_acao:
                return acao

        return None

    def listaAcoes(self):
        return self.acoes.copy()

    def substituirPokemon(self, time):

        if time == "A":
            indice = self.indiceAtivoA
            equipe = self.timeA

        elif time == "B":
            indice = self.indiceAtivoB
            equipe = self.timeB

        else:
            return None

        # A substituição automática só acontece após uma derrota.
        atual = self.obterPokemonAtivo(time)

        if atual is None or not atual.estaDerrotado():
            return None

        # Procura o próximo Pokémon disponível na ordem do time.
        for i in range(indice + 1, len(equipe.pokemons)):

            estado = self.estadosPokemon[(time, i)]

            if not estado.estaDerrotado():

                if time == "A":
                    self.indiceAtivoA = i
                else:
                    self.indiceAtivoB = i

                return estado

        # Nenhum Pokémon disponível: o time foi derrotado.
        if time == "A":
            self.indiceAtivoA = len(equipe.pokemons)
        else:
            self.indiceAtivoB = len(equipe.pokemons)

        return None

    def verificaVencedor(self):

        if self.indiceAtivoA >= len(self.timeA.pokemons):
            return self.timeB

        if self.indiceAtivoB >= len(self.timeB.pokemons):
            return self.timeA

        return None

    def encerraCombate(self):

        if self.status != "EM_ANDAMENTO":
            return False

        vencedor = self.verificaVencedor()

        if vencedor is None:
            return False

        self.vencedor = vencedor
        self.status = "ENCERRADO"
        self.vezAtual = None

        return True

    def finalizarRodada(self):

        if self.status != "EM_ANDAMENTO":
            return False

        estadoA = self.obterPokemonAtivo("A")
        estadoB = self.obterPokemonAtivo("B")

        # Verifica se houve derrota nesta rodada.
        derrotaA = (
            estadoA is not None
            and estadoA.estaDerrotado()
        )

        derrotaB = (
            estadoB is not None
            and estadoB.estaDerrotado()
        )

        # Sem derrota, a rodada só termina após os dois turnos.
        if (
            not derrotaA
            and not derrotaB
            and self.turnosNaRodada < 2
        ):
            return False

        # Substitui os Pokémon derrotados.
        if derrotaA:
            self.substituirPokemon("A")

        if derrotaB:
            self.substituirPokemon("B")

        # Verifica se um dos times ficou sem Pokémon.
        if self.verificaVencedor() is not None:
            return self.encerraCombate()

        # Inicia a próxima rodada com uma nova comparação de velocidade.
        return self.iniciarRodada(_interna=True)

    def salvarEstadoAnterior(self):

        estados = {}

        # Salva os atributos temporários dos seis Pokémon.
        for chave, estado in self.estadosPokemon.items():
            estados[chave] = estado.salvarEstado()

        # Salva também os atributos de controle do combate.
        return {
            "estadosPokemon": estados,
            "rodada": self.rodada,
            "status": self.status,
            "vencedor": self.vencedor,
            "indiceAtivoA": self.indiceAtivoA,
            "indiceAtivoB": self.indiceAtivoB,
            "vezAtual": self.vezAtual,
            "turnosNaRodada": self.turnosNaRodada
        }

    def restaurarEstado(self, estadoAnterior):

        # Restaura o estado de cada Pokémon.
        for chave, dados in estadoAnterior["estadosPokemon"].items():
            self.estadosPokemon[chave].restaurarEstado(dados)

        # Restaura o controle do combate.
        self.rodada = estadoAnterior["rodada"]
        self.status = estadoAnterior["status"]
        self.vencedor = estadoAnterior["vencedor"]

        self.indiceAtivoA = estadoAnterior["indiceAtivoA"]
        self.indiceAtivoB = estadoAnterior["indiceAtivoB"]

        self.vezAtual = estadoAnterior["vezAtual"]
        self.turnosNaRodada = estadoAnterior["turnosNaRodada"]

    def removerUltimaAcao(self):

        # Não é permitido desfazer ações de um combate encerrado.
        if self.status != "EM_ANDAMENTO":
            return False

        if len(self.acoes) == 0:
            return False

        ultimaAcao = self.acoes[-1]

        if ultimaAcao.estadoAnterior is None:
            return False

        # Retorna ao estado anterior à execução da última ação.
        self.restaurarEstado(ultimaAcao.estadoAnterior)

        # Remove a ação desfeita do histórico.
        self.acoes.pop()

        return True

#======================= Execução dos Ataques ================================


    def verificaAtkDisponivel(self, ataque):

        if self.status != "EM_ANDAMENTO":
            return False

        atacante = self.obterPokemonAtivo(self.vezAtual)

        if atacante is None or ataque is None:
            return False

        if atacante.estaDerrotado() or atacante.estaAtordoado():
            return False

        # Verifica se o ataque pertence ao Pokémon ativo.
        if not any(
            acao is ataque
            for acao in atacante.pokemon.ataques
        ):
            return False

        ultimoTentado = atacante.ultimoAtaqueTentado

        if (
            ultimoTentado is not None
            and ultimoTentado.id == ataque.id
        ):

            # Ataques que não podem ser usados em sequência,
            # mesmo quando a tentativa anterior errou.
            if ataque.bloqueiaSequencia:
                return False

            # Os demais ataques não podem ser repetidos
            # imediatamente quando a tentativa anterior acertou.
            if atacante.ultimoAtaqueTentadoAcertou:
                return False

        return True

    def verificarAcerto(self, ataque, atacante):

        precisao = ataque.precisao

        concentracao = atacante.buscarEfeito("CONCENTRACAO")
        reducao = atacante.buscarEfeito("REDUCAO_PRECISAO")

        if (
            concentracao is not None
            and ataque.categoria in ("ESPECIAL", "ASSINATURA")
        ):
            precisao += concentracao["efeito"].valor

        if reducao is not None:
            precisao -= reducao["efeito"].valor

        # Mantém a precisão entre 0% e 100%.
        precisao = max(0, min(100, precisao))

        acertou = random.randint(1, 100) <= precisao

        # A redução de precisão é consumida nesta tentativa,
        # independentemente de o ataque acertar.
        atacante.removerEfeito("REDUCAO_PRECISAO")

        # A Concentração é consumida na próxima tentativa
        # de um especial ou assinatura.
        if ataque.categoria in ("ESPECIAL", "ASSINATURA"):
            atacante.removerEfeito("CONCENTRACAO")

        return acertou

    def calcDano(
        self, ataque, atacante, alvo,
        bonusBase=0, bonusDano=0, reducaoDano=0
    ):

        # Dano base do ataque.
        dano = ataque.obterDanoBase(atacante.pokemon)

        # Acréscimos fixos, como os de Cadeia Alimentar.
        dano += bonusBase

        # Bônus percentual de dano do atacante.
        dano *= 1 + bonusDano / 100

        # Multiplicadores de tipo.
        if ataque.tipo == alvo.pokemon.fraqueza:
            dano *= 1.25

        elif ataque.tipo == alvo.pokemon.resistencia:
            dano *= 0.8

        # Defesa percentual atual do alvo.
        dano *= 1 - alvo.defesaAtual / 100

        # Redução temporária do dano do atacante.
        dano *= 1 - reducaoDano / 100

        # Arredonda apenas no final.
        return max(1, math.floor(dano))

    def aplicarDano(self, alvo, dano):

        vidaAnterior = alvo.vidaAtual

        alvo.receberDano(dano)

        # Retorna o dano efetivo, limitado à vida disponível.
        return vidaAnterior - alvo.vidaAtual

    def processarEfeitos(
        self, efeitosValidos, atacante, alvo, momento
    ):

        if momento == "ANTES_DANO":

            bonusBase = 0

            for efeito in efeitosValidos:

                if efeito.tipo == "DANO_ADICIONAL":

                    if efeito.verificaProb():
                        bonusBase += efeito.valor

            return bonusBase

        if momento != "DEPOIS_DANO":
            raise ValueError(
                "Momento de processamento inválido."
            )

        aplicados = []

        for efeito in efeitosValidos:

            # O dano adicional já foi processado.
            # A repetição é controlada por executarTurno().
            if efeito.tipo in ("DANO_ADICIONAL", "REPETICAO"):
                continue

            if not efeito.verificaProb():
                continue

            # Identifica quem receberá o efeito.
            if efeito.alvo == "ATACANTE":
                destinatario = atacante

            elif efeito.alvo == "ALVO":
                destinatario = alvo

            else:
                raise ValueError(
                    f"Alvo do efeito inválido: {efeito.alvo}"
                )

            # Não aplica novos efeitos a um Pokémon derrotado.
            if destinatario.estaDerrotado():
                continue

            if efeito.tipo == "CURA":

                vidaAnterior = destinatario.vidaAtual

                destinatario.recuperarVida(efeito.valor)

                valorAplicado = (
                    destinatario.vidaAtual - vidaAnterior
                )

            elif efeito.tipo in (
                "CONCENTRACAO",
                "ATORDOAMENTO",
                "BONUS_DANO",
                "BONUS_DEFESA",
                "REDUCAO_DANO",
                "REDUCAO_PRECISAO"
            ):

                destinatario.adicionarEfeito(efeito)
                valorAplicado = efeito.valor

                # O bônus de defesa será ativado
                # no início da próxima rodada.
                if efeito.tipo == "BONUS_DEFESA":

                    registro = destinatario.buscarEfeito(
                        "BONUS_DEFESA"
                    )

                    registro["ativarNaRodada"] = (
                        self.rodada + 1
                    )

            else:
                raise ValueError(
                    f"Tipo de efeito desconhecido: {efeito.tipo}"
                )

            aplicados.append({
                "tipo": efeito.tipo,
                "valor": valorAplicado,
                "alvo": efeito.alvo
            })

        return aplicados

    def atualizarEfeitos(self):

        for estado in self.estadosPokemon.values():

            # A defesa é recalculada a cada rodada.
            estado.defesaAtual = float(estado.pokemon.defesa)

            registro = estado.buscarEfeito("BONUS_DEFESA")

            if registro is None:
                continue

            rodadaAtivacao = registro["ativarNaRodada"]

            # O bônus já cumpriu sua duração.
            if self.rodada > rodadaAtivacao:

                estado.removerEfeito("BONUS_DEFESA")

            # O bônus vale durante esta rodada.
            elif self.rodada == rodadaAtivacao:

                bonus = registro["efeito"].valor

                estado.defesaAtual *= 1 + bonus / 100

    def avancarTurno(self, houveDerrota=False):

        self.turnosNaRodada += 1

        # Uma derrota encerra a rodada imediatamente.
        if houveDerrota or self.turnosNaRodada >= 2:
            return self.finalizarRodada()

        # Caso contrário, passa a vez ao outro time.
        if self.vezAtual == "A":
            self.vezAtual = "B"
        else:
            self.vezAtual = "A"

        return True

    def executarTurno(self, ataque=None):
        """Executa a ação de forma transacional: erros não deixam dano parcial."""
        if self.status != "EM_ANDAMENTO":
            raise ValueError("O combate não está em andamento.")

        estadoAntes = self.salvarEstadoAnterior()
        quantidadeAcoes = len(self.acoes)

        try:
            return self._executarTurno(ataque)
        except Exception:
            self.restaurarEstado(estadoAntes)
            del self.acoes[quantidadeAcoes:]
            raise

    def _executarTurno(self, ataque=None):

        if self.status != "EM_ANDAMENTO":
            raise ValueError(
                "O combate não está em andamento."
            )

        atacante = self.obterPokemonAtivo(self.vezAtual)

        ladoAlvo = "B" if self.vezAtual == "A" else "A"
        alvo = self.obterPokemonAtivo(ladoAlvo)

        if atacante is None or alvo is None:
            raise ValueError(
                "Não existem Pokémon ativos."
            )

        # Valida a ação antes de alterar o combate.
        # Um Pokémon atordoado perde o turno automaticamente.
        if not atacante.estaAtordoado():

            if not self.verificaAtkDisponivel(ataque):
                raise ValueError("Ataque indisponível.")

        # Salva o estado para permitir desfazer a ação.
        estadoAnterior = self.salvarEstadoAnterior()

        idAcao = max((registro.id for registro in self.acoes), default=0) + 1

        # ================== Atordoamento ==================

        if atacante.estaAtordoado():

            atacante.removerEfeito("ATORDOAMENTO")

            # O turno perdido interrompe a sequência
            # de ataques consecutivos.
            atacante.ultimoAtaqueTentado = None
            atacante.ultimoAtaqueTentadoAcertou = False

            acao = CombateAcao(
                id=idAcao,
                rodada=self.rodada,
                atacante=atacante,
                alvo=None,
                ataque=None,
                acertou=False,
                danoCausado=0,
                estadoAnterior=estadoAnterior
            )

            self.addAcao(acao)
            self.avancarTurno()

            return acao

        # ================== Preparação do ataque ==================

        contexto = {
            "atacante": atacante,
            "alvo": alvo
        }

        # As condições são verificadas antes do primeiro golpe.
        efeitosValidos = [
            efeito
            for efeito in ataque.efeitos
            if efeito.verificaCond(contexto)
        ]

        # Rejeita configurações incompatíveis antes de alterar a vida.
        tiposSuportados = {
            "DANO_ADICIONAL", "REPETICAO", "CURA",
            "CONCENTRACAO", "ATORDOAMENTO", "BONUS_DANO",
            "BONUS_DEFESA", "REDUCAO_DANO", "REDUCAO_PRECISAO"
        }
        for efeito in efeitosValidos:
            if efeito.tipo not in tiposSuportados:
                raise ValueError(f"Tipo de efeito desconhecido: {efeito.tipo}")
            if efeito.alvo not in ("ATACANTE", "ALVO"):
                raise ValueError(f"Alvo do efeito inválido: {efeito.alvo}")

        # Consulta os modificadores que já estavam ativos.
        bonusDano = atacante.buscarEfeito("BONUS_DANO")
        reducaoDano = atacante.buscarEfeito("REDUCAO_DANO")

        valorBonus = (
            bonusDano["efeito"].valor
            if bonusDano is not None else 0
        )

        valorReducao = (
            reducaoDano["efeito"].valor
            if reducaoDano is not None else 0
        )

        danoCausado = 0
        efeitosAplicados = []

        # ================== Primeiro golpe ==================

        acertou = self.verificarAcerto(ataque, atacante)

        if acertou:

            bonusBase = self.processarEfeitos(
                efeitosValidos,
                atacante,
                alvo,
                "ANTES_DANO"
            )

            if bonusBase > 0:

                efeitosAplicados.append({
                    "tipo": "DANO_ADICIONAL",
                    "valor": bonusBase,
                    "alvo": "ALVO"
                })

            dano = self.calcDano(
                ataque,
                atacante,
                alvo,
                bonusBase,
                valorBonus,
                valorReducao
            )

            danoCausado += self.aplicarDano(alvo, dano)

            # ================== Segundo golpe ==================

            # Só pode ocorrer se o alvo sobreviveu ao primeiro.
            if not alvo.estaDerrotado():

                for efeito in efeitosValidos:

                    if efeito.tipo != "REPETICAO":
                        continue

                    if efeito.verificaProb():

                        # A repetição possui sua própria
                        # verificação de precisão.
                        segundoAcertou = self.verificarAcerto(
                            ataque,
                            atacante
                        )

                        danoSegundo = 0

                        if segundoAcertou:

                            danoRepetido = self.calcDano(
                                ataque,
                                atacante,
                                alvo,
                                bonusBase,
                                valorBonus,
                                valorReducao
                            )

                            danoSegundo = self.aplicarDano(
                                alvo,
                                danoRepetido
                            )

                            danoCausado += danoSegundo

                        # Registra se a repetição realmente acertou.
                        efeitosAplicados.append({
                            "tipo": "REPETICAO",
                            "valor": 1,
                            "alvo": "ALVO",
                            "acertou": segundoAcertou,
                            "danoCausado": danoSegundo
                        })

                    # Nunca permite um terceiro golpe.
                    break

        # ================== Consumo dos efeitos antigos ==================

        # A redução de dano vale para a ação inteira,
        # mesmo quando o ataque erra.
        atacante.removerEfeito("REDUCAO_DANO")

        if acertou:

            # O bônus anterior vale para a ação inteira.
            # É consumido somente se houve acerto.
            atacante.removerEfeito("BONUS_DANO")

            # Aplica os efeitos produzidos por este ataque.
            efeitosAplicados.extend(
                self.processarEfeitos(
                    efeitosValidos,
                    atacante,
                    alvo,
                    "DEPOIS_DANO"
                )
            )

            atacante.ultimoAtaque = ataque

        # Registra a tentativa mesmo quando o ataque erra.
        atacante.ultimoAtaqueTentado = ataque
        atacante.ultimoAtaqueTentadoAcertou = acertou

        # ================== Registro da ação ==================

        acao = CombateAcao(
            id=idAcao,
            rodada=self.rodada,
            atacante=atacante,
            alvo=alvo,
            ataque=ataque,
            acertou=acertou,
            danoCausado=danoCausado,
            efeitosAplicados=efeitosAplicados,
            estadoAnterior=estadoAnterior
        )

        self.addAcao(acao)

        # Passa a vez ou encerra a rodada após uma derrota.
        self.avancarTurno(alvo.estaDerrotado())

        return acao


            self.vencedor = self.pokemonA

        return self.vencedor
