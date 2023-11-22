import turtle
import random
from tkinter import messagebox

screen = turtle.Screen()
position = [-120, -60, 0, 60, 120, 180]
speed = [10, 20, 15, 17, 13, 75]
colors = ["red", "green", "blue", "orange", "purple", "pink"]
turtles = []
for i in range(6):
    ime = turtle.Turtle(shape="turtle")
    ime.fillcolor(colors[i])
    ime.penup()
    ime.goto(-270, position[i])
    turtles.append(ime)

n = 0
user_input = turtle.textinput("Input", "What turtle do you bet on? Insert color ")
while n < 10000:
    for i in range(6):
        turtles[i].forward(random.choice(speed))
        n += 1
        x = turtles[i].xcor()
        if x > 240:
            print("You bet on: ", user_input)
            print("Won turtle: ", turtles[i].fillcolor())
            break
    if x > 240:
        break


if user_input == turtles[i].fillcolor():
    messagebox.showinfo("Result: You won", f"You bet on: {user_input} and won: {turtles[i].fillcolor()}")
else:
    messagebox.showinfo("Result: You lost", f"You bet on: {user_input}, but won: {turtles[i].fillcolor()}")

screen.exitonclick()
