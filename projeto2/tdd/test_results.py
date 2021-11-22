'''
Autora: Mariana Queiroz
Data: Nov. 2021
Arquivo de teste para usar o pytest.
'''
# importando bibliotecas
from euro import rolling_mean,read_data

def test_read_data():
    read_data("file.csv")

def test_rolling_mean():
    df = read_data("~/Documentos/MLOps-DCA0305/projeto2/euro-daily-hist_1999_2020.csv")
    df = df[['[US dollar ]','Period\\Unit:']]
    df = df[df['[US dollar ]'] != '-']
    rolling_mean(df, '[US dollar ]', 30)
