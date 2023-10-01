print('''       ||
 .-----  -----.
 |  __    __  |                  
 | |_ |  | _| |                     
 |   \ \/ /   |
 |    \  /    |                    
 |     \/     |
 |            |
 '-----..----sSSSSSSSs
       ||  sSSSSSSSSSSSs
       || sSSS,_   _,SSSs
       ||SSSS |'| |'| SSSS  
       ||SSSS "" - "" SSSSs
       ||SSS\'' ___,''/SSSs    
       ||SSSS\  `-'  /SSSSS
       ||SSSS(`-----')SSSS   
   _.-'||  ,  `-._.-'    `.
 .'   ,||_//___  Y         ;     
 `.    `" \___/             ;          
   `-.___.'            `;   ;
        ||`:            :;   ;  \n ''')


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is her name? \n")

name1_lower= name1.lower()
name2_lower=name2.lower()

count_true1=name1_lower.count("t")+name1_lower.count("r")+name1_lower.count("u")+name1_lower.count("e")

count_true2 = name2_lower.count("t")+name2_lower.count("r")+name2_lower.count("u")+name2_lower.count("e")


total_true = count_true1 + count_true2

count_love1=name1_lower.count("l")+name1_lower.count("o")+name1_lower.count("v")+name1_lower.count("e")

count_love2=name2_lower.count("l")+name2_lower.count("o")+name2_lower.count("v")+name2_lower.count("e")

total_love = count_love1 + count_love2

total_score= str(total_true) + str(total_love) 

final_total=int(total_score)

if final_total < 10 or final_total > 90 :
  print(f"Your score is {total_score}, you go together like coke and mentos.")

elif  40<= final_total <= 50 :
  print(f"Your score is {total_score}, you are alright together.") 

else :
  print(f"Your score is {total_score}.")


