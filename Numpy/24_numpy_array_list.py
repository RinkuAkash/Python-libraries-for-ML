'''
Created on 21/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to convert a NumPy array into Python list structure. 
Expected Output:
Original array elements:
[[0 1]
[2 3] 
[4 5]] 
Array to list: 
[[0, 1], [2, 3], [4, 5]]
'''

import numpy as np 

array=np.array([[0,1],[2,3],[4,5]])
print(array.tolist())