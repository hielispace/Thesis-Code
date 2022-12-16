# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:53:17 2022

@author: Eli Asarch
"""

"""
What this code does is finds when the interior sun goes from being dominated
by radition pressure
"""




import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#imports python addons

filename = 'Data_sun.txt'
data = np.loadtxt(filename, delimiter='  ', skiprows=1, dtype=float)
index_0 = len(data)
#This is importing the data from the solar model which is in the text document
#'Data_sun.txt' each coluum is seperated by a double space
#it also takes the length of that data and calls it index



i = 0
i0 = 0
R = 6.957 * 10 ** 8 #Radius of the sun in meters
radius = []
temp = []
pressure = []
n0 = 50
n = 10
m = 20
i = 0
while i*n < index_0:   
    if data[i*n][1] > .1:
        radius.append(data[i*n][1])
        temp.append(data[i*n][2])
        pressure.append(data[i*n][4])
    i = i + 1
i = 0
index_1 = len(radius)
print(radius)

#this extracts the radius (r/R_sun), tempurature (K), and Pressure (Pa)
#from the data, in colums 2, 3, and 5 (to a computer 1, 2 and 4 because they
#start counting from 0
#I'm using every 10th term from the data, because the step size is so small
#it creates strange results
#also near the core results are strange because as we get closer to the core
#T goes to 0 and P goes to 0, so I start at r/R = 0.05, which is good enough.

    
i = 0 #index for the while loop
j = 0 #index for the table values 
cross = 0 #the r value that will be when grab_ab crosses 2.5


dP_dr = [] #dP/dr
dT_dr = [] #dT/dr
dP_dT = [] #dP/dT
dP_dT = [] #dP/dT
grad = [] #grad_ab
radius_table = [0.10518, 0.19749,0.29853,0.3973,0.50246,0.59692,0.69946,0.71377,
                0.80103,0.9002,0] 
#stores the radius values for the table in the paper, the 0 is to make python happy
grad_table = [] #stores the grad values for the table in the paper
#defined as empty to be filled in with the code below



while i+1 < index_1:
    yT = temp[i+1] - temp[i]
    yP = pressure[i+1] - pressure[i]
    x = (radius[i+1] - radius[i]) * R #gets in terms of meters instead of r/R
    dT_dr.append(yT / x)
    dP_dr.append(yP / x)
    dP_dT.append((dP_dr[i]) / (dT_dr[i]))
    grad.append(temp[i] * dP_dT[i] / pressure[i])
    
    """
    locally, the derivative is delta_y/delta_x, that is what this code is doing
    it gets dP/dr and dT/dr, I need dP/dT, which is equal to dP/dr / dT/dr
    the thing I am actually after grad_ab, is T/P * dP/dT, so
    that calculation is done as well
    """

    if ((grad[i] <= 2.5) and (cross == 0)):
        cross = radius[i]
        #this checks for the first time that the crietrion is met, when
        #grad_ab < 2.5
    if ((radius_table[j] == radius[i]) and (j < 10)):
       #the check breaks when j = 10 so the last 0 in radius_table was added,
       #it does not affect the final result
       grad_table.append(temp[i] * dP_dT[i] / pressure[i])
       print(j)
       j = j + 1
       
    i = i + 1



    
    
  
print(cross) #this is, according to my code at r/R = 0.71377, which is close
# to the actual value of 0.714. For the purposes of a rough approximation
#that is just meant to illistrate the Criteron, good enough.

i = 0
while i < len(grad_table):
    grad_table[i] = round(grad_table[i], 3)
    i = i + 1
    
print(grad_table)
radius.pop() #grad has one less term than radius, so python will not graph it
#all this does is remove the last term of radius so python is happy.
"""
mymodel = np.poly1d(np.polyfit(radius, grad, 10))    
myline = np.linspace(0.1, 0.95, 1000)
plt.plot(myline, mymodel(myline), color = 'black', linestyle = '-.')
"""
plt.plot(radius, grad, color = 'b')
plt.xlabel("radius (solar radii)")
plt.ylabel("T/P x dP/dT")
plt.axhline(y = 2.5, color = 'r', linestyle = '-.')
plt.axvline(x = cross, color = 'g', linestyle= '--')
#plt.savefig('thesis_graph.png')




    

   
    




    
    
    
    
    



