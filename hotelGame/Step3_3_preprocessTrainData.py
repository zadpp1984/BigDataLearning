# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:11:16 2017

@author: user
"""

import pandas as pd
import numpy as np
import DataPrepare as DP

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\'

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

def read_data(file):
    
    with open(file, 'r') as f:
        columns = f.readline().strip('\n').split('\t') 
    
    dataset = pd.DataFrame()
    file_handler = pd.read_table(file,
                                 sep='\t',
                                 chunksize=100000,
                                 usecols=columns,
                                 low_memory=False)
    
    i = 1
    for data_i in file_handler:
        dataset = pd.concat((dataset,data_i),axis=0,ignore_index=True)
        print i
        i+=1

    del data_i
    return dataset

dataset1 = read_data(path_train)
#dataset1.dropna(axis=1,how='all',inplace=True)
#dataset1.dropna(axis=0,how='any',inplace=True)
#dataset2 = read_data(path_test)
#dataset1.describe(percentiles=[.05,.25,.75,.95,.99],include='all').to_csv(path+'describe.csv')
#dataset1.describe(percentiles=[.05,.25,.75,.95,.99],include='all')
#dataset1.info(verbose=True,null_counts=True)


"""""""""""""""""""""""""""""""""""""""""""""""""""
      predict
"""""""""""""""""""""""""""""""""""""""""""""""""""
date_train_t1 = ['2013-04-14',
                 '2013-04-15',
                 '2013-04-16',
                 '2013-04-17',
                 '2013-04-18']
date_train_t1 = ['2013-04-19',
                 '2013-04-20']


dataset1 = DP.prepareData(dataset1)
dataset1.fillna(0,inplace=True)

dataset1 = dataset1.ix[dataset1['orderlabel'].isin(date_train_t1),DP.select_features1]


