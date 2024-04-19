from cpf_cnpj import Documento

exemplo_cpf = "50927117878"
exemplo_cnpj = "33592510000154"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)