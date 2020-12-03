import turtle

wn = turtle.Screen()
wn.bgcolor("black")

rabbit = turtle.Turtle()
rabbit.pencolor("orange")
rabbit.hideturtle()
rabbit.pensize(5)
rabbit.speed(0)


rabbit.penup()
rabbit.left(90)
rabbit.forward(130)
rabbit.right(90)
rabbit.pendown()

for i in range(17):
    rabbit.left(5)
    rabbit.forward(250)

    rabbit.right(90)
    rabbit.forward(5)
    rabbit.circle(80)
    '''for i in range(360):
        rabbit.left(1)
        rabbit.forward(1)'''

'''for i in range(17):
    rabbit.left(5)
    rabbit.forward(90)

    rabbit.right(45)
    rabbit.right(90)
    rabbit.circle(60)
    rabbit.left(90)
    rabbit.forward(45)
    rabbit.forward(5)
    for i in range(360):
        rabbit.left(1)
        rabbit.forward(1)'''

wn.exitonclick()