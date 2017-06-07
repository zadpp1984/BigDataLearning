# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:57:53 2017

@author: Chenanyun
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

path = 'F:\\MyPython\\resource\\ctrip\\'
#path = 'E:\\cay\\resource\\'
path_train = path+'room_train.csv'


usecols=['star' ,'rank' ,
         'returnvalue' ,'price_deduct' ,
         'basic_minarea' ,
         'roomservice_1' ,'roomservice_2' ,
         'roomservice_3' ,'roomservice_4' ,
         'roomservice_5' ,'roomservice_6' ,
         'roomservice_7' ,'roomservice_8' ,
         'roomtag_1' ,'roomtag_3' ,
         'roomtag_4' ,'roomtag_5' ,
         'basic_week_ordernum_ratio' ,
         'basic_recent3_ordernum_ratio' ,'basic_comment_ratio'
         ]
train_cols = ['star' ,'rank' ,'returnvalue' ,'price_deduct' ,'roomservice_1' ,'roomservice_2' ,'roomservice_3' ,'roomservice_4' ,'roomservice_5' ,'roomservice_6' ,'roomservice_7' ,'roomservice_8' ,'roomtag_1' ,'roomtag_3' ,'roomtag_4' ,'roomtag_5' ,'basic_week_ordernum_ratio' ,'basic_recent3_ordernum_ratio' ,'basic_comment_ratio']
test_cols = ['basic_minarea']
x_train = pd.read_table(path_train,sep=',',chunksize=100000,usecols=usecols,low_memory=False)
data_train = pd.DataFrame()
data_test = pd.DataFrame()
total_train,j = 0,1

for data_i in x_train:
    data_train = pd.concat((data_i[train_cols],data_train),axis=0,ignore_index=True)
    data_test = pd.concat((data_i[test_cols],data_test),axis=0,ignore_index=True)
    total_train += data_i.shape[0]
    print(j,end=',')
    j+=1
    if total_train >= 1000000:
        break    

print(data_train.shape)
print(data_test.shape)


from sklearn import neighbors
from sklearn import tree
from sklearn import svm
from sklearn import ensemble


def try_different_method(diff_reg):
    diff_reg.fit(X_train,y_train)
    score = diff_reg.score(X_test, y_test.ravel())
#    score = diff_reg.score(X_test, y_test)
    result = diff_reg.predict(X_test)
    
    print("mean:",np.fabs(result - y_test.ravel()).mean())
    # 用scikit-learn计算MSE
    print ("MSE:",metrics.mean_squared_error(y_test, result))
    # 用scikit-learn计算RMSE
    print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, result)))
    plt.figure(figsize=(12, 5))
#    plt.plot(np.arange(len(result)), y_test.ravel(),'-',label='true value')
#    plt.plot(np.arange(len(result)),result.ravel(),'ro-',label='predict value')

    plt.scatter(np.arange(len(result)), y_test.ravel())
    plt.scatter(np.arange(len(result)),result.ravel())

#    plt.scatter(np.arange(len(result)), y_test)
#    plt.scatter(np.arange(len(result)),result)
    plt.title('score: %f'%score)
    plt.legend()
    plt.show()

#data_scale = preprocessing.scale(data_train)
#X_train, X_test, y_train, y_test = train_test_split(data_scale, data_test, test_size=0.25,random_state=1)

X_train, X_test, y_train, y_test = train_test_split(data_train.values, data_test.values, test_size=0.25,random_state=1)

print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)


tree_reg = tree.DecisionTreeRegressor()
rf =ensemble.RandomForestRegressor(n_estimators=15)
ada = ensemble.AdaBoostRegressor(n_estimators=50)
gbrt = ensemble.GradientBoostingRegressor(n_estimators=100)
knn_reg = neighbors.KNeighborsRegressor(n_neighbors=30, weights='distance')

#svm太慢了
#svr = svm.SVR()

try_different_method(rf)








