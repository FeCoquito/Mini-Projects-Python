numero = int(input("Digite um numero de 4 algarismos:"))
print("************************************")

AB = numero//100
CD = numero%100
novo = (CD*100) + AB
final = novo - 10

print(" O resultado é {}".format(final))