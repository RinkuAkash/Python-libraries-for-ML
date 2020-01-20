'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to save a Numpy array to a text file.
'''

import numpy as np 

array=np.array([1,2,3,4,5,6,7,8,9])
np.savetxt("NumPyArray.txt",array)