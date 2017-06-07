# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:25:02 2017

@author: Chenanyun

对数据做预处理
"""
"""
        数据准备
"""

from sklearn.datasets import load_iris

iris = load_iris()

train_data = iris.data 
target_data = iris.target

"""
from numpy import hstack, vstack, array, median, nan
from numpy.random import choice
#特征矩阵加工
#使用vstack增加一行含缺失值的样本(nan, nan, nan, nan)
#使用hstack增加一列表示花的颜色（0-白、1-黄、2-红），花的颜色是随机的，意味着颜色并不影响花的分类
train_data = hstack((choice([0, 1, 2], size=train_data.shape[0]+1).reshape(-1,1), vstack((train_data, array([nan, nan, nan, nan]).reshape(1,-1)))))
#目标值向量加工
#增加一个目标值，对应含缺失值的样本，值为众数
target_data = hstack((target_data, array([median(target_data)])))
"""



"""
        缺失值计算
"""
#缺失值计算，返回值为计算缺失值后的数据
#参数missing_value为缺失值的表示形式，默认为NaN
#参数strategy为缺失值填充方式，默认为mean（均值）
from sklearn.preprocessing import Imputer
Imputer().fit_transform(train_data)


"""
        无量纲化
"""
#1.标准化
#根据【均值】和【标准差】调整
from sklearn.preprocessing import StandardScaler
StandardScaler().fit_transform(train_data)


#2.区间缩放
#利用最大最小值缩放
#区间缩放，返回值为缩放到[0, 1]区间的数据
from sklearn.preprocessing import MinMaxScaler
MinMaxScaler().fit_transform(train_data)

#3.正则化
#正则化和标准化的区别是正则化是根据【特征均值】和【特征值标准差】调整
from sklearn.preprocessing import Normalizer
Normalizer().fit_transform(train_data)


"""
        对定量特征二值化
"""
#主要是阈值设定 threshold=n
#阈值设置为3，返回值为二值化后的数据
from sklearn.preprocessing import Binarizer
Binarizer(threshold=3).fit_transform(train_data)

"""
        对定性特征哑编码
        TODO iris数据都是定量的，没必要做
"""
#哑编码，对IRIS数据集的目标值，返回值为哑编码后的数据
from sklearn.preprocessing import OneHotEncoder
OneHotEncoder().fit_transform(target_data.reshape((1,-1)))



"""
        数据变换
"""
#1.多项式转换
#参数degree为度，默认值为2
from sklearn.preprocessing import PolynomialFeatures
PolynomialFeatures().fit_transform(train_data)

#2.自定义转换函数
#第一个参数是单变元函数
#本例为对数函数的数据变换
from numpy import log1p
from sklearn.preprocessing import FunctionTransformer
FunctionTransformer(log1p).fit_transform(train_data)

