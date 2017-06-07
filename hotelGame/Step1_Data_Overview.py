# -*- coding: utf-8 -*-
"""
Created on Sat May 27 00:27:47 2017

@author: Chenanyun
"""

import pandas as pd

path = 'F:\\MyPython\\resource\\ctrip\\'
#path = 'E:\\cay\\resource\\'

path_train = path+'competition_train.txt'
#path_train = path+'competition_test.txt'

basicCol=[
        'orderid'
        ,'uid'
        ,'orderdate'
        ,'hotelid'
        ,'basicroomid'
        ,'roomid'
        ,'orderlabel'
        ,'star'
        ,'rank'
        ,'returnvalue'
        ,'price_deduct'
        ,'basic_minarea'
        ,'basic_maxarea'
        ,'roomservice_1'
        ,'roomservice_2'
        ,'roomservice_3'
        ,'roomservice_4'
        ,'roomservice_5'
        ,'roomservice_6'
        ,'roomservice_7'
        ,'roomservice_8'
        ,'roomtag_1'
        ,'roomtag_2'
        ,'roomtag_3'
        ,'roomtag_4'
        ,'roomtag_5'
        ,'roomtag_6'
        ,'user_confirmtime'
        ,'user_avgadvanceddate'
        ,'user_avgstar'
        ,'user_avggoldstar'
        ,'user_avgrecommendlevel'
        ,'user_avgroomnum'
        ,'ordertype_1_ratio'
        ,'ordertype_2_ratio'
        ,'ordertype_3_ratio'
        ,'ordertype_4_ratio'
        ,'ordertype_5_ratio'
        ,'ordertype_6_ratio'
        ,'ordertype_7_ratio'
        ,'ordertype_8_ratio'
        ,'ordertype_9_ratio'
        ,'ordertype_10_ratio'
        ,'ordertype_11_ratio'
        ,'user_avgdealpriceholiday'
        ,'user_avgdealpriceworkday'
        ,'user_avgdealprice'
        ,'user_avgpromotion'
        ,'user_avgprice_star'
        ,'orderbehavior_1_ratio'
        ,'orderbehavior_2_ratio'
        ,'orderbehavior_3_ratio_1week'
        ,'orderbehavior_4_ratio_1week'
        ,'orderbehavior_5_ratio_1week'
        ,'orderbehavior_3_ratio_1month'
        ,'orderbehavior_4_ratio_1month'
        ,'orderbehavior_5_ratio_1month'
        ,'orderbehavior_3_ratio_3month'
        ,'orderbehavior_4_ratio_3month'
        ,'orderbehavior_5_ratio_3month'
        ,'orderbehavior_6_ratio'
        ,'orderbehavior_7_ratio'
        ,'orderbehavior_8'
        ,'orderbehavior_9'
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
        ,'user_ordnum_1week'
        ,'user_avgprice_1week'
        ,'user_medprice_1week'
        ,'user_minprice_1week'
        ,'user_maxprice_1week'
        ,'user_roomservice_3_123ratio_1week'
        ,'user_roomservice_7_1ratio_1week'
        ,'user_roomservice_7_0ratio_1week'
        ,'user_roomservice_4_5ratio_1week'
        ,'user_roomservice_4_4ratio_1week'
        ,'user_roomservice_4_2ratio_1week'
        ,'user_roomservice_4_3ratio_1week'
        ,'user_roomservice_4_0ratio_1week'
        ,'user_ordnum_1month'
        ,'user_avgprice_1month'
        ,'user_medprice_1month'
        ,'user_minprice_1month'
        ,'user_maxprice_1month'
        ,'user_roomservice_3_123ratio_1month'
        ,'user_roomservice_7_1ratio_1month'
        ,'user_roomservice_7_0ratio_1month'
        ,'user_roomservice_4_5ratio_1month'
        ,'user_roomservice_4_4ratio_1month'
        ,'user_roomservice_4_2ratio_1month'
        ,'user_roomservice_4_3ratio_1month'
        ,'user_roomservice_4_0ratio_1month'
        ,'user_ordnum_3month'
        ,'user_avgprice_3month'
        ,'user_medprice_3month'
        ,'user_minprice_3month'
        ,'user_maxprice_3month'
        ,'user_roomservice_3_123ratio_3month'
        ,'user_roomservice_7_1ratio_3month'
        ,'user_roomservice_7_0ratio_3month'
        ,'user_roomservice_4_5ratio_3month'
        ,'user_roomservice_4_4ratio_3month'
        ,'user_roomservice_4_2ratio_3month'
        ,'user_roomservice_4_3ratio_3month'
        ,'user_roomservice_4_0ratio_3month'
        ,'basic_week_ordernum_ratio'
        ,'basic_recent3_ordernum_ratio'
        ,'basic_comment_ratio'
        ,'basic_30days_ordnumratio'
        ,'basic_30days_realratio'
        ,'room_30days_ordnumratio'
        ,'room_30days_realratio'
        ,'orderid_lastord'
        ,'orderdate_lastord'
        ,'hotelid_lastord'
        ,'roomid_lastord'
        ,'basicroomid_lastord'
        ,'rank_lastord'
        ,'return_lastord'
        ,'price_last_lastord'
        ,'roomservice_2_lastord'
        ,'roomservice_3_lastord'
        ,'roomservice_4_lastord'
        ,'roomservice_5_lastord'
        ,'roomservice_6_lastord'
        ,'roomservice_8_lastord'
        ,'roomtag_2_lastord'
        ,'roomtag_3_lastord'
        ,'roomtag_4_lastord'
        ,'roomtag_5_lastord'
        ,'roomtag_6_lastord'
        ,'star_lastord'
        ,'hotel_minprice_lastord'
        ,'basic_minprice_lastord'
         ]

usecols = [
        'orderlabel'
        ,'ordertype_1_ratio'
        ,'ordertype_2_ratio'
        ,'ordertype_3_ratio'
        ,'ordertype_4_ratio'
        ,'ordertype_5_ratio'
        ,'ordertype_6_ratio'
        ,'ordertype_7_ratio'
        ,'ordertype_8_ratio'
        ,'ordertype_9_ratio'
        ,'ordertype_10_ratio'
        ,'ordertype_11_ratio'
        ]

file_handler = pd.read_table(path_train,
                             sep='\t',
                             chunksize=100000,
                             usecols=usecols,
                             low_memory=False)

dataset = pd.DataFrame()
total_train,j = 0,1
for data_i in file_handler:
    dataset = pd.concat((dataset,data_i),axis=0,ignore_index=True)
    total_train += data_i.shape[0]
    print(j,end=',')
    j+=1
#    if total_train >= 1000000:
#        break 
del data_i

#dataset.describe().to_csv(path+'describe.csv')

#dataset['orderdate'] = pd.to_datetime(dataset['orderdate'],format='%Y-%m-%d')
#dataset.describe(include='all')
#dataset.head(10)

import matplotlib as plt
import seaborn as sns


plt.figure.Figure(figsize=(30,30))
corr1 = dataset.dropna().corr()
sns.heatmap(corr1,annot=True)

