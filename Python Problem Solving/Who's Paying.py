names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

import random 

# way number 1

#len_list =len(names)
#random_name = random.randint(0,len_list-1)

#print(f"{names[random_name]} is going to buy the meal today.")


# way number 2

person_who_pay = random.choice(names)

print(f"{person_who_pay} is going to buy the meal today.")
