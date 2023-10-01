import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title("Egypt's State Guessing Game")
image = "egypte49.gif"
my_screen.setup(height=850,width=850)
my_screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Egypt's states.csv")

state_list = data.state.to_list()

state_name_list = []


while len(state_name_list) < 3:

    user_answer = my_screen.textinput(title=f" {len(state_name_list)}/3 Guess The State",
                                      prompt="Enter The Name Of State:").title()

    state_name = data[data.state == user_answer]
    x = state_name.x
    y = state_name.y

    if user_answer == "Exit":
        state_learn = []
        for s in state_list:
            if s not in state_name_list:
                state_learn.append(s)
        data_learn = pandas.DataFrame(state_learn)
        data_learn.to_csv("state_to_learn")

        break

    if user_answer in state_list:
        state_name_list.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x), int(y))
        t.write(state_name.state.item())



'''
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

'''
