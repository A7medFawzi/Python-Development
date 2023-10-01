import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dic_of_alphapet = {rows.letter:rows.code for (index,rows) in data.iterrows()}
user_input = input("Enter Your Name Please: ").upper()

#lst_input = list(user_input)
#alpha_list = []
#for lr in lst_input:
    #alpha_list.append(dic_of_alphapet[lr])

phonatic_list = [dic_of_alphapet[lr] for lr in user_input]
print(phonatic_list)