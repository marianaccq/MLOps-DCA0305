'''
Autora: Mariana Queiroz
Data: Nov. 2021
Este projeto tem o objetivo de limpar e analisar do conjunto
de dados eBay Kleinanzeige, de acordo com as instruções
do curso da plataforma Dataquest.io.
'''

# importando bibliotecas
import pandas as pd

# lendo o conjunto de dados
autos = pd.read_csv("autos.csv", encoding='Latin-1')

# renomeando todas as colunas para o padrão snake_case
autos.columns=['date_crawled', 'name', 'seller', 'offer_type', 'price', 'abtest',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer', 'registration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'num_pictures', 'postal_code',
       'last_seen']

# dropando colunas com valores repetidos
# pylint: disable=E1101
autos = autos.drop(columns=['num_pictures', 'offer_type','seller'], axis=1)

# retirando caracteres não numéricos dos preços e quilimetragem
autos.price = [value.replace('$','').replace(',','') for value in autos.price]
autos.odometer = [value.replace('km','').replace(',','') for value in autos.odometer]

# convertendo para um valor numerico
autos.price = pd.to_numeric(autos.price)
autos.odometer = pd.to_numeric(autos.odometer)

# renomeando a coluna odometer
autos.rename(columns={'odometer':'odometer_km'}, inplace=True)

# eliminando outlines da coluna prices
autos = autos[autos.price.between(1,350000)]

# visualizando valores de datas
autos['date_crawled'].str[:10].value_counts(normalize=True, dropna=False).sort_index()
autos['ad_created'].str[:10].value_counts(normalize=True, dropna=False).sort_index()
autos['last_seen'].str[:10].value_counts(normalize=True, dropna=False).sort_index()

# eliminando outlines da coluna registration_year
autos = autos[autos.registration_year.between(1910,2016)]

# pegando as 20 primeiras marcas que mais aparecem no conjunto de dados
first_20_brands = autos.brand.value_counts().head(20).index

# agregando os valores da média de preços e quilometragem das 20 marcas
dict_agg_brand={}
dict_agg_km={}
for brand in first_20_brands:
    mean_price_brand = autos[autos['brand']==brand]['price'].mean()
    mean_km_brand = autos[autos['brand']==brand]['odometer_km'].mean()
    dict_agg_brand[brand]=mean_price_brand
    dict_agg_km[brand]=mean_km_brand

# transformando o dict em Serie
brand_mean_series = pd.Series(dict_agg_brand)
km_mean_series = pd.Series(dict_agg_km)

# transformando as Series em DataFrame
df_brand_mean = pd.DataFrame(brand_mean_series, columns=['mean_price'])
df_brand_mean['mean_km'] = km_mean_series

# observando o dataframe, a media de quilometragem não tem relação com a média de preços
print('finalizou')
