import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) - Facil / (2) - Médio / (3) - Difìcil")

    nivel = int(input("O nìvel será: "))

    if(nivel == 1 ):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {} de".format(rodada,total_de_tentativas))
        chute = int(input("Digite o seu numero entre 1 e 100:"))
        print("Você digitou" , chute)

        if(chute < 1 or chute> 100):
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou  = chute == numero_secreto
        maior    = chute  > numero_secreto
        menor    = chute  < numero_secreto


        if(acertou):
            print("voce esta certo e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que o numero secreto")
            elif(menor):
                print("Você errou! Seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo o numero secreto era {}".format(numero_secreto))

if(__name__== "__main__"):
    jogar()
