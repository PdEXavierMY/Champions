import pandas

df2017 = pandas.read_csv('data/champions-league-2017-CentralEuropeanStandardTime.csv')
df2018 = pandas.read_csv('data/champions-league-2018-WEuropeStandardTime.csv')
df2019 = pandas.read_csv('data/champions-league-2019-WEuropeStandardTime.csv')
df2020 = pandas.read_csv('data/champions-league-2020-UTC.csv')
df2021 = pandas.read_csv('data/champions-league-2021-UTC.csv')
df2022 = pandas.read_csv('data/champions-league-2022-UTC.csv')
df2023 = pandas.read_csv('data/champions-league-2023-UTC.csv')

# Eliminar las columnas que no interesan de los DataFrames (Date, Location, Group)

df2017 = df2017.drop(["Date", "Location", "Group"], axis=1)
df2018 = df2018.drop(["Date", "Location", "Group"], axis=1)
df2019 = df2019.drop(["Date", "Location", "Group"], axis=1)
df2020 = df2020.drop(["Date", "Location", "Group"], axis=1)
df2021 = df2021.drop(["Date", "Location", "Group"], axis=1)
df2022 = df2022.drop(["Date", "Location", "Group"], axis=1)
df2023 = df2023.drop(["Date", "Location", "Group"], axis=1)

# Añade la columna 'Winner' basada en la columna 'Result'
df2017['Winner'] = df2017.apply(lambda row: row['Home Team'] if int(row['Result'].split(' - ')[0]) > int(row['Result'].split(' - ')[1]) else row['Away Team'], axis=1)
df2018['Winner'] = df2018.apply(lambda row: row['Home Team'] if int(row['Result'].split(' - ')[0]) > int(row['Result'].split(' - ')[1]) else row['Away Team'], axis=1)
df2019['Winner'] = df2019.apply(lambda row: row['Home Team'] if int(row['Result'].split(' - ')[0]) > int(row['Result'].split(' - ')[1]) else row['Away Team'], axis=1)
df2020['Winner'] = df2020.apply(lambda row: row['Home Team'] if int(row['Result'].split(' - ')[0]) > int(row['Result'].split(' - ')[1]) else row['Away Team'], axis=1)
df2021['Winner'] = df2021.apply(lambda row: row['Home Team'] if int(row['Result'].split(' - ')[0]) > int(row['Result'].split(' - ')[1]) else row['Away Team'], axis=1)
df2022['Winner'] = df2022.apply(lambda row: row['Home Team'] if int(row['Result'].split(' - ')[0]) > int(row['Result'].split(' - ')[1]) else row['Away Team'], axis=1)

print(df2017)