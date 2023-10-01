def merge_sorted (list1,list2):
  l3 = list1 + list2
  l3.sort()
  return l3


first_list = [5,8,900,60]
second_list = [100,50,70,90]
print(f"The Final list is: {merge_sorted(first_list,second_list)}.")
