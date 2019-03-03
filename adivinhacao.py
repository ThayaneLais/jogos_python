
import random


def jogar():

    cabecalho()

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    nivel = define_nivel()

    tentativas = numero_tentativas(nivel)

    for rodada in range(1, tentativas + 1):

        chute = solicita_chute(rodada, tentativas)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            perdeu(maior, menor, numero_secreto, chute, pontos)


def cabecalho():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


def define_nivel():
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    return nivel


def numero_tentativas(nivel):
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    return total_de_tentativas


def perdeu(maior, menor, numero_secreto, chute, pontos):
    if maior:
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif menor:
        print("Você errou! O seu chute foi menor do que o número secreto.")
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos


def solicita_chute(rodada, tentativas):
    print(f"Tentativa {rodada} de {tentativas}")

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    return chute


if __name__ == "__main__":
    jogar()
