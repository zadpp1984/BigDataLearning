# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 18:32:51 2017

@author: Chenanyun
"""

import pandas as pd
import DataPrepare as DP
import xgboost as xgb

select_features = [
 'star'
,'rank'
,'returnvalue'
,'price_deduct'
,'basic_minarea'
#,'roomservice_1'
,'roomservice_2'
#,'roomservice_3'
#,'roomservice_4'
,'roomservice_5'
#,'roomservice_6'
,'roomservice_7'
#,'roomservice_8'
,'roomtag_1'
,'roomtag_2'
,'roomtag_3'
,'roomtag_4'
,'roomtag_5'
#,'roomtag_6'
,'user_confirmtime'
,'user_avgadvanceddate'
,'user_avgstar'
,'user_avggoldstar'
,'user_avgrecommendlevel'
,'user_avgroomnum'
,'user_avgdealpriceholiday'
,'user_avgdealpriceworkday'
,'user_avgdealprice'
,'user_avgpromotion'
,'user_avgprice_star'
,'user_ordernum'
,'user_activation'
,'user_avgprice'
,'user_maxprice'
,'user_minprice'
,'user_stdprice'
,'user_cvprice'
,'user_citynum'
,'user_avgroomarea'
,'user_roomservice_4_0ratio'
,'user_roomservice_4_2ratio'
,'user_roomservice_4_3ratio'
,'user_roomservice_4_4ratio'
,'user_roomservice_4_1ratio'
,'user_roomservice_4_5ratio'
,'user_roomservice_3_123ratio'
,'user_roomservice_6_2ratio'
,'user_roomservice_6_1ratio'
,'user_roomservice_6_0ratio'
,'user_roomservice_5_1ratio'
,'user_roomservice_7_0ratio'
,'user_roomservice_2_1ratio'
,'user_roomservice_8_1ratio'
,'user_rank_ratio'
,'user_roomservice_5_345ratio'
,'basic_week_ordernum_ratio'
,'basic_recent3_ordernum_ratio'
,'basic_comment_ratio'
,'rank_lastord'
,'return_lastord'
,'price_last_lastord'
,'roomservice_2_lastord'
#,'roomservice_3_lastord'
#,'roomservice_4_lastord'
,'roomservice_5_lastord'
#,'roomservice_6_lastord'
#,'roomservice_8_lastord'
,'roomtag_2_lastord'
,'roomtag_3_lastord'
,'roomtag_4_lastord'
,'roomtag_5_lastord'
,'roomtag_6_lastord'
,'star_lastord'
,'hotel_minprice_lastord'
,'basic_minprice_lastord'
#,'order_index'
,'same_as_last_hotel'
,'same_as_last_basic_room'
,'same_as_last_room'
,'same_service2'
,'same_service3'
,'same_service4'
,'same_service5'
,'same_service6'
,'same_service8'
,'same_tag2'
,'same_tag3'
,'same_tag4'
,'same_tag5'
,'same_tag6'
,'distance_last_tag3'
,'distance_avg_star'
,'distance_last_star'
,'distance_avg_return'
,'distance_last_return'
,'avg_roomarea'
#,'distance_avg_roomarea'
,'distance_avg_price'
,'distance_avg_holiday_price'
,'distance_avg_workday_price'
,'between_max_min'
,'distance_avg_rank'
,'distance_last_rank'
,'date_from_last'
,'is_holiday'
#,'room_order_num'
#,'basicroom_order_num'
#,'hotel_order_num'
,0
,1
,2
,3
,4
,5
,6
,7
,8
,9
,10
,11
,12
,13
,14
,15
,16
,17
,18
,19
,20
,21
,22
,23
,24
,25
,26
,27
,28
,29
,30
,31
,32
,33
,34
,35
,36
,37
,38
        ]

path = 'F:\\MyPython\\resource\\ctrip\\'
#path = 'E:\\cay\\resource\\temp\\'

#from sklearn.externals.joblib import load
#gbc = load('gbc_total.dmp')
bst = xgb.Booster() #init model
bst.load_model("xgboost.model") # load data

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



result_pd = pd.DataFrame()


path_train = path+'test_1.csv'
dataset1 = read_data(path_train)
dataset1 = DP.prepareData(dataset1)
compare_train = dataset1.ix[:,['orderid','roomid']]
dataset1 = dataset1[select_features]
xg_test = xgb.DMatrix(dataset1)

predict_train = bst.predict(xg_test)

compare_train = pd.concat([compare_train,pd.DataFrame(predict_train)],axis=1)
result_pd = pd.concat([result_pd,compare_train.loc[compare_train.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax()),['orderid','roomid']]])    

result_pd.to_csv(path+'\\result\\result_total1.csv',index=False)