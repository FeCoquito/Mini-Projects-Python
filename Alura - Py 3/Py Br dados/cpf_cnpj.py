from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos esta incorreta!!!")

class DocCpf:
    def __imit__(self,documento):
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf invalido!")

    def __str__(self):
        return self.formtar_cpf()

    def cpf_e_valido(self, cpf):
            validador_cpf = CPF()
            return validador_cpf.validate(cpf)

    def formtar_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __imit__(self,documento):
        if self.cnpj_e_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj invalido!")

    def __str__(self):
        return self.formtar_cnpj()

    def cnpj_e_valido(self, cnpj):
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(cnpj)

    def formtar_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

