# Créé par mitan, le 02/11/2025 en Python 3.7
# ex_4_4.py
from turtle import Screen, Turtle
import math

def draw_radiating_lines(win_width=200, win_height=200, steps=72):
    screen = Screen()
    screen.setup(win_width, win_height)
    screen.title("Des lignes")
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    # positionnement au centre (0,0) par défaut
    cx, cy = 0, 0

    # rayon = demi-diagonale pour atteindre les coins
    radius = math.hypot(win_width/2, win_height/2)

    for i in range(steps):
        angle = 360 * i / steps
        t.setheading(angle)
        t.goto(cx, cy)
        t.pendown()
        # aller au bord dans la direction 'angle'
        t.forward(radius)
        t.penup()
        t.goto(cx, cy)

    screen.mainloop()

if __name__ == "__main__":
    draw_radiating_lines(200, 200, steps=120)  # augmente steps pour plus de lignes

