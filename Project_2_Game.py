#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

while True :
    a= ["stone","paper","scissor"]
    b= random.choice(a)

    user= input("\nEnter your choice- stone, paper, scissor : ")
    print("\nComputer input is:",b)
    print("\nUser's input is:",user)
    
    if (b=="stone" and user=="paper") or (b=="paper" and user=="scissor") or (b=="scissor" and user=="stone"):
        print("\nCongratulations !!!!!!!!!!! YOU WON THE GAME .......")
        
    elif (b=="stone" and user=="scissor") or (b=="paper" and user == "stone") or (b=="scissor" and user=="paper"):
        print ("\nComputer WON the game\nbetter luck next time!\n")
        
    elif (b=="stone" and user=="stone") or (b=="paper" and user=="paper") or (b=="rock" and user=="rock"):
        print("It's a tie")
        
    else:
        print("Wrong Entry")


# In[ ]:




