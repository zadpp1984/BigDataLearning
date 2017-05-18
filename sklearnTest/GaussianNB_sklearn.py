# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:13:49 2017

@author: Chenanyun
"""

from sklearn import naive_bayes
import numpy as np


X = np.array([-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2])
Y = np.array([1,1,1,2,2,2])

clf = naive_bayes.GaussianNB()

clf.fit(X,Y)

print (clf.predict([-0.8,-1]))

clf_pf=naive_bayes.GaussianNB()
clf_pf.partial_fit(X,Y,np.unique(Y))

print(clf_pf.predict([-0.8,-1]))