# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:37:28 2017

@author: Chenanyun
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np

iris = load_iris()

train = iris.data
y = iris.target

print(len(train))

clf = RandomForestClassifier(n_estimators=1500)
clf.fit(train,y)

print(clf.feature_importances_)

print(clf.predict([[4.4,2.9,1.4,0.2],[5.9,3.,5.1,1.8]]))