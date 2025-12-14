# Créé par mitan, le 02/11/2025 en Python 3.7
# ex_4_6.py
from turtle import Screen, Turtle

def draw_square(t, x, y, size, fill=False):
    """Trace un carré de coin inférieur gauche (x,y) et côté size."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    if fill:
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    if fill:
        t.end_fill()
    t.penup()

def echiquier(num_cases=8, win_size=800):
    screen = Screen()
    screen.setup(win_size, win_size)
    screen.title("Échiquier")
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.color("black", "black")  # trait noir, remplissage noir pour cases noires

    # calcul de la taille de chaque case pour que l'échiquier tienne dans la fenêtre
    square_size = win_size / num_cases

    # commencer en bas-gauche (on centrera le dessin)
    start_x = -win_size/2
    start_y = -win_size/2

    for row in range(num_cases):
        for col in range(num_cases):
            x = start_x + col * square_size
            y = start_y + row * square_size
            # si (row+col) pair => case noire (ou inverse selon convention)
            if (row + col) % 2 == 0:
                draw_square(t, x, y, square_size, fill=True)
            else:
                # case blanche : on trace seulement le contour (ou ne rien faire)
                t.penup()
                t.goto(x, y)
                t.pendown()
                for _ in range(4):
                    t.forward(square_size)
                    t.left(90)
                t.penup()

    screen.mainloop()

if __name__ == "__main__":
    echiquier(num_cases=8, win_size=800)  # version fixe 800x800
    # Pour la version adaptable, appelle echiquier(num_cases=8, win_size=la_taille_que_tu_veux)

