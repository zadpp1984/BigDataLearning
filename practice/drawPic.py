# -*- coding: utf-8 -*-
"""
Created on Sun May 28 23:15:13 2017

@author: Chenanyun
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = np.linspace(1,9,9).reshape(3,3)

index = ['A','B','C']

data_pd = pd.DataFrame(data,columns=index)

data_pd = pd.concat((data_pd,data_pd),axis=0,ignore_index=True)

print(data_pd)
sns.barplot(x='A',y='B',hue='C',data=data_pd)


data_pd[data_pd['A']==7]=1


data_pd