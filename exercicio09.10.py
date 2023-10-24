import turtle
import random

gaby = turtle.Turtle()
colors = ['cyan', 'blue', 'yellow', 'green', 'pink', 'purple', 'red', 'orange']

for c in range(180):
    color = random.choice(colors)
    gaby.color(color)
    gaby.forward(2)
    gaby.right(2)