'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem statement:
20. Write a Python program to concatenate two 2-dimensional arrays. 
Expected Output:
Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
Expected Output:
[[ 0 1 3 0 2 4]
[ 5 7 9 6 8 10]] 
'''

import numpy as np 

array1=np.array([[0,1,3],[5,7,9]])
array2=np.array([[0,2,4],[6,8,10]])
print(np.concatenate((array1,array2),1))