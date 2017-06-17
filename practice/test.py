# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:00:29 2017

@author: user
"""

import pandas as pd
import numpy as np


#

path = 'E:\\cay\\resource\\temp\\'

m=11
index=1

path_train = path+'train_total'+str(m)+'_'+str(index)+'.csv'


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

dataset1 = read_data(path_train)

    
dataset1['orderid'] = dataset1['orderid'].apply(lambda x: x[6:])
dataset1['uid'] = dataset1['uid'].apply(lambda x: x[5:])
dataset1['hotelid'] = dataset1['hotelid'].apply(lambda x: x[6:])
dataset1['basicroomid'] = dataset1['basicroomid'].apply(lambda x: x[6:])
dataset1['roomid'] = dataset1['roomid'].apply(lambda x: x[5:])


mydict1 = {
        'order_price_index':0,
        'df_index':0,
        'last_orderid':'',
        'order_pd':dataset1['orderid']
        }

def add_order_price_index(x,md):
    order_price_index = md['order_price_index']
    df_index = md['df_index']
    last_orderid = md['last_orderid']
    order_pd = md['order_pd']
    
    this_order = order_pd[df_index]
    
    if this_order == last_orderid:
        pass
    else:
        order_price_index = 0
    order_price_index += 1
    
    md['order_price_index'] = order_price_index
    md['df_index'] = df_index + 1
    md['last_orderid'] = this_order
    return order_price_index
dataset1.sort_values(['orderid','price_deduct'],inplace=True)
dataset1.reset_index(drop=True,inplace=True)
dataset1['new']=0
dataset1['new'] = dataset1['new'].apply(add_order_price_index,args=(mydict1,))
mydict2 = {
        'order_price_index':1,
        'basicroom_price_index':1,
        'df_index':0,
        'last_orderid':'',
        'last_basicroomid':'',
        'order_and_basicroom':dataset1[['orderid','basicroomid']]
        }

def add_basicroom_price_index(x,md):
    basicroom_price_index = md['basicroom_price_index']
    df_index = md['df_index']
    last_orderid = md['last_orderid']
    last_basicroomid = md['last_basicroomid']
    order_and_basicroom = md['order_and_basicroom']
    
    this_order = order_and_basicroom.ix[df_index,'orderid']
    this_basic = order_and_basicroom.ix[df_index,'basicroomid']
    
    if this_order == last_orderid:
        if this_basic != last_basicroomid:
            basicroom_price_index = 0    
    else:
        basicroom_price_index = 0
    basicroom_price_index += 1
    
    md['basicroom_price_index'] = basicroom_price_index
    md['df_index'] = df_index + 1
    md['last_orderid'] = this_order
    md['last_basicroomid'] = this_basic
    return basicroom_price_index

dataset1.sort_values(['orderid','basicroomid','price_deduct'],inplace=True)
dataset1.reset_index(drop=True,inplace=True)
dataset1['new2'] = 0
dataset1['new2'] = dataset1['new2'].apply(add_basicroom_price_index,args=(mydict2,))





