# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:06:56 2017

@author: Chenanyun
"""

import pandas as pd

path_train = 'F:\\MyPython\\resource\\ctrip\\competition_train.txt'
usecols='uid orderlabel hotelid basicroomid roomid star rank returnvalue price_deduct basic_minarea basic_maxarea roomservice_1 roomservice_2 roomservice_3 roomservice_4 roomservice_5 roomservice_6 roomservice_7 roomservice_8 roomtag_1 roomtag_2 roomtag_3 roomtag_4 roomtag_5 roomtag_6 basic_week_ordernum_ratio basic_recent3_ordernum_ratio basic_comment_ratio basic_30days_ordnumratio basic_30days_realratio room_30days_ordnumratio room_30days_realratio '.split()
#x_train是读取块，循环是对读取块的遍历
x_train = pd.read_table(path_train,sep='\t',chunksize=100000,usecols=usecols,low_memory=False)
data_hotel = pd.DataFrame()
total_train,j = 0,1
for data_i in x_train:
    data_hotel = pd.concat((data_hotel,data_i),axis=0,ignore_index=True)
    total_train += data_i.shape[0]
    print(j,end=',')
    j+=1


data_hotel.head()

print(data_hotel.index)

