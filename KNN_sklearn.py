# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:38:19 2017

@author: Chenanyun
"""
#导入KNN包
from sklearn.neighbors import KNeighborsClassifier

#训练样本特征集
X=[[0.5,0.5],[0.2,0.3],[0.9,0.1],[1.2,0.8],[1.5,0.6],[1.8,0.3]]

#对应训练样本的类别值
y=[1,1,1,2,2,2]

#创建KNN分类对象
neigh=KNeighborsClassifier(n_neighbors=3)

#调用fit方法，训练模型
neigh.fit(X,y)

#找到属性最近的3个邻居，得到的是邻居的下标值
print (neigh.kneighbors([[0.9,0.7],[1.6,0.1]],3,False))

#预测待分类样本的类别值
print (neigh.predict([[0.9,0.7],[1.6,0.1]]))

#待分类样本在各个类别的中概率
print (neigh.predict_proba([[0.9,0.7],[1.6,0.1]]))

#用测试数据，计算模型分类准确率
print (neigh.score([[0.9,0.7],[1.6,0.1]],[1,2]))

