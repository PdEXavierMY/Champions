import pandas

df2017 = pandas.read_csv('data/champions-league-2017-CentralEuropeanStandardTime.csv')
df2018 = pandas.read_csv('data/champions-league-2018-WEuropeStandardTime.csv')
df2019 = pandas.read_csv('data/champions-league-2019-WEuropeStandardTime.csv')
df2020 = pandas.read_csv('data/champions-league-2020-UTC.csv')
df2021 = pandas.read_csv('data/champions-league-2021-UTC.csv')
df2022 = pandas.read_csv('data/champions-league-2022-UTC.csv')

# Eliminar las columnas que no interesan de los DataFrames (Date, Location, Group)

df2017 = df2017.drop(["Date", "Location", "Group"], axis=1)
df2018 = df2018.drop(["Date", "Location", "Group"], axis=1)
df2019 = df2019.drop(["Date", "Location", "Group"], axis=1)
df2020 = df2020.drop(["Date", "Location", "Group"], axis=1)
df2021 = df2021.drop(["Date", "Location", "Group"], axis=1)
df2022 = df2022.drop(["Date", "Location", "Group"], axis=1)
