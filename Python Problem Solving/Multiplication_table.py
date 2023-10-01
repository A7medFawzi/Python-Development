def multiplication_table (number):
  count=0
  final=0
  while final != 10 :
    count+=1
    state = number*count 
    final +=1

    print( f"{number} * {count} = {state}")
  return ''


number= int(input("Enter number: "))
print (f"The multiplication Table of {number} is:")

multiplication_table(number)