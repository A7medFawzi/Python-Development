from turtle import Turtle, Screen
import random

game_end = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
my_screen.title("Turtle Racing Game")
user_predict = my_screen.textinput("Make your prediction", "Which turtle do you think will win the race? Enter a "
                                                           "color: ")
colors = ["red", "green", "orange", "blue", "yellow", "purple"]
y_position = [150, 100, 50, 0, -50, -100]
all_turtle = []

for t_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t_index])
    new_turtle.goto(x=-230, y=y_position[t_index])
    all_turtle.append(new_turtle)

if user_predict:
    game_end = True

while game_end:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            game_end = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_predict:
                print(f"You win, the winning turtle is the {winning_turtle} turtle.")
            else:
                print(f"You lose, the winning turtle is the {winning_turtle} turtle.")

        random_walk = random.randint(0, 5)
        turtle.forward(random_walk)

my_screen.exitonclick()
