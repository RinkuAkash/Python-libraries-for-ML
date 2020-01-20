'''
Created on 20/01/2020
@author: B Akash
'''
'''
problem statement:
Write a Python program to change the data type of an array. 
Expected Output:
[[ 2 4 6]
[ 6 8 10]] 
Data type of the array x is: int32 
New Type: float64 
[[ 2. 4. 6.] 
[ 6. 8. 10.]]
'''

import numpy as np 

array=np.array([[2,4,6],[6,8,10]],dtype=np.int32)
print(array)
print(np.array(array,dtype=np.float64))