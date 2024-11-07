import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#chargement du fichier
World_data = pd.read_csv('~/Téléchargements/World Population Live Dataset.csv')

#Afficher les infos 
print("Données de la population mondiale : ")
print(World_data.head())
print(World_data.describe())
print(World_data.info())
print(World_data.tail())

#Identification des messages clé
'''
La population totale
Les taux de croissance
Les croissances ou decroissances rapides de certains pays
La densité de la population et la taille du pays
La densité de population élevée au Bangladesh
'''

#Histoire
'''
L'histoire pourrait mettre en avant la compétition pour la prmière place en termes de
population entre la Chine et l'Inde .En regardant le taux de croissance ces deux pays se valent,
d'un coté nous avons 1.00 et de l'autre coté 1.01 ,ainsi que le pourcentage de la population
mondiale où les deux pays sont en tete avec 17.88% pour la Chine et 17.77% pour l'Inde.
La Chine et l'Inde ont des pourcentages de croissances rapides par rapport à certains pays 
comme les Etats unis ,l'Indonésie ,le Pakistan,le Nigéria ,etc cette disproportionnalité peut
etre expliquer par plusieurs facteurs et peut jouer sur la demographie mondiale.
En regardant certains pays ,nous constatons, qu'ils ont des densités disproportionnelle à la taille
de leur population, et c'est l'exemple de la Russie qui a une densité plus faible et une population
élevée contrairement au Bangladesh qui a une densité forte .
La densité de population élevée  au Bangladesh peut soulever des questions  sur les défis liés  à 
la surproduction, tels que l'utilisation des resssources, l'urbanisation et la pression des infrastructures.
'''


# Exemple de données pour certains pays et leur populations
countries = ['China', 'India', 'USA', 'IDSIA', 'PKTAN', 'NGRIA', 'BRAZL', 'BGLDS', 'RSSIA']
population_data = np.array([
    [1425887, 1417173, 338290, 275501, 235825, 218541, 215313, 171186, 144713],
    [146.8933, 431.0675, 36.0935, 144.6529, 267.4018, 236.5759, 25.2841, 1160.035, 8.4636]
])

growth_rate_data = np.array([
    [1.00, 1.01, 1.00, 1.01, 1.02, 1.02, 1.00, 1.01, 1.00],
    [17.88, 17.77, 4.24, 3.45, 2.96, 2.74, 2.70, 2.15, 1.81]
])


 

# Création de la figure et des sous-graphiques
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Sous-graphique 1 : Population totale
axs[0, 0].bar(countries, population_data[0], color='skyblue')
axs[0, 0].set_ylabel('Population (en millions)')
axs[0, 0].set_title('Population des pays en 2022')
#axs[0, 0].set_xlabel(countries, rotation = 45, ha = 'left')

# Sous-graphique 2 : Taux de croissance
axs[0, 1].bar(countries, growth_rate_data[0], color='lightgreen')
axs[0, 1].set_ylabel('Taux de croissance')
axs[0, 1].set_title('Taux de croissance démographique en 2022')
#axs[0, 1].set_xlabel(countries, rotation = 45, ha = 'right')

# Sous-graphique 3 : Croissances/décroissances rapides
axs[1, 0].bar(countries, growth_rate_data[1], color='coral')
axs[1, 0].set_ylabel('Croissance/décroissance (%)')
axs[1, 0].set_title('Croissances/décroissances rapides en 2022')
#axs[1, 0].set_xlabel(countries, rotation = 45, ha = 'right')

# Sous-graphique 4 : Densité de population
axs[1, 1].scatter(population_data[0], growth_rate_data[0], color='purple')
axs[1, 1].set_xlabel('Population (en millions)')
axs[1, 1].set_ylabel('Taux de croissance')
axs[1, 1].set_title('Relation entre population et taux de croissance')

# Ajustement de l'espacement entre les sous-graphiques
plt.tight_layout()
plt.subplots_adjust(hspace=0.30, wspace=0.30)
# Affichage de la figure
plt.show()
