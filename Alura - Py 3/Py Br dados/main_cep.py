import requests
from acesso_cep import BuscaEndereco

cep = 11045101
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

a = objeto_cep.acessa_via_cep()
print(a)