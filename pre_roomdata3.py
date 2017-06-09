# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:58:39 2017

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\'
path_train = path+'room_train_nan_train.csv'


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
    data_hotel = pd.concat((data_hotel,data_i),axis=0,ignore_index=True)
    total_train += data_i.shape[0]
    print(j,end=',')
    j+=1
    if total_train >= 1000000:
        break 

for x in range(len(usecols)):
    plt.figure(x,figsize=(15,6))
    plt.hist(data_hotel.ix[:,x].values, bins=20, alpha=0.5)
    plt.xlabel(usecols[x])
    plt.ylabel('num')

data_hotel[data_hotel.price_deduct>10000]

plt.figure(22,figsize=(20,6))
plt.plot(data_hotel.index.values,data_hotel['star'].values)
plt.scatter(data_hotel['basic_minarea'].values,data_hotel['price_deduct'].values)

plt.hist(data_hotel['basic_minarea'].values)


sns.distplot(data_hotel['basic_minarea'].values)
sns.plt.show()

data_hotel[data_hotel['basic_minarea']>2000]
data_hotel[data_hotel['basic_minarea']>2000].describe()