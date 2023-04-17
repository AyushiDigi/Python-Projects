#!/usr/bin/env python
# coding: utf-8

# In[1]:


math=5
science=7
fictional=10
novels=30

username = "ayushi@gmail.com"
password = "1234"

print ("ENTER YOUR LOGIN DETAILS BELOW")

u = input ("Enter Username : ")
p = input("Enter Password : ")

if u==username.lower() and p==password :
    print ("login successful")
    while True:
        print ("\n\n******************* WELCOME TO LIBRARY *****************************\n\n")
        print ("\nAvailabe maths books in library : ",math)
        print ("\nAvailabe science books in library : ",science)
        print ("\nAvailabe fiction books in library : ",fictional)
        print ("\nAvailabe novels in library : ",novels)
        
        a=input("""\nYou want to borrow book or you want to return the borrowed book? 
        \npress r to return book or press b to borrow book : """)
        
        if a.lower() == "b":
            borrower= input ("\nEnter borrower's name : ")
            choice= int(input ("""\nwhich kind of books do you want to borrow : 
               \n Type 1 to borrow math book
               \n Type 2 to borrow science book
               \n press 3 to borrow fictional book
               \n press 4 to borrow novel
               \n Enter your book choice: """))
            if choice==1:
                num_book=int(input("\nHow many math book do you want to borrow? "))
                if num_book<=math:
                    math-=num_book
                    print(f"\n{borrower}, you have successfully borrowed {num_book} math book!")
                    print ("\nAvailable math book after borrowing : ",math)
                else:
                    print(f"\nSorry, only {math} math book left.")
            elif choice==2:
                num_book=int(input("\nHow many science book do you want to borrow? "))
                if num_book<=science:
                    science-=num_book
                    print(f"\n{borrower}, you have successfully borrowed {num_book} science book!")
                    print ("\nAvailable science book after borrowing : ",science)
                else:
                    print(f"\nSorry,{science} science book left.")
            
            elif choice==3:
                num_book=int(input("\nHow many fictional book do you want to borrow? "))
                if num_book<=fictional:
                    fictional-=num_book
                    print(f"\n{borrower}, you have successfully borrowed {num_book} fictional book!")
                    print ("\nAvailable fictional book after borrowing : ",fictional)
                else:
                    print(f"\nSorry,{fictional} fictional book left.")
            elif choice==4:
                num_book=int(input("\nHow many novel do you want to borrow? "))
                if num_book<=novels:
                    novels-=num_book
                    print(f"\n{borrower}, you have successfully borrowed {num_book} novel(s)!")
                    print ("\nAvailable novels after borrowing : ",novels)
                else:
                    print(f"\nSorry,{novels} novel left.")
        elif a.lower() == "r":
            choice= int(input ("""\nWhich kind of book you want to return : 
               \n Type 1 to return math book
               \n Type 2 to return science book
               \n Press 3 to return fictional book
               \n Press 4 to return novel
               \n Enter your book choice: """))
        if choice==1:
            num_book=int(input("\nHow many math book do you want to return? "))
            math+=num_book
            print(f"\n{num_book} math book have been returned successfully!")
            print ("\nAvailable math book after return :" ,math)
        else:
            print ("\nInvalid input. Please try again.")
        
        if choice==2:
            num_book=int(input("\nHow many science book do you want to return? "))
            science+=num_book
            print(f"\n{num_book} science book have been returned successfully!")
            print ("\nAvailable science book after return :" ,science)
        else:
            print ("\nInvalid input. Please try again.")
        
        if choice==3:
            num_book=int(input("\nHow many fictional book do you want to return? "))
            fictional+=num_book
            print(f"\n{num_book} fictional book have been returned successfully!")
            print ("\nAvailable fictional book after return :" ,fictional)
        else:
            print ("\nInvalid input. Please try again.")
        
        if choice==4:
            num_book=int(input("\nHow many novel do you want to return? "))
            fictional+=num_book
            print(f"\n{num_book} novel​ have been returned successfully!")
            print ("\nAvailable fictional book novelafter return :" ,novel)
        else:
            print ("\nInvalid input. Please try again.")
else :
    print ("Login unsuccessful. Try again later")



# In[ ]:




