from datas_br import DatasBr

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)

hoje = DatasBr()
print(hoje.tempo_cadastro())