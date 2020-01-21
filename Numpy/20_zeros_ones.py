'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem  statement:
Write a Python program to create an array which looks like below array. 
Expected Output:
[[ 0. 0. 0.]
[ 1. 0. 0.]
[ 1. 1. 0.]
[ 1. 1. 1.]]
'''

import numpy as np 

array=np.zeros((4,3))
for i in range(0,3):
    array[i+1:,:i+1]=1
print(array)