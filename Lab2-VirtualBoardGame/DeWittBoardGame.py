#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:38:17 2022

@author: juliadewitt
"""
import random as ra
import math as ma
import time as tm

n=4

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
            "Ah. Safe by the hair of your teeth.",
            "Eh. You can stay here, I guess.",
            "Nothing exciting to see here.",
            "No pain, no gain...but also no loss.",
            "Stick around for a while...or don't. Up to you."]

#gOod spot
o=ra.choice(p)
#bad spot
v=ra.choice(g)
#neutral spot
y=ra.choice(u)

'''

HOW TO PRINT SPACE RESPONSES:
    
print(o,n,".") GOOD
print(v,n,".") BAD
print(y) NEUTRAL

'''

print(o,n,".") 
print(v,n,".") 
print(y)

c=input("Press enter to play ")

z=ra.randint(1,6)
print("You rolled: ",z)

a=1
b=1

if a>=1:
    a=a+z
print("Your new position is:", a)
    
if a==(1,4):
    print(y)
    
c

if b>=1:
    b=b+z
    