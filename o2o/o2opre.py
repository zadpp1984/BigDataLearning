# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 19:51:02 2017

@author: Chenanyun
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = 'F:\\MyPython\\resource\\data\\020data\\'

filename1=path+'ccf_offline_stage1_test_revised.csv'
filename2=path+'ccf_offline_stage1_train.csv'
filename3=path+'ccf_online_stage1_train.csv'


with open(filename1, 'r') as f:
    columns1 = f.readline().strip('\n').split(',') 

with open(filename2, 'r') as f:
    columns2 = f.readline().strip('\n').split(',')
    
with open(filename3, 'r') as f:
    columns3 = f.readline().strip('\n').split(',') 

def read_table(file,columns):
    thisfile = pd.read_table(file
                             ,sep=','
                             ,chunksize=100000
                             ,usecols=columns
                             ,low_memory=False
                             )
    thisdata = pd.DataFrame()
    j=1
    for data_i in thisfile:
        thisdata = pd.concat((thisdata,data_i),axis=0,ignore_index=True)
        print(j,end=',')
        j+=1
    return thisdata

data_test = read_table(filename1,columns1)
data_train = read_table(filename2,columns2)


data_test.replace('null',np.NAN,inplace=True)
data_train.replace('null',np.NAN,inplace=True)
data_train['Coupon_id']


data_test['Date_received'] = pd.to_datetime(data_test['Date_received'],format='%Y%m%d')
data_train['Date_received'] = pd.to_datetime(data_train['Date_received'],format='%Y%m%d')
data_train['Date'] = pd.to_datetime(data_train['Date'],format='%Y%m%d')
data_test.head()
data_train.head()

data_test.info()
data_train.info()

data_train.describe()
len(data_test[data_test['Distance'].isnull()])/len(data_test)