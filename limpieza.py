import pandas

df2017 = pandas.read_csv('data/champions-league-2017-CentralEuropeanStandardTime.csv')
df2018 = pandas.read_csv('data/champions-league-2018-WEuropeStandardTime.csv')
df2019 = pandas.read_csv('data/champions-league-2019-WEuropeStandardTime.csv')
df2020 = pandas.read_csv('data/champions-league-2020-UTC.csv')
df2021 = pandas.read_csv('data/champions-league-2021-UTC.csv')
df2022 = pandas.read_csv('data/champions-league-2022-UTC.csv')
wins = pandas.read_csv('data/wins.csv')

#saca la suma de todos los valores de la columna 'Champions'
print(wins['Champions'].sum())