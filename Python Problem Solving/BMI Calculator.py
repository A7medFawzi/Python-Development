print('''
██████  ███    ███ ██      ██████  █████  ██       ██████ ██    ██ ██       █████  ████████  ██████  ██████  
██   ██ ████  ████ ██     ██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
██████  ██ ████ ██ ██     ██      ███████ ██      ██      ██    ██ ██      ███████    ██    ██    ██ ██████  
██   ██ ██  ██  ██ ██     ██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
██████  ██      ██ ██      ██████ ██   ██ ███████  ██████  ██████  ███████ ██   ██    ██     ██████  ██   ██ 
                                                                                                             
'''                                                                                                            
)

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))



bmi= weight / height**2 
new_bmi=round(bmi)

if bmi < 18.5 :
  print(f"Your BMI is {new_bmi}, you are underweight.")
if bmi < 25 :
  print(f"Your BMI is {new_bmi}, you have a normal weight.")
elif bmi <30:
  print(f"Your BMI is {new_bmi}, you are slightly overweight.")
elif bmi < 35:
   print(f"Your BMI is {new_bmi}, you are obese.")
else:
  print(f"Your BMI is {new_bmi}, you are clinically obese.")

