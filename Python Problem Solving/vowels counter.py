def vowels_count (paragraph):
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  count = 0  
  for letter in paragraph :
    if letter in vowels:
      count += 1
  return  count 

paragraph_entry = input("Please write text: ")
print(f'There is {vowels_count(paragraph_entry)} vowels letters in your text.')


