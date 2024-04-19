salario= float(input("Digite seu salarios: "))

if salario <= 1499.15:
    "Print você é Isento"

if salario >= 1499.16 and salario <= 2246.75:
    aliquota = 7.5
    dedução = 112.43
    Imposto = (salario * aliquota / 100) - dedução

if salario >= 2246.76 and salario <= 2995.71:
    aliquota = 15.0
    dedução = 280.94
    Imposto = (salario * aliquota / 100) - dedução

if salario >= 2995.71 and salario <= 3143.19:
    aliquota = 22.5
    dedução = 505.62
    Imposto = (salario * aliquota / 100) - dedução

if salario >= 3743.19:
    aliquota = 27.5
    dedução = 692.78
    Imposto = (salario * aliquota / 100) - dedução

print("O total de imposto a ser pago é %.2f"%Imposto,"reais")
