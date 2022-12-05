import turtle
import time
from turtle import Turtle
from random import randint
from types import NoneType

#change the window title to Turtle race
window=turtle.Screen()
window.title("Turtle Race")

#create the turtle run title in the middle of the screen 
#as well as back ground color
turtle.bgcolor("Light Blue")
turtle.speed(0)
turtle.penup()
turtle.setpos(-110,300)
turtle.write("TURTLE RUN",font=("Arial",30,"bold")) 
turtle.penup()

#creates the finish line graphic
finish = Turtle(visible=False)
finish.speed('fastest')
finish.penup()

finish.color('Purple')
finish.goto(160, 145)
finish.write("Finish-Line" ,font=("Ariel",15,"bold"))
finish.width(4)
finish.goto(200, 120)
finish.right(90)
finish.pendown()

for _ in range(20):
    finish.color('orange')
    finish.forward(5)
    finish.color('yellow')
    finish.forward(5)

#turtle 1
turtle_1= Turtle()
turtle_1.speed(0)
turtle_1.color("green")
turtle_1.shape("turtle")
turtle_1.penup()
turtle_1.goto(-250, 100)
turtle_1.pendown()

#turtle 2
turtle_2= Turtle()
turtle_2.speed(0)
turtle_2.color("brown")
turtle_2.shape("turtle")
turtle_2.penup()
turtle_2.goto(-250, 50)
turtle_2.pendown()

#turtle 3
turtle_3 = Turtle()
turtle_3.speed(0)
turtle_3.color("red")
turtle_3.shape("turtle")
turtle_3.penup()
turtle_3.goto(-250, 0)
turtle_3.pendown()

#turtle 4 
turtle_4 = Turtle()
turtle_4.speed(0)
turtle_4.color("black")
turtle_4.shape("turtle")
turtle_4.penup()
turtle_4.goto(-250, -50)
turtle_4.pendown()

time.sleep(1) # pauses game for 1 second

#race starting
#this is how the turtles run by moving randomly between 1 - 5
for i in range (145):
    turtle_1.forward(randint(1,5))
    turtle_2.forward(randint(1,5))
    turtle_3.forward(randint(1,5))
    turtle_4.forward(randint(1,5))

#to declare a winning turtle
turtles = [turtle_1,turtle_2,turtle_3,turtle_4]
color = ["red","black","brown","green"]
winner = None

while not winner:
    for turtle in turtles:
        turtle.forward(randint(1, 5))
        if turtle.xcor() >= 190:
            winner = turtle
            break  # we have a winner!
    else: # no break
        continue

    break

finish.pencolor(winner.pencolor())
finish.write("{} won the race!".format(winner.pencolor()), font=("ariel", 30, "bold"))

time.sleep(5)

turtle.exitonclick()




























