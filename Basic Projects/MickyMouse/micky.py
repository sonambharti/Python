#Importing Liabraries
from tkinter import N
import turtle
import colorsys

#Initialize a variable for turtles
micky = turtle.Turtle()
micky.speed(0)

#create a turtle screen
screen = turtle.Screen()
#Define height and width of screen
screen.setup(1200, 600)
#Define Background color of Screen
screen.bgcolor('#ffdbac')
screen.update()

#Define title of program
turtle.title("Mickey Mouse")

#Code for drawing head of mickey mouse

#Initializing starting point of head
micky.goto(0, -150)
#filling color in head
micky.begin_fill()
#setting color of head
micky.color('black')
#drawing head
micky.circle(150)
#ending fill
micky.end_fill()



#Code for drawings ears of mickey mouse

#left ear
#initializing starting point of left ear
micky.goto(-120,100)
#filling color in left ear
micky.begin_fill()
#setting color of left ear
micky.color('black')
#drawing left ear
micky.circle(90)
#ending fill
micky.end_fill()


#right ear
#initializing starting point of right ear
micky.goto(120,100)
#filling color in right ear
micky.begin_fill()
#setting color of right ear
micky.color('black')
#drawing right ear
micky.circle(90)
#ending fill
micky.end_fill()

#Code for drawing face of mickey mouse

#initializing starting point of face dip
micky.goto(40,-190)
#filling color in face dip
micky.begin_fill()
#setting color of face dip
micky.color('#ffdbac')
#drawing face dip
micky.circle(120)
#ending fill
micky.end_fill()

micky.goto(-40,-190)
micky.begin_fill()
micky.color('#ffdbac')
micky.circle(120)
micky.end_fill()

#Code for face outline

#initializing starting point of face outline
micky.goto(0,-150)
#setting color of face outline
micky.color('black')
#drawing face outline
micky.circle(150)

# Code for drawing eyes of mickey mouse

# initializing starting point of left eye
micky.penup()
micky.goto(-50, -25)
micky.pendown()


def draw_left_eye(rad):
    for i in range(4):
        # two arcs
        # filling color in eyes
        micky.begin_fill()
        # setting color of eyes
        micky.color('white')
        # DRAW eyes
        micky.circle(rad, 90)
        micky.circle(rad // 4, 90)
        # ending fill
        micky.end_fill()

# Main section
# tilt the shape to negative 45
micky.seth(45)
draw_left_eye(40)



#Code  of left eye ball
micky.penup()
micky.goto(-50,-20)
micky.pendown()
#filling color in left eye
micky.begin_fill()
#setting color of left eye
micky.color('black')
#drawing left eye
micky.circle(8)
#ending fill
micky.end_fill()

#initializing starting point of right eye

micky.penup()
micky.goto(55,-25)
micky.pendown()


def draw_eye(rad):
    for i in range(4):
        # two arcs
        # filling color in eyes
        micky.begin_fill()
        # setting color of eyes
        micky.color('white')
        # DRAW eyes
        micky.circle(rad, 90)
        micky.circle(rad // 4, 90)
        # ending fill
        micky.end_fill()


# Main section
# tilt the shape to negative 45
micky.seth(45)
draw_eye(40)

# Code  of left eye ball
micky.penup()
micky.goto(-50, -20)
micky.pendown()
# filling color in left eye
micky.begin_fill()
# setting color of left eye
micky.color('black')
# drawing left eye
micky.circle(8)
# ending fill
micky.end_fill()

# initializing starting point of right eye

micky.penup()
micky.goto(55, -25)
micky.pendown()


def draw_eye(rad):
    for i in range(4):
        # two arcs
        # filling color in eyes
        micky.begin_fill()
        # setting color of eyes
        micky.color('white')
        # DRAW eyes
        micky.circle(rad, 90)
        micky.circle(rad // 4, 90)
        # ending fill
        micky.end_fill()


# Main section
# tilt the shape to negative 45
micky.seth(45)
draw_eye(40)

# code for right eye ball
micky.penup()
micky.goto(50, -20)
micky.pendown()
# filling color in right eye
micky.begin_fill()
# setting color of right eye
micky.color('black')
# drawing right eye
micky.circle(8)
# ending fill
micky.end_fill()

# Code for drawing outline of eyes of mickey mouse
# initializing starting point of right eye outline
micky.penup()
micky.goto(55, -25)
micky.pendown()


def draw_reye_outline(rad):
    for i in range(4):
        # two arcs
        micky.circle(rad, 90)
        micky.circle(rad // 4, 90)


# Main section
# tilt the shape to negative 45
micky.seth(45)
draw_reye_outline(40)

# initializing starting point of left eye outline
micky.penup()
micky.goto(-50, -25)
micky.pendown()


def draw_leye_outline(rad):
    for i in range(4):
        # two arcs
        micky.circle(rad, 90)
        micky.circle(rad // 4, 90)


# Main section
# tilt the shape to negative 45
micky.seth(45)
draw_leye_outline(40)

# Code for drawing nose of mickey mouse

# initializing starting point of nose
micky.penup()
micky.goto(-20, -50)
micky.pendown()


def draw(rad):
    for i in range(3):
        # two arcs
        # filling color in nose
        micky.begin_fill()
        # setting color of nose
        micky.color('black')
        # DRAW NOSE
        micky.circle(rad, 90)
        micky.circle(rad // 3, 90)
        # ending fill
        micky.end_fill()


# Main section
# tilt the shape to negative 45
micky.seth(-45)
draw(25)

# speed of turtle
micky.speed(3)


#Code for drawing lips of mickey mouse

#initializing starting point of lips
micky.speed(0)
micky.penup()
micky.goto(-48,-78)
micky.pendown()
#direction of turtle
micky.right(90)
#setting heading of turtle
micky.setheading(-50)
#drawing lips
for x in range (110):
  micky.forward(1)
  micky.left(1)
# micky.left(110)
# micky.forward(110)
# micky.end_fill()
micky.speed(0)

#Code for drawing eyebrows of mickey mouse


micky.setheading(-155)
#setting color of left eyebrow
micky.color('black')
#intialze pen thickness
micky.pensize(2)
micky.penup()
#initializing starting point of left eyebrow
micky.goto(-40,-70)
micky.pendown()
#drawing left eyebrow
micky.circle(30,40)
#hide turtle
micky.hideturtle()


#code for drawing right eyebrow
micky.setheading(-245)
#setting color of right eyebrow
micky.color('black')
#intialze pen thickness
micky.pensize(2)
micky.penup()
#initializing starting point of right eyebrow
micky.goto(50,-80)
micky.pendown()
#drawing right eyebrow
micky.circle(30,40)
#hide turtle
micky.hideturtle()

#Code for drawing tongue of mickey mouse
micky.pensize(1)
micky.penup()
micky.goto(-33,-92)
micky.pendown()
#direction of turtle
micky.right(90)
#setting heading of turtle
micky.setheading(-45)
#drawing lips
micky.forward(20)
micky.circle(25,95)
micky.forward(20)

#code for holding output screen
turtle.mainloop()