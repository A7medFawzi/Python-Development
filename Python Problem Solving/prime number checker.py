def prime_checker(number):
    my_number = False
    for num in range(2, number - 1):
        if number % num == 0:
          my_number = True
    if my_number == True:
        print("this is not prime number")
    else:
        print("this is prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
