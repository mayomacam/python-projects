import turtle
import random
wn = turtle.Screen()
wn.bgpic("1.png")
#wn.bgpic("3.jpeg")

ab = turtle.Turtle()
ab.shape("classic")

dist = 5
ab.up()
a = ['#ff6666',"green","orange","blue","#66ffff","magenta","yellow","skyblue","aqua", "yellowgreen", "brown", "purple", "white"]

for i in range(60):
    if i%2 == 0:
        ab.dot()
    if i%3== 0:
        ab.shape("square")
    if i%5 == 0:
        ab.shape("circle")
    if i%7 == 0:
        ab.shape("triangle")
    ab.color(random.choice(a))
    ab.stamp()
    ab.forward(dist)
    ab.right(24)
    dist= dist+2


wn.exitonclick()