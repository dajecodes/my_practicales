import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

#price for 2018-2021
bitcoin = [3869.47, 7188.46, 22203.31, 29391.78]
years=[int(2018),2019,2020,2021]

""" 
You decide to start a Bitcoin mining business in January of 2017. You make an initial investment
 of $500K to buy the required mining hardware.
Each year the hardware can mine 10 bitcoins, so your first return will come on January 1, 2018.
"""
cf=[-500*1000]
# for x in bitcoin:
#     cf.append(x*10)
cf.extend(list(map(lambda x:x*10,bitcoin)))

# print(npf.irr(cf))
def no_of_bitcoins(price,investment):
    return investment/price

def current_value(price,no_of_coins):
    return price*no_of_coins

coins=no_of_bitcoins(bitcoin[0],1000)

val=list(map(lambda x:current_value(x,coins),bitcoin))

plt.plot(years,val)
plt.savefig("plot.png")