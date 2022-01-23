#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:38:17 2022

@author: juliadewitt
"""
import random as ra
import time as tm


#Positive beginnings
p=["Woohoo! You're in luck! Jump forward",
            "Lucky, lucky. Jump forward",
            "You know, if this required skill, this would almost be impressive. Jump forward",
            "You've got a knack for this...random...game...Jump forward"]
#neGative beginnings
g=["Yikes. Real Bummer. Really sucks. Go back",
            "Wow, you really aren't great at this game, huh? Go back",
            "Heehee. You have to go back",
            "Whoops! Go back"]

#neUtral responses
u=["Phew, you're safe...For now.",
            "Ah. Safe by the skin of your teeth.",
            "Eh. You can stay here, I guess.",
            "Nothing exciting to see here.",
            "No pain, no gain...but also no loss.",
            "Stick around for a while...or don't. Up to you."]

#roll agaIn responses
l=["That was awful. Try again.",
   "Do better this time. Try again." ,
   "Here, you seem like you could use another go. Try again." ,
   "I'm doing all I can to help, dude. Try again."]



#Winning message
w="Yay. You won. Noice."

'''

HOW TO PRINT SPACE RESPONSES:
    
print(ra.choice(p),n,".") GOOD
print(ra.choice(g),n,".") BAD
print(ra.choice(u)) NEUTRAL

'''


n=ra.randint(1,5)



#c=input("Press enter to roll.")

z=ra.randint(1,6)
#print("You rolled: ",z)

a=1
b=1
input("Welcome to the mystical and fantastical world of THE MOST COMPLEX GAME EVER. Press enter to begin.")


while(a<100) and (b<100):
    print("P1's turn.")
    tm.sleep(1)
    input("Press enter to roll.")
    z=ra.randint(1,6)
    print("You rolled: ",z)
    tm.sleep(1)
    while a<100:
        if a>=1:
            a=a+z
        print("P1, your new position is:", a)
        tm.sleep(1)
        if a==(1,5):
            print(ra.choice(u))
            tm.sleep(1)
        while a%9==0:
            input("Special space! Press enter to reveal your fate!")
            tm.sleep(1)
            print(ra.choice(l))
            tm.sleep(1)
            input("Press enter to roll.")
            tm.sleep(1)
            z=ra.randint(1,6)
            print("You rolled: ",z)
            tm.sleep(1)
            if a>=1:
                a=a+z
            print("P1, your new position is:", a)
            tm.sleep(1)
            if a%9>=1:
                break
        if a % 6 == 0:
            a=a+n
            input("Special space! Press enter to reveal your fate!")
            tm.sleep(1)
            print(ra.choice(p),n,".")
            tm.sleep(1)
            print("P1, your new position is:", a)
            tm.sleep(1)
            print("P1, your turn is over.")
            tm.sleep(1)
            input("Press enter to pass the die.")
            tm.sleep(1)
            break
        elif a % 7 == 0:
            a=a-n
            input("Special space! Press enter to reveal your fate!")
            tm.sleep(1)
            print(ra.choice(g),n,".")
            tm.sleep(1)
            print("P1, your new position is:", a)
            tm.sleep(1)
            print("P1, your turn is over.")
            tm.sleep(1)
            input("Press enter to pass the die.")
            tm.sleep(1)
            break
        elif a>=100:
            print(w)
            tm.sleep(1)
            break
        else:
            print(ra.choice(u))
            tm.sleep(1)
            print("P1, your turn is over.")
            tm.sleep(1)
            input("Press enter to pass the die.")
            tm.sleep(1)
            break
            
    
    z=ra.randint(1,6)
    
    
    print("P2's turn.")
    tm.sleep(1)
    input("Press enter to roll.")
    tm.sleep(1)
    z=ra.randint(1,6)
    print("You rolled: ",z)
    tm.sleep(1)
    while b<100:
        if b>=1:
            b=b+z
        print("P2, your new position is:", b)
        tm.sleep(1)
        if b==(1,5):
            print(ra.choice(u))
            tm.sleep(1)
        while b%9==0:
            input("Special space! Press enter to reveal your fate!")
            tm.sleep(1)
            print(ra.choice(l))
            tm.sleep(1)
            input("Press enter to roll.")
            tm.sleep(1)
            z=ra.randint(1,6)
            print("You rolled :",z)
            tm.sleep(1)
            if b>=1:
                b=b+z
            print("P2, your new position is:", b)
            tm.sleep(1)
            if b%9>=1:
                break
        if b % 6 == 0:
            b=b+n
            input("Special space! Press enter to reveal your fate!")
            tm.sleep(1)
            print(ra.choice(p),n,".")
            tm.sleep(1)
            print("P2, your new position is:", b)
            tm.sleep(1)
            print("P2, your turn is over.")
            tm.sleep(1)
            input("Press enter to pass the die.")
            tm.sleep(1)
            break
        elif a % 7 == 0:
            b=b-n
            input("Special space! Press enter to reveal your fate!")
            tm.sleep(1)
            print(ra.choice(g),n,".")
            tm.sleep(1)
            print("P2, your new position is:", b)
            tm.sleep(1)
            print("P2, your turn is over.")
            tm.sleep(1)
            input("Press enter to pass the die.")
            tm.sleep(1)
            break
        elif b>=100:
            print(w)
            tm.sleep(1)
            break
        else:
            print(ra.choice(u))
            tm.sleep(1)
            print("P2, your turn is over.")
            tm.sleep(1)
            input("Press enter to pass the die.")
            tm.sleep(1)
            break


'''
    if b>=1:
        b=b+z
    print("P2, your new position is:", b)
        
    if b==(1,7):
        print(y)
    while a%2==0:
      print(i)
      input("Press enter to roll.")
      if a>=1:
          a=a+z
      print("P1, your new position is:", a)
      if a%2>=1:
          break
    elif b % 6 == 0:
        b=b+n
        print(o,n,".")
        print("P2, your new position is:", b)
    elif b % 7 == 0:
        b=b-n
        print(v,n,".")
        print("P2, your new position is:", b)
    elif b==100:
        print(w)
        break
    else:
        print(y)
        print("P1, you're up.")
        
        '''
        
        
        
        
        