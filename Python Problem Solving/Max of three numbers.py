enter1 = int(input("First number: "))
enter2 = int(input("Second number: "))
enter3 = int(input("Third number: "))

max_num=max(enter1,enter2)

if enter3 > max_num :
  print(f"Largest number you entered is: {enter3}")
else:
  print(f"Largest number you entered is: {max_num}")