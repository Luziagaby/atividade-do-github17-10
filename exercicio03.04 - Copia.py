import turtle
import random

turtle = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'black', ' pink']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(200)
    turtle.left(120)