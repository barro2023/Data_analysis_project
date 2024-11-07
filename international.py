import pandas as pd
import matplotlib.pyplot as plt


#Chargement de la donnée
international_data = pd.read_csv('~/Téléchargements/international_matches.csv',nrows = 1000)

#Affichage des informations de la donnée
print("Données internationale : ")
print(international_data.head())
print(international_data.describe())
print(international_data.info())
print(international_data.tail())

#Messages clé
'''
Performance des équipes à domicile et à l'exterieur
Impact des continents sur les performances
Tournoi et resultats
Performances des équipes
'''

#Histoire
'''
Impact des continents sur les performances
'''

#Répresentation
continent_stats = international_data.groupby('home_team_continent')['home_team_result'].value_counts().unstack().fillna(0)

# Création du graphique à barres empilées
continent_stats.plot(kind='bar', stacked=True)
plt.title('Impact des continents sur les performances')
plt.xlabel('Continent')
plt.ylabel('Nombre de matchs')
plt.subplots_adjust(bottom = 0.25)
plt.show()


