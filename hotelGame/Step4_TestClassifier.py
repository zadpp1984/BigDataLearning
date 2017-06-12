# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:44:52 2017

@author: Chenanyun
"""

import pandas as pd
import numpy as np
import xgboost as xgb

def printScore(compare,result,predict):
    combine = pd.concat([compare,pd.DataFrame(predict)],axis=1)
    maxr = combine.loc[combine.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax())]
    maxr = pd.merge(maxr,result,on=['orderid'])
    print len(maxr[maxr['roomid_x']==maxr['roomid_y']])/float(len(maxr))

def read_data(file):
    
    with open(file, 'r') as f:
        columns = f.readline().strip('\n').split(',') 
    
    dataset = pd.DataFrame()
    file_handler = pd.read_table(file,
                                 sep=',',
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

bst = xgb.Booster() #init model
bst.load_model("xgboost.model") # load data
dataset2 = read_data('preprocessed_test.csv').values
xg_test = xgb.DMatrix(dataset2)
predict_test = bst.predict(xg_test) 


compare_test = read_data('preprocessed_test_compare.csv')
result_test = compare_test.ix[compare_test['orderlabel']==1,['orderid','roomid']]
printScore(compare_test,result_test,predict_test)
