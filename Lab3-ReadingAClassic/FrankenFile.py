#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:05:42 2022

@author: juliadewitt
"""


import numpy as np
import matplotlib.pyplot as plt

#functions
def names_list(x):
    #counts names in given chapter
    print("Chapter",x) 
    m=r"/Users/juliadewitt/Desktop/School Stuff/Senior Year/Second Semester/Scientific Computing/FrankC1.txt"
    m=m[:-5]+str(x)+".txt"
    in_file=open (m,"r")
    data=in_file.read()
    occurrencesVF=data.count("Frankenstein")+data.count("Victor")+data.count("Victor Frankenstein")
    print("Victor count:",occurrencesVF)
    occurrencesHC=data.count("Clerval")+data.count("Henry Clerval")+data.count("Henry")
    print("Clerval count:",occurrencesHC)
    occurrencesFM=data.count("The Creature")+data.count("creature ")+data.count("Creature")
    print("Creature count:",occurrencesFM)
    occurrencesAG=data.count("Agatha")
    print("Agatha count:",occurrencesAG)
    occurrencesCA=data.count("Caroline")
    print("Caroline count:",occurrencesCA)
    occurrencesDL=data.count("Old Man De Lacey")+data.count("De Lacey")
    print("De Lacey count:",occurrencesDL)
    occurrencesEZ=data.count("Elizabeth")
    print("Elizabeth count:",occurrencesEZ)
    occurrencesER=data.count("Ernest")
    print("Ernest count:",occurrencesER)
    occurrencesFX=data.count("Felix")
    print("Felix count:",occurrencesFX)
    occurrencesJS=data.count("Justine")
    print("Justine count:",occurrencesJS)   
    occurrencesWL=data.count("William")
    print("William count:",occurrencesWL)  
    in_file.close()
 

    
def names_chart(x):
    #counts names in given chapter
   # print("Chapter",x) 
    m=r"/Users/juliadewitt/Desktop/School Stuff/Senior Year/Second Semester/Scientific Computing/FrankC1.txt"
    m=m[:-5]+str(x)+".txt"
    in_file=open (m,"r")
    data=in_file.read()
   # occurrencesdummy=data.count("twerk")
    occurrencesVF=data.count("Frankenstein")+data.count("Victor")+data.count("Victor Frankenstein")
    occurrencesHC=data.count("Clerval")+data.count("Henry Clerval")+data.count("Henry")
    occurrencesFM=data.count("The Creature")+data.count("creature ")+data.count("Creature")
    occurrencesAG=data.count("Agatha")
    occurrencesCA=data.count("Caroline")
    occurrencesDL=data.count("Old Man De Lacey")+data.count("De Lacey")
    occurrencesEZ=data.count("Elizabeth")
    occurrencesER=data.count("Ernest")
    occurrencesFX=data.count("Felix")
    occurrencesJS=data.count("Justine")
    occurrencesWL=data.count("William")
    in_file.close()
    temp=[]
   # temp.append(occurrencesdummy)
    temp.append(occurrencesVF)
    temp.append(occurrencesHC)
    temp.append(occurrencesFM)
    temp.append(occurrencesAG)
    temp.append(occurrencesCA)
    temp.append(occurrencesDL)
    temp.append(occurrencesEZ)
    temp.append(occurrencesER)
    temp.append(occurrencesFX)
    temp.append(occurrencesJS)
    temp.append(occurrencesWL)
    
    return temp
    
'''
#program
def temp1(x):
    for x in range(1,25):
        print(names_list(x))
'''

x=(0,0,0,0,0,0,0,0,0,0,0)

temp1=[]
temp1.append(x)
for x in range(1,25):
    temp1.append(names_chart(x))


r=np.array(temp1)    
print(r)   


def graph(x,p):       
    plt.rcdefaults()
    fig, ax=plt.subplots()

    Chapter=(range(1,26))
    y_pos=np.arange(len(Chapter))
    Mentions=(r[:,x])
    ax.barh(y_pos, Mentions, align='center')
    ax.set_yticks(y_pos)
    
    ax.set_xlabel('Mentions')
    ax.set_ylabel('Chapter')
    ax.set_title(p)
                  
    plt.show()

names=("Victor Frankenstein","Henry Clerval","The Creature","Agatha","Caroline",
       "Old Man De Lacey","Elizabeth","Ernest","Felix","Justine","William")

print(graph(0,"Mentions of Victor in Frankenstein"))
print(graph(1,"Mentions of Henry Clerval in Frankenstein"))
print(graph(2,"Mentions of The Creature in Frankenstein"))
print(graph(3,"Mentions of Agatha in Frankenstein"))
print(graph(4,"Mentions of Caroline in Frankenstein"))
print(graph(5,"Mentions of Old Man De Lacey in Frankenstein"))
print(graph(6,"Mentions of Elizabeth in Frankenstein"))
print(graph(7,"Mentions of Ernest in Frankenstein"))
print(graph(8,"Mentions of Felix in Frankenstein"))
print(graph(9,"Mentions of Justine in Frankenstein"))
print(graph(10,"Mentions of William in Frankenstein"))
              
              
              
              