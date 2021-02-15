import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win ? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtles = []

for index in range(0, 6):
    turtle = t.Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[index])
    turtles.append(turtle)

#the race doesnt have start prematurely with this
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_bet:
                print(f"You've won! The winner is {turtle.pencolor()}")
            else:
                print(f"You've lost! The winner is {turtle.pencolor()}")
            is_race_on = False

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
