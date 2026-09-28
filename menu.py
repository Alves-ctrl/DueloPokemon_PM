from DAO_Entidade import EntidadeDAO
from Classe_Pokemon import Pokemon
from Classe_Acao import Acao
from Classe_Combate import Combate
from Classe_Time import Time
from Classe_Treinador import Treinador

def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido.")




class Menu:

    def __init__(self):
        self.dao_pokemon = EntidadeDAO.get_instancia(Pokemon)
        self.dao_acao = EntidadeDAO.get_instancia(Acao)
        self.dao_combate = EntidadeDAO.get_instancia(Combate)
        for dao in (self.dao_pokemon, self.dao_acao, self.dao_combate):
            dao.recuperar()

    def salvar_tudo(self):
        for dao in (self.dao_pokemon, self.dao_acao, self.dao_combate):
            dao.persistir()

    def iniciar(self):

        while True:
            print("\n========== MENU PRINCIPAL ===========")
            print("1 - Pokémon")
            print("2 - Ação")
            print("3 - Combate")
            print("0 - Sair")
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.menu_pokemon()
            elif opcao == "2":
                self.menu_acao()
            elif opcao == "3":
                self.menu_combate()
            elif opcao == "0":
                self.salvar_tudo()
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida.")


    def menu_pokemon(self):

        while True:

            print("\n============= POKÉMON ===============")
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Excluir")
            print("4 - Buscar por ID")
            print("5 - Listar todos")
            print("0 - Voltar")
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir_pokemon()

            elif opcao == "2":
                self.alterar_pokemon()

            elif opcao == "3":
                self.excluir_pokemon()

            elif opcao == "4":
                self.buscar_pokemon()

            elif opcao == "5":
                self.listar_pokemons()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")


    def menu_acao(self):

        while True:

            print("\n=============== AÇÃO ================")
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Excluir")
            print("4 - Buscar por ID")
            print("5 - Listar todos")
            print("0 - Voltar")
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir_acao()

            elif opcao == "2":
                self.alterar_acao()

            elif opcao == "3":
                self.excluir_acao()

            elif opcao == "4":
                self.buscar_acao()

            elif opcao == "5":
                self.listar_acoes()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")


    def menu_combate(self):

        while True:

            print("\n============== COMBATE ==============")
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Excluir")
            print("4 - Buscar por ID")
            print("5 - Listar todos")
            print("0 - Voltar")
            print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir_combate()

            elif opcao == "2":
                self.alterar_combate()

            elif opcao == "3":
                self.excluir_combate()

            elif opcao == "4":
                self.buscar_combate()

            elif opcao == "5":
                self.listar_combates()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")


    def inserir_pokemon(self):
        print("\n--- Inserir Pokémon ---")
        id_ = ler_int("ID: ")
        nome = input("Nome: ")
        tipo = input("Tipo: ")
        fraqueza = input("Fraqueza: ")
        resistencia = input("Resistência: ")
        ataque = ler_int("Ataque: ")
        defesa = ler_int("Defesa: ")
        vidaMaxima = ler_int("Vida máxima: ")
        velocidade = ler_int("Velocidade: ")

        ataques = []
        print("Escolha os ataques deste Pokémon (0 para terminar):")
        while True:
            self.listar_acoes()
            id_acao = ler_int("ID da ação (0 para parar): ")
            if id_acao == 0:
                break
            acao = self.dao_acao.buscar(id_acao)
            if acao is None:
                print("Ação não encontrada.")
                continue
            ataques.append(acao)

        pokemon = Pokemon(id_, nome, tipo, fraqueza, resistencia,
                          ataque, defesa, vidaMaxima, velocidade, ataques)

        if self.dao_pokemon.salvar(pokemon):
            self.dao_pokemon.persistir()
            print("Pokémon inserido.")
        else:
            print("Já existe um Pokémon com esse ID.")

    def alterar_pokemon(self):
        print("\n--- Alterar Pokémon ---")
        pokemon = self.dao_pokemon.buscar(ler_int("ID do Pokémon: "))
        if pokemon is None:
            print("Pokémon não encontrado.")
            return

        nome = input(f"Nome [{pokemon.nome}]: ")
        if nome:
            pokemon.nome = nome

        self.dao_pokemon.atualizar(pokemon)
        self.dao_pokemon.persistir()
        print("Pokémon atualizado.")

    def excluir_pokemon(self):
        print("\n--- Excluir Pokémon ---")
        if self.dao_pokemon.apagar(ler_int("ID do Pokémon: ")):
            self.dao_pokemon.persistir()
            print("Pokémon excluído.")
        else:
            print("Pokémon não encontrado.")

    def buscar_pokemon(self):
        print("\n--- Buscar Pokémon ---")
        pokemon = self.dao_pokemon.buscar(ler_int("ID do Pokémon: "))
        print(pokemon if pokemon else "Pokémon não encontrado.")

    def listar_pokemons(self):
        print("\n--- Lista de Pokémon ---")
        for p in self.dao_pokemon.carregar():
            print(p)

# Ação

    def inserir_acao(self):
        print("\n--- Inserir Ação ---")
        id_ = ler_int("ID: ")
        nome = input("Nome: ")
        tipo = input("Tipo: ")
        categoria = input("Categoria (BASICO/ESPECIAL/ASSINATURA): ").upper()
        dano = None if categoria == "BASICO" else ler_int("Dano: ")
        precisao = ler_int("Precisão (0-100): ")

        acao = Acao(id_, nome, tipo, categoria, dano, precisao)

        if self.dao_acao.salvar(acao):
            self.dao_acao.persistir()
            print("Ação inserida.")
        else:
            print("Já existe uma ação com esse ID.")

    def alterar_acao(self):
        print("\n--- Alterar Ação ---")
        acao = self.dao_acao.buscar(ler_int("ID da ação: "))
        if acao is None:
            print("Ação não encontrada.")
            return

        nome = input(f"Nome [{acao.nome}]: ")
        if nome:
            acao.nome = nome

        self.dao_acao.atualizar(acao)
        self.dao_acao.persistir()
        print("Ação atualizada.")

    def excluir_acao(self):
        print("\n--- Excluir Ação ---")
        if self.dao_acao.apagar(ler_int("ID da ação: ")):
            self.dao_acao.persistir()
            print("Ação excluída.")
        else:
            print("Ação não encontrada.")

    def buscar_acao(self):
        print("\n--- Buscar Ação ---")
        acao = self.dao_acao.buscar(ler_int("ID da ação: "))
        print(acao if acao else "Ação não encontrada.")

    def listar_acoes(self):
        print("\n--- Lista de Ações ---")
        for a in self.dao_acao.carregar():
            print(a)

#Combate

    def escolher_time(self, nome_time, treinador):
        time_ = Time(id=None, nome=nome_time, treinador=treinador)
        print(f"\nEscolha os 3 Pokémons do {nome_time}:")
        while not time_.estaCompleto():
            self.listar_pokemons()
            id_pokemon = ler_int("ID do Pokémon: ")
            pokemon = self.dao_pokemon.buscar(id_pokemon)
            if pokemon is None:
                print("ID não encontrado.")
                continue
            if not time_.addPokemon(pokemon):
                print("Esse Pokémon já está no time ou o time está cheio.")
                continue
        return time_

    def inserir_combate(self):
        print("\n--- Novo Combate ---")

        nome_a = input("Nome do Treinador A: ")
        treinador_a = Treinador(id=1, nome=nome_a)
        time_a = self.escolher_time("Time A", treinador_a)
        treinador_a.addTime(time_a)

        nome_b = input("Nome do Treinador B: ")
        treinador_b = Treinador(id=2, nome=nome_b)
        time_b = self.escolher_time("Time B", treinador_b)
        treinador_b.addTime(time_b)

        ids = [c.id for c in self.dao_combate.carregar()]
        combate = Combate(id=max(ids, default=0) + 1, timeA=time_a, timeB=time_b)
        combate.iniciarCombate()

        print("\nCombate iniciado!\n")

        while combate.status == "EM_ANDAMENTO":
            lado = combate.vezAtual
            ativo = combate.obterPokemonAtivo(lado)
            nome_treinador = treinador_a.nome if lado == "A" else treinador_b.nome

            print(f"\nVez de {nome_treinador} ({lado}) - {ativo.pokemon.nome} "
                  f"(Vida: {ativo.vidaAtual}/{ativo.pokemon.vidaMaxima})")

            if ativo.estaAtordoado():
                input("Pokémon atordoado, pressione Enter para passar o turno...")
                resultado = combate.executarTurno(None)
                print(resultado)
                continue

            disponiveis = [a for a in ativo.pokemon.ataques
                          if combate.verificaAtkDisponivel(a)]

            if not disponiveis:
                print("Nenhum ataque disponível, passando o turno.")
                resultado = combate.executarTurno(None)
                print(resultado)
                continue

            print("Ataques disponíveis:")
            for i, a in enumerate(disponiveis):
                print(f"{i + 1} - {a.nome} (precisão {a.precisao}%)")

            escolha = ler_int("Escolha o ataque: ")
            while escolha < 1 or escolha > len(disponiveis):
                escolha = ler_int("Opção inválida. Escolha o ataque: ")

            ataque = disponiveis[escolha - 1]
            resultado = combate.executarTurno(ataque)
            print(resultado)

        print(f"\n--- Combate encerrado! Vencedor: {combate.vencedor.nome} ---")

        self.dao_combate.salvar(combate)
        self.dao_combate.persistir()
    def alterar_combate(self):
        print("\n--- Alterar Combate (ações) ---")
        combate = self.dao_combate.buscar(ler_int("ID do combate: "))
        if combate is None:
            print("Combate não encontrado.")
            return
        for i, a in enumerate(combate.mostrarAcao()):
            print(i, a)
        indice = ler_int("Índice da ação a remover (-1 para cancelar): ")
        acao = combate.buscarAcao(indice)
        if acao and combate.delAcao(acao):
            self.dao_combate.atualizar(combate)
            self.dao_combate.persistir()
            print("Ação removida do combate.")

    def excluir_combate(self):
        print("\n--- Excluir Combate ---")
        if self.dao_combate.apagar(ler_int("ID do combate: ")):
            self.dao_combate.persistir()
            print("Combate excluído.")
        else:
            print("Combate não encontrado.")

    def buscar_combate(self):
        print("\n--- Buscar Combate ---")
        c = self.dao_combate.buscar(ler_int("ID do combate: "))
        if c is None:
            print("Combate não encontrado.")
            return
        print(c)
        for a in c.listaAcoes():
            print("  ", a)

    def listar_combates(self):
        print("\n--- Lista de Combates ---")
        for c in self.dao_combate.carregar():
            print(c)
