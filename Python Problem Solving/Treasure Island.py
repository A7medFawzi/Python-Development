print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


first= input("You are in the road then , you had crossroad left and right which road do you chosse ! left or right !\n").lower()

if first == ("left") :

  second=input("You have reached a lake and must go to the other side! What would you choose swimming, or wait for a boat?\n").lower()

  if second == "wait":

    third=input("In front of you three coluered doors , Red , Yellow and Blue , which doors you choose!\n")


    if third == "Yellow" :

      print("You win.\n")

    elif third == "Red" :

      print ("Burned By fire.Game Over\n")

    elif third == "Blue" :

      print("Eaten By Beats , Game Over.\n")

    else:

      print("Game Over.\n")

  else:

      print("Attacked by trout, Game Over.\n")
  
else :

  print("You fell into a hole, Game over.\n")


