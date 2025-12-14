from turtle import *

def spirale() : 
    speed("fastest")
    rayon = 1 
    rayonS = 100
    while (rayon < rayonS) : 
        circle(rayon, 180)
        rayon+=2

spirale()
done()