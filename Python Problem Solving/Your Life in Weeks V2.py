age = input("What is your current age?")

age_as_int= int(age)

days=(90*365) -(365 * age_as_int)
weeks=(90*52) -(52*age_as_int)

months=(90*12)-(12*age_as_int)

print(f"If you will live 90 years,You have {days} days, {weeks} weeks, and {months} months left.")



