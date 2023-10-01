import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("USA STATES GUESSING GAME")
image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)

Guessed_states = []

data = pandas.read_csv("50_states.csv")

states_list = data.state.to_list()

while len(Guessed_states) < 50 :
    user_asnswer = my_screen.textinput(title=f"your score {len(Guessed_states)}/50 Guess the state",
                                       prompt="what is the state?").title()

    if user_asnswer == "Exit":
        missimg_states = [state for state in states_list if state not in Guessed_states]
        #for state in states_list:
         #   if state not in Guessed_states:
          #      missimg_states.append(state)
        data_to_learn = pandas.DataFrame(missimg_states)
        data_to_learn.to_csv("States to learn")

        break

    if user_asnswer in states_list:

        states_row = data[data.state == user_asnswer]
        Guessed_states.append(user_asnswer)
        s_name = turtle.Turtle()
        s_name.hideturtle()
        s_name.penup()
        s_name.goto(int(states_row.x),int(states_row.y))
        s_name.write(states_row.state.item())

