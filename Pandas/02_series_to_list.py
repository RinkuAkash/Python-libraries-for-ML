'''
Created on 21/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to convert a Panda module Series to Python list and it's type. 
'''

import pandas as pd 

series=pd.Series([1,2,3,4,5,6])
print(series.tolist())