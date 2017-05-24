# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:58:38 2017

@author: Chenanyun
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

from sklearn.cross_validation import train_test_split

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

x_train = pd.read_table(path_train,sep=',',chunksize=100000,usecols=usecols,low_memory=False)
data_hotel = pd.DataFrame()
total_train,j = 0,1

for data_i in x_train:
    data_train = data_i[['star' ,'rank' ,'returnvalue' ,'price_deduct' ,'roomservice_1' ,'roomservice_2' ,'roomservice_3' ,'roomservice_4' ,'roomservice_5' ,'roomservice_6' ,'roomservice_7' ,'roomservice_8' ,'roomtag_1' ,'roomtag_3' ,'roomtag_4' ,'roomtag_5' ,'basic_week_ordernum_ratio' ,'basic_recent3_ordernum_ratio' ,'basic_comment_ratio']].values
    data_test = data_i[['basic_minarea']].values
    
    total_train += data_i.shape[0]
    print(j,end=',')
    j+=1
    if total_train >= 100000:
        break 



X_train, X_test, y_train, y_test = train_test_split(data_train, data_test, random_state=1)

print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)


from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)

linreg.coef_.shape
print (linreg.intercept_)
print (linreg.coef_)


#模型拟合测试集
y_pred = linreg.predict(X_test)
from sklearn import metrics
# 用scikit-learn计算MSE
print ("MSE:",metrics.mean_squared_error(y_test, y_pred))
# 用scikit-learn计算RMSE
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))




from sklearn.model_selection import cross_val_predict
predicted = cross_val_predict(linreg, data_train, data_test, cv=10)
# 用scikit-learn计算MSE
print ("MSE:",metrics.mean_squared_error(data_test, predicted))
# 用scikit-learn计算RMSE
print ("RMSE:",np.sqrt(metrics.mean_squared_error(data_test, predicted)))

fig, ax = plt.subplots()
ax.scatter(data_test, predicted)
ax.plot([data_test.min(), data_test.max()], [data_test.min(), data_test.max()], 'k--', lw=4)
ax.set_xlabel('data_test')
ax.set_ylabel('predicted')
plt.show()