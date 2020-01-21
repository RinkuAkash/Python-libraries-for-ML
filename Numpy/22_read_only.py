'''
Created on 21/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to make an array immutable (read-only). 
Expected Output:
Test the array is read-only or not:
Try to change the value of the first element:
Traceback (most recent call last):
File "19236bd0-0bd9-11e7-a232-c706d0968eb6.py", line 6, in 
x[0] = 1
ValueError: assignment destination is read-only
'''

import numpy as np 

array=np.array([1,2,3,4])
array.flags.writeable=False
array[0]=10