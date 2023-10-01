from flask import Flask
import random


app = Flask(__name__)

rand_num = random.randint(0, 9)

@app.route("/")
def greeting():
    return "<h1>Guess a number between 0 and 9</h1>" \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'




@app.route("/<int:guessed_num>")
def func_of_game(guessed_num):

    if guessed_num == rand_num:
        return "<h1 style='color: purple'>You found me</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif guessed_num < rand_num:
        return "<h1 style='color: red'>Two Low,Try again</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif guessed_num > rand_num:
        return "<h1 style='color: green'>Two High,Try again</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
