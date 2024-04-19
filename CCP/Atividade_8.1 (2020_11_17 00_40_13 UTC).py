soma=1
cont=0
N=int(input("Digite o valor de N:"))
while True:
    if cont==N:
        break
    cont=cont+1
    soma=soma+1/cont
print("E= %.2f"%soma)