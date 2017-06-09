# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:04:12 2017

@author: Chenanyun
"""

import pandas as pd
import numpy as np

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\'

path_train = path+'competition_train.txt'
path_test = path+'competition_test.txt'

date_train = ['2013-04-14',
              '2013-04-15',
              '2013-04-16',
              '2013-04-17',
              '2013-04-18',
              '2013-04-19',
              '2013-04-20']

date_test = ['2013-04-21',
              '2013-04-22',
              '2013-04-23',
              '2013-04-24',
              '2013-04-25',
              '2013-04-26',
              '2013-04-27']

with open(path_train, 'r') as f:
    columns_train = f.readline().strip('\n').split('\t') 
with open(path_test, 'r') as f:
    columns_test = f.readline().strip('\n').split('\t') 
    
for i in np.linspace(1,7,num=7,endpoint=True,dtype='int'):
        
    file_handler1 = pd.read_table(path_train,
                                 sep='\t',
                                 chunksize=100000,
                                 usecols=columns_train,
                                 low_memory=False)
    
    file_handler2 = pd.read_table(path_test,
                                 sep='\t',
                                 chunksize=100000,
                                 usecols=columns_test,
                                 low_memory=False)
    
    dataset1 = pd.DataFrame()
    total_train,j = 0,1
    for data_i in file_handler1:
        dataset1 = pd.concat((dataset1,data_i[data_i['orderdate']==date_train[i]]),axis=0,ignore_index=True)
        total_train += dataset1.shape[0]
        print(j,end=',')
        j+=1

    dataset1.to_csv(path+'train_'+str(i)+'.csv',index=False)
    del data_i
    del dataset1
    
    dataset2 = pd.DataFrame()
    total_train,j = 0,1
    for data_i in file_handler2:
        dataset2 = pd.concat((dataset2,data_i[data_i['orderdate']==date_test[i]]),axis=0,ignore_index=True)
        total_train += dataset2.shape[0]
        print(j,end=',')
        j+=1
    dataset2.to_csv(path+'test_'+str(i)+'.csv',index=False)
    del data_i
    del dataset2


