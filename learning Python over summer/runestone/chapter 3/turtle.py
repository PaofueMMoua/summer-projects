
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(list(range(5, 60, 2)))
tess.up()                     # this is new
for size in range(5, 240, 2):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(size/2)          # move tess along
    tess.right(35)              # and turn her
    tess.speed(100)

wn.exitonclick()
