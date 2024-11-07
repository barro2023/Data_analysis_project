import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis les fichiers CSV
soccer_data = pd.read_csv('~/Téléchargements/soccer21-22.csv',nrows=25)
weeklyrank_data = pd.read_csv('~/Téléchargements/weeklyrank.csv',nrows=25)

# Afficher les premières lignes des datasets
print("Données Soccer 21-22:")
print(soccer_data.head())
print(soccer_data.tail())

print("\nDonnées Weekly Rank:")
print(weeklyrank_data.head())
print(weeklyrank_data.tail())

print("\Données Soccer 21-22:")
print(soccer_data.describe())
print(weeklyrank_data.info())

print("\nDonnées Weekly Rank:")
print(weeklyrank_data.describe())
print(soccer_data.info())



#Identification des messages clé
'''
(Soccer 21-22 et Weekly Rank):
Corrélation entre les performances et le classement: 
Nous pourrions explorer la corrélation entre les performances (but marqué, but encaissé) 
et le classement hebdomadaire pour voir s'il y a une tendance.
Évolution des performances au fil du temps :
Visualiser comment les performances des équipes influent sur leur classement au fil des semaines.
Impact des fautes, des corners et des cartons :
Examiner si les statistiques de jeu (fautes, corners, cartons) ont un impact sur les résultats et le classement.
'''

#Histoire
'''
_Histoire : "La Course au Sommet"
.Début de la Saison :
Au début de la saison, les équipes entament la compétition avec des performances diverses. 
Certaines ont des débuts percutants, marquant beaucoup de buts et remportant des victoires, 
tandis que d'autres rencontrent des difficultés.
.Impact des Performances sur le Classement :
Nous examinons comment les performances, mesurées par les buts marqués (FTHG) et la différence de buts (GD),
influent sur le classement hebdomadaire. Des équipes ayant une bonne différence de buts sont-elles constamment en haut du classement?
.Tournants de la Saison :
Identifier les semaines clés où des changements significatifs dans le classement ont eu lieu. 
Cela pourrait être dû à des séries de victoires, des revirements de situation ou des performances inattendues.
.Facteurs Influents :
Analyser si des facteurs tels que les fautes, 
les corners et les cartons ont eu un impact sur les résultats et le classement des équipes.
.Les Ténors du Classement :
Suivre les équipes qui ont maintenu une position élevée tout au long de la saison et comprendre ce qui a contribué à leur constance.
.Course pour les Places Européennes ou le Maintien :
Examiner comment la bataille pour les places européennes et la lutte contre la relégation ont évolué au fil des semaines.
.Clôture de la Saison :
Conclure en observant comment les équipes ont consolidé leur position en fin de saison et 
si les résultats des dernières semaines ont eu un impact sur le classement final.
'''

# Fusionner les deux datasets sur la colonne 'Team'
merged_data = pd.merge(soccer_data, weeklyrank_data, left_on=['HomeTeam'], right_on=['Team'])

# Liste de toutes les équipes
teams_list = merged_data['Team'].unique()

# Tracer l'évolution du classement hebdomadaire pour toutes les équipes
plt.figure(figsize=(12, 8))

for team_name in teams_list:
    team_data = merged_data[merged_data['Team'] == team_name]
    plt.plot(team_data['Week'].values, team_data['Rank'].values, label=team_name)

plt.xlabel('Semaine')
plt.ylabel('Classement Hebdomadaire')
plt.title('Évolution du Classement Hebdomadaire pour Toutes les Équipes')
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left')
plt.grid(True)
plt.show()
