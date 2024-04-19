print("Problema sobre IPVA")
print("*******************")
vveic = float(input("Qual valor do veiculo: "))
nme = int(input("Qual foi o mês de compra:  "))

vanaula = vveic*0.04
qm = 13-nme
vimp = (vanaula*qm)/12

print("Valor total do IPVA anual: R$ %.2f"%vanaula)
print("Valor do IPVA: R$ %.2f"%vimp)