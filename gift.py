# Import turtle package
import turtle
import time

from cv2 import circle
  
# Creating a turtle object(pen)
pen = turtle.Turtle()
pen.ht()

# used for flowers
pen2 = turtle.Turtle()
pen3 = turtle.Turtle()

pen2.ht()
pen3.ht()

#used for intro
pen4 = turtle.Turtle()
pen4.ht()

# Screen stuff
turtle.Screen().bgcolor("beige")
screen = turtle.Screen()

# Defining a method to draw curve
def heartCurve():
    pen.speed(0)
    for i in range(200):
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)
  
# Defining method to draw a full heart
def heart():
    pen.st()
    pen.fillcolor('red')
    pen.begin_fill() # start fill
    pen.left(140) # rotate pen
    pen.forward(113) # line
    heartCurve() # draw left curve
    pen.left(120) # rotate pen
    heartCurve() # draw right curve
    pen.forward(112) # line
    pen.end_fill() # end fill
    pen.ht()
  

def intro():
    pen4.up()
    pen4.goto(-200, 0) # set to middle of screen
    pen4.down()
    pen4.color("black")
    pen4.write("I know I can't be there for this so here you go...", font=("Verdana", 12, "bold"))
    time.sleep(5)
    pen4.clear()
    

def txt():
    pen.speed(6)
    pen.up()
    pen.setpos(-68, 95) # Move turtle to right position (in heart)
    pen.down()
    pen.color('lightgreen')
    pen.write("Be My Valantine?", font=("Verdana", 12, "bold"))

def fromTxt():
    pen.up()
    pen.goto(-60, -200)
    pen.down()
    pen.color("black")
    pen.write("From: booger", font=("Verdana", 12, "bold"))


def flower():
    pen3.speed(0)
    pen2.speed(0)

    # create two flowers same time
    for i in range(100):
        pen3.circle(100-i, 90)
        pen3.left(90)
        pen3.circle(100-i, 90)
        pen3.left(18)

        pen2.circle(100-i, 90)
        pen2.left(90)
        pen2.circle(100-i, 90)
        pen2.left(18)

# setting up positions for flowers
def firstCorner():
    pen3.color('pink')
    pen3.up()
    pen3.goto(300, 200)
    pen3.down()

def secondCorner():
    pen3.color('green')
    pen3.up()
    pen3.goto(-300, screen.window_height()/4)
    pen3.down()

def thirdCorner():
    pen2.color('pink')
    pen2.up()
    pen2.goto(-300, -200)
    pen2.down()

def fourthCorner():
    pen2.color('green')
    pen2.up()
    pen2.goto(300, -200)
    pen2.down()

# draw first opposite sides hearts
def setOne():
    firstCorner()
    thirdCorner()
    flower()

# draw second opposite sides hearts
def setTwo():
    secondCorner()
    fourthCorner()
    flower()

# main funtion
def main():
    intro()
    setOne()
    heart()
    txt()
    fromTxt()
    setTwo()


main()

time.sleep(7)
