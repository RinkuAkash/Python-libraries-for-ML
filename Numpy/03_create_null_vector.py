'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to create a null vector of size 10 and update sixth value to 11. 
[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 
Update sixth value to 11 
[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
'''

import numpy as np
nullVector=np.zeros(10)
print(nullVector)
nullVector[6]=11
print(nullVector)