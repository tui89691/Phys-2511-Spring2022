#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 13:01:53 2022

@author: juliadewitt
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp


delta_x=float(input("Input delta x value: "))

x=np.arange(-5,5,delta_x)

def y1(x):
    return (-0.5*x)+4.0
def y2(x):
    #print(x)
    return (-0.29*x*x)-x+12.5
def y3(x):
    return 1.0+10*(x+1.0)*np.exp(-x**2)

F1=y1(x)
F2=y2(x)
F3=y3(x)


area1=sum(delta_x*F1)
area2=sum(delta_x*F2)
area3=sum(delta_x*F3)

'''
print(area1)
print(area2)
print(area3)
'''

ac=[40.0,100.83,27.72]

def percdif(j,k):
    return((j-k)/k)*100

percdif1=percdif(area1,ac[0])
percdif2=percdif(area2,ac[1])
percdif3=percdif(area3,ac[2])

#percdifs=[percdif1,percdif2,percdif3]

Rpercdif1=[]
Rpercdif2=[]
Rpercdif3=[]

for n in np.arange(.1,1,.01):
    f=np.arange(-5,5,n)
    
    R1=y1(f)
    R2=y2(f)
    R3=y3(f)
    
    Rarea1=sum(n*R1)
    Rarea2=sum(n*R2)
    Rarea3=sum(n*R3)
    '''
    print(Rarea1)
    print(Rarea2)
    print(Rarea3)
    '''
    new_Rpercdif1=percdif(Rarea1,ac[0])
    Rpercdif1.append(new_Rpercdif1)
    new_Rpercdif2=percdif(Rarea2,ac[1])
    Rpercdif2.append(new_Rpercdif2)
    new_Rpercdif3=percdif(Rarea3,ac[2])
    Rpercdif3.append(new_Rpercdif3)
    
h=np.array(Rpercdif1)    
i=np.array(Rpercdif2)
j=np.array(Rpercdif3)

k=np.arange(.1,1,.01)

'''
print(h)
print(i)
print(j)
'''
print("Calculated area of y1 using Riemann sum with delta x value of", delta_x,"is", area1)
print("Calculated area of y2 using Riemann sum with delta x value of", delta_x,"is", area2)
print("Calculated area of y3 using Riemann sum with delta x value of", delta_x,"is", area3)

print("")
print("Percent difference between calculated area and actual area of y1:", percdif1)
print("Percent difference between calculated area and actual area of y2:", percdif2)
print("Percent difference between calculated area and actual area of y3:", percdif3)

print("")
f=sp.integrate.quadrature(y1,-5,5)
g=sp.integrate.quadrature(y2,-5,5)
w=sp.integrate.quadrature(y3,-5,5)
print("")
print("Calculated area of y1 using scipy.integrate.quadrature", f)
print("Calculated area of y2 using scipy.integrate.quadrature", g)
print("Calculated area of y3 using scipy.integrate.quadrature", w)

print("")

print("Percent difference between calculated area and scipy.integrate.quadrature area of y1:", percdif(area1,f))
print("Percent difference between calculated area and scipy.integrate.quadrature area of y2:", percdif(area2,g))
print("Percent difference between calculated area and scipy.integrate.quadrature area of y3:", percdif(area3,w))

fig,ax=plt.subplots()
ax.scatter(k,h)
ax.scatter(k,i)
ax.scatter(k,j)
ax.set_xlabel("Delta X Values")
ax.set_ylabel("% Difference b/w Approximated and Actual Area on [-5,5]")

plt.show()


'''
fig,ax=plt.subplots()
ax.scatter(delta_x,percdif1)
ax.scatter(delta_x,percdif2)
ax.scatter(delta_x,percdif3)
plt.show()
'''
'''
fig,ax=plt.subplots()
ax.plot(x,F1)
ax.plot(x,F2)
ax.plot(x,F3)


plt.show()
'''