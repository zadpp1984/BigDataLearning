# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 21:23:30 2017

@author: Chenanyun
"""
import pandas as pd
import numpy as np
import xgboost as xgb

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



Y1 = read_data('preprocessed_train_Y.csv').values.ravel()
dataset1 = read_data('preprocessed_train.csv').values
xg_train = xgb.DMatrix(dataset1, label=Y1.ravel())
num_round = 140
param = {'bst:max_depth':4, 'bst:eta':0.3, 'silent':1, 'objective':'binary:logistic' }
plst = param.items()
#plst += [('eval_metric', 'auc')] # Multiple evals can be handled in this way
#plst += [('eval_metric', 'ams@0')]
#evallist  = [(Y2.values.ravel(),'eval'), (dataset2.values,'train')]
#bst = xgb.train( plst, xg_train, num_round, evallist )

bst = xgb.train( plst, xg_train, num_round )
bst.save_model('xgboost.model')
