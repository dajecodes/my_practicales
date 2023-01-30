import numpy as np

""" 
NumPy Creating Arrays

To create array data can be given as tuple or list

"""
# data as list
print('array create by list')
data=np.array([1,2,3,4,5,6])
print(data)
a=[22,12,24,32,54]
data1=np.array(a)
print(data1)

# data as tuple
print('array create by tuple')
data2=np.array((12,13,14,15,16))
print(data2)
b=(23,24,25,26,27)
data3=np.array(b)
print(data3)
""" 
Check Number of Dimensions?
NumPy Arrays provides the ndim attribute that
 returns an integer that tells us how many dimensions
 the array have.
"""
# 2D array
print('2D array')
data4=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data4)
print(data4.ndim)

# 3D array
print('3D array')
data5=np.array([[[1,2,3],[4,5,6]],
                [[7,8,9],[10,11,12]],
                [[13,14,15],[16,17,18]]])
print(data5)
print(data5.ndim)

""" 
When the array is created,
 you can define the number of dimensions by using the ndmin argument."""

data6=np.array([1,2,3,4],ndmin=4)
print(data6)
print(data6.ndim)
