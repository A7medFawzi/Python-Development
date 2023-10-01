def word_count (paragraph):
  count = 0

  for space in paragraph :
    if space == ' ':
      count += 1
  return  count + 1 

paragraph_entry = input("Please write text: ")
print(f'There is {word_count(paragraph_entry)} words in your text.')


