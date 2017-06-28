# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:00:34 2017

@author: Chenanyun
"""


import pandas as pd
import DataPrepare2 as DP2
import xgboost as xgb

#path = 'F:\\MyPython\\resource\\ctrip\\sorted\\'
path = 'E:\\cay\\resource\\temp\\'

#from sklearn.externals.joblib import load
#gbc = load('gbc_total.dmp')
bst1 = xgb.Booster() 
bst1.load_model("xgboost10_1.model")

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

i=7
path_train = path+'test_'+str(i)+'_sorted.csv'

dataset1 = DP2.prepareData(read_data(path_train))


compare_train = dataset1.ix[:,['orderid','roomid']]
dataset1 = dataset1[DP2.select_features]


xg_test = xgb.DMatrix(dataset1)
predict1 = bst1.predict(xg_test)
mix1 = pd.concat([compare_train,pd.DataFrame(predict1)],axis=1)

result_pd1 = pd.DataFrame()
result_pd1 = pd.concat([result_pd1,mix1.loc[mix1.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax()),['orderid','roomid']]])   
result_pd1.columns = ['orderid','predict_roomid']
result_pd1.to_csv(path+'submission_sample'+str(i)+'.csv',index=False)
