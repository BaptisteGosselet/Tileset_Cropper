#!/usr/bin/python3

import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


#Paramètres
NB_LIGNES = 2
NB_COLONNES = 6
CHEMIN_FICHIER = "example.png"
NOMS_SORTIE = "Chess"

AFFICHAGE = False #affiche les images avant de s'enregistrer si True
EXTENTION = CHEMIN_FICHIER[-3] + CHEMIN_FICHIER[-2] + CHEMIN_FICHIER[-1]


#Traitement
listeImg = []
tileset = img.imread(CHEMIN_FICHIER)
largeur = int(tileset.shape[0] / NB_LIGNES)
longueur = int(tileset.shape[1] / NB_COLONNES)
img = np.zeros((largeur, longueur, 4))

for l in range(NB_LIGNES):
    for c in range(NB_COLONNES):
        img = np.zeros((largeur, longueur, 4))
        for i in range(int(len(img))):
            for j in range(int(len(img[0]))):
                img[i][j] = tileset[i+(largeur*l)][j+(longueur*c)]
              
        listeImg.append(img)


#Enregistrement
for i in range(len(listeImg)):
    if(AFFICHAGE):
        plt.imshow(listeImg[i])
        plt.show()
    filename = NOMS_SORTIE + str(i) + '.' + EXTENTION
    plt.imsave(filename,listeImg[i])

print("Fait.")
