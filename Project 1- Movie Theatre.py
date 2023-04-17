#!/usr/bin/env python
# coding: utf-8

# In[ ]:


r_seat=20 #available recliner seats
n_seat=50 #available normal seats

while True :

    print ("-"*80)
    print ("                         WELCOME TO INOX CINEMAS")
    print ("-"*80)

    
    name = input("\nEnter Customer Name :  ")
    seat = int(input ("\nHow many seats do you want to book?  "))
    print ("\nThe price of Normal Seat is Rs. 250/- \nThe price of Recliner Seat is Rs. 450/- ")
    seat_type = input ("\nWhat type of seats do you want to have? (normal/recliner)  ")
    
    if seat_type == "recliner" or seat_type == "Recliner": 
        if r_seat>seat: 
            amount = seat*450
            print ("_"*80)
            print ("_"*80)
            print("\nThe amount of recliner seat is: ",amount)
            print ("_"*80)
            r_seat -=seat
            print ("_"*80)
            print ("\navailable recliner seats now after this booking: ",r_seat)
            print ("_"*80)
            
        if r_seat<seat : print ("\nRecliner seats not available")
        if r_seat ==0: print ("\nRecliner seats Bookings full")
    
    
    if seat_type == "normal" or seat_type == "Normal": 
        if n_seat>seat: 
            amount = seat*250
            print ("_"*80)
            print ("_"*80)
            print("\nThe amount of Normal seat is : " ,amount)
            print ("_"*80)
            n_seat -=seat
            print ("_"*80)
            print ("\navailable normal seats now after this booking: ",n_seat)
            print ("_"*80)
            
        if n_seat<seat: print ("\nNormal seat is not available")
        if n_seat ==0: print ("\nNormal seats Bookings full")
    
    print ("_"*80)
    combo = input ("\ndo you want combo of rs. 300?   ")
    if combo == "yes" :
        amount +=300
        print ("_"*80)
        print ("_"*80)
        print ("\nAfter adding combo final payable amount is : ",amount)
        print ("_"*80)
        print ("_"*80)
    else :
        print ("_"*80)
        print ("_"*80)
        print ("\nFinal payable amount is : ",amount)
        print ("_"*80)
        print ("_"*80)


