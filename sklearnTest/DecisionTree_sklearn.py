# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:31:05 2017

@author: Chenanyun
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

#print(iris.data)
#print(iris.target)

dt = DecisionTreeClassifier()

dt.fit(iris.data,iris.target)

print (dt.predict([5.8, 2.7, 5.1, 1.9]))

from sklearn.cross_validation import cross_val_score

print (cross_val_score(dt,iris.data,iris.target,cv=5))