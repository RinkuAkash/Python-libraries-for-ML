'''
Created on 21/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Python program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
'''


import pandas as  pd 
import numpy as np 

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

dataFrame= pd.DataFrame(exam_data,labels)

dataFrame=dataFrame.sort_values(by='name',ascending=False)
print("sort by name:")
print(dataFrame)
print("sort by score:")
print(dataFrame.sort_values(by='score'))