from DAO_Entidade import EntidadeDAO
from Classe_Pokemon import Pokemon
from Classe_Acao import Acao
from Classe_Combate import Combate

class Menu:

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
        pass

    def alterar_pokemon(self):
        print("\n--- Alterar Pokémon ---")
        pass

    def excluir_pokemon(self):
        print("\n--- Excluir Pokémon ---")
        pass

    def buscar_pokemon(self):
        print("\n--- Buscar Pokémon ---")
        pass

    def listar_pokemons(self):
        print("\n--- Lista de Pokémon ---")
        pass


    def inserir_acao(self):
        print("\n--- Inserir Ação ---")
        pass

    def alterar_acao(self):
        print("\n--- Alterar Ação ---")
        pass

    def excluir_acao(self):
        print("\n--- Excluir Ação ---")
        pass

    def buscar_acao(self):
        print("\n--- Buscar Ação ---")
        pass

    def listar_acoes(self):
        print("\n--- Lista de Ações ---")
        pass


  def escolher_time(self, nome_time):
        time = []
        print(f"\nEscolha os 3 Pokemons do {nome_time}:")
        for i in range(3):
            while True:
                p = self.dao_pokemon.buscar(ler_int(f"{i + 1} Pokémon (ID): "))
                if p is None:
                    print("ID não encontrado.")
                    continue
                time.append(p)
                break
        return time

    def inserir_combate(self):
        print("\n--- Inserir Combate ---")
        ids = [c.id for c in self.dao_combate.carregar()]
        combate = Combate(max(ids, default=0) + 1)
        combate.definirTimes(self.escolher_time("Time A"),
                             self.escolher_time("Time B"))
        print(f"\nVencedor: {combate.duelar()}")
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
        for a in c.mostrarAcao():
            print("  ", a)

    def listar_combates(self):
        print("\n--- Lista de Combates ---")
        for c in self.dao_combate.carregar():
            print(c)
