'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program compare two arrays using numpy. 
Array a: [1 2]
Array b: [4 5]
a > b 
[False False]
a >= b 
[False False] 
a < b 
[ True True] 
a <= b 
[ True True]
'''

import numpy as np 

a=np.array([1,2])
b=np.array([4,5])
print("a>b : ",a>b)
print("a>=b: ",a>=b)
print("a<b : ",a<b)
print("a<=b: ",a<=b)