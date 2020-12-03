import turtle

wn = turtle.Screen()
wn.bgcolor("black")
rabbit = turtle.Turtle()

rabbit.pencolor("black")
rabbit.speed(0)
rabbit.hideturtle()
#rabbit.shape("turtle")
rabbit.color("white","pink")

'''for i in range(8):
    rabbit.forward(80)
    rabbit.left(80)
    rabbit.forward(80)
    rabbit.circle(40)
    rabbit.circle(20)
    rabbit.backward(80)
    rabbit.circle(40)'''
rabbit.begin_fill()
for i in range(6):
    if i%2==0:
        rabbit.pencolor("red")
    else:
        rabbit.pencolor("blue")
    rabbit.circle(15)
    rabbit.backward(20)
    rabbit.circle(15)
    rabbit.backward(20)
    rabbit.circle(15)
    rabbit.backward(20)
    rabbit.circle(30)
    rabbit.circle(15)
    rabbit.left(60)
    rabbit.circle(15)
    rabbit.backward(80)
    rabbit.circle(40)



'''for i in range(6):
    rabbit.color("orange","red")'''


rabbit.end_fill()
wn.exitonclick()