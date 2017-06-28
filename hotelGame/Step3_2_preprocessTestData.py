# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:09:03 2017

@author: Chenanyun
"""
import pandas as pd
import numpy as np
import DataPrepare2 as DP2

#path = 'F:\\MyPython\\resource\\ctrip\\sorted\\'
path = 'E:\\cay\\resource\\temp\\'

path_train = path+'train_6_sorted.csv'


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
dataset1 = DP2.prepareData(dataset1)

#dataset1.fillna(0,inplace=True)

#my_list=[
#        'basic_week_ordernum_ratio'
#        ,'basic_recent3_ordernum_ratio'
#        ,'basic_comment_ratio'
#        ,'basic_30days_ordnumratio'
#        ,'basic_30days_realratio'
##        ,'room_30days_ordnumratio'
##        ,'room_30days_realratio'
#]
#path_room = path+'room.csv'
#df = read_data(path_room)
#dataset1.drop(my_list,axis=1,inplace=True)
#dataset1 = pd.merge(dataset1,df,on=['orderid','hotelid','basicroomid'],how='left',suffixes=['','_y'])


dataset1[DP2.select_features].to_csv(path+'preprocessed_test.csv',sep='\t',index=False)
dataset1[['orderid','roomid','orderlabel']].to_csv(path+'preprocessed_test_compare.csv',sep='\t',index=False)
