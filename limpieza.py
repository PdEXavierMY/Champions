import pandas as pd

df2017 = pd.read_csv('data/champions-league-2017-CentralEuropeanStandardTime.csv')
df2018 = pd.read_csv('data/champions-league-2018-WEuropeStandardTime.csv')
df2019 = pd.read_csv('data/champions-league-2019-WEuropeStandardTime.csv')
df2020 = pd.read_csv('data/champions-league-2020-UTC.csv')
df2021 = pd.read_csv('data/champions-league-2021-UTC.csv')
df2022 = pd.read_csv('data/champions-league-2022-UTC.csv')
df2023 = pd.read_csv('data/champions-league-2023-UTC.csv')

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

#contar los goles totales de cada equipo y partido
def procesar_datos(df):
    # Dividir los goles de cada equipo y crear las nuevas columnas
    df[['Home Team Goals', 'Away Team Goals']] = df['Result'].str.split(' - ', expand=True)
    # Convertir los valores de goles a tipo numérico
    df['Home Team Goals'] = pd.to_numeric(df['Home Team Goals'])
    df['Away Team Goals'] = pd.to_numeric(df['Away Team Goals'])
    # Calcular el total de goles del partido
    df['Match Goals'] = df['Home Team Goals'] + df['Away Team Goals']

procesar_datos(df2017)
procesar_datos(df2018)
procesar_datos(df2019)
procesar_datos(df2020)
procesar_datos(df2021)
procesar_datos(df2022)

# Ver si hay valores nulos
'''
print(df2017.isnull().sum())
print(df2018.isnull().sum())
print(df2019.isnull().sum())
print(df2020.isnull().sum())
print(df2021.isnull().sum())
print(df2022.isnull().sum())
'''
'''
# a csv
df2017.to_csv('data/champions-league-2017.csv', index=False)
df2018.to_csv('data/champions-league-2018.csv', index=False)
df2019.to_csv('data/champions-league-2019.csv', index=False)
df2020.to_csv('data/champions-league-2020.csv', index=False)
df2021.to_csv('data/champions-league-2021.csv', index=False)
df2022.to_csv('data/champions-league-2022.csv', index=False)
'''


# crear un csv de equipos con goles totales segun los datos
diccionario_equipos_goles = {}


def actualizar_diccionario_desde_csv(csv_file, diccionario):
    # Leer el archivo CSV
    df = pd.read_csv(csv_file)
    
    # Iterar sobre cada fila del DataFrame
    for index, row in df.iterrows():
        # Obtener el nombre del equipo local y sus goles
        equipo_local = row['Home Team']
        goles_local = row['Home Team Goals']
        
        # Actualizar el diccionario con los goles del equipo local
        if equipo_local in diccionario:
            diccionario[equipo_local] += goles_local
        else:
            diccionario[equipo_local] = goles_local
        
        # Obtener el nombre del equipo visitante y sus goles
        equipo_visitante = row['Away Team']
        goles_visitante = row['Away Team Goals']
        
        # Actualizar el diccionario con los goles del equipo visitante
        if equipo_visitante in diccionario:
            diccionario[equipo_visitante] += goles_visitante
        else:
            diccionario[equipo_visitante] = goles_visitante
    
    return diccionario

for csv_file in ['data/champions-league-2017.csv', 'data/champions-league-2018.csv', 'data/champions-league-2019.csv', 'data/champions-league-2020.csv', 'data/champions-league-2021.csv', 'data/champions-league-2022.csv']:
    diccionario_equipos_goles = actualizar_diccionario_desde_csv(csv_file, diccionario_equipos_goles)

# ordenar el diccionario de mayor goles a menor
diccionario_equipos_goles = dict(sorted(diccionario_equipos_goles.items(), key=lambda item: item[1], reverse=True))

# pasar el diccionario a un csv con pandas con los campos 'Equipo' y 'Goles'
df_equipos_goles = pd.DataFrame(diccionario_equipos_goles.items(), columns=['Equipo', 'Goles'])
df_equipos_goles.to_csv('data/equipos-goles.csv', index=False)

#ahora vamos a hacer un csv de equipos con su probabilidad de victoria, empate o derrota segun criterios establecidos
#primero sacar otros dos diccionarios con las champions ganadas y el ranking uefa

diccionario_equipos_champions = {}
diccionario_equipos_ranking = {}

def actualizar_equipos_champions(diccionario_equipos_champions, diccionario_equipos_goles):
    # Leer el archivo CSV de victorias de la Champions League
    df_wins = pd.read_csv('data/wins.csv', header=None, names=['Equipo', 'Victorias'])

    # Iterar sobre los equipos en el diccionario de equipos y actualizar los datos de la Champions League
    for equipo, goles in diccionario_equipos_goles.items():
        # Buscar el equipo en el DataFrame de victorias de la Champions League
        victorias_equipo = df_wins[df_wins['Equipo'] == equipo]['Victorias'].values
        if len(victorias_equipo) > 0:
            diccionario_equipos_champions[equipo] = victorias_equipo[0]
        else:
            diccionario_equipos_champions[equipo] = 0
    
    return diccionario_equipos_champions

def actualizar_equipos_ranking(diccionario_equipos_ranking):
    # Leer el archivo CSV del ranking UEFA
    df_uefa_ranking = pd.read_csv('data/UEFA_Ranking.csv')

    # Iterar sobre los equipos en el diccionario de equipos y actualizar los datos del ranking UEFA
    for equipo in diccionario_equipos_ranking.keys():
        # Buscar el equipo en el DataFrame del ranking UEFA
        puntuaje_equipo = df_uefa_ranking[df_uefa_ranking['Club'] == equipo]['Total Points'].values
        if len(puntuaje_equipo) > 0:
            diccionario_equipos_ranking[equipo] = puntuaje_equipo[0]
        else:
            diccionario_equipos_ranking[equipo] = None
    
    return diccionario_equipos_ranking

diccionario_equipos_champions = actualizar_equipos_champions(diccionario_equipos_champions, diccionario_equipos_goles)
diccionario_equipos_ranking = actualizar_equipos_ranking(diccionario_equipos_ranking)

print(diccionario_equipos_champions)
diccionario_equipos_champions = {equipo: int(goles) if isinstance(goles, str) else goles for equipo, goles in diccionario_equipos_champions.items()}

# Sumar los valores en el diccionario
suma = sum(diccionario_equipos_champions.values())

print("La suma de todos los valores en el diccionario es:", suma)
print(diccionario_equipos_ranking)

