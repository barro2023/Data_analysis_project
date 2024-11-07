import pandas as pd
import matplotlib.pyplot as plt

#chargement du fichier
netflix_data = pd.read_csv('~/Téléchargements/netflix1.csv',nrows=30)

#Afficher les premières lignes du dataset
print("Données netflix1:")
print(netflix_data.head())
print(netflix_data.describe())
print(netflix_data.info())
print(netflix_data.tail())

#Identification des messages clés
'''
La diversité des origines des contenus.
Les classifications d'ages prédominantes.
Les genres les plus répresentés.
'''

#Histoire
'''
Il était une fois, dans le vaste royaume du streaming, 
un monde magique appelé Netflix. Ce royaume était unique en son genre, 
car il abritait une immense diversité de contenus, une véritable mosaïque culturelle.

En commençant notre aventure, nous sommes transportés au Brésil, 
où le réalisateur Bruno Garotti nous invite à découvrir un monde 
plein de rires et de féerie. À travers sa production en septembre 2021, 
il nous présente un film familial, plein de magie, classé TV-PG, une expérience que toute la famille peut partager.

En poursuivant notre voyage, nous traversons les États-Unis, 
où Kirsten Johnson nous emmène dans un documentaire captivant intitulé 
"Dick Johnson Is Dead". Sorti en 2020, ce film, classé PG-13,
nous offre une perspective unique sur la vie et la mort, tout en explorant les thèmes universels de l'amour et de la perte.

Nous faisons ensuite une escale en France avec Julien Leclercq,
qui nous plonge dans l'univers sombre et mystérieux de "Ganglands". 
Cette série, classée TV-MA, nous transporte dans le monde du crime, 
offrant une expérience immersive entre suspense et action, une véritable exploration 
des recoins les plus secrets de la société.

De retour aux États-Unis, nous sommes accueillis par le réalisateur Mike Flanagan
, qui nous guide à travers les ruelles sombres de "Midnight Mass". Cette série, 
classée TV-MA, promet une aventure passionnante, mêlant drame, horreur et mystère, 
une véritable plongée dans l'inconnu.
'''

# Création du graphique
plt.figure(figsize=(10, 6))
plt.bar(netflix_data['title'], netflix_data['duration'], color='skyblue')
plt.xlabel('Titres des Films')
plt.ylabel('Durée (en minutes)')
plt.title('Durée des Films dans le Dataset Netflix')
# Rotation des étiquettes pour une meilleure lisibilité
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.50)  
plt.show()
