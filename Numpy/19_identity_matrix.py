'''
Created on 20/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to create a 3-D array with ones on a diagonal and zeros elsewhere. 
Expected Output:
[[ 1. 0. 0.]
[ 0. 1. 0.] 
[ 0. 0. 1.]]
'''

import numpy as np 

print(np.identity(3))