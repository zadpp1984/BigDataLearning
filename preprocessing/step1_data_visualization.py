# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:28:47 2017

@author: Chenanyun

数据可视化
"""
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
%matplotlib qt5

#iris_sns = sns.load_dataset("iris")
iris = load_iris()

iris_pd = pd.DataFrame(np.hstack((iris.data ,iris.target.reshape(-1,1))))

sns.set(style="ticks", color_codes=True)


#pairplot  配对图
sns.pairplot(iris_pd, hue=4)
sns.pairplot(iris_pd, diag_kind="kde", hue=4)
sns.pairplot(iris_pd, kind="reg", hue=4)
_ = sns.pairplot(iris_pd[:50], vars=[0, 1,4], hue=4, size=4)



#distplot  柱状图
sns.set(rc={"figure.figsize": (8, 4)})
sns.distplot(iris_pd.ix[:,1])



#from string import ascii_uppercase
#import numpy as np
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#
#sns.set(style="white")
#
## Generate a large random dataset
#rs = np.random.RandomState(33)
#d = pd.DataFrame(data=rs.normal(size=(100, 26)),
#                 columns=list(ascii_uppercase[:26]))
#
## Compute the correlation matrix
#corr = d.corr()
#
## Generate a mask for the upper triangle
#mask = np.zeros_like(corr, dtype=np.bool)
#mask[np.triu_indices_from(mask)] = True
#
## Set up the matplotlib figure
#f, ax = plt.subplots(figsize=(11, 9))
#
## Generate a custom diverging colormap
#cmap = sns.diverging_palette(220, 10, as_cmap=True)
#
## Draw the heatmap with the mask and correct aspect ratio
#sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3,
#            square=True, xticklabels=5, yticklabels=5,
#            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)