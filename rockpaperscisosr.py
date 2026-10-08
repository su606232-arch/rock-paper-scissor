"""
workflow of project
1 input free user (rock ,paper, scissor)
2 computer choice(computer will chose randomly not conditionly )
3 result print 

cases
a rock 
rock - rock = tie
rock - paper = paper win 
rock - scissor = rock win 


b paper 
paper - paper = tie
paper - rock = papwer win 
paper - scissor = scissor win

c sessior 
sessior - sessior = tie
scissor - rock = rock win 
scissor - paper = scissor win 
"""
    
import random
item_list= ["Rock ", "Paper", "Scissor"]

user_choice = input ( "Enter your move  = Rock,Paper , Scissor")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chose are same: = match tie")
    
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers rock = computer ")
    else:
        print("rock smshes scissor = you win")
        
elif user_choice == "Paper ":
    if comp_choice == "Scissor":
        print("scioor cuts paper , computer win")
    else:
        print("paper covers rock , you win ")
        
elif user_choice == "Scissor":
    if comp_choice == "paper":
        print("scissor cuts paper ,you win")
    else:
        print("rock smasher scissor , commputer win")
        
        
    
        
