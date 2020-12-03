import turtle

wn = turtle.Screen()
wn.bgcolor("black")
rabbit = turtle.Turtle()
rabbit.pensize(2)
rabbit.pencolor("red")
rabbit.speed(0)
rabbit.hideturtle()
rabbit.shape("turtle")


for i in range(1):
    for colors in ["red","green","blue","orange","cyan"]:
        rabbit.color(colors)
        rabbit.forward(72)
        rabbit.left(120)
        rabbit.forward(120)
        rabbit.circle(70)
        rabbit.circle(50)
        rabbit.circle(30)
        rabbit.circle(10)
        rabbit.right(45)
        rabbit.backward(120)
        rabbit.circle(100)

rabbit.penup()
#rabbit.goto(0, 150)
rabbit.pendown()
for j in range(12):
    for i in range(3):
        if i == 0:
            rabbit.circle(30)
            rabbit.backward(10)
            rabbit.color("green")
            rabbit.circle(20)
        else:
            rabbit.color("red")
            rabbit.circle(i*5+90)
            rabbit.backward(10)
            rabbit.color("green")
            rabbit.circle(i*5+45)
        rabbit.color("blue")
        rabbit.circle(30)
        rabbit.forward(i+10)
        rabbit.right(10)
        rabbit.color("yellow")
        rabbit.circle(40)




wn.exitonclick()