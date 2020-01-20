'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to append values to the end of an array. 
Expected Output:
Original array:
[10, 20, 30] 
After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]
'''

import numpy as np 

array1=[10,20,30]
values=[40,50,60,70,80,90]
print(np.append(array1,values))