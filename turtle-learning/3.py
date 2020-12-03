import turtle

wn = turtle.Screen()
wn.bgcolor("black")
rabbit = turtle.Turtle()

rabbit.pencolor("black")
rabbit.speed(10)
#rabbit.hideturtle()
rabbit.shape("turtle")


for i in range(1):
    for colors in ["red","green","blue","orange","cyan"]:
        rabbit.color(colors)
        rabbit.forward(120)
        rabbit.left(120)
        rabbit.forward(120)
        rabbit.circle(40)
        rabbit.circle(20)
        rabbit.right(45)
        rabbit.backward(80)
        rabbit.circle(40)



wn.exitonclick()