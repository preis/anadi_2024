# librarias
import pandas as pd
import matplotlib as mpl  # não sei se é necessária!!!!!!!!!!!!!!!!!
import matplotlib.pyplot as plt
import numpy as np

# leitura e apresentação do dataset
CO_data = pd.read_csv("./CO_data.csv", delimiter=",")
# print(CO_data)

# ----------------Análise e exploração dos dados------------------
# tamado do dataset
# n_linhas, n_colunas= CO_data.shape
# print('Numero de linhas: {}  Numero de colunas: {}'.format(n_linhas, n_colunas))

# --Construa um gráfico que permita visualizar as emissões totais de CO2 de Portugal no período 1900-2021. Encontre o ano em que foi emitido um valor máximo de CO2. --
# cria novo dataset e vai buscar apenas onde o país é Portugal
CO_data2 = CO_data[CO_data['country'] == 'Portugal']

# definir tamanho,valores das colunas e linhas, labels e titulo do gráfico
plt.figure(figsize=(10, 6))
plt.plot(CO_data2['year'], CO_data2['co2'], color='blue')
plt.xlabel('Ano')
plt.ylabel('CO2 (milhões de toneladas)')
plt.title('Emissão de CO2 em Portugal 1900-2021')

# ESTE BOCADO TIVE UM POUCO AUXILIO DO CHATGPT
# vê o valor max de CO2 e o correspondente ano
ano_max_CO2 = CO_data2.loc[CO_data2['co2'].idxmax(), 'year']
valor_max_CO2 = CO_data2['co2'].max()
# Marcando o ponto do valor máximo no gráfico
plt.scatter(ano_max_CO2, valor_max_CO2, color='red')
plt.text(ano_max_CO2, valor_max_CO2, f'CO2 Máximo de valor {valor_max_CO2} no ano {ano_max_CO2}',
         horizontalalignment='right', verticalalignment='bottom', color='red')

# apresenta o gráfico com grid
plt.grid(True)
plt.show()
# print(CO_max=CO_data2['co2'].max())


# ---Construa um gráfico que permita comparar, no período 1900-2021, as emissões de CO2 de Portugalprovenientes de: cimento, carvão, queima (flaring), gas, metano, óxido nitroso e do petróleo.---
# carvao coal_co2  - cimento cement_co2 - queima flaring_co2 - gas gas_co2 - methane -  oxido nitrido nitrous_oxide - petroleo oil_co2

print("---Valores nulos---")
print(CO_data2[CO_data2.isnull().any(axis=1)])

# seleciona as colunas necessárias
fontes_CO2 = ['coal_co2', 'cement_co2', 'flaring_co2', 'gas_co2', 'methane', 'nitrous_oxide', 'oil_co2']
# das colunas necessárias vai ao dataset buscar o ano correspondente
dados_fontes_CO2 = CO_data2[['year'] + fontes_CO2]

# para cada fonte cria uma coluna por ano com a respetiva cor
emissions = ['coal_co2', 'cement_co2', 'flaring_co2', 'gas_co2', 'methane', 'nitrous_oxide', 'oil_co2']
colors = ['black', 'gray', 'pink', 'blue', 'yellow', 'orange', 'red']
labels = ['Carvão', 'Cimento', 'Queima', 'Gás', 'Metano', 'Óxido Nitroso', 'Petróleo']
bottom = 0
for value, color, label in zip(emissions, colors, labels):
    plt.bar(dados_fontes_CO2['year'], dados_fontes_CO2[value], bottom=bottom, label=label, color=color)
    bottom += dados_fontes_CO2[value]

# definir labels titulos e apresentar grid
plt.xlabel('Ano')
plt.ylabel('CO2 (milhões de toneladas)')
plt.title('Emissões de CO2 em Portugal de diferentes fontes 1900-2021')
plt.legend(loc='upper left')
plt.grid(True)
# garante que os componentes não ficam subrepostos
plt.tight_layout()
plt.show()

# -----Construa um gráfico que permita comparar, no período 1900-2021, as emissões de CO2 per capita de Portugal com a Espanha. ---
# cria uma nova coluna que calcula o co2 per capita
CO_data['co2_percapita'] = CO_data['co2'] / CO_data['population']

# gráfico de barras
largura = 0.4
plt.figure(figsize=(13, 8))
# para cada país vai buscar o valor de co2 em um respetivo ano
for i, pais in enumerate(['Portugal', 'Spain']):
    valores = CO_data[CO_data['country'] == pais]
    # posiciona as barras tendo em conta a largura e ajusta
    posicao_barras = np.arange(len(valores['year'])) + (i * largura) - 0.2
    plt.bar(posicao_barras, valores['co2'], width=largura, label=pais)
plt.xticks(np.arange(len(valores['year'])), valores['year'], rotation=90)
plt.xlabel('Ano')
plt.ylabel('CO2 per capita (toneladas)')
plt.title('Emissões de CO2 per capita de Portugal e Espanha (1900-2021)')
plt.legend()
plt.grid(True)
plt.show()

# gráfico de linhas
plt.figure(figsize=(13, 8))
for pais in ['Portugal', 'Spain']:
    valores = CO_data[CO_data['country'] == pais]
    plt.plot(valores['year'], valores['co2_percapita'], label=pais)
plt.xlabel('Ano')
plt.ylabel('CO2 per capita (toneladas)')
plt.title('Emissões de CO2 per capita de Portugal e Espanha 1900-2021')
plt.legend()
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

# --Construa um gráfico que permita comparar as emissões de CO2 originadas pelo carvão dos Estados Unidos, China, Índia, União Europeia (a 27) e a Rússia no período 2000-2021.--

# cria um novo dataset só com os países e anos desejados
CO_data4 = CO_data[
    (CO_data['country'].isin(['United States', 'China', 'India', 'European Union (27)', 'Russia', 'Spain'])) & (
                CO_data['year'] >= 2000)]
print()
# não foi encontrado nulos nas colunas importantes
print(CO_data4[CO_data4.isnull().any(axis=1)])

# antigo
# obtem o valor unico de cada país
# paises=CO_data4['country'].unique()
##largura de barra da cada país
# largura=0.2
# plt.figure(figsize=(14,8))
##ciclo for onde para cada país da lista paises vai buscar o valor das emissões co2 e o ano 
# for i,pais in enumerate(paises):
#    dados_pais=CO_data4[CO_data4['country']==pais]
#    posicao_barras=np.arange(len(dados_pais['year']))+(i*largura) #posiciona as barras de maneira a não ficarem sobrepostas e uma por ano
#    plt.bar(posicao_barras,dados_pais['co2'],width=largura,label=pais)
# plt.xlabel('Ano')
# plt.ylabel('CO2 (milhões de toneladas)')
# plt.title('Emissões de CO2 em vários países 2000-2021')
# plt.xticks(np.arange(len(dados_pais['year'])) + largura * (len(paises) - 1) / 2, dados_pais['year'])
# plt.legend()
# plt.grid(True)
# plt.show()

# gráfico pedido pelo professor(time series)
plt.figure(figsize=(14, 8))
# para cada país filtra os dados(usado para a label) e apresenta
for country in CO_data4['country'].unique():
    # Filtra os dados para o país atual
    country_co2 = CO_data4[CO_data4['country'] == country]
    # Plota os dados para o país atual
    plt.plot(country_co2['year'], country_co2['co2'], label=country)
plt.xlabel('Ano')
plt.ylabel('CO2 (milhões de toneladas)')
plt.title('Emissões de CO2 ao longo do tempo em vários países 2000-2021')
plt.legend()
plt.grid(True)
plt.show()

# ------Construa uma tabela que indique, para cada uma das regiões: Estados Unidos, China, Índia, União Europeia (a 27) e a Rússia, as médias das emissões de CO2 devidas a cimento, carvão,
# queima (flaring), gas, metano, óxido nitroso e do petróleo no período 2000-2021. (formate as entradas da tabela de forma a terem apenas 3 casas decimais). ------

# ao dataset já criado com os países e anos pedidos,faz a média de cada emissão necessária usando aggregate e arredonda para 3 casas decimais
CO_data5 = CO_data4.groupby('country').agg(
    {'cement_co2': 'mean', 'coal_co2': 'mean', 'flaring_co2': 'mean', 'gas_co2': 'mean', 'methane': 'mean',
     'nitrous_oxide': 'mean', 'oil_co2': 'mean'})
CO_data5 = CO_data5.round(3)
# colocar o nome das colunas mais explicitos
CO_data5.columns = ['CO2 do cimento', 'CO2 do carvão', 'CO2 da queima (flaring)', 'CO2 do gás', 'Metano',
                    'Óxido nitroso', 'CO2 do petróleo']
print("-----------Médias das emissões de CO2 por tipo de emissão e região 2000-2021 -----------")
print(CO_data5)

# -------------------------------------------------------------------------------
