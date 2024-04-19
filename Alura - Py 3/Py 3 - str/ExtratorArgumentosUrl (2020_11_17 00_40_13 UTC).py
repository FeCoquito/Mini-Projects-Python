

class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.url_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url invalida!")

    def __str__(self):
        moedaOrigem,moedaDestino = self.extraiArgumentos()
        representacaoString = "Valor: {} Moeda Origem: {} , Moeda Destino: {} ".format(self.retornaValor(),moedaOrigem,moedaDestino)
        return representacaoString

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def url_valida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino","real",1)
        print(self.url)

    def extraiArgumentos(self):

        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        iniceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&valor")

        moedaDestino = self.url[iniceInicialMoedaDestino:indiceFinalMoedaDestino]

        return moedaOrigem,moedaDestino

    def retornaValor(self):
        buscaValor = "Valor=".lower()
        inicioSubstringValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[inicioSubstringValor:]
        return valor

    def encontraIndiceInicial(self,moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)