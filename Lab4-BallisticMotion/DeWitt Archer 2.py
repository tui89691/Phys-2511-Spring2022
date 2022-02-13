#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:18:52 2022

@author: juliadewitt
"""
import math as ma
import numpy as np
import matplotlib.pyplot as plt
import time as tm

#which=input("There are 5 targets available for you to shoot (1, 2, 3, 4, and 5). Choose a target: ")
theta=ma.radians(float((input("Projectile angle [deg]: "))))
v0=float(input("Initial velocity [m/s]: "))
timesteps=float(input("Provide number of timesteps: "))



ynaut=1
xnaut=0
g=9.8
time=v0/g
delta_t=time/timesteps
m=0.018

a_x=0
a_y=-g

v_x0=v0*ma.cos(theta)
v_y0=v0*ma.sin(theta)

v_x=[v_x0]
v_y=[v_y0]

pos_x=[xnaut]
pos_y=[ynaut]

positionfinal_x=2*v_x0*time

for n in np.arange(0,time,delta_t):
   new_vx=v_x[-1]+a_x*n
   v_x.append(new_vx)  
  
   new_vy=v_y[-1]+a_y*n
   v_y.append(new_vy)     
  
   new_pos_x=pos_x[-1]+v_x[-1]*n 
   pos_x.append(new_pos_x)    
  
   new_pos_y=pos_y[-1]+v_y[-1]*n
   pos_y.append(new_pos_y)
  
   if new_pos_y <=0:
       break
plt.scatter(pos_x,pos_y)
plt.show

'''
print(v_x)
print(v_y)
print(pos_x)
print(pos_y)
\

if which==1:
    target=300
if which==2:
    target=100
if which==3:
    target=100
if which==4:
    target=1000
if which==5:
    target=3000
 '''   

target=450

print(" ")

print("Your arrow is whistling through the air!!!")

tm.sleep(3)
print("It's hit... something! But has it hit the target?")
tm.sleep(2)

if pos_x[-1] == target:
    print("Yes!!! You did it! Great job!")
else:
    print("Nope. Better luck next time.")

print(" ")

tm.sleep(2)
print("The theoretical landing position of your shot is", positionfinal_x, "m from your starting position.")

tm.sleep(2)
print("The simulated landing position of your shot is", pos_x[-1], "m from your starting position.")

tm.sleep(2)
print("The difference between these two values is", positionfinal_x-pos_x[-1],"m.")

print(" ")

tm.sleep(3)
print("The target is" , target, "m from your starting position.")

tm.sleep(1)
if pos_x[-1] > target:
    overshot=pos_x[-1]-target
    print("You overshot the target by", overshot, "m")

if pos_x[-1] < target:
    undershot=target-pos_x[-1]
    print("You undershot the target by", undershot, "m.")  

if pos_x[-1] == target:
    print("You have hit the target!")



