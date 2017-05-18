# -*- coding: utf-8 -*-
"""
Created on Sat May 13 13:05:48 2017

@author: Chenanyun
"""

from sklearn import naive_bayes
import numpy as np


X = np.random.randint(5, size=(6, 100))
y = np.array([1,2,3,4,5,6])

clf = naive_bayes.MultinomialNB()

clf.fit(X,y)

print (clf.predict(X[2:3]))
    
