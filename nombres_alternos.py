import pandas as pd

data = ['data/equipos-goles.csv', 'data/victorias.csv', 'data/champions_wins.csv']

# Atletico Madrid', 'Atlético', 'Atlético Madrid', 'Atlético de Madrid' por 'Atlético Madrid'
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Atletico Madrid', 'Atlético', 'Atlético de Madrid'], 'Atlético Madrid')
    df.to_csv(data[i], index=False)

# FC Bayern Munich', 'Bayern Munich', 'Bayern' por 'Bayern München'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['FC Bayern Munich', 'Bayern Munich', 'Bayern'], 'Bayern München')
    df.to_csv(data[i], index=False)

# 'Borussia Dortmund', 'Dortmund' por 'Borussia Dortmund'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Borussia Dortmund', 'Dortmund'], 'Borussia Dortmund')
    df.to_csv(data[i], index=False)

# 'CSKA Moscow', 'CSKA Moskva' por 'CSKA Moscow'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['CSKA Moscow', 'CSKA Moskva'], 'CSKA Moscow')
    df.to_csv(data[i], index=False)

# 'Galatasaray', 'Galatasaray Istanbul' por 'Galatasaray'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Galatasaray', 'Galatasaray Istanbul'], 'Galatasaray')
    df.to_csv(data[i], index=False)

# 'Leverkusen', 'Bayer Leverkusen' por 'Bayer Leverkusen'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Leverkusen', 'Bayer Leverkusen'], 'Bayer Leverkusen')
    df.to_csv(data[i], index=False)

# FC Porto', 'Porto' por 'FC Porto'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['FC Porto', 'Porto'], 'FC Porto')
    df.to_csv(data[i], index=False)

# 'FC Barcelona', 'Barcelona' por 'FC Barcelona'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['FC Barcelona', 'Barcelona'], 'FC Barcelona')
    df.to_csv(data[i], index=False)

# 'FC Basel', 'Basel' por 'FC Basel'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['FC Basel', 'Basel'], 'FC Basel')
    df.to_csv(data[i], index=False)

# 'FC Schalke 04', 'Schalke 04', 'Schalke' por 'Schalke 04'

for i in range(len(data)):

    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['FC Schalke 04', 'Schalke 04', 'Schalke'], 'Schalke 04')
    df.to_csv(data[i], index=False)

# 'FC Zenit', 'Zenit' por 'Zenit St. Petersburg'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['FC Zenit', 'Zenit'], 'Zenit St. Petersburg')
    df.to_csv(data[i], index=False)

# 'Juventus', 'Juventus Turin' por 'Juventus'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Juventus', 'Juventus Turin'], 'Juventus')
    df.to_csv(data[i], index=False)

# 'Manchester City', 'Manchester City FC', 'Man City', 'Man. City' por 'Manchester City'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Manchester City', 'Manchester City FC', 'Man City', 'Man. City'], 'Manchester City')
    df.to_csv(data[i], index=False)

# 'Manchester United', 'Man United', 'Man. United', 'Manchester United FC' por 'Manchester United'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Manchester United', 'Man United', 'Man. United', 'Manchester United FC'], 'Manchester United')
    df.to_csv(data[i], index=False)

# 'Olympiakos', 'Olympiakos Piraeus' por 'Olympiakos Piraeus'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Olympiakos', 'Olympiakos Piraeus', 'Olympiacos'], 'Olympiakos Piraeus')
    df.to_csv(data[i], index=False)

# 'Inter", "Internazionale' por 'Internazionale"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Inter', 'Internazionale'], 'Internazionale')
    df.to_csv(data[i], index=False)

# 'Milan', 'AC Milan' por 'AC Milan"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Milan', 'AC Milan'], 'AC Milan')
    df.to_csv(data[i], index=False)

# Tottenham', 'Tottenham Hotspur' por 'Tottenham Hotspur'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Tottenham', 'Tottenham Hotspur'], 'Tottenham Hotspur')
    df.to_csv(data[i], index=False)

# Monaco', 'AS Monaco' por 'AS Monaco"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Monaco', 'AS Monaco'], 'AS Monaco')
    df.to_csv(data[i], index=False)

# 'Borussia Mönchengladbach', 'Mönchengladbach' por 'Borussia Mönchengladbach"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Borussia Mönchengladbach', 'Mönchengladbach'], 'Borussia Mönchengladbach')
    df.to_csv(data[i], index=False)

# 'Paris Saint-Germain', 'Paris SG', 'PSG' por 'Paris Saint-Germain"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Paris Saint-Germain', 'Paris SG', 'PSG', 'Paris'], 'Paris Saint-Germain')
    df.to_csv(data[i], index=False)

# 'Real Madrid', 'Real Madrid CF' por 'Real Madrid"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Real Madrid', 'Real Madrid CF'], 'Real Madrid')
    df.to_csv(data[i], index=False)

# 'Roma', 'AS Roma' por 'AS Roma"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Roma', 'AS Roma'], 'AS Roma')
    df.to_csv(data[i], index=False)

# 'Sevilla', 'Sevilla FC' por 'Sevilla"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Sevilla', 'Sevilla FC'], 'Sevilla')
    df.to_csv(data[i], index=False)

# 'Shakhtar Donetsk', 'Shakhtar' por 'Shakhtar Donetsk"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Shakhtar Donetsk', 'Shakhtar'], 'Shakhtar Donetsk')
    df.to_csv(data[i], index=False)

# 'Valencia', 'Valencia CF' por 'Valencia"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Valencia', 'Valencia CF'], 'Valencia')
    df.to_csv(data[i], index=False)

# 'Lepizig', 'RB Leipzig', 'Leipzig' por 'RB Leipzig"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Lepizig', 'RB Leipzig', 'Leipzig'], 'RB Leipzig')
    df.to_csv(data[i], index=False)

# 'Salzburg', 'Red Bull Salzburg' por 'FC Salzburg"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Salzburg', 'Red Bull Salzburg'], 'FC Salzburg')
    df.to_csv(data[i], index=False)

# 'Sporting', 'Sporting CP' por 'Sporting CP Lisbon"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Sporting', 'Sporting CP'], 'Sporting CP Lisbon')
    df.to_csv(data[i], index=False)

# 'Lyon', 'Olympique Lyon' por 'Olympique Lyon"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Lyon', 'Olympique Lyon'], 'Olympique Lyon')
    df.to_csv(data[i], index=False)

# 'Lokomotive Moscow', 'Lokomotiv Moscow', 'Lokomotiv Moskva' por 'Lokomotiv Moscow"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Lokomotive Moscow', 'Lokomotiv Moscow', 'Lokomotiv Moskva'], 'Lokomotiv Moscow')
    df.to_csv(data[i], index=False)

# 'Plzen', 'Viktoria Plzen' por 'Viktoria Plzen"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Plzen', 'Viktoria Plzen'], 'Viktoria Plzen')
    df.to_csv(data[i], index=False)

# 'LOSC', 'Lille' por 'Lille OSC"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['LOSC', 'Lille'], 'Lille OSC')
    df.to_csv(data[i], index=False)

# 'Hoffenheim', 'TSG Hoffenheim' por '1899 Hoffenheim"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Hoffenheim', 'TSG Hoffenheim'], '1899 Hoffenheim')
    df.to_csv(data[i], index=False)

# 'Marseille', 'Olympique Marseille' por 'Olympique Marseille"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Marseille', 'Olympique Marseille'], 'Olympique Marseille')
    df.to_csv(data[i], index=False)

# 'Sheriff Tiraspol', 'Sheriff' por 'Sheriff Tiraspol"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Sheriff Tiraspol', 'Sheriff'], 'Sheriff Tiraspol')
    df.to_csv(data[i], index=False)

# 'M. Haifa', 'Maccabi Haifa' por 'Maccabi Haifa"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['M. Haifa', 'Maccabi Haifa'], 'Maccabi Haifa')
    df.to_csv(data[i], index=False)

# 'Frankfurt', 'Eintracht Frankfurt' por 'Eintracht Frankfurt"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Frankfurt', 'Eintracht Frankfurt'], 'Eintracht Frankfurt')
    df.to_csv(data[i], index=False)

# 'Krasnodar', 'FC Krasnodar' por 'FK Krasnodar"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Krasnodar', 'FC Krasnodar'], 'FK Krasnodar')
    df.to_csv(data[i], index=False)

# 'Genk', 'KRC Genk' por 'Racing Genk"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Genk', 'KRC Genk'], 'Racing Genk')
    df.to_csv(data[i], index=False)

# 'Wolfsburg', 'VfL Wolfsburg' por 'VfL Wolfsburg"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Wolfsburg', 'VfL Wolfsburg'], 'VfL Wolfsburg')
    df.to_csv(data[i], index=False)

# 'Midtjylland', 'FC Midtjylland' por 'FC Midtjylland"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Midtjylland', 'FC Midtjylland'], 'FC Midtjylland')
    df.to_csv(data[i], index=False)

# 'Maribor', 'NK Maribor' por 'NK Maribor"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Maribor', 'NK Maribor'], 'NK Maribor')
    df.to_csv(data[i], index=False)

# 'Rennes', 'Stade Rennais' por 'Stade Rennais"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Rennes', 'Stade Rennais'], 'Stade Rennais')
    df.to_csv(data[i], index=False)

# 'Qarabag', 'Qarabag Agdam' por 'Qarabag FK"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Qarabag', 'Qarabag Agdam'], 'Qarabag FK')
    df.to_csv(data[i], index=False)

# 'AEK', 'AEK Athens' por 'AEK Athens"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['AEK', 'AEK Athens'], 'AEK Athens')
    df.to_csv(data[i], index=False)

# 'Rangers', 'Rangers FC' por 'Glasgow Rangers"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Rangers', 'Rangers FC'], 'Glasgow Rangers')
    df.to_csv(data[i], index=False)

# 'Malmo FF', 'Malmö FF' por 'Malmö FF"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Malmo FF', 'Malmö FF'], 'Malmö FF')
    df.to_csv(data[i], index=False)

# 'Copenhagen', 'FC Copenhagen' por 'FC København"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Copenhagen', 'FC Copenhagen'], 'FC København')
    df.to_csv(data[i], index=False)

# 'Atalanta', 'Atalanta BC' por 'Atlantas Klaipeda"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Atalanta', 'Atalanta BC'], 'Atlantas Klaipeda')
    df.to_csv(data[i], index=False)

# 'Ajax', 'AFC Ajax' por 'Ajax"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(['Ajax', 'AFC Ajax'], 'Ajax')
    df.to_csv(data[i], index=False)

# 'Benfica', 'SL Benfica' por 'Benfica"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['Benfica', 'SL Benfica'], 'Benfica')
    df.to_csv(data[i], index=False)

# 'APOEL', 'APOEL Nicosia', 'apoel' por 'APOEL Nicosia"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['APOEL', 'APOEL Nicosia', 'apoel'], 'APOEL Nicosia')
    df.to_csv(data[i], index=False)

# 'PSV', 'PSV Eindhoven' por 'PSV Eindhoven"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Equipo'] = df['Equipo'].replace(
        ['PSV', 'PSV Eindhoven'], 'PSV Eindhoven')
    df.to_csv(data[i], index=False)