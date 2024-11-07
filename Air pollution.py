#Importation des bibliothèques
import pandas as pd
import matplotlib.pyplot as plt


#Chargement de la donnée
Air_data = pd.read_csv('~/Téléchargements/Air Pollution.csv',nrows=500)


#Affichages des informations
print("Données de la pollution de l'air : ")
print(Air_data.head())
print(Air_data.describe())
print(Air_data.info())
print(Air_data.tail())



#Identification des messages clés
'''
Variation temporelle
Comparaison entre villes
Type de polluants
Couverture temporelle
Mise à jour
'''


#Histoire
'''
Comparaison entre villes:
Representer la pollution entre différentes villes pour une année donnée avec un graphe en barres
'''

# Choisissez une année spécifique, par exemple 2016
year_to_compare = 2016

# Filtrer les données pour l'année choisie
data_for_year = Air_data[Air_data['Year'] == year_to_compare]

# Tracer le graphique en barres comparatif
plt.figure(figsize=(12, 8))

# Barres pour PM2.5
plt.bar(data_for_year['City'], data_for_year["PM2.5 (μg/m3)"], color='blue', label='PM2.5')

# Barres pour PM10
plt.bar(data_for_year['City'], data_for_year['PM10 (μg/m3)'], color='orange', label='PM10')

# Barres pour NO2
plt.bar(data_for_year['City'], data_for_year['NO2 (μg/m3)'], color='green', label='NO2')

# Ajout d'étiquettes et de titres
plt.xlabel('Ville')
plt.ylabel('Concentration (µg/m³)')
plt.title(f'Comparaison de la Pollution entre les Villes en {year_to_compare}')
plt.legend(loc = 'upper right')

# Afficher le graphique
plt.xticks(rotation=45, ha='right')  # Rotation des étiquettes pour une meilleure lisibilité
plt.xticks(range(0, len(data_for_year['City']), 2), data_for_year['City'][::2])
plt.tight_layout()  # Ajustement automatique de la mise en page
plt.subplots_adjust(bottom=0.30)
plt.show()


