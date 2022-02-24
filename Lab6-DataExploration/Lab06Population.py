#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:08:13 2022

@author: juliadewitt
"""
import numpy as np
import matplotlib.pyplot as plt

m=r"/Users/juliadewitt/Desktop/School Stuff/Senior Year/Second Semester/Scientific Computing/WorldPop.txt"
in_file=open(m,"r")
yr=[]
pp=[]
for line in in_file:
    x=line.split(r"|")
    r=int(x[-1])
    if r==100:
        yr.append(int(x[0]))
        pp.append(int(x[2]))
in_file.close()

year=np.array(yr)
pop=np.array(pp)

#print(year)
#print(pop)


plt.scatter(year,pop)
plt.xlabel("Year")
plt.ylabel("Number of 100 Year Olds")
plt.title("Number of 100 Year Old US Residents Reported from 1990 Projected through 2060")
plt.show()

print("Caption- The above figure depicts the number of 100-year-old US residents (100USR) per year according to the United States Census Bureau. Population estimate data from 2010 to 2019 are derived from the 2010 US Census. Projected data for 2020 to 2060 are based on projections determined in 2017 utilizing the cohort-component method. (US Census Bureau)")
print("")
print("In plotting the number of 100USR per year vs. time, a loosely exponential trend over many years arises. From 1990 to approximately 2000, the plotting is nearly linear, which suggests a direct variation relationship between the progression of time and the number of 100USR. However, after a slight decrease in the number of 100USR from 2000 to approximately 2005, the trend resumed its increase in closer to a parabolic fashion. In order to project the number of people in each age group from 2020 to 2060, the US Census Bureau implements the cohort-component method. The cohort-component method the different population-impacting factors are mathematically imposed on each individual “cohort” of people born per year. In addition to birth and death rates, the migration patterns of individuals must also be considered when studying the number of residents in a given area. Finally, the “projected fertility rates” (US Census Bureau) are applied to the female population and the resulting number of births are added to the initial population. This cohort-component method provides for a dramatic increase of 100USR per year from approximately 2020 to 2060 that corresponds most to an exponential growth from 2030 to 2045, then a nearly linear growth pattern from 2045 to 2060.")
print("")
print("The US Census Bureau also provides information regarding the population of the entirety of the world. Furthermore, the data collected and calculated is broken down into three subsets for each country reported—an inclusive male and female count, a male count, and a female count. Therefore, for every year’s worth of data for each country, three sets of data are present for each age of human (the reported range of ages is 0 through 100, including both 0 and 100). The above figure details the number of 100USR for the inclusive male and female count. ")
print("")
print("MLA Citation of data source: “Population Estimates and Projections for 227 Countries and Areas.” International Database (IDB), United States Census Bureau, https://www.census.gov/data-tools/demo/idb/#/country?COUNTRY_YEAR=2022&amp;COUNTRY_YR_ANIM=2060. ")

#x=line.split("|")
#int(x[-1])---gives age
