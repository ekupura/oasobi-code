#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def pulse (input_data):
    output_data = np.array([]) #空の行列
    for i in x:
        if (i >= 1.0 and i <= 2):
            output_data = np.append(output_data,1)
        else:
            output_data = np.append(output_data,0)
    return output_data

x = np.arange(-3,3,0.001)
y = pulse(x)
plt.plot(x,y)
plt.xlim([0,3])
plt.ylim([-1,2])
plt.show()
