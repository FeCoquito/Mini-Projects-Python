SC = float(input("Carlos digite seu salario: "))
SJ = SC * 0.5
cont = 0
while SJ <= SC:
    SC = SC * 1.02
    SJ = SJ * 1.25
    cont += 1
print(f'Passar {cont} meses')