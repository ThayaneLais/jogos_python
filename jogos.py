import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
        novamente()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()
        novamente()
    else:
        print("Opção inválida!")


def novamente():
    print("Deseja jogar novamente?")
    jogar_novamente = int(input(" 1 - Sim  2 - Não"))

    if jogar_novamente == 1:
        escolhe_jogo()
    else:
        exit()


if __name__ == "__main__":
    escolhe_jogo()
