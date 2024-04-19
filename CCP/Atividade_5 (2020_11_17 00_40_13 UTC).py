dtg = int(input(("Qual quantidade de detergente: ")))
spo = int(input(("Qual quantidade de sabão em pó: ")))
esp = int(input(("Qual quantidade de esponja: ")))
qkit = dtg//4
if qkit > spo//3:
    qkit = spo //3
if qkit > esp//5:
    qkit = esp//5

print(f"Quantidade máxima de kit = {qkit}")
