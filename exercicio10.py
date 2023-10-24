import turtle

turtle = turtle.Turtle()

for _ in range(4):
    turtle.shape('triangle')
    turtle.color('red')
    turtle.forward(100)
    turtle.right(90)
    
    turtle.penup()
    turtle.forward(150)
    turtle.right(90)
    
for _ in range(4):
     turtle.pendown()
     turtle.shape('circle')
     turtle.color('red')
     turtle.left(90)
     turtle.forward(100)
        
turtle.penup()
turtle.forward(150)
turtle.right(90)
        
 for _ in range(4):
    turtle.pendown()
    turtle.shape('classic')
    turtle.color('red')
    turtle.forward(100)
    turtle.left(90)
            
turtle.penup()
turtle.forward(300)
turtle.right(90)
            
 for _ in range(4):
     turtle.pendown()
     turtle.shape('square')
     turtle.color('black')
     turtle.right(90)
     turtle.forward(100)

turtle.penup()
turtle.forwaed(30)
turtle.left(90)

for _ in range(3):
    turtle.pendown()
    turtle.shape('turtle')
    turtle.color('cyan')
    turtle.right(90)
    turtle.forward(400)
    
turtle.forward(150)
turtle.right(90)
turtle.forwaed(400)
turtle.right(90)
turtle.forwaed(150)