# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:43:05 2017

@author: Chenanyun
"""
import pandas as pd

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\temp\\'

index = 7

#path_in = path+'train_'+str(index)+'.csv'
#path_out = path+'train_'+str(index)+'_sorted.csv'

path_in = path+'test_'+str(index)+'.csv'
path_out = path+'test_'+str(index)+'_sorted.csv'


def read_data(file):
    
    with open(file, 'r') as f:
        columns = f.readline().strip('\n').split('\t') 
    
    dataset = pd.DataFrame()
    file_handler = pd.read_table(file,
                                 sep='\t',
                                 chunksize=1000000,
                                 usecols=columns,
                                 low_memory=False)
    
    i = 1
    for data_i in file_handler:
        dataset = pd.concat((dataset,data_i),axis=0,ignore_index=True)
        print i
        i+=1

    del data_i
    return dataset

dataset1 = read_data(path_in)

dataset1['orderid'] = dataset1['orderid'].apply(lambda x: x[6:])
dataset1['uid'] = dataset1['uid'].apply(lambda x: x[5:])
dataset1['hotelid'] = dataset1['hotelid'].apply(lambda x: x[6:])
dataset1['basicroomid'] = dataset1['basicroomid'].apply(lambda x: x[6:])
dataset1['roomid'] = dataset1['roomid'].apply(lambda x: x[5:])

space_dict = {
         'orderid_lastord':'      '
        ,'hotelid_lastord':'      '
        ,'basicroomid_lastord':'      '
        ,'roomid_lastord':'     '
        }
dataset1.fillna(space_dict,inplace=True)
dataset1['orderid_lastord'] = dataset1['orderid_lastord'].apply(lambda x: x[6:])
dataset1['hotelid_lastord'] = dataset1['hotelid_lastord'].apply(lambda x: x[6:])
dataset1['basicroomid_lastord'] = dataset1['basicroomid_lastord'].apply(lambda x: x[6:])
dataset1['roomid_lastord'] = dataset1['roomid_lastord'].apply(lambda x: x[5:])


dataset1.sort_values(['orderid','price_deduct'],inplace=True)
dataset1.reset_index(drop=True,inplace=True)
mydict1 = {
        'order_price_index':0,
        'df_index':0,
        'last_orderid':'',
        'order_pd':dataset1['orderid'],
        
        'last_price_deduct':0,
        'price_pd':dataset1['price_deduct']
        }
def add_order_price_index(x,md):
    order_price_index = md['order_price_index']
    df_index = md['df_index']
    last_orderid = md['last_orderid']
    order_pd = md['order_pd']
    this_order = order_pd[df_index]
    
    last_price_deduct = md['last_price_deduct']
    price_pd = md['price_pd']
    this_price = price_pd[df_index]
    
    if this_order == last_orderid:
        if this_price == last_price_deduct:
            pass
        else:
            order_price_index+=1
    else:
        order_price_index = 1
    
    
    md['order_price_index'] = order_price_index
    md['df_index'] = df_index + 1
    md['last_orderid'] = this_order
    md['last_price_deduct'] = this_price
    return order_price_index

dataset1['order_price_index']=0
dataset1['order_price_index'] = dataset1['order_price_index'].apply(add_order_price_index,args=(mydict1,))


dataset1.sort_values(['orderid','basicroomid','price_deduct'],inplace=True)
dataset1.reset_index(drop=True,inplace=True)
mydict2 = {
        'basicroom_price_index':1,
        'df_index':0,
        'last_orderid':'',
        'last_basicroomid':'',
        'order_and_basicroom':dataset1[['orderid','basicroomid']],
        
        'last_price_deduct':0,
        'price_pd':dataset1['price_deduct']
        }
def add_basicroom_price_index(x,md):
    basicroom_price_index = md['basicroom_price_index']
    df_index = md['df_index']
    last_orderid = md['last_orderid']
    last_basicroomid = md['last_basicroomid']
    order_and_basicroom = md['order_and_basicroom']
    
    this_order = order_and_basicroom.ix[df_index,'orderid']
    this_basic = order_and_basicroom.ix[df_index,'basicroomid']
    
    last_price_deduct = md['last_price_deduct']
    price_pd = md['price_pd']
    this_price = price_pd[df_index]
    
    if this_order == last_orderid:
        if this_basic == last_basicroomid:
            if this_price == last_price_deduct:
                pass
            else:
                basicroom_price_index += 1
        else:
            basicroom_price_index = 1
    else:
        basicroom_price_index = 1
    
    md['basicroom_price_index'] = basicroom_price_index
    md['df_index'] = df_index + 1
    md['last_orderid'] = this_order
    md['last_basicroomid'] = this_basic
    md['last_price_deduct'] = this_price
    return basicroom_price_index


dataset1['basicroom_price_index'] = 0
dataset1['basicroom_price_index'] = dataset1['basicroom_price_index'].apply(add_basicroom_price_index,args=(mydict2,))

dataset1.sort_values(['orderid','basicroomid','rank'],inplace=True)
dataset1.reset_index(drop=True,inplace=True)
    
mydict3 = {
        'basicroom_rank_index':1,
        'df_index':0,
        'last_orderid':'',
        'last_basicroomid':'',
        'order_and_basicroom':dataset1[['orderid','basicroomid']]
        }
def add_basicroom_rank_index(x,md):
    basicroom_rank_index = md['basicroom_rank_index']
    df_index = md['df_index']
    last_orderid = md['last_orderid']
    last_basicroomid = md['last_basicroomid']
    order_and_basicroom = md['order_and_basicroom']
    
    this_order = order_and_basicroom.ix[df_index,'orderid']
    this_basic = order_and_basicroom.ix[df_index,'basicroomid']
    
    if this_order == last_orderid:
        if this_basic != last_basicroomid:
            basicroom_rank_index = 0    
    else:
        basicroom_rank_index = 0
    basicroom_rank_index += 1
    
    md['basicroom_rank_index'] = basicroom_rank_index
    md['df_index'] = df_index + 1
    md['last_orderid'] = this_order
    md['last_basicroomid'] = this_basic
    return basicroom_rank_index


dataset1['basicroom_rank_index'] = 0
dataset1['basicroom_rank_index'] = dataset1['basicroom_rank_index'].apply(add_basicroom_rank_index,args=(mydict3,))

dataset1.sort_values(['orderid','hotelid','basic_week_ordernum_ratio'],ascending=False,inplace=True)
dataset1.reset_index(drop=True,inplace=True)
mydict4 = {
        'basic_week_ordernum_ratio_index':1,
        'df_index':0,
        'last_orderid':'',
        'last_hotelid':'',
        'last_basic_week_ordernum_ratio':0,
        'order_and_hotel':dataset1[['orderid','hotelid']],
        'basic_week_ordernum_ratio_pd':dataset1['basic_week_ordernum_ratio']
        }
def add_basic_week_ordernum_ratio_index(x,md):
    basic_week_ordernum_ratio_index = md['basic_week_ordernum_ratio_index']
    df_index = md['df_index']
    order_and_hotel = md['order_and_hotel']
    basic_week_ordernum_ratio_pd = md['basic_week_ordernum_ratio_pd']
    
    this_order = order_and_hotel.ix[df_index,'orderid']
    this_hotel = order_and_hotel.ix[df_index,'hotelid']
    this_ratio = basic_week_ordernum_ratio_pd[df_index]
    
    last_orderid = md['last_orderid']
    last_hotelid = md['last_hotelid']
    last_basic_week_ordernum_ratio = md['last_basic_week_ordernum_ratio']
    
    if this_order == last_orderid:
        if this_hotel == last_hotelid:
            if this_ratio == last_basic_week_ordernum_ratio:
                pass
            else:
                basic_week_ordernum_ratio_index += 1
        else:
            basic_week_ordernum_ratio_index = 1
    else:
        basic_week_ordernum_ratio_index = 1
    
    md['basic_week_ordernum_ratio_index'] = basic_week_ordernum_ratio_index
    md['df_index'] = df_index + 1
    md['last_orderid'] = this_order
    md['last_hotelid'] = this_hotel
    md['last_basic_week_ordernum_ratio'] = this_ratio
    return basic_week_ordernum_ratio_index

dataset1['basic_week_ordernum_ratio_index'] = 0
dataset1['basic_week_ordernum_ratio_index'] = dataset1['basic_week_ordernum_ratio_index'].apply(add_basic_week_ordernum_ratio_index,args=(mydict4,))


dataset1.sort_values(['orderid','hotelid','basic_recent3_ordernum_ratio'],ascending=False,inplace=True)
dataset1.reset_index(drop=True,inplace=True)
mydict5  = {
        'basic_recent3_ordernum_ratio_index':1,
        'df_index':0,
        'last_orderid':'',
        'last_hotelid':'',
        'last_basic_recent3_ordernum_ratio_ratio':0,
        'order_and_hotel':dataset1[['orderid','hotelid']],
        'basic_recent3_ordernum_ratio_pd':dataset1['basic_recent3_ordernum_ratio']
        }
def add_basic_recent3_ordernum_ratio_index(x,md):
    basic_recent3_ordernum_ratio_index = md['basic_recent3_ordernum_ratio_index']
    df_index = md['df_index']
    order_and_hotel = md['order_and_hotel']
    basic_recent3_ordernum_ratio_pd = md['basic_recent3_ordernum_ratio_pd']
    
    this_order = order_and_hotel.ix[df_index,'orderid']
    this_hotel = order_and_hotel.ix[df_index,'hotelid']
    this_ratio = basic_recent3_ordernum_ratio_pd[df_index]
    
    last_orderid = md['last_orderid']
    last_hotelid = md['last_hotelid']
    last_basic_recent3_ordernum_ratio_ratio = md['last_basic_recent3_ordernum_ratio_ratio']
    
    if this_order == last_orderid:
        if this_hotel == last_hotelid:
            if this_ratio == last_basic_recent3_ordernum_ratio_ratio:
                pass
            else:
                basic_recent3_ordernum_ratio_index += 1
        else:
            basic_recent3_ordernum_ratio_index = 1
    else:
        basic_recent3_ordernum_ratio_index = 1
    
    md['basic_recent3_ordernum_ratio_index'] = basic_recent3_ordernum_ratio_index
    md['df_index'] = df_index + 1
    md['last_orderid'] = this_order
    md['last_hotelid'] = this_hotel
    md['last_basic_recent3_ordernum_ratio_ratio'] = this_ratio
    return basic_recent3_ordernum_ratio_index

dataset1['basic_recent3_ordernum_ratio_index'] = 0
dataset1['basic_recent3_ordernum_ratio_index'] = dataset1['basic_recent3_ordernum_ratio_index'].apply(add_basic_recent3_ordernum_ratio_index,args=(mydict5,))


dataset1.sort_values(['orderid','hotelid','basic_comment_ratio'],ascending=False,inplace=True)
dataset1.reset_index(drop=True,inplace=True)
mydict6 = {
        'basic_comment_ratio_index':1,
        'df_index':0,
        'last_orderid':'',
        'last_hotelid':'',
        'last_basic_comment_ratio':0,
        'order_and_hotel':dataset1[['orderid','hotelid']],
        'basic_comment_ratio_pd':dataset1['basic_comment_ratio']
        }
def add_basic_comment_ratio_index(x,md):
    basic_comment_ratio_index = md['basic_comment_ratio_index']
    df_index = md['df_index']
    order_and_hotel = md['order_and_hotel']
    basic_comment_ratio_pd = md['basic_comment_ratio_pd']
    
    this_order = order_and_hotel.ix[df_index,'orderid']
    this_hotel = order_and_hotel.ix[df_index,'hotelid']
    this_ratio = basic_comment_ratio_pd[df_index]
    
    last_orderid = md['last_orderid']
    last_hotelid = md['last_hotelid']
    last_basic_comment_ratio = md['last_basic_comment_ratio']
    
    if this_order == last_orderid:
        if this_hotel == last_hotelid:
            if this_ratio == last_basic_comment_ratio:
                pass
            else:
                basic_comment_ratio_index += 1
        else:
            basic_comment_ratio_index = 1
    else:
        basic_comment_ratio_index = 1
    
    md['basic_comment_ratio_index'] = basic_comment_ratio_index
    md['df_index'] = df_index + 1
    md['last_orderid'] = this_order
    md['last_hotelid'] = this_hotel
    md['last_basic_comment_ratio'] = this_ratio
    return basic_comment_ratio_index

dataset1['basic_comment_ratio_index'] = 0
dataset1['basic_comment_ratio_index'] = dataset1['basic_comment_ratio_index'].apply(add_basic_comment_ratio_index,args=(mydict6,))


dataset1.to_csv(path_out,sep='\t',index=False)