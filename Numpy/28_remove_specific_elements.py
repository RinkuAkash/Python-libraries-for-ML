'''
Created on 21/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to remove specific elements in a numpy array. 

Expected Output:
Original array: 
[ 10 20 30 40 50 60 70 80 90 100]
Delete first, fourth and fifth elements:
[ 20 30 60 70 80 90 100]
'''

import numpy as np 

array=np.array([ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(np.delete(array,[0,3,4]))