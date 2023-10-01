def duplicate_remover (list_check) :
  each_word = []
  for name in list_check :
    if name not in each_word:
      each_word.append(name)
  return each_word





take_list = ['ahmed','khalid','mitwali','marzok','ahmed','khalid','ahmed']
print(f"The final list is: {duplicate_remover(take_list)}")

      


