def leap_year (year):
  if year % 4 == 0 :
    if year % 100 == 0 :
      if year % 400 == 0 :
        print("This is a Leap year.")
      else:
        print("This is not a Leap year.")
    else:
      print("This is a Leap year.")
  else:
    print("This is not a Leap year.")


year_want_check = int(input("Enter The year you want to check: "))

leap_year(year_want_check)
