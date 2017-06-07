# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:04:12 2017

@author: Chenanyun
"""

import pandas as pd

path = 'F:\\MyPython\\resource\\ctrip\\'
#path = 'E:\\cay\\resource\\'

path_train = path+'competition_train.txt'
#path_train = path+'competition_test.txt'

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
    columns = f.readline().strip('\n').split('\t') 

file_handler = pd.read_table(path_train,
                             sep='\t',
                             chunksize=100000,
                             usecols=columns,
                             low_memory=False)

dataset = pd.DataFrame()
total_train,j = 0,1
for data_i in file_handler:
    dataset = pd.concat((dataset,data_i[data_i['orderdate']==date_train[0]]),axis=0,ignore_index=True)
    total_train += dataset.shape[0]
    print(j,end=',')
    j+=1
#    if total_train >= 100000:
#        break 
del data_i

dataset.to_csv(path+'train_01.csv',index=False)
#dataset.to_csv(path+'test_01.csv',index=False)


