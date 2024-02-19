import pandas as pd

data = ['data/champions-league-2017.csv', 'data/champions-league-2018.csv', 'data/champions-league-2019.csv', 'data/champions-league-2020.csv', 'data/champions-league-2021.csv', 'data/champions-league-2022.csv']

# Atletico Madrid', 'Atlético', 'Atlético Madrid', 'Atlético de Madrid' por 'Atlético Madrid'
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Atletico Madrid', 'Atlético', 'Atlético de Madrid'], 'Atlético Madrid')
    df['Away Team'] = df['Away Team'].replace(
        ['Atletico Madrid', 'Atlético', 'Atlético de Madrid'], 'Atlético Madrid')
    df['Winner'] = df['Winner'].replace(
        ['Atletico Madrid', 'Atlético', 'Atlético de Madrid'], 'Atlético Madrid')
    df.to_csv(data[i], index=False)

# FC Bayern Munich', 'Bayern Munich', 'Bayern' por 'Bayern München'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Bayern Munich', 'Bayern Munich', 'Bayern'], 'Bayern München')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Bayern Munich', 'Bayern Munich', 'Bayern'], 'Bayern München')
    df['Winner'] = df['Winner'].replace(
        ['FC Bayern Munich', 'Bayern Munich', 'Bayern'], 'Bayern München')
    df.to_csv(data[i], index=False)

# 'Borussia Dortmund', 'Dortmund' por 'Borussia Dortmund'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Borussia Dortmund', 'Dortmund'], 'Borussia Dortmund')
    df['Away Team'] = df['Away Team'].replace(
        ['Borussia Dortmund', 'Dortmund'], 'Borussia Dortmund')
    df['Winner'] = df['Winner'].replace(
        ['Borussia Dortmund', 'Dortmund'], 'Borussia Dortmund')
    df.to_csv(data[i], index=False)

# 'CSKA Moscow', 'CSKA Moskva' por 'CSKA Moscow'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['CSKA Moscow', 'CSKA Moskva'], 'CSKA Moscow')
    df['Away Team'] = df['Away Team'].replace(
        ['CSKA Moscow', 'CSKA Moskva'], 'CSKA Moscow')
    df['Winner'] = df['Winner'].replace(
        ['CSKA Moscow', 'CSKA Moskva'], 'CSKA Moscow')
    df.to_csv(data[i], index=False)

# 'Galatasaray', 'Galatasaray Istanbul' por 'Galatasaray'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Galatasaray', 'Galatasaray Istanbul'], 'Galatasaray')
    df['Away Team'] = df['Away Team'].replace(
        ['Galatasaray', 'Galatasaray Istanbul'], 'Galatasaray')
    df['Winner'] = df['Winner'].replace(
        ['Galatasaray', 'Galatasaray Istanbul'], 'Galatasaray')
    df.to_csv(data[i], index=False)

# 'Leverkusen', 'Bayer Leverkusen' por 'Bayer Leverkusen'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Leverkusen', 'Bayer Leverkusen'], 'Bayer Leverkusen')
    df['Away Team'] = df['Away Team'].replace(
        ['Leverkusen', 'Bayer Leverkusen'], 'Bayer Leverkusen')
    df['Winner'] = df['Winner'].replace(
        ['Leverkusen', 'Bayer Leverkusen'], 'Bayer Leverkusen')
    df.to_csv(data[i], index=False)

# FC Porto', 'Porto' por 'FC Porto'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Porto', 'Porto'], 'FC Porto')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Porto', 'Porto'], 'FC Porto')
    df['Winner'] = df['Winner'].replace(
        ['FC Porto', 'Porto'], 'FC Porto')
    df.to_csv(data[i], index=False)

# 'FC Barcelona', 'Barcelona' por 'FC Barcelona'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Barcelona', 'Barcelona'], 'FC Barcelona')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Barcelona', 'Barcelona'], 'FC Barcelona')
    df['Winner'] = df['Winner'].replace(
        ['FC Barcelona', 'Barcelona'], 'FC Barcelona')
    df.to_csv(data[i], index=False)

# 'FC Basel', 'Basel' por 'FC Basel'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Basel', 'Basel'], 'FC Basel')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Basel', 'Basel'], 'FC Basel')
    df['Winner'] = df['Winner'].replace(
        ['FC Basel', 'Basel'], 'FC Basel')
    df.to_csv(data[i], index=False)

# 'FC Schalke 04', 'Schalke 04', 'Schalke' por 'Schalke 04'

for i in range(len(data)):

    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Schalke 04', 'Schalke 04', 'Schalke'], 'Schalke 04')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Schalke 04', 'Schalke 04', 'Schalke'], 'Schalke 04')
    df['Winner'] = df['Winner'].replace(
        ['FC Schalke 04', 'Schalke 04', 'Schalke'], 'Schalke 04')
    df.to_csv(data[i], index=False)

# 'FC Zenit', 'Zenit' por 'Zenit St. Petersburg'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Zenit', 'Zenit'], 'Zenit St. Petersburg')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Zenit', 'Zenit'], 'Zenit St. Petersburg')
    df['Winner'] = df['Winner'].replace(
        ['FC Zenit', 'Zenit'], 'Zenit St. Petersburg')
    df.to_csv(data[i], index=False)

# 'Juventus', 'Juventus Turin' por 'Juventus'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Juventus', 'Juventus Turin'], 'Juventus')
    df['Away Team'] = df['Away Team'].replace(
        ['Juventus', 'Juventus Turin'], 'Juventus')
    df['Winner'] = df['Winner'].replace(
        ['Juventus', 'Juventus Turin'], 'Juventus')
    df.to_csv(data[i], index=False)

# 'Manchester City', 'Manchester City FC', 'Man City', 'Man. City' por 'Manchester City'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Manchester City', 'Manchester City FC', 'Man City', 'Man. City'], 'Manchester City')
    df['Away Team'] = df['Away Team'].replace(
        ['Manchester City', 'Manchester City FC', 'Man City', 'Man. City'], 'Manchester City')
    df['Winner'] = df['Winner'].replace(
        ['Manchester City', 'Manchester City FC', 'Man City', 'Man. City'], 'Manchester City')
    df.to_csv(data[i], index=False)

# 'Manchester United', 'Man United', 'Man. United', 'Manchester United FC' por 'Manchester United'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Manchester United', 'Man United', 'Man. United', 'Manchester United FC'], 'Manchester United')
    df['Away Team'] = df['Away Team'].replace(
        ['Manchester United', 'Man United', 'Man. United', 'Manchester United FC'], 'Manchester United')
    df['Winner'] = df['Winner'].replace(
        ['Manchester United', 'Man United', 'Man. United', 'Manchester United FC'], 'Manchester United')
    df.to_csv(data[i], index=False)

# 'Olympiakos', 'Olympiakos Piraeus' por 'Olympiakos Piraeus'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Olympiakos', 'Olympiakos Piraeus', 'Olympiacos'], 'Olympiakos Piraeus')
    df['Away Team'] = df['Away Team'].replace(
        ['Olympiakos', 'Olympiakos Piraeus', 'Olympiacos'], 'Olympiakos Piraeus')
    df['Winner'] = df['Winner'].replace(
        ['Olympiakos', 'Olympiakos Piraeus', 'Olympiacos'], 'Olympiakos Piraeus')
    df.to_csv(data[i], index=False)

# 'Inter", "Internazionale' por 'Internazionale"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Inter', 'Internazionale'], 'Internazionale')
    df['Away Team'] = df['Away Team'].replace(
        ['Inter', 'Internazionale'], 'Internazionale')
    df['Winner'] = df['Winner'].replace(
        ['Inter', 'Internazionale'], 'Internazionale')
    df.to_csv(data[i], index=False)

# 'Milan', 'AC Milan' por 'AC Milan"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Milan', 'AC Milan'], 'AC Milan')
    df['Away Team'] = df['Away Team'].replace(
        ['Milan', 'AC Milan'], 'AC Milan')
    df['Winner'] = df['Winner'].replace(
        ['Milan', 'AC Milan'], 'AC Milan')
    df.to_csv(data[i], index=False)

# Tottenham', 'Tottenham Hotspur' por 'Tottenham Hotspur'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Tottenham', 'Tottenham Hotspur'], 'Tottenham Hotspur')
    df['Away Team'] = df['Away Team'].replace(
        ['Tottenham', 'Tottenham Hotspur'], 'Tottenham Hotspur')
    df['Winner'] = df['Winner'].replace(
        ['Tottenham', 'Tottenham Hotspur'], 'Tottenham Hotspur')
    df.to_csv(data[i], index=False)

# Monaco', 'AS Monaco' por 'AS Monaco"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Monaco', 'AS Monaco'], 'AS Monaco')
    df['Away Team'] = df['Away Team'].replace(
        ['Monaco', 'AS Monaco'], 'AS Monaco')
    df['Winner'] = df['Winner'].replace(
        ['Monaco', 'AS Monaco'], 'AS Monaco')
    df.to_csv(data[i], index=False)

# 'Borussia Mönchengladbach', 'Mönchengladbach' por 'Borussia Mönchengladbach"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Borussia Mönchengladbach', 'Mönchengladbach'], 'Borussia Mönchengladbach')
    df['Away Team'] = df['Away Team'].replace(
        ['Borussia Mönchengladbach', 'Mönchengladbach'], 'Borussia Mönchengladbach')
    df['Winner'] = df['Winner'].replace(
        ['Borussia Mönchengladbach', 'Mönchengladbach'], 'Borussia Mönchengladbach')
    df.to_csv(data[i], index=False)

# 'Paris Saint-Germain', 'Paris SG', 'PSG' por 'Paris Saint-Germain"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Paris Saint-Germain', 'Paris SG', 'PSG', 'Paris'], 'Paris Saint-Germain')
    df['Away Team'] = df['Away Team'].replace(
        ['Paris Saint-Germain', 'Paris SG', 'PSG', 'Paris'], 'Paris Saint-Germain')
    df['Winner'] = df['Winner'].replace(
        ['Paris Saint-Germain', 'Paris SG', 'PSG', 'Paris'], 'Paris Saint-Germain')
    df.to_csv(data[i], index=False)

# 'Real Madrid', 'Real Madrid CF' por 'Real Madrid"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Real Madrid', 'Real Madrid CF'], 'Real Madrid')
    df['Away Team'] = df['Away Team'].replace(
        ['Real Madrid', 'Real Madrid CF'], 'Real Madrid')
    df['Winner'] = df['Winner'].replace(
        ['Real Madrid', 'Real Madrid CF'], 'Real Madrid')
    df.to_csv(data[i], index=False)

# 'Roma', 'AS Roma' por 'AS Roma"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Roma', 'AS Roma'], 'AS Roma')
    df['Away Team'] = df['Away Team'].replace(
        ['Roma', 'AS Roma'], 'AS Roma')
    df['Winner'] = df['Winner'].replace(
        ['Roma', 'AS Roma'], 'AS Roma')
    df.to_csv(data[i], index=False)

# 'Sevilla', 'Sevilla FC' por 'Sevilla"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Sevilla', 'Sevilla FC'], 'Sevilla')
    df['Away Team'] = df['Away Team'].replace(
        ['Sevilla', 'Sevilla FC'], 'Sevilla')
    df['Winner'] = df['Winner'].replace(
        ['Sevilla', 'Sevilla FC'], 'Sevilla')
    df.to_csv(data[i], index=False)

# 'Shakhtar Donetsk', 'Shakhtar' por 'Shakhtar Donetsk"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Shakhtar Donetsk', 'Shakhtar'], 'Shakhtar Donetsk')
    df['Away Team'] = df['Away Team'].replace(
        ['Shakhtar Donetsk', 'Shakhtar'], 'Shakhtar Donetsk')
    df['Winner'] = df['Winner'].replace(
        ['Shakhtar Donetsk', 'Shakhtar'], 'Shakhtar Donetsk')
    df.to_csv(data[i], index=False)

# 'Valencia', 'Valencia CF' por 'Valencia"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Valencia', 'Valencia CF'], 'Valencia')
    df['Away Team'] = df['Away Team'].replace(
        ['Valencia', 'Valencia CF'], 'Valencia')
    df['Winner'] = df['Winner'].replace(
        ['Valencia', 'Valencia CF'], 'Valencia')
    df.to_csv(data[i], index=False)

# 'Lepizig', 'RB Leipzig', 'Leipzig' por 'RB Leipzig"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Lepizig', 'RB Leipzig', 'Leipzig'], 'RB Leipzig')
    df['Away Team'] = df['Away Team'].replace(
        ['Lepizig', 'RB Leipzig', 'Leipzig'], 'RB Leipzig')
    df['Winner'] = df['Winner'].replace(
        ['Lepizig', 'RB Leipzig', 'Leipzig'], 'RB Leipzig')
    df.to_csv(data[i], index=False)

# 'Salzburg', 'Red Bull Salzburg' por 'FC Salzburg"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Salzburg', 'Red Bull Salzburg'], 'FC Salzburg')
    df['Away Team'] = df['Away Team'].replace(
        ['Salzburg', 'Red Bull Salzburg'], 'FC Salzburg')
    df['Winner'] = df['Winner'].replace(
        ['Salzburg', 'Red Bull Salzburg'], 'FC Salzburg')
    df.to_csv(data[i], index=False)

# 'Sporting', 'Sporting CP' por 'Sporting CP Lisbon"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Sporting', 'Sporting CP'], 'Sporting CP Lisbon')
    df['Away Team'] = df['Away Team'].replace(
        ['Sporting', 'Sporting CP'], 'Sporting CP Lisbon')
    df['Winner'] = df['Winner'].replace(
        ['Sporting', 'Sporting CP'], 'Sporting CP Lisbon')
    df.to_csv(data[i], index=False)

# 'Lyon', 'Olympique Lyon' por 'Olympique Lyon"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Lyon', 'Olympique Lyon'], 'Olympique Lyon')
    df['Away Team'] = df['Away Team'].replace(
        ['Lyon', 'Olympique Lyon'], 'Olympique Lyon')
    df['Winner'] = df['Winner'].replace(
        ['Lyon', 'Olympique Lyon'], 'Olympique Lyon')
    df.to_csv(data[i], index=False)

# 'Lokomotive Moscow', 'Lokomotiv Moscow', 'Lokomotiv Moskva' por 'Lokomotiv Moscow"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Lokomotive Moscow', 'Lokomotiv Moscow', 'Lokomotiv Moskva'], 'Lokomotiv Moscow')
    df['Away Team'] = df['Away Team'].replace(
        ['Lokomotive Moscow', 'Lokomotiv Moscow', 'Lokomotiv Moskva'], 'Lokomotiv Moscow')
    df['Winner'] = df['Winner'].replace(
        ['Lokomotive Moscow', 'Lokomotiv Moscow', 'Lokomotiv Moskva'], 'Lokomotiv Moscow')
    df.to_csv(data[i], index=False)

# 'Plzen', 'Viktoria Plzen' por 'Viktoria Plzen"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Plzen', 'Viktoria Plzen'], 'Viktoria Plzen')
    df['Away Team'] = df['Away Team'].replace(
        ['Plzen', 'Viktoria Plzen'], 'Viktoria Plzen')
    df['Winner'] = df['Winner'].replace(
        ['Plzen', 'Viktoria Plzen'], 'Viktoria Plzen')
    df.to_csv(data[i], index=False)

# 'LOSC', 'Lille' por 'Lille OSC"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['LOSC', 'Lille'], 'Lille OSC')
    df['Away Team'] = df['Away Team'].replace(
        ['LOSC', 'Lille'], 'Lille OSC')
    df['Winner'] = df['Winner'].replace(
        ['LOSC', 'Lille'], 'Lille OSC')
    df.to_csv(data[i], index=False)

# 'Hoffenheim', 'TSG Hoffenheim' por '1899 Hoffenheim"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Hoffenheim', 'TSG Hoffenheim'], '1899 Hoffenheim')
    df['Away Team'] = df['Away Team'].replace(
        ['Hoffenheim', 'TSG Hoffenheim'], '1899 Hoffenheim')
    df['Winner'] = df['Winner'].replace(
        ['Hoffenheim', 'TSG Hoffenheim'], '1899 Hoffenheim')
    df.to_csv(data[i], index=False)

# 'Marseille', 'Olympique Marseille' por 'Olympique Marseille"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Marseille', 'Olympique Marseille'], 'Olympique Marseille')
    df['Away Team'] = df['Away Team'].replace(
        ['Marseille', 'Olympique Marseille'], 'Olympique Marseille')
    df['Winner'] = df['Winner'].replace(
        ['Marseille', 'Olympique Marseille'], 'Olympique Marseille')
    df.to_csv(data[i], index=False)

# 'Sheriff Tiraspol', 'Sheriff' por 'Sheriff Tiraspol"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Sheriff Tiraspol', 'Sheriff'], 'Sheriff Tiraspol')
    df['Away Team'] = df['Away Team'].replace(
        ['Sheriff Tiraspol', 'Sheriff'], 'Sheriff Tiraspol')
    df['Winner'] = df['Winner'].replace(
        ['Sheriff Tiraspol', 'Sheriff'], 'Sheriff Tiraspol')
    df.to_csv(data[i], index=False)

# 'M. Haifa', 'Maccabi Haifa' por 'Maccabi Haifa"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['M. Haifa', 'Maccabi Haifa'], 'Maccabi Haifa')
    df['Away Team'] = df['Away Team'].replace(
        ['M. Haifa', 'Maccabi Haifa'], 'Maccabi Haifa')
    df['Winner'] = df['Winner'].replace(
        ['M. Haifa', 'Maccabi Haifa'], 'Maccabi Haifa')
    df.to_csv(data[i], index=False)

# 'Frankfurt', 'Eintracht Frankfurt' por 'Eintracht Frankfurt"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Frankfurt', 'Eintracht Frankfurt'], 'Eintracht Frankfurt')
    df['Away Team'] = df['Away Team'].replace(
        ['Frankfurt', 'Eintracht Frankfurt'], 'Eintracht Frankfurt')
    df['Winner'] = df['Winner'].replace(
        ['Frankfurt', 'Eintracht Frankfurt'], 'Eintracht Frankfurt')
    df.to_csv(data[i], index=False)

# 'Krasnodar', 'FC Krasnodar' por 'FK Krasnodar"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Krasnodar', 'FC Krasnodar'], 'FK Krasnodar')
    df['Away Team'] = df['Away Team'].replace(
        ['Krasnodar', 'FC Krasnodar'], 'FK Krasnodar')
    df['Winner'] = df['Winner'].replace(
        ['Krasnodar', 'FC Krasnodar'], 'FK Krasnodar')
    df.to_csv(data[i], index=False)

# 'Genk', 'KRC Genk' por 'Racing Genk"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Genk', 'KRC Genk'], 'Racing Genk')
    df['Away Team'] = df['Away Team'].replace(
        ['Genk', 'KRC Genk'], 'Racing Genk')
    df['Winner'] = df['Winner'].replace(
        ['Genk', 'KRC Genk'], 'Racing Genk')
    df.to_csv(data[i], index=False)

# 'Wolfsburg', 'VfL Wolfsburg' por 'VfL Wolfsburg"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Wolfsburg', 'VfL Wolfsburg'], 'VfL Wolfsburg')
    df['Away Team'] = df['Away Team'].replace(
        ['Wolfsburg', 'VfL Wolfsburg'], 'VfL Wolfsburg')
    df['Winner'] = df['Winner'].replace(
        ['Wolfsburg', 'VfL Wolfsburg'], 'VfL Wolfsburg')
    df.to_csv(data[i], index=False)

# 'Midtjylland', 'FC Midtjylland' por 'FC Midtjylland"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Midtjylland', 'FC Midtjylland'], 'FC Midtjylland')
    df['Away Team'] = df['Away Team'].replace(
        ['Midtjylland', 'FC Midtjylland'], 'FC Midtjylland')
    df['Winner'] = df['Winner'].replace(
        ['Midtjylland', 'FC Midtjylland'], 'FC Midtjylland')
    df.to_csv(data[i], index=False)

# 'Maribor', 'NK Maribor' por 'NK Maribor"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Maribor', 'NK Maribor'], 'NK Maribor')
    df['Away Team'] = df['Away Team'].replace(
        ['Maribor', 'NK Maribor'], 'NK Maribor')
    df['Winner'] = df['Winner'].replace(
        ['Maribor', 'NK Maribor'], 'NK Maribor')
    df.to_csv(data[i], index=False)

# 'Rennes', 'Stade Rennais' por 'Stade Rennais"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Rennes', 'Stade Rennais'], 'Stade Rennais')
    df['Away Team'] = df['Away Team'].replace(
        ['Rennes', 'Stade Rennais'], 'Stade Rennais')
    df['Winner'] = df['Winner'].replace(
        ['Rennes', 'Stade Rennais'], 'Stade Rennais')
    df.to_csv(data[i], index=False)

# 'Qarabag', 'Qarabag Agdam' por 'Qarabag FK"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Qarabag', 'Qarabag Agdam'], 'Qarabag FK')
    df['Away Team'] = df['Away Team'].replace(
        ['Qarabag', 'Qarabag Agdam'], 'Qarabag FK')
    df['Winner'] = df['Winner'].replace(
        ['Qarabag', 'Qarabag Agdam'], 'Qarabag FK')
    df.to_csv(data[i], index=False)

# 'AEK', 'AEK Athens' por 'AEK Athens"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['AEK', 'AEK Athens'], 'AEK Athens')
    df['Away Team'] = df['Away Team'].replace(
        ['AEK', 'AEK Athens'], 'AEK Athens')
    df['Winner'] = df['Winner'].replace(
        ['AEK', 'AEK Athens'], 'AEK Athens')
    df.to_csv(data[i], index=False)

# 'Rangers', 'Rangers FC' por 'Glasgow Rangers"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Rangers', 'Rangers FC'], 'Glasgow Rangers')
    df['Away Team'] = df['Away Team'].replace(
        ['Rangers', 'Rangers FC'], 'Glasgow Rangers')
    df['Winner'] = df['Winner'].replace(
        ['Rangers', 'Rangers FC'], 'Glasgow Rangers')
    df.to_csv(data[i], index=False)

# 'Malmo FF', 'Malmö FF' por 'Malmö FF"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Malmo FF', 'Malmö FF'], 'Malmö FF')
    df['Away Team'] = df['Away Team'].replace(
        ['Malmo FF', 'Malmö FF'], 'Malmö FF')
    df['Winner'] = df['Winner'].replace(
        ['Malmo FF', 'Malmö FF'], 'Malmö FF')
    df.to_csv(data[i], index=False)

# 'Copenhagen', 'FC Copenhagen' por 'FC København"
    
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Copenhagen', 'FC Copenhagen'], 'FC København')
    df['Away Team'] = df['Away Team'].replace(
        ['Copenhagen', 'FC Copenhagen'], 'FC København')
    df['Winner'] = df['Winner'].replace(
        ['Copenhagen', 'FC Copenhagen'], 'FC København')
    df.to_csv(data[i], index=False)

# 'Atalanta', 'Atalanta BC' por 'Atlantas Klaipeda"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Atalanta', 'Atalanta BC'], 'Atlantas Klaipeda')
    df['Away Team'] = df['Away Team'].replace(
        ['Atalanta', 'Atalanta BC'], 'Atlantas Klaipeda')
    df['Winner'] = df['Winner'].replace(
        ['Atalanta', 'Atalanta BC'], 'Atlantas Klaipeda')
    df.to_csv(data[i], index=False)

# 'Ajax', 'AFC Ajax' por 'Ajax"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(['Ajax', 'AFC Ajax'], 'Ajax')
    df['Away Team'] = df['Away Team'].replace(['Ajax', 'AFC Ajax'], 'Ajax')
    df['Winner'] = df['Winner'].replace(['Ajax', 'AFC Ajax'], 'Ajax')
    df.to_csv(data[i], index=False)

# 'Benfica', 'SL Benfica' por 'Benfica"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Benfica', 'SL Benfica'], 'Benfica')
    df['Away Team'] = df['Away Team'].replace(
        ['Benfica', 'SL Benfica'], 'Benfica')
    df['Winner'] = df['Winner'].replace(
        ['Benfica', 'SL Benfica'], 'Benfica')
    df.to_csv(data[i], index=False)

# 'APOEL', 'APOEL Nicosia', 'apoel' por 'APOEL Nicosia"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['APOEL', 'APOEL Nicosia', 'apoel'], 'APOEL Nicosia')
    df['Away Team'] = df['Away Team'].replace(
        ['APOEL', 'APOEL Nicosia', 'apoel'], 'APOEL Nicosia')
    df['Winner'] = df['Winner'].replace(
        ['APOEL', 'APOEL Nicosia', 'apoel'], 'APOEL Nicosia')
    df.to_csv(data[i], index=False)

# 'PSV', 'PSV Eindhoven' por 'PSV Eindhoven"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['PSV', 'PSV Eindhoven'], 'PSV Eindhoven')
    df['Away Team'] = df['Away Team'].replace(
        ['PSV', 'PSV Eindhoven'], 'PSV Eindhoven')
    df['Winner'] = df['Winner'].replace(
        ['PSV', 'PSV Eindhoven'], 'PSV Eindhoven')
    df.to_csv(data[i], index=False)