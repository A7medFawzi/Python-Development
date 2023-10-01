ask_number = int(input("Enter number: "))

ele = []

for num in range (ask_number):

  if num % 3 == 0 and num % 5 == 0 :
    ele.append(num)
  
print("The numbers are: ",ele)








