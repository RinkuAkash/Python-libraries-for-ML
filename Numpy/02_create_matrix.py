'''
Created on 20/01/2020
@author: B Akash
'''
'''
Problem statement:
Create a 3x3 matrix with values ranging from 2 to 10.  
Expected Output:
[[ 2 3 4] 
[ 5 6 7] 
[ 8 9 10]] 
'''

import numpy as np

array=np.arange(2,11)
print(array.reshape(3,3))