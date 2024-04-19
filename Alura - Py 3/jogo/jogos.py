import forca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("Bem vindo, escolha seu jogo!")
    print("********************************")

    print("(1) para Forca e (2) para Adivinhação")

    jogo = int(input("Qual é o jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print(" Jogando Adivinhação")
        adivinhacao.jogar()

if(__name__== "__main__"):
    escolhe_jogo()