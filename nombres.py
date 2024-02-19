import pandas as pd

data = ['data/champions-league-2017.csv', 'data/champions-league-2018.csv', 'data/champions-league-2019.csv', 'data/champions-league-2020.csv', 'data/champions-league-2021.csv', 'data/champions-league-2022.csv']

# Atletico Madrid', 'Atlético', 'Atlético Madrid', 'Atlético de Madrid' por 'Atlético Madrid'
for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Atletico Madrid', 'Atlético', 'Atlético de Madrid'], 'Atlético Madrid')
    df['Away Team'] = df['Away Team'].replace(
        ['Atletico Madrid', 'Atlético', 'Atlético de Madrid'], 'Atlético Madrid')
    df.to_csv(data[i], index=False)

# FC Bayern Munich', 'Bayern Munich', 'Bayern' por 'Bayern München'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Bayern Munich', 'Bayern Munich', 'Bayern'], 'Bayern München')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Bayern Munich', 'Bayern Munich', 'Bayern'], 'Bayern München')
    df.to_csv(data[i], index=False)

# 'Borussia Dortmund', 'Dortmund' por 'Borussia Dortmund'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Borussia Dortmund', 'Dortmund'], 'Borussia Dortmund')
    df['Away Team'] = df['Away Team'].replace(
        ['Borussia Dortmund', 'Dortmund'], 'Borussia Dortmund')
    df.to_csv(data[i], index=False)

# 'CSKA Moscow', 'CSKA Moskva' por 'CSKA Moscow'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['CSKA Moscow', 'CSKA Moskva'], 'CSKA Moscow')
    df['Away Team'] = df['Away Team'].replace(
        ['CSKA Moscow', 'CSKA Moskva'], 'CSKA Moscow')
    df.to_csv(data[i], index=False)

# 'Galatasaray', 'Galatasaray Istanbul' por 'Galatasaray'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Galatasaray', 'Galatasaray Istanbul'], 'Galatasaray')
    df['Away Team'] = df['Away Team'].replace(
        ['Galatasaray', 'Galatasaray Istanbul'], 'Galatasaray')
    df.to_csv(data[i], index=False)

# 'Leverkusen', 'Bayer Leverkusen' por 'Bayer Leverkusen'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Leverkusen', 'Bayer Leverkusen'], 'Bayer Leverkusen')
    df['Away Team'] = df['Away Team'].replace(
        ['Leverkusen', 'Bayer Leverkusen'], 'Bayer Leverkusen')
    df.to_csv(data[i], index=False)

# FC Porto', 'Porto' por 'FC Porto'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Porto', 'Porto'], 'FC Porto')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Porto', 'Porto'], 'FC Porto')
    df.to_csv(data[i], index=False)

# 'FC Barcelona', 'Barcelona' por 'FC Barcelona'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Barcelona', 'Barcelona'], 'FC Barcelona')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Barcelona', 'Barcelona'], 'FC Barcelona')
    df.to_csv(data[i], index=False)

# 'FC Basel', 'Basel' por 'FC Basel'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Basel', 'Basel'], 'FC Basel')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Basel', 'Basel'], 'FC Basel')
    df.to_csv(data[i], index=False)

# 'FC Schalke 04', 'Schalke 04', 'Schalke' por 'Schalke 04'

for i in range(len(data)):

    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Schalke 04', 'Schalke 04', 'Schalke'], 'Schalke 04')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Schalke 04', 'Schalke 04', 'Schalke'], 'Schalke 04')
    df.to_csv(data[i], index=False)

# 'FC Zenit', 'Zenit' por 'Zenit St. Petersburg'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['FC Zenit', 'Zenit'], 'Zenit St. Petersburg')
    df['Away Team'] = df['Away Team'].replace(
        ['FC Zenit', 'Zenit'], 'Zenit St. Petersburg')
    df.to_csv(data[i], index=False)

# 'Juventus', 'Juventus Turin' por 'Juventus'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Juventus', 'Juventus Turin'], 'Juventus')
    df['Away Team'] = df['Away Team'].replace(
        ['Juventus', 'Juventus Turin'], 'Juventus')
    df.to_csv(data[i], index=False)

# 'Manchester City', 'Manchester City FC', 'Man City', 'Man. City' por 'Manchester City'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Manchester City', 'Manchester City FC', 'Man City', 'Man. City'], 'Manchester City')
    df['Away Team'] = df['Away Team'].replace(
        ['Manchester City', 'Manchester City FC', 'Man City', 'Man. City'], 'Manchester City')
    df.to_csv(data[i], index=False)

# 'Manchester United', 'Man United', 'Man. United', 'Manchester United FC' por 'Manchester United'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Manchester United', 'Man United', 'Man. United', 'Manchester United FC'], 'Manchester United')
    df['Away Team'] = df['Away Team'].replace(
        ['Manchester United', 'Man United', 'Man. United', 'Manchester United FC'], 'Manchester United')
    df.to_csv(data[i], index=False)

# 'Olympiakos', 'Olympiakos Piraeus' por 'Olympiakos Piraeus'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Olympiakos', 'Olympiakos Piraeus'], 'Olympiakos Piraeus')
    df['Away Team'] = df['Away Team'].replace(
        ['Olympiakos', 'Olympiakos Piraeus'], 'Olympiakos Piraeus')
    df.to_csv(data[i], index=False)

# 'Inter", "Internazionale' por 'Internazionale"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Inter', 'Internazionale'], 'Internazionale')
    df['Away Team'] = df['Away Team'].replace(
        ['Inter', 'Internazionale'], 'Internazionale')
    df.to_csv(data[i], index=False)

# 'Milan', 'AC Milan' por 'AC Milan"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Milan', 'AC Milan'], 'AC Milan')
    df['Away Team'] = df['Away Team'].replace(
        ['Milan', 'AC Milan'], 'AC Milan')
    df.to_csv(data[i], index=False)

# Tottenham', 'Tottenham Hotspur' por 'Tottenham Hotspur'

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Tottenham', 'Tottenham Hotspur'], 'Tottenham Hotspur')
    df['Away Team'] = df['Away Team'].replace(
        ['Tottenham', 'Tottenham Hotspur'], 'Tottenham Hotspur')
    df.to_csv(data[i], index=False)

# Monaco', 'AS Monaco' por 'AS Monaco"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Monaco', 'AS Monaco'], 'AS Monaco')
    df['Away Team'] = df['Away Team'].replace(
        ['Monaco', 'AS Monaco'], 'AS Monaco')
    df.to_csv(data[i], index=False)

# 'Borussia Mönchengladbach', 'Mönchengladbach' por 'Borussia Mönchengladbach"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Borussia Mönchengladbach', 'Mönchengladbach'], 'Borussia Mönchengladbach')
    df['Away Team'] = df['Away Team'].replace(
        ['Borussia Mönchengladbach', 'Mönchengladbach'], 'Borussia Mönchengladbach')
    df.to_csv(data[i], index=False)

# 'Paris Saint-Germain', 'Paris SG', 'PSG' por 'Paris Saint-Germain"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Paris Saint-Germain', 'Paris SG', 'PSG'], 'Paris Saint-Germain')
    df['Away Team'] = df['Away Team'].replace(
        ['Paris Saint-Germain', 'Paris SG', 'PSG'], 'Paris Saint-Germain')
    df.to_csv(data[i], index=False)

# 'Real Madrid', 'Real Madrid CF' por 'Real Madrid"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Real Madrid', 'Real Madrid CF'], 'Real Madrid')
    df['Away Team'] = df['Away Team'].replace(
        ['Real Madrid', 'Real Madrid CF'], 'Real Madrid')
    df.to_csv(data[i], index=False)

# 'Roma', 'AS Roma' por 'AS Roma"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Roma', 'AS Roma'], 'AS Roma')
    df['Away Team'] = df['Away Team'].replace(
        ['Roma', 'AS Roma'], 'AS Roma')
    df.to_csv(data[i], index=False)

# 'Sevilla', 'Sevilla FC' por 'Sevilla"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Sevilla', 'Sevilla FC'], 'Sevilla')
    df['Away Team'] = df['Away Team'].replace(
        ['Sevilla', 'Sevilla FC'], 'Sevilla')
    df.to_csv(data[i], index=False)

# 'Shakhtar Donetsk', 'Shakhtar' por 'Shakhtar Donetsk"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Shakhtar Donetsk', 'Shakhtar'], 'Shakhtar Donetsk')
    df['Away Team'] = df['Away Team'].replace(
        ['Shakhtar Donetsk', 'Shakhtar'], 'Shakhtar Donetsk')
    df.to_csv(data[i], index=False)

# 'Valencia', 'Valencia CF' por 'Valencia"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Valencia', 'Valencia CF'], 'Valencia')
    df['Away Team'] = df['Away Team'].replace(
        ['Valencia', 'Valencia CF'], 'Valencia')
    df.to_csv(data[i], index=False)

# 'Lepizig', 'RB Leipzig' por 'RB Leipzig"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Lepizig', 'RB Leipzig'], 'RB Leipzig')
    df['Away Team'] = df['Away Team'].replace(
        ['Lepizig', 'RB Leipzig'], 'RB Leipzig')
    df.to_csv(data[i], index=False)

# 'Atalanta', 'Atalanta BC' por 'Atlantas Klaipeda"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Atalanta', 'Atalanta BC'], 'Atlantas Klaipeda')
    df['Away Team'] = df['Away Team'].replace(
        ['Atalanta', 'Atalanta BC'], 'Atlantas Klaipeda')
    df.to_csv(data[i], index=False)

# 'Ajax', 'AFC Ajax' por 'Ajax"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(['Ajax', 'AFC Ajax'], 'Ajax')
    df['Away Team'] = df['Away Team'].replace(['Ajax', 'AFC Ajax'], 'Ajax')
    df.to_csv(data[i], index=False)

# 'Benfica', 'SL Benfica' por 'Benfica"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Benfica', 'SL Benfica'], 'Benfica')
    df['Away Team'] = df['Away Team'].replace(
        ['Benfica', 'SL Benfica'], 'Benfica')
    df.to_csv(data[i], index=False)

# 'APOEL', 'APOEL Nicosia', 'apoel' por 'APOEL Nicosia"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['APOEL', 'APOEL Nicosia', 'apoel'], 'APOEL Nicosia')
    df['Away Team'] = df['Away Team'].replace(
        ['APOEL', 'APOEL Nicosia', 'apoel'], 'APOEL Nicosia')
    df.to_csv(data[i], index=False)

# 'PSV', 'PSV Eindhoven' por 'PSV Eindhoven"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['PSV', 'PSV Eindhoven'], 'PSV Eindhoven')
    df['Away Team'] = df['Away Team'].replace(
        ['PSV', 'PSV Eindhoven'], 'PSV Eindhoven')
    df.to_csv(data[i], index=False)

# 'Malmo', 'Malmö', 'Malmö FF' por 'Malmo FF"

for i in range(len(data)):
    df = pd.read_csv(data[i])
    df['Home Team'] = df['Home Team'].replace(
        ['Malmo', 'Malmö', 'Malmö FF'], 'Malmo FF')
    df['Away Team'] = df['Away Team'].replace(
        ['Malmo', 'Malmö', 'Malmö FF'], 'Malmo FF')
    df.to_csv(data[i], index=False)