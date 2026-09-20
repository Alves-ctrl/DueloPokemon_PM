from Classes import Pokemon
from Classes import Acoes
from Classes import Combate


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

    # POKÉMON
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

  
    # AÇÃO
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


    # COMBATE
    def inserir_combate(self):
        print("\n--- Inserir Combate ---")
        pass

    def alterar_combate(self):
        print("\n--- Alterar Combate ---")
        pass

    def excluir_combate(self):
        print("\n--- Excluir Combate ---")
        pass

    def buscar_combate(self):
        print("\n--- Buscar Combate ---")
        pass

    def listar_combates(self):
        print("\n--- Lista de Combates ---")
        pass