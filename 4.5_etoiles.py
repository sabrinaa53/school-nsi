# Créé par mitan, le 02/11/2025 en Python 3.7
# ex_4_5.py
from turtle import Screen, Turtle

def etoile5(t, longueur):
    """Trace une étoile à 5 branches avec la tortue t, longueur d'un côté = longueur."""
    # L'angle interne pour une étoile à 5 branches est 144°
    for i in range(5):
        t.forward(longueur)
        t.right(144)

def ligne_d_etoiles(count=9, start_x=-300, y=0, gap=60, sizes=None):
    screen = Screen()
    screen.setup(800, 200)
    screen.title("Des étoiles")
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    if sizes is None:
        # créer une progression de tailles si l'utilisateur n'a pas fourni
        sizes = [10 + i*8 for i in range(count)]

    x = start_x
    for size in sizes:
        t.goto(x, y)
        t.setheading(0)
        t.pendown()
        # tracer l'étoile centrée approximativement : déplacer d'abord pour centrer visuellement
        t.penup()
        # on recule la moitié d'un côté pour que l'étoile soit mieux centrée sur x
        t.forward(-size/2)
        t.pendown()
        etoile5(t, size)
        t.penup()
        x += gap

    screen.mainloop()

if __name__ == "__main__":
    # Exemple : 9 étoiles avec tailles croissantes
    sizes = [8, 12, 18, 26, 36, 26, 18, 12, 8]
    ligne_d_etoiles(count=len(sizes), start_x=-350, y=0, gap=80, sizes=sizes)

