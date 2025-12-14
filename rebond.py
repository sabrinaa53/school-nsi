from turtle import *

#Configuration de la fenêtre
setup(400, 400)        # taille de la fenêtre
bgcolor("white")       # fond blanc
title("Rebond de balle")

#Création de la balle
shape("circle")        # forme : cercle
color("red")           # couleur de la balle
penup()                # pas de trace
speed("fastest")

#Variables de mouvement
y  = -180               # position de départ (à gauche)
dy = 10                # déplacement horizontal
aller_retour = 0       

#Boucle principale 
while aller_retour < 3:
    clear()            # efface l’ancienne position
    sety(y)            # met à jour la position
    y += dy            # avance la balle

    # Rebond sur les bords
    if y > 180 or y < -180:
        dy = -dy       # inverse la direction
        aller_retour += 0.5  # 1 aller-retour = 2 rebonds (aller + retour)

#Fin du programme
hideturtle()
done()
