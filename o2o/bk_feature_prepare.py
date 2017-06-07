# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 10:51:50 2017

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

class Action:
    'type 1:无券消费 2:领券消费 3:领券未消费'
    'User_id Merchant_id Coupon_id Date_received Date'
    def __init__(self, row):
        self.user = User.get(row['User_id'])
        self.merchant = Merchant.get(row['Merchant_id'])
        self.Date_received = row['Date_received']
        self.Date_buy = row['Date']
        if row['Date'] is np.nan:
#            领券未消费
            self.type = 3
            self.coupon = Coupon.get(row['Coupon_id'])
            self.coupon.addAction(self)
        else:
#            购买行为
            if row['Coupon_id'] is np.nan:
#                无券消费
                self.type = 1
            else:
#                领券消费
                self.type = 2
                self.coupon = Coupon.get(row['Coupon_id'])
                self.coupon.addAction(self)

#        存储彼此之间关系
        self.user.addAction(self)
        self.merchant.addAction(self)
        
class User:
    thismap={}
    def __init__(self, id):
        self.id = id
        self.totalAction = []
        self.noCouponConsumption = []
        self.couponConsumption = []
        self.couponArray = []
        
    def get(id):
        if  id in User.thismap:
            user = User.thismap[id]
        else:
            user = User(id)
        return user
    
    def addAction(self, action):
        self.totalAction.append(action)
        if action.type == 1:
            self.noCouponConsumption.append(action)
        elif action.type ==2:
            self.couponConsumption.append(action)
            self.couponArray.append(action.coupon)
        else:
            self.couponArray.append(action.coupon)
            
            
class Merchant:
    thismap={}
    def __init__(self, id):
        self.id = id
        self.couponArray = []
        
    def get(id):
        if  id in Merchant.thismap:
            merchant = Merchant.thismap[id]
        else:
            merchant = Merchant(id)
        return merchant
    
    def addAction(self, action):
        self.totalAction.append(action)
        if action.type == 1:
            self.noCouponConsumption.append(action)
        elif action.type ==2:
            self.couponConsumption.append(action)
            self.couponArray.append(action.coupon)
        else:
            self.couponArray.append(action.coupon)
            
class Coupon:
    thismap={}
    def __init__(self, id):
        self.id = id

    def get(id):
        if id is np.nan:
            return np.nan
        else:
            if  id in Coupon.thismap:
                coupon = Coupon.thismap[id]
            else:
                coupon = Coupon(id)
        return coupon


    
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




data_train = read_table(filename2,columns2)
data_train.replace('null',np.NAN,inplace=True)
data_train['Date_received'] = pd.to_datetime(data_train['Date_received'],format='%Y%m%d')
data_train['Date'] = pd.to_datetime(data_train['Date'],format='%Y%m%d')
data_train['Consumption_type']=0

#def parse_consumption_type()
data_train[data_train['Date'].isnull()]['Consumption_type']=1

index = 1
for index,row in data_train.iterrows():
    action = Action(row)
    
    
    index+=1
    if index == 5:
        break




 
data_train.head()