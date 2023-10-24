import turtle
import random

turtle = turtle.Turtle()

colors = ['purtle', 'green', 'blue', 'yellow', 'pink', 'black', 'plum', 'red']
for _ in range (9):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(200)
    turtle.backward(200)
    turtle.right(50)