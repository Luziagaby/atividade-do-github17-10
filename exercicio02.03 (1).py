import turtle

gaby = turtle.Turtle()
gaby.shape('triangle')
gaby.pensize(5)


for color in ['black', 'pink', 'blue', 'red' ]:
    gaby.color(color)
    gaby.forward(150)
    gaby.right(90)
gaby.penup()
gaby.forward(200)
gaby.pendown()
for color in ['black', 'pink', 'blue', 'red']:
    gaby.color(color)
    gaby.forward(150)
    gaby.right(90)