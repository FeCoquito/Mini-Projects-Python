import re

email_1 = "Meu numero é 1234-1234"
email_2 = "Fale comigo em 1234-1234 esse é meu numero"
email_3 = "1234-1234 é meu telefone"
email_4 = "oaoaoaooooo 994311764 ou 7465-7854"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao,email_4)
print(retorno)