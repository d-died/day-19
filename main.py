from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def line_up():
    y_axis = -100
    for turtle in range(len(colors)):
        new_turt = Turtle("turtle")
        new_turt.color(colors[turtle])
        new_turt.penup()
        new_turt.goto(x=-230, y=int(f"{y_axis}"))
        y_axis += 50
        all_turtles.append(new_turt)

def random_move(tortoise):
    random_num = random.randint(0, 10)
    tortoise.forward(random_num)

if user_bet:
    game_on = True

line_up()
while game_on:
    for t in all_turtles:
        random_move(t)
        if t.xcor() > 230:
            game_on = False
            winner = t.pencolor()
            if winner.lower() == user_bet.lower():
                print(f"You won! {winner} won gold!")
            else:
                print(f"Your bet lost. {winner} took 1st!")


screen.exitonclick()