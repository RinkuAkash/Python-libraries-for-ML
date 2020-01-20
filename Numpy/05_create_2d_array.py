'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to create a 2d array with 1 on the border and 0 inside.  
Expected Output:
Original array: 
[[ 1. 1. 1. 1. 1.] 
[ 1. 1. 1. 1. 1.] 
[ 1. 1. 1. 1. 1.] 
[ 1. 1. 1. 1. 1.] 
[ 1. 1. 1. 1. 1.]] 
1 on the border and 0 inside in the array 
[[ 1. 1. 1. 1. 1.] 
[ 1. 0. 0. 0. 1.] 
[ 1. 0. 0. 0. 1.] 
[ 1. 0. 0. 0. 1.] 
[ 1. 1. 1. 1. 1.]]
'''

import numpy as np

array=np.ones((5,5))
array[1:4,1:4]=0
print(array)
