# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:05:58 2017

@author: user
"""

import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
#%matplotlib qt5


dataset=np.linspace(0,100)

plt.scatter(dataset,dataset)

plt.scatter(dataset,np.power(dataset,0.1))
plt.scatter(dataset,np.power(dataset,0.5))

plt.scatter(dataset,np.power(dataset,2))
plt.scatter(dataset,np.power(dataset,3))

#plt.scatter(dataset,np.sin(dataset))
#plt.scatter(dataset,np.cos(dataset))

plt.scatter(dataset,np.log(dataset))
plt.scatter(dataset,np.log2(dataset))
plt.scatter(dataset,np.log10(dataset))
plt.scatter(dataset,np.log1p(dataset))
