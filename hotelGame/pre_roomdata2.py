# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:58:38 2017

@author: Chenanyun
"""

import pandas as pd
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\'
path_train = path+'room_train_nan_train.csv'


alldata = ClassificationDataSet(19, 1, nb_classes=3)

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
    for x in range(len(data_test)):
        alldata.addSample(data_train[x], data_test[x])
    
    total_train += data_i.shape[0]
    print(j,end=',')
    j+=1
    if total_train >= 1000000:
        break 

del data_train
del data_test
del data_i

    
tstdata_temp, trndata_temp = alldata.splitWithProportion(0.25)  
  
tstdata = ClassificationDataSet(19, 1, nb_classes=3)  
for n in range(0, tstdata_temp.getLength()):  
    tstdata.addSample( tstdata_temp.getSample(n)[0], tstdata_temp.getSample(n)[1] )  
  
trndata = ClassificationDataSet(19, 1, nb_classes=3)  
for n in range(0, trndata_temp.getLength()):  
    trndata.addSample( trndata_temp.getSample(n)[0], trndata_temp.getSample(n)[1] )  





type(data_train)
alldata.addSample(data_train, data_i[['basic_minarea']].values)
del data_i

data_hotel.dtypes
data_hotel.describe()

