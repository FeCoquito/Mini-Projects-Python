slr = float(input("Qual é o seu salário: "))
ts = int(input("Quantos anos está na empresa: "))
print("******************************")

if ts <= 3:
    aum = slr*2.5/100
if ts > 3:
    aum = slr*(2.5+((ts - 3)*1.7))/100

print("Seu adicional sera de R$ {}".format(aum))
