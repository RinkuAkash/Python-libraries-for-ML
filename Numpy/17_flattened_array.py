'''
Created on 20/01/2020
@author: B Akash
'''
'''
Program statement:
Write a Python program to create a contiguous flattened array. 
Original array:
[[10 20 30] 
[20 40 50]] 
New flattened array: 
[10 20 30 20 40 50]
'''

import numpy as np 

array=np.array([[10,20,30],[20,40,50]])

print(array.flatten())