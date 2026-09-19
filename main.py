from Treinador import Treinador
from Duelo import Duelo


def main():

    print(" BEM-VINDO AO JOGO POKEMO")

    nome1= input("Teinador 01\n")
    nome2= input("teinador 02\n")
    treinador1 = Treinador(1, nome1)
    treinador2 = Treinador(2, nome2)


    duelo = Duelo(1, treinador1, treinador2)

    
    duelo.times()

    duelo.iniciar()

    print(f"\nVencedor: {duelo.vencedor.nome}")


if __name__ == "__main__":
    main()