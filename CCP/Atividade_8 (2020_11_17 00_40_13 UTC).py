cont = 0
media  = 0
while True:
    diam = float(input('Digite os valores dos diametros: '))
    if diam == 0:
        media = media/cont
        break
    media = media + diam
    cont += 1

print(f'O valor da media dos diametros é {media}')