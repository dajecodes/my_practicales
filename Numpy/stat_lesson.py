""" 
[18, 24, 67, 55, 42, 14, 19, 26, 33]
The mean is the average value of the dataset. We can calculate it
 by adding all prices together and dividing by the number of products: mean = 298/9 = 33.1
"""
data=[18, 24, 67, 55, 42, 14, 19, 26,33]
mean=sum(x for x in data)/len(data)
print(mean)
""" 
median: the middle value of an ordered dataset.
"""
data.sort()
# print((len(data)//2)+1 if len(data)%2 !=2 else )
median=None
if len(data)%2 !=0:
    median=data[(len(data)//2)]
else:
    median=(data[len(data)/2]+data[(len(data)/2-1)])/2
# The median is 26, as that's the middle value.
print(median)  
# mean round to 2 digits
mean = round(mean,2)

""" 
The Standard Deviation is a measure of how spread out our data is.
To calculate it, we first need to calculate a value called 
Variance: which is the average of the squared differences from the mean.
So, for our  data: the mean is 33.1. To calculate the variance, we take the 
difference between each value and the mean, square it, and then average the 
result: Variance = 292.5
"""
# calculate variance
total_sd=0
for i in data:
    total_sd += (i-mean)**2

variance=round(total_sd/len(data),2)
print(variance)

""" 
Now we take the square root of the Variance, to get the Standard Deviation: std = 17.1
"""
import math as ma
std=round(ma.sqrt(variance),2)
print(std)

vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]
#your code goes here
mean=sum(x for x in vac_nums)/len(vac_nums)
total_sd=0
for i in vac_nums:
    total_sd +=(i-mean)**2

variance=round(total_sd/len(vac_nums),4)
print(variance)

import numpy as np
a = np.array([[1, 2, 3, 4, 5]])

mean = np.sum(a)/a.size
print(mean)
v = np.sum((a-mean)**2)/a.size
print(v)