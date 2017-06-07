# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:09:03 2017

@author: Chenanyun
"""
import pandas as pd
import numpy as np

path = 'F:\\MyPython\\resource\\ctrip\\'
#path = 'E:\\cay\\resource\\'

path_train = path+'train_01.csv'
path_test = path+'test_01.csv'

def read_data(file):
    
    with open(file, 'r') as f:
        columns = f.readline().strip('\n').split(',') 
    
    dataset = pd.DataFrame()
    file_handler = pd.read_table(path_train,
                                 sep=',',
                                 chunksize=100000,
                                 usecols=columns,
                                 low_memory=False)
    
    i = 1
    for data_i in file_handler:
        dataset = pd.concat((dataset,data_i),axis=0,ignore_index=True)
        print(i,end=',')
        i+=1

    del data_i
    return dataset

dataset1 = read_data(path_train)
#dataset2 = read_data(path_test)

#dataset1.describe(percentiles=[.05,.25,.75,.95,.99])
#dataset1.info(verbose=True,null_counts=True)

"""""""""""""""""""""""""""""""""""""""""""""""""""
      process data
"""""""""""""""""""""""""""""""""""""""""""""""""""
#fillna(0)
zero_dict = {
        'roomservice_1':0
        ,'roomservice_4':0
        ,'basic_week_ordernum_ratio':0
        ,'basic_recent3_ordernum_ratio':0
        ,'basic_comment_ratio':0
        ,'user_roomservice_4_0ratio':0
        ,'user_roomservice_4_1ratio':0
        ,'user_roomservice_4_5ratio':0
        ,'user_roomservice_6_2ratio':0
        ,'user_roomservice_6_1ratio':0
        ,'user_roomservice_6_0ratio':0
        ,'user_roomservice_2_1ratio':0
        ,'user_roomservice_5_345ratio':0
        }
dataset1.fillna(zero_dict,inplace=True)
#fillna(mean)
mean_dict={
        'roomtag_3':dataset1['roomtag_3'].mean()
        ,'user_confirmtime':dataset1['user_confirmtime'].mean()
        ,'user_avgdealprice':dataset1['user_avgdealprice'].mean()
        ,'user_avgpromotion':dataset1['user_avgpromotion'].mean()
        ,'user_avgprice_star':dataset1['user_avgprice_star'].mean()
        ,'user_activation':dataset1['user_activation'].mean()
        ,'user_stdprice':dataset1['user_stdprice'].mean()
        ,'user_cvprice':dataset1['user_cvprice'].mean()
        }

dataset1.fillna(mean_dict,inplace=True)

mean_temp_dict={
         'roomservice_2_lastord':dataset1['roomservice_2_lastord'].mean()
        ,'roomservice_3_lastord':dataset1['roomservice_3_lastord'].mean()
        ,'roomservice_4_lastord':dataset1['roomservice_4_lastord'].mean()
        ,'roomservice_5_lastord':dataset1['roomservice_5_lastord'].mean()
        ,'roomservice_6_lastord':dataset1['roomservice_6_lastord'].mean()
        ,'roomservice_8_lastord':dataset1['roomservice_8_lastord'].mean()
        ,'roomtag_3_lastord':dataset1['roomtag_3_lastord'].mean()
        ,'roomtag_4_lastord':dataset1['roomtag_4_lastord'].mean()
        ,'roomtag_5_lastord':dataset1['roomtag_5_lastord'].mean()
        ,'roomtag_6_lastord':dataset1['roomtag_6_lastord'].mean()
        ,'hotel_minprice_lastord':dataset1['hotel_minprice_lastord'].mean()
        ,'basic_minprice_lastord':dataset1['basic_minprice_lastord'].mean()
        ,'rank_lastord':dataset1['rank_lastord'].mean()
        ,'return_lastord':dataset1['return_lastord'].mean()
        ,'price_last_lastord':dataset1['price_last_lastord'].mean()
        ,'star_lastord':dataset1['star_lastord'].mean()
#        TODO
        ,'user_rank_ratio':dataset1['user_rank_ratio'].mean()
        ,'basic_minarea':dataset1['basic_minarea'].mean()
        ,'basic_maxarea':dataset1['basic_maxarea'].mean()
#        TODO
        }

dataset1.fillna(mean_temp_dict,inplace=True)

#(0,1)处理
zeroone_arr=[
        'roomtag_2'
        ,'roomtag_2_lastord'
        ]

dataset1.ix[dataset1.roomtag_2.isnull(),'roomtag_2'] = 0
dataset1.ix[dataset1.roomtag_2.notnull(),'roomtag_2'] = 1
dataset1.ix[dataset1.roomtag_2_lastord.isnull(),'roomtag_2_lastord'] = 0
dataset1.ix[dataset1.roomtag_2_lastord.notnull(),'roomtag_2_lastord'] = 1



"""
        对定性特征哑编码
"""
#哑编码，对IRIS数据集的目标值，返回值为哑编码后的数据
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(categorical_features=np.array([14]),
                    n_values=[3])
enc.fit(dataset1)
enc.transform(dataset1.values)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#trainX = dataset1[:100000]
#testX = dataset1[100001:200000]
#
#
#compareX = trainX[['orderid','basicroomid']]
#resultX = trainX.ix[trainX['orderlabel']==1,['orderid','basicroomid']]
#
#trainX.fillna(0,inplace=True)
#trainY = trainX[['orderlabel']]
#testX.fillna(0,inplace=True)
#testY = testX[['orderlabel']]
#drop_cols = [
#             'orderlabel',
#             'orderid',
#             'uid',
#             'orderdate',
#             'hotelid',
#             'basicroomid',
#             'roomid',
#             'orderid_lastord',
#             'orderdate_lastord',
#             'hotelid_lastord',
#             'roomid_lastord',
#             'basicroomid_lastord',
#             ]
#trainX.drop(drop_cols,axis=1,inplace=True)
#testX.drop(drop_cols,axis=1,inplace=True)
#
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#sc.fit(trainX)
#trainX_std = sc.transform(trainX)
#testX_std = sc.transform(testX)
#
#from sklearn.linear_model import LogisticRegression
#lr = LogisticRegression(C=1, random_state=0,class_weight='balanced')
#lr.fit(trainX_std,trainY.values.ravel())
#result = lr.predict_proba(trainX_std)
#
#
#result_pd = pd.DataFrame(result[:,1])
#combine_train = pd.concat([compareX,result_pd],axis=1)
#maxr = combine_train.groupby('orderid',as_index=False).max()
#
#maxr = pd.merge(maxr,resultX,on=['orderid'])
#len(maxr[maxr['basicroomid_x']==maxr['basicroomid_y']])/len(maxr)


