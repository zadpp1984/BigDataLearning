# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:09:03 2017

@author: Chenanyun
"""
import pandas as pd
import numpy as np
import DataPrepare as DP

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\temp\\'

path_train = path+'train_6.csv'
#path_train = path+'train_total.csv'
#path_test = path+'test_1.csv'


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
dataset1 = DP.prepareData(dataset1)

dataset1.fillna(0,inplace=True)

dataset1[DP.select_features1].to_csv('preprocessed_test.csv',index=False)
dataset1[['orderid','roomid','orderlabel']].to_csv('preprocessed_test_compare.csv',index=False)
