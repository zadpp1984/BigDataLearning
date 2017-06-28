# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:06:36 2017

@author: Chenanyun
"""

import pandas as pd
import DataPrepare2 as DP2

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
#        if len(dataset) >= 10000:
#            break

    del data_i
    return dataset



path = 'E:\\cay\\resource\\temp\\'
#path = 'F:\\MyPython\\resource\\ctrip\\sorted\\'

dataset1 = DP2.prepareData(read_data(path+'train_total6_1.csv'))
    
dataset1.to_csv(path+'test\\test2.csv',sep='\t',index=False)

#dataset1.sort_values(['hotelid','basicroomid','roomid'],inplace=True)

dataset1.describe(percentiles=[.01,.05,.25,.75,.95,.99],include='all').to_csv(path+'test\\describe.csv')

