ask_number = int(input("How many numbers you want to enter?: "))

list_numbers=[]

for once in range (ask_number):
  
  averge_numbers = int(input("Enter the number: "))
  list_numbers.append(averge_numbers)

average = sum(list_numbers) / len(list_numbers)

print(f"The average of numbers you entered is: {round(average,2)}")






