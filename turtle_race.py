import turtle as t
import random
from tkinter import *

window = Tk()
window.geometry("400x250")
window.title("Show!!!")

screen = t.Screen()
screen.setup(height=500, width=600)
pen = t.Turtle(visible=False)
pen.penup()
pen.speed(0)
pen.goto(-250, 200)
for i in range(21):
    pen.write(i)
    pen.forward(25)

x = -250
pen.goto(-250, 200)
pen.right(90)
for i in range(21):
    for j in range(10):
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(10)
    pen.penup()
    pen.forward(5)
    pen.write(i)
    pen.goto(x + (i + 1) * 25, 200)

all_turtles = []
y_position = [160, 100, 40, -20]
colors = ['red', 'green', 'blue', 'black']
for turtle in range(0, 4):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()

    turtles.goto(x=-250, y=y_position[turtle])

    turtles.color(colors[turtle])
    for i in range(5):
        turtles.left(72)

    all_turtles.append(turtles)

def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 250:
            run = False
            winner_color = colors[all_turtles.index(turtle)]
            username = Label(window, text=f"{winner_color} turtle wins").place(x=30, y=50)
            window.update()  # Update the window to display the label

run = True
while run:
    random_walk(all_turtles)

screen.exitonclick()
window.mainloop()
