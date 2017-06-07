# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:59:12 2017

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

#columns_type=['int64'         #User_id
#              ,'int64'        #Merchant_id
#              ,'int64'        #Coupon_id
#              ,'object'       #Discount_rate
#              ,'int64'        #Distance
#              ,'int64'        #Date_received
#              ,'int64'        #Date
#              ]

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
    print('\n')
    return thisdata

#    'Discount_type 0:无 1:打折 2:满减
def parse_Discount_type(x):
    if x is np.nan:
        return 0
    else:
        if ':' in x:
            return 2
        else:
            return 1

def parse_Discount_type_1(x):
    if x is np.nan:
        return 0.
    else:
        if ':' in x:
            return 0.
        else:
            return float(x)

def parse_Discount_type_2(x):
    if x is np.nan:
        return 0.
    else:
        if ':' in x:
            fill,reduce = x.split(':')
            return 1 - int(reduce)/int(fill)
        else:
            return 0.

def parse_Discount_type_2_threshold(x):
    if x is np.nan:
        return 0.
    else:
        if ':' in x:
            fill,reduce = x.split(':')
            return fill
        else:
            return 0.

print('读取文件...', end='\n')
data_train = read_table(filename2,columns2)
print('置换null...', end='\n')
data_train.replace('null',np.nan,inplace=True)


print('转换时间格式...', end='\n')
#时间格式转换
data_train['Date_received'] = pd.to_datetime(data_train['Date_received'],format='%Y%m%d')
data_train['Date'] = pd.to_datetime(data_train['Date'],format='%Y%m%d')

print('数据类型 Consumption_type 1:无券消费 2:领券消费 3:领券未消费', end='\n')
#Consumption_type 1:无券消费 2:领券消费 3:领券未消费
data_train['Consumption_type'] = 2
data_train.ix[data_train.Coupon_id.isnull(),'Consumption_type'] = 1
data_train.ix[(data_train.Consumption_type==2) & (data_train.Date.notnull()),'Consumption_type'] = 3
              

print('分析折扣类型', end='\n')
#Discount_type 0:无 1:打折 2:满减
data_train['Discount_type'] = data_train['Discount_rate'].apply(parse_Discount_type)

print(' 分析直接打折', end='\n')
#Discount_type_1 具体折扣
data_train['Discount_type_1'] = data_train['Discount_rate'].apply(parse_Discount_type_1)

print(' 分析满减打折', end='\n')
#Discount_type_2 具体满减比例
data_train['Discount_type_2'] = data_train['Discount_rate'].apply(parse_Discount_type_2)
data_train['Discount_type_2_threshold'] = data_train['Discount_rate'].apply(parse_Discount_type_2_threshold)


print('消费券使用间隔分析...',end='\n')
data_train['period']=data_train['Date'] - data_train['Date_received']

print('has_Distance分析...',end='\n')
#has_Distance 0:没有Distance项 1:有Distance项
data_train['has_Distance'] = 0
data_train.ix[data_train.Distance.notnull(),'has_Distance'] = 1

Merchant_number_of_Coupon_map = {}

data_train.head(10)
data_train.info()

usergb = data_train.groupby('User_id')
dir(usergb.count())


data_train[data_train['User_id']==4]

"""
血的教训呀  不要轻易用for循环处理pandas
index = 1
for index,row in data_train.iterrows():
#    'Consumption_type 1:无券消费 2:领券消费 3:领券未消费'
    if row['Date'] is np.nan:
        data_train.loc[index,'Consumption_type'] = 3
    else:
        if row['Coupon_id'] is np.nan:
            data_train.loc[index,'Consumption_type'] = 1
        else:
            data_train.loc[index,'Consumption_type'] = 2

    if not pd.isnull(row['Date']) and not pd.isnull(row['Date_received']):
        data_train.loc[index,'period'] = row['Date'] - row['Date_received']

    index+=1
    if index % 10 == 0:
        print(index)
    if index  == 100:
        break
"""


#plt.figure(figsize=[12,10])
##sns.distplot(data_train[data_train['Consumption_type']==1].Consumption_type.values, color='red')
#sns.distplot(data_train[data_train['Consumption_type']==2].Discount_type_2.values, color='blue')
#sns.distplot(data_train[data_train['Consumption_type']==3].Discount_type_2.values, color='orange')
#
#
#sns.pairplot(data_train[:50]
#            ,vars=['Discount_type','Discount_type_1','Discount_type_2']
#            ,hue='Consumption_type')

