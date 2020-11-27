import numpy as np

# Values
L = 100
x0 = 47
# Functions
c = 5
cv = 10
m = (c/cv)**2


def initializer(x):
    if(x<x0):
        return x/x0
    else:
        return (L-x)/(L-x0)

init = np.vectorize(initializer)

def step(before,now):
    result = np.zeros(now.shape)
    for i in range(1,len(now)-1):
        result[i] = 2*now[i] - before[i] + m*(now[i+1] + now[i-1]-2*now[i] )
    return result
