'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem statement:
 Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern. 
Checkerboard pattern:
[[0 1 0 1 0 1 0 1] 
[1 0 1 0 1 0 1 0] 
[0 1 0 1 0 1 0 1] 
[1 0 1 0 1 0 1 0] 
[0 1 0 1 0 1 0 1] 
[1 0 1 0 1 0 1 0] 
[0 1 0 1 0 1 0 1] 
[1 0 1 0 1 0 1 0]]
'''

import numpy as np 

array=np.zeros((8,8))
array[1::2,::2]=1
array[::2,1::2]=1

print(array.reshape(8,8))
