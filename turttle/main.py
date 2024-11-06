import turtle as t

tim = t.Turtle()

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

while not t.distance(tim) == 100:
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.right(90)






screen = t.Screen()
screen.exitonclick()

