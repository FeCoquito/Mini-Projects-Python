#pip install anaconda
#pip install pandas
#pip install IPython
from IPython.display import display
import pandas as pd
import numpy as np

#criar um data Frame apartir de um dicionario
venda = {'data':['15/02/2021', '16/02/2021'],
          'valor':[500, 300],
          'produto': ['feijão','arroz'],
          'gtde': [50 , 70]
          }
venda_df = pd.DataFrame(venda)
print(venda_df)
display(venda_df)

#importar uma tabela já existente

vendas_df = pd.read_excel("Vendas.xlsx")
display(vendas_df.head(10))
print(vendas_df.shape)

#analise basica dos dados
display(vendas_df.describe())

#separar uma coluna
produtos = vendas_df['Produto']
display(produtos)

#pegar uma linha
display(vendas_df.loc[1:5])

#pegar linhas que corresponde a uma condição
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']

#pegar varias linhas e colunas usando o loc => .loc[linha, coluna]
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja','Produto','Quantidade']]
display(vendas_norteshopping_df)

#a partir de uma coluna existente
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
display(vendas_df)

#criar uma coluna nova
vendas_df.loc[:,'Imposto'] = 0
display(vendas_df)

#adicionar uma linha
vendas_dez_def = pd.read_excel("Vendas - Dez.xlsx")
vendas_df = pd.concat([vendas_df,vendas_dez_def])
display(vendas_df)

#excluir linha ou coluna ( coluna = axis=1 / linha axis = 0)
vendas_df = vendas_df.drop("Imposto",axis=1)

#deletar linhas e colunas completamente vazias
vendas_df = vendas_df.dropna(how='all', axis=1)

#deletar linhas que possuem pelo menos 1 valor vazio
vendas_df = vendas_df.dropna()

#prencher valores vazios com a meida da coluna
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
display(vendas_df)

#prencher valores vazios com o ultimo valor
vendas_df['Comissão'] = vendas_df.fill()

#contar os valores da forma que vc pedir
transacoe_loja = vendas_df['ID Loja'].value_counts() 
display(transacoe_loja)

#agrupar os valores
faturamento_produto = vendas_df[['Produto','Valor Final']].groupby('Produto').sum(numeric_only=True)
display(faturamento_produto)

#mesclar tabelas
gerente_df = pd.read_excel("Gerentes.xlsx")
vendas_df= vendas_df.merge(gerente_df)
display(vendas_df)