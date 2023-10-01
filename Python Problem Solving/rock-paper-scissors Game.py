import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('''                                        
,---.          |                                                       o                         
|---',---.,---.|__/         ,---.,---.,---.,---.,---.        ,---.,---..,---.,---.,---.,---.,---.
|  \ |   ||    |  \         |   |,---||   ||---'|            `---.|    |`---.`---.|   ||    `---.
`   ``---'`---'`   ` |      |---'`---^|---'`---'`     |      `---'`---'``---'`---'`---'`    `---'
                    '       |         |           \n ''')


print("|||Welcome to rock-paper-scissors Game|||\n")

game_graphic = [rock,paper,scissors]
user_choice=int(input("What do you choose? Type [0] for Rock, [1] for Paper or [2] for Scissors: "))
computer_choice=random.randint(0,2)

def graphic (user_choice,computer_choice):
    global game_graphic
    print("\nYou choose:")
    print(game_graphic[user_choice])
    print("Computer choose:")
    print(game_graphic[computer_choice])


if user_choice >=3 or user_choice <0 :
  print("You enter invalid number,Try again!")

elif user_choice == 0 and computer_choice == 2:
    graphic(user_choice,computer_choice)
    print("Result: You win 🥳!")

elif user_choice == 2 and computer_choice == 0:
    graphic(user_choice,computer_choice)
    print("Result: You lose 😈!")

elif user_choice > computer_choice:
    graphic(user_choice,computer_choice)
    print("Result: You win 🥳!")

elif user_choice == computer_choice:
  graphic(user_choice,computer_choice)
  print("It's a draw 🤪,Try again!")
 
else:
  graphic(user_choice,computer_choice)
  print("Result: You lose 😈!")
  
