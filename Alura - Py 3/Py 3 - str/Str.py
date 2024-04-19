from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentoUrl = ExtratorArgumentosUrl(url)
argumentoUrl2 = ExtratorArgumentosUrl(url)

print(argumentoUrl)

print((argumentoUrl==argumentoUrl))