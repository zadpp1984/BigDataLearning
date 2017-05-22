# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:41:31 2017

@author: Chenanyun
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

path_train = 'F:\\MyPython\\resource\\ctrip\\competition_train.txt'
usecols=['uid' ,'orderlabel', 'hotelid' ,'basicroomid' ,'roomid' ,'star' ,'rank' ,'returnvalue' ,'price_deduct' ,'basic_minarea' ,'basic_maxarea' ,'roomservice_1' ,'roomservice_2' ,'roomservice_3' ,'roomservice_4' ,'roomservice_5' ,'roomservice_6' ,'roomservice_7' ,'roomservice_8' ,'roomtag_1' ,'roomtag_3' ,'roomtag_4' ,'roomtag_5' ,'basic_week_ordernum_ratio' ,'basic_recent3_ordernum_ratio' ,'basic_comment_ratio']

x_train = pd.read_table(path_train,sep='\t',chunksize=100000,usecols=usecols,low_memory=False)
data_hotel = pd.DataFrame()
total_train,j = 0,1
for data_i in x_train:
    data_hotel = pd.concat((data_hotel,data_i),axis=0,ignore_index=True)
    total_train += data_i.shape[0]
    print(j,end=',')
    j+=1
#    if total_train >= 1000000:
#        break 


#data_hotel.describe().to_csv('F:\\MyPython\\resource\\ctrip\\describe.csv')
meanval = data_hotel[['roomtag_3']].mean()
data_hotel = data_hotel.fillna({'roomservice_1':0,'roomservice_4':0, 'basic_week_ordernum_ratio':0, 'basic_recent3_ordernum_ratio':0, 'basic_comment_ratio':0})

data_hotel = data_hotel.fillna({'roomtag_3':meanval})

data_hotel.describe()

data_hotel.dropna().to_csv('F:\\MyPython\\resource\\ctrip\\room_train.csv')
data_hotel[data_hotel.basic_minarea == pd.NaT].head()
