'''
Created on 21/01/2020
@author: B Akash
'''
'''
Problem statement:
 Write a Python program to how to add an extra column to an numpy array. 

Expected Output:
[[ 10 20 30 100]
[ 40 50 60 200]]
'''

import numpy as np 

array=np.array([[10,20,30],[40,50,60]])
newColumns=np.array([100,200])
print(np.column_stack((array,newColumns)))