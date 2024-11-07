import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

CO2_data = pd.read_csv('~/Téléchargements/CO2 emission by countries.csv',encoding='latin-1', nrows=1000)

#Affichage des informations
print("Données de CO2 : ")
print(CO2_data.head())
print(CO2_data.describe())
print(CO2_data.info())
print(CO2_data.tail())

#Identification des messages clés.
'''
Analyser les émissions de CO2 au fil des années
Comparer l'émission de  CO2 entre différents pays
Correler la population avec  l'émission de CO2
Distribuer des émissions de CO2 par habitant
'''

#Histoire
'''
Analyse des émissions de CO2 au fil du temps :
Utilisez un graphique en ligne pour montrer comment les émissions 
de CO2 varient au fil des années pour un ou plusieurs pays.
Axe des x : Années, Axe des y : Émissions de CO2 (Tons)
Comparaison des émissions de CO2 entre différents pays :

Utilisez un diagramme à barres pour comparer les émissions de CO2 entre plusieurs pays.
Axe des x : Pays, Axe des y : Émissions de CO2 (Tons)
Corrélation entre la population et les émissions de CO2 :

Utilisez un nuage de points pour montrer s'il existe une corrélation
 entre la population d'un pays et ses émissions de CO2.
Axe des x : Population, Axe des y : Émissions de CO2 (Tons)
Distribution des émissions de CO2 par habitant :

Utilisez un histogramme pour montrer comment les émissions de CO2 par habitant sont réparties.
Axe des x : Émissions de CO2 par habitant, Axe des y : Fréquence
'''

#Representation

# Sélection des données pour les dix premiers pays du dataset
top_countries_data = CO2_data.groupby('Country').head(10)

# Création de la figure avec des sous-graphiques
fig, axs = plt.subplots(len(top_countries_data['Country'].unique()), 1, figsize=(10, 20), sharex=True)

for i, (country, data) in enumerate(top_countries_data.groupby('Country')):
    ax = axs[i]
    
    # Plot pour les émissions de CO2
    ax.bar(data['Year'], data['CO2 emission (Tons)'], color='blue', alpha=0.7, label='CO2 emission (Tons)')
    ax.set_ylabel('CO2 émis (Tons)')
    
    # Convertir les colonnes 'Year' et 'Population(2022)' en tableaux NumPy
    year_values = data['Year'].values
    population_values = data['Population(2022)'].values
    
    # Création d'un deuxième axe pour la population
    ax2 = ax.twinx()
    ax2.plot(year_values, population_values, color='green', marker='o', label='Population')
    ax2.set_ylabel('Population', color='green')
    
    # Ajout d'une légende pour le premier axe
    ax.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
    
    # Ajout d'un titre pour chaque sous-graphique
    ax.set_title(f'Données pour {country}')

# Ajout d'une légende commune pour tout le graphique
plt.subplots_adjust(top=0.9, hspace=0.5)
plt.show()
