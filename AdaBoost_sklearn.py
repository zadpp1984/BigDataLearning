# -*- coding: utf-8 -*-
"""
Created on Mon May 15 23:31:57 2017

@author: Chenanyun
"""

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

abc = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),algorithm="SAMME",n_estimators=200)

abc.fit(X,y)

print(abc.feature_importances_)

print(abc.predict([[4.4,2.9,1.4,0.2],[5.9,3.0,5.1,1.8]]))
