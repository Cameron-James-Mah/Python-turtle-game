import turtle
import math
import random

#Screen
sc = turtle.Screen()
sc.bgcolor("black")
turtle.delay(5)

sc.tracer(2)

#draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-375, -375)
mypen.pendown()
mypen.pensize(3)
turtle.turtlesize(12, 12, 12)
mypen.speed(0)

for side in range(4):
    mypen.forward(750)
    mypen.left(90)
mypen.hideturtle()

#player
player = turtle.Turtle()
player.color("cyan")
player.shape("turtle")
player.penup()
player.setposition(-350, 350)
player.speed(0)
turtle.shapesize(12, 12, 12)
player.pensize(5)

#Obstacle makers
Obstacle1 = turtle.Turtle()
Obstacle1.speed(0)
Obstacle1.color("white", "white")
Obstacle1.pensize(1)
Obstacle1.penup()
Obstacle1.setposition(-375, 320)
Obstacle1.pendown()
Obstacle1.begin_fill()
Obstacle1.forward(650)
Obstacle1.right(90)
Obstacle1.forward(30)
Obstacle1.right(90)
Obstacle1.forward(650)
Obstacle1.right(90)
Obstacle1.forward(30)
Obstacle1.end_fill()

#2
Obstacle1.penup()
Obstacle1.setposition(375, 155)
Obstacle1.pendown()
Obstacle1.begin_fill()
Obstacle1.seth(180)
Obstacle1.forward(650)
Obstacle1.left(90)
Obstacle1.forward(30)
Obstacle1.left(90)
Obstacle1.forward(650)
Obstacle1.left(90)
Obstacle1.forward(30)
Obstacle1.end_fill()

#3
Obstacle1.penup()
Obstacle1.setposition(175, 155)
Obstacle1.pendown()
Obstacle1.begin_fill()
Obstacle1.seth(90)
Obstacle1.forward(90)
Obstacle1.left(90)
Obstacle1.forward(30)
Obstacle1.left(90)
Obstacle1.forward(90)
Obstacle1.left(90)
Obstacle1.forward(30)
Obstacle1.end_fill()

#4
Obstacle1.penup()
Obstacle1.setposition(-245, 155)
Obstacle1.pendown()
Obstacle1.begin_fill()
Obstacle1.seth(90)
Obstacle1.forward(90)
Obstacle1.left(90)
Obstacle1.forward(30)
Obstacle1.left(90)
Obstacle1.forward(90)
Obstacle1.left(90)
Obstacle1.forward(30)
Obstacle1.end_fill()

#5
Obstacle1.penup()
Obstacle1.setposition(-55, 290)
Obstacle1.pendown()
Obstacle1.begin_fill()
Obstacle1.seth(270)
Obstacle1.forward(90)
Obstacle1.left(90)
Obstacle1.forward(30)
Obstacle1.left(90)
Obstacle1.forward(90)
Obstacle1.left(90)
Obstacle1.forward(30)
Obstacle1.end_fill()

#6
Obstacle1.penup()
Obstacle1.setposition(-375, -95)
Obstacle1.seth(0)
Obstacle1.pendown()
Obstacle1.begin_fill()
Obstacle1.forward(750)
Obstacle1.right(90)
Obstacle1.forward(30)
Obstacle1.right(90)
Obstacle1.forward(750)
Obstacle1.right(90)
Obstacle1.forward(30)
Obstacle1.end_fill()
Obstacle1.hideturtle()

#Teleport start
TeleportS = turtle.Turtle()
TeleportS.color("yellow")
TeleportS.penup()
TeleportS.speed(0)
TeleportS.setposition(275, -95)
TeleportS.begin_fill()
TeleportS.seth(0)
TeleportS.forward(100)
TeleportS.left(90)
TeleportS.forward(220)
TeleportS.left(90)
TeleportS.forward(100)
TeleportS.left(90)
TeleportS.forward(220)
TeleportS.end_fill()
TeleportS.hideturtle()

#Teleport end
TeleportE = turtle.Turtle()
TeleportS.color("yellow")
TeleportS.penup()
TeleportS.speed(0)
TeleportS.setposition(-375, -275)
TeleportS.begin_fill()
TeleportS.seth(0)
TeleportS.forward(50)
TeleportS.left(90)
TeleportS.forward(50)
TeleportS.left(90)
TeleportS.forward(50)
TeleportS.left(90)
TeleportS.forward(50)
TeleportS.end_fill()
TeleportS.hideturtle()

#Squares
#1
Square1 = turtle.Turtle()
Square1.color("red")
Square1.shape("square")
Square1.penup()
Square1.setposition(265, -85)
Square1.speed(0)
Square1.seth(90)


#2
Square2 = turtle.Turtle()
Square2.color("red")
Square2.shape("square")
Square2.penup()
Square2.setposition(-40, -85)
Square2.speed(0)
Square2.seth(90)

#3
Square3 = turtle.Turtle()
Square3.color("red")
Square3.shape("square")
Square3.penup()
Square3.setposition(112, 110)
Square3.speed(0)
Square3.seth(270)

#4
Square4 = turtle.Turtle()
Square4.color("red")
Square4.shape("square")
Square4.penup()
Square4.setposition(-202, 110)
Square4.speed(0)
Square4.seth(270)

#Circles
Circle1 = turtle.Turtle()
Circle1.color("red")
Circle1.shape("circle")
Circle1.penup()
Circle1.setposition(0, -250)
Circle1.speed(0)
Circle1.seth(random.randint(0,270))


#2
Circle2 = turtle.Turtle()
Circle2.color("red")
Circle2.shape("circle")
Circle2.penup()
Circle2.setposition(0, -250)
Circle2.speed(0)
Circle2.seth(random.randint(0,270))

#3
Circle3 = turtle.Turtle()
Circle3.color("red")
Circle3.shape("circle")
Circle3.penup()
Circle3.setposition(0, -250)
Circle3.speed(0)
Circle3.seth(random.randint(0,270))

#4
# Circle4 = turtle.Turtle()
# Circle4.color("red")
# Circle4.shape("circle")
# Circle4.penup()
# Circle4.setposition(0, -250)
# Circle4.speed(8)
# Circle4.seth(random.randint(0,270))

#5
CircleWin = turtle.Turtle()
CircleWin.color("blue")
CircleWin.shape("circle")
CircleWin.penup()
CircleWin.setposition(0, -250)
CircleWin.speed(8)
CircleWin.seth(random.randint(0,270))

speed = 0

tries = 0
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def start():
    global speed
    speed = 2
def stop():
    global speed
    speed = 0

#Keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(start, "Up")
turtle.onkey(stop, "Down")

def Collision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

#Initialize tries
mypen.undo()
mypen.penup()
mypen.hideturtle()
mypen.setposition(-475, 350)
triesString = "Deaths: %s" % tries
mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))


while True:
    player.forward(speed)

    Square1.forward(2)
    Square2.forward(2)
    Square3.forward(2)
    Square4.forward(2)

    Circle1.forward(3)
    Circle2.forward(3)
    Circle3.forward(3)
    # Circle4.forward(5)
    CircleWin.forward(4)

    #TeleportS
    if 275 < player.xcor() < 375 and -95 < player.ycor() < 125:
        player.setposition(-375, -250)
        speed = 0

    #Circle movement
    if Circle1.xcor() > 375 or Circle1.xcor() < -375 or Circle1.ycor() > -130 or Circle1.ycor() < -375:
        Circle1.right(random.randint(0,180))

    if Circle2.xcor() > 375 or Circle2.xcor() < -375 or Circle2.ycor() > -130 or Circle2.ycor() < -375:
        Circle2.right(random.randint(0,180))

    if Circle3.xcor() > 375 or Circle3.xcor() < -375 or Circle3.ycor() > -130 or Circle3.ycor() < -375:
        Circle3.right(random.randint(0,180))

    # if Circle4.xcor() > 375 or Circle4.xcor() < -375 or Circle4.ycor() > -130 or Circle4.ycor() < -375:
    #     Circle4.right(random.randint(0,180))

    if CircleWin.xcor() > 375 or CircleWin.xcor() < -375 or CircleWin.ycor() > -130 or CircleWin.ycor() < -375:
        CircleWin.right(random.randint(0,180))

    #Square movement
    if Square1.ycor() > 110 or Square1.ycor() < -85:
        Square1.right(180)

    if Square2.ycor() > 110 or Square2.ycor() < -85:
        Square2.right(180)

    if Square3.ycor() > 110 or Square3.ycor() < -85:
        Square3.right(180)

    if Square4.ycor() > 110 or Square4.ycor() < -85:
        Square4.right(180)

    #Circle collision
    if Collision(player, Circle1):
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s" % tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))

    if Collision(player, Circle2):
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s" % tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))

    if Collision(player, Circle3):
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s" % tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))

    if Collision(player, CircleWin):
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        turtle.clearscreen()
        mypen.setposition(0, 0)
        sc.bgcolor("black")
        End = "Victory"
        mypen.write(End, False, align="left", font=("Arial", 30, "normal"))
        mypen.penup()
        mypen.setposition(0, -150)
        mypen.pendown()
        triesString = "Deaths: %s" % tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))
        break


    #Square collision
    if Collision(player, Square1):
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s" % tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))

    if Collision(player, Square2):
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s" % tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))

    if Collision(player, Square3):
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s" % tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))

    if Collision(player, Square4):
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s" % tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))

    #Boundary check
    if player.xcor() > 375 or player.xcor() < -375:
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s"%tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))

    if player.ycor() > 375 or player.ycor() < -375:
        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s"%tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))

    if -375 < player.xcor() < 270 and 280 < player.ycor() < 325 or \
        -275 < player.xcor() < 375 and 115 < player.ycor() < 165 or \
        145 < player.xcor() < 175 and 155 < player.ycor() < 255 or\
        -275 < player.xcor() < -245 and 155 < player.ycor() < 255 or \
            -60 < player.xcor() < -20 and 190 < player.ycor() < 300 or -375 < player.xcor() < 275 and -130 < player.ycor() < -90:

        player.setposition(-350, 350)
        tries += 1
        speed = 0
        mypen.undo()
        mypen.penup()
        mypen.hideturtle()
        mypen.setposition(-475, 350)
        triesString = "Deaths: %s"%tries
        mypen.write(triesString, False, align="left", font=("Arial", 14, "normal"))


turtle.done()