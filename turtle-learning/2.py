import turtle

wn = turtle.Screen()
wn.bgcolor("black")
rabbit = turtle.Turtle()
rabbit.speed(0)
#rabbit.pencolor("black")

'''for i in range(12):
    for colors in ["red", "green", "blue", "orange", "yellow", "cyan"]:
        rabbit.color(colors)
        rabbit.circle(150)
        rabbit.left(5)'''

for i in range(54):
    for colors in ["red", "green", "blue", "orange", "yellow", "cyan", "pink"]:
        rabbit.color(colors)
        rabbit.circle(150)
        rabbit.left(1)
wn.exitonclick()