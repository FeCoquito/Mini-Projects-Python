def conta():

    class Conta:

        def __init__(self, numero, titular, saldo, limite):
            print("Construido objeto... {}".format(self))
            self.__numero = numero
            self.__titular = titular
            self.__saldo = saldo
            self.__limite = limite

        def extrato(self):
            print("Saldo de {} do titular {}".format(self.__saldo,self.__titular))

        def deposita(self,valor):
            self.__saldo += valor
            print("Seu saldo total agora é {}".format(self.__saldo))

        def __pode_sacar(self, valor_a_sacar):
            valor_disponivel_a_sacar = self.__saldo + self.__limite
            return  valor_a_sacar <= valor_disponivel_a_sacar

        def saca(self, valor):
            if(self.__pode_sacar(valor)):
                self.__saldo -=valor
                print("Seu saldo total agora é {}".format(self.__saldo))
            else:
                print("O valor do saque de {} é maior que seu limite".format(valor))


        def trasfere(self, valor, destino):
            self.saca(valor)
            destino.deposita(valor)
            print("Seu saldo total agora é {}".format(self.__saldo))

        @property
        def limite(self):
            return self.__limite

        @property
        def titular(seft):
            return seft.__titular

        @property
        def saldo(seft):
            return seft.__saldo

        @limite.setter
        def limite(self, limite):
            self.__limite = limite
            print("Seu novo limite é {}".format(self.__limite))

        @staticmethod
        def codigo_banco():
            return "001"

        @staticmethod
        def codigo_bancos():
            return {"BB": "001", "Caixa":"104", "Bradesco":"237"}

if(__name__== "__main__"):
    conta()