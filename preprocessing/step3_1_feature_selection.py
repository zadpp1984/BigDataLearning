# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:26:33 2017

@author: Chenanyun

数据中特征选择的方法与降维
"""
"""
        数据准备
"""
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
iris_pd = pd.DataFrame(iris.data)
iris_pd.describe()
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                        特征选择
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
        过滤法(Filter)
"""
#1.方差选择法
#阈值由参数threshold决定
from sklearn.feature_selection import VarianceThreshold
VarianceThreshold(threshold=3).fit_transform(iris.data)


#2.相关系数
#先计算各个特征对目标值的相关系数以及相关系数的P值
from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr
#python2好像好使  SelectKBest(lambda X, Y: np.array(map(lambda x:pearsonr(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)
SelectKBest(lambda X, Y: tuple(map(tuple,np.array(list(map(lambda x:pearsonr(x, Y), X.T))).T)), k=2).fit_transform(iris.data, iris.target)



#3.卡方检验
#经典的卡方检验是检验[定性]自变量对[定性]因变量的相关性
#[定性变量]个体只能归属于几种互不相容类别中的一种时，一般是用非数字来表达其类别，这样的观测数据称为定性变量。
#统计量的含义就是自变量对因变量的相关性
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#选择K个最好的特征，返回选择特征后的数据
SelectKBest(chi2, k=2).fit_transform(iris.data, iris.target)
chi2(iris.data,iris.target)



#4.互信息法
#经典的互信息也是评定自变量对定性因变量的相关性
#from sklearn.feature_selection import SelectKBest
#from minepy import MINE
##由于MINE的设计不是函数式的，定义mic方法将其为函数式的，返回一个二元组，二元组的第2项设置成固定的P值0.5
#def mic(x, y):
#    m = MINE()
#    m.compute_score(x, y)
#    return (m.mic(), 0.5)
##选择K个最好的特征，返回特征选择后的数据
#SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=2).fit_transform(iris.data, iris.target)

"""
        包装法(Wrapper)
"""
#递归特征消除发
#递归消除特征法使用一个基模型来进行多轮训练，每轮训练后，消除若干权值系数的特征，再基于新的特征集进行下一轮训练
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
#参数estimator为基模型
#参数n_features_to_select为选择的特征个数
RFE(estimator=LogisticRegression(), n_features_to_select=2).fit_transform(iris.data, iris.target)

"""
        嵌入法(Embedded)
"""
#1.基于惩罚项的特征选择法
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
#带L1惩罚项的逻辑回归作为基模型的特征选择
SelectFromModel(LogisticRegression(penalty="l1", C=0.1)).fit_transform(iris.data, iris.target)

#L1惩罚项降维的原理在于保留多个对目标值具有同等相关性的特征中的一个，所以没选到的特征不代表不重要.故，可结合L2惩罚项来优化。
#具体操作以后再说

#2.基于树模型的特征选择法
#树模型中GBDT也可用来作为基模型进行特征选择
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier
#GBDT作为基模型的特征选择
SelectFromModel(GradientBoostingClassifier()).fit_transform(iris.data, iris.target)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                        降维
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#1.主成分分析法（PCA）
from sklearn.decomposition import PCA
#主成分分析法，返回降维后的数据
#参数n_components为主成分数目
iris_pca = PCA(n_components=2).fit_transform(iris.data)
plt.scatter(iris_pca[:,0],iris_pca[:,1])



#2.线性判别分析法（LDA）
from sklearn.lda import LDA
#线性判别分析法，返回降维后的数据
#参数n_components为降维后的维数
iris_lda = LDA(n_components=2).fit_transform(iris.data, iris.target)
plt.scatter(iris_lda[:,0],iris_lda[:,1])



