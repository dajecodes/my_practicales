""" 
The given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one
 standard deviation from the mean.
"""
import numpy as np
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
players.sort()
data=np.array(players)

mean=np.sum(data)/data.size

variance=np.sum((data-mean)**2)/data.size
std=np.sqrt(variance)
print(data)
print(mean)
print(std)
count=0
bot=mean-std
top =mean+std
for i in data:
    if bot<i<top :
        count +=1

print(count)