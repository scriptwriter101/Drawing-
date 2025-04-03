import turtle

screen = turtle.Screen()

screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)

def move_turtle(orientation, distance):
    pen.setheading(orientation)
    pen.forward(distance)

def set_color(color):
    pen.color(color)

width = 1
def change_width(delta):
    global width
    width = max(1, width + delta)
    pen.width(width)

screen.listen()

screen.onkey(lambda: move_turtle(90, 10), "w")
screen.onkey(lambda: move_turtle(180, 10), "a")
screen.onkey(lambda: move_turtle(270, 10), "s")
screen.onkey(lambda: move_turtle(0, 10), "d")

screen.onkey(lambda: set_color("red"), "1")
screen.onkey(lambda: set_color("orange"), "2")
screen.onkey(lambda: set_color("yellow"), "3")
screen.onkey(lambda: set_color("green"), "4")
screen.onkey(lambda: set_color("blue"), "5")
screen.onkey(lambda: set_color("purple"), "6")
screen.onkey(lambda: set_color("white"), "7")
screen.onkey(lambda: set_color("black"), "8")

screen.onkey(lambda: change_width(-1), "9")
screen.onkey(lambda: change_width(1), "0")

while True:
    screen.update()
