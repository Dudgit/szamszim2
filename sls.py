#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functions import *



x = np.linspace(0,L,100)
y = init(x)
y_container= [y,step(y,y)]

for i in range(1,1000):
    y_container.append(step(y_container[i-1],y_container[i]))


# %%

# %%
