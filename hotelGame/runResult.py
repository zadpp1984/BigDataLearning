# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 18:32:51 2017

@author: Chenanyun
"""

import pandas as pd
import DataPrepare as DP
import xgboost as xgb

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\temp\\'

#from sklearn.externals.joblib import load
#gbc = load('gbc_total.dmp')
bst1 = xgb.Booster() 
bst2 = xgb.Booster() 
bst3 = xgb.Booster() 
bst4 = xgb.Booster() 
bst1.load_model("xgboost10_1.model")
bst2.load_model("xgboost10_2.model")
bst3.load_model("xgboost10_3.model")
bst4.load_model("xgboost10_4.model")

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

weight=[1,1,1,1]

result_pd1 = pd.DataFrame()
result_pd2 = pd.DataFrame()
result_pd3 = pd.DataFrame()
result_pd4 = pd.DataFrame()
result_pd5 = pd.DataFrame()

for i in [1,2,3,4,5,6,7]:
    path_train = path+'test_'+str(i)+'.csv'
    dataset1 = read_data(path_train)
    dataset1 = DP.prepareData(dataset1)
    dataset1.fillna(0,inplace=True)
    compare_train = dataset1.ix[:,['orderid','roomid']]
    dataset1 = dataset1[DP.select_features1]
    xg_test = xgb.DMatrix(dataset1,featrue_names=DP.select_features1)

    predict1 = bst1.predict(xg_test)
    predict2 = bst2.predict(xg_test)
    predict3 = bst3.predict(xg_test)
    predict4 = bst4.predict(xg_test)
    predict5 = weight[0]*predict1 + weight[1]*predict2 + weight[2]*predict3 + weight[3]*predict4

    mix1 = pd.concat([compare_train,pd.DataFrame(predict1)],axis=1)
    mix2 = pd.concat([compare_train,pd.DataFrame(predict2)],axis=1)
    mix3 = pd.concat([compare_train,pd.DataFrame(predict3)],axis=1)
    mix4 = pd.concat([compare_train,pd.DataFrame(predict4)],axis=1)
    mix5 = pd.concat([compare_train,pd.DataFrame(predict5)],axis=1)
    
    result_pd1 = pd.concat([result_pd1,mix1.loc[mix1.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax()),['orderid','roomid']]])   
    result_pd2 = pd.concat([result_pd2,mix2.loc[mix2.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax()),['orderid','roomid']]])   
    result_pd3 = pd.concat([result_pd3,mix3.loc[mix3.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax()),['orderid','roomid']]])  
    result_pd4 = pd.concat([result_pd4,mix4.loc[mix4.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax()),['orderid','roomid']]])  
    result_pd5 = pd.concat([result_pd5,mix5.loc[mix5.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax()),['orderid','roomid']]])    

result_pd1.columns = ['orderid','predict_roomid']
result_pd1.to_csv(path+'submission_sample1.csv',index=False)
result_pd2.columns = ['orderid','predict_roomid']
result_pd2.to_csv(path+'submission_sample2.csv',index=False)
result_pd3.columns = ['orderid','predict_roomid']
result_pd3.to_csv(path+'submission_sample3.csv',index=False)
result_pd4.columns = ['orderid','predict_roomid']
result_pd4.to_csv(path+'submission_sample4.csv',index=False)
result_pd5.columns = ['orderid','predict_roomid']
result_pd5.to_csv(path+'submission_sample.csv',index=False)