def fibonacci (number_of_series):

  list1 = [0,1]

  for num in range (number_of_series-2) :
  
    list1.append(list1[-1]+list1[-2])
  
  return list1


series_numbers = int(input("Enter The number of series: "))
print(f"The fibonacci series is: {fibonacci(series_numbers)}.")
