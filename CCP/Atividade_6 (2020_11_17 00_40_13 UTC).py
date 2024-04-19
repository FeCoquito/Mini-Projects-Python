distancia = float(input("Digite a distancia: "))
serie = input("Digite a série: ")

if serie == 100:
    if distancia <= 1.4:
        tela  = 32
    if distancia >= 1.5 and distancia <= 2.6:
        tela = 37
    if distancia > 2.6:
        tela = 42

else:
    if distancia <= 2.8:
        tela = 42
    if distancia >= 2.9 and distancia <= 3.6:
        tela = 50
    if distancia > 3.6:
        tela = 61

print("O tamanho da televisão sera de {}".format(tela))
