'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to add a border (filled with 0's) around an existing array. 
Expected Output:
Original array: 
[[ 1. 1. 1.] 
[ 1. 1. 1.] 
[ 1. 1. 1.]] 
1 on the border and 0 inside in the array 
[[ 0. 0. 0. 0. 0.] 
[ 0. 1. 1. 1. 0.] 
[ 0. 1. 1. 1. 0.] 
[ 0. 1. 1. 1. 0.] 
[ 0. 0. 0. 0. 0.]]
'''

import numpy as np

array=np.ones((3,3))

print(np.pad(array,pad_width=1,constant_values=0))