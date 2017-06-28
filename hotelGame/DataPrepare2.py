# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:13:14 2017

@author: Chenanyun
"""

import pandas as pd
import numpy as np

select_features = [
#'orderid'
#,'uid'
#,'orderdate'
#,'hotelid'
#,'basicroomid'
#,'roomid'
#,'orderlabel'
'star'
,'rank'
,'returnvalue'
,'price_deduct'
,'basic_minarea'
,'basic_maxarea'
,'roomservice_2'
,'roomservice_5'
,'roomservice_7'
,'roomtag_1'
,'roomtag_2'
,'roomtag_3'
,'roomtag_4'
,'roomtag_5'
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
,'rank_lastord'
,'return_lastord'
,'price_last_lastord'
,'roomservice_2_lastord'
,'roomservice_5_lastord'
,'roomtag_2_lastord'
,'roomtag_3_lastord'
,'roomtag_4_lastord'
,'roomtag_5_lastord'
,'hotel_minprice_lastord'
,'basic_minprice_lastord'
,'order_index'
,'order_price_index'
,'basicroom_price_index'
,'basicroom_rank_index'
,'basic_week_ordernum_ratio_index'
,'basic_recent3_ordernum_ratio_index'
,'basic_comment_ratio_index'
,'is_holiday'
,'price_diff_order'
,'price_diff_order_price_ratio'
,'price_diff_hotel'
,'price_diff_hotel_price_ratio'
,'price_diff_basicroom'
,'price_diff_basicroom_price_ratio'
,'price_diff_user_avgdealpriceholiday'
,'price_diff_user_avgdealpriceworkday'
,'price_diff_user_avgdealprice'
,'price_diff_user_avgprice'
,'price_diff_user_maxprice'
,'price_diff_user_minprice'
,'price_diff_user_avgprice_1week'
,'price_diff_user_medprice_1week'
,'price_diff_user_minprice_1week'
,'price_diff_user_maxprice_1week'
,'price_diff_user_avgprice_1month'
,'price_diff_user_medprice_1month'
,'price_diff_user_minprice_1month'
,'price_diff_user_maxprice_1month'
,'price_diff_user_avgprice_3month'
,'price_diff_user_medprice_3month'
,'price_diff_user_minprice_3month'
,'price_diff_user_maxprice_3month'
,'price_diff_hotel_minprice_lastord'
,'price_diff_basic_minprice_lastord'
,'price_diff_price_last_lastord'
#,'price_diff_user_avgdealpriceholiday_price_ratio'
#,'price_diff_user_avgdealpriceworkday_price_ratio'
#,'price_diff_user_avgdealprice_price_ratio'
#,'price_diff_user_avgprice_price_ratio'
#,'price_diff_user_maxprice_price_ratio'
#,'price_diff_user_minprice_price_ratio'
#,'price_diff_user_avgprice_1week_price_ratio'
#,'price_diff_user_medprice_1week_price_ratio'
#,'price_diff_user_minprice_1week_price_ratio'
#,'price_diff_user_maxprice_1week_price_ratio'
#,'price_diff_user_avgprice_1month_price_ratio'
#,'price_diff_user_medprice_1month_price_ratio'
#,'price_diff_user_minprice_1month_price_ratio'
#,'price_diff_user_maxprice_1month_price_ratio'
#,'price_diff_user_avgprice_3month_price_ratio'
#,'price_diff_user_medprice_3month_price_ratio'
#,'price_diff_user_minprice_3month_price_ratio'
#,'price_diff_user_maxprice_3month_price_ratio'
#,'price_diff_hotel_minprice_lastord_price_ratio'
#,'price_diff_basic_minprice_lastord_price_ratio'
#,'price_diff_price_last_lastord_price_ratio'
,'price_diff_last_price_last_hotel'
,'price_diff_last_price_last_basic'
,'price_bigger_then_user_max'
,'price_lowwer_then_user_min'
,'price_bigger_then_user_maxprice_1week'
,'price_lowwer_then_user_minprice_1week'
,'price_bigger_then_user_maxprice_1month'
,'price_lowwer_then_user_minprice_1month'
,'price_bigger_then_user_maxprice_3month'
,'price_lowwer_then_user_minprice_3month'
,'distance_avg_return'
,'distance_last_return'
,'discount_ratio'
,'price_per_area'
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
,'distance_last_star'
,'distance_avg_star'
,'date_from_last'
,'user_roomservice_8_345ratio'
,'user_roomservice_8_2ratio'
,'user_roomservice_4_1ratio_3month'
,'user_roomservice_4_1ratio_1month'
,'user_roomservice_4_1ratio_1week'
,'match_roomservice_2'
,'match_roomservice_3'
#,'user_roomservice_4_max'
,'match_roomservice_4'
,'match_roomservice_5'
#,'user_roomservice_6_max'
,'match_roomservice_6'
,'match_roomservice_7'
#,'user_roomservice_8_max'
,'match_roomservice_8'
,'match_roomservice_3_1week'
#,'user_roomservice_4_1week_max'
,'match_roomservice_4_1week'
,'match_roomservice_7_1week'
,'match_roomservice_3_1month'
#,'user_roomservice_4_1month_max'
,'match_roomservice_4_1month'
,'match_roomservice_7_1month'
,'match_roomservice_3_3month'
#,'user_roomservice_4_3month_max'
,'match_roomservice_4_3month'
,'match_roomservice_7_3month'
,'diff_most_popular_basic_comment'
,'diff_most_popular_basicroom_week'
,'diff_most_popular_basicroom_recent3'
,'diff_most_popular_basicroom_30days'
,'diff_most_popular_basicroom_realratio_30days'
,'diff_most_popular_room_30days_ordnumratio'
,'diff_most_popular_room_30days_realratio'
,'distance_avg_rank'
,'distance_last_rank'
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
,39
        ]


"""""""""""""""""""""""""""""""""""""""""""""""""""
          process data
"""""""""""""""""""""""""""""""""""""""""""""""""""
def prepareData(dataset1):
        
    dataset1.ix[dataset1['basic_minarea']<=0,'basic_minarea'] = np.nan
    dataset1.ix[dataset1['basic_maxarea']<=0,'basic_maxarea'] = np.nan
    
    
    #    roomid中包含rank信息 这里给删掉
    mydict1 = {
            'index':0,
            'rank_pd':dataset1['rank']
            }
    def cut_rank(x,md):
        this_index = md['index']
        rank_pd = md['rank_pd']
        this_rank = rank_pd[this_index]
        rank_len = -1
        if this_rank >= 100:
            rank_len = -3
        elif this_rank >=10:
            rank_len = -2
        
        md['index'] = this_index + 1
        return str(x)[:rank_len]
    dataset1['newroomid'] = dataset1['roomid'].apply(cut_rank,args=(mydict1,))
    dataset1['newroomid'] = dataset1['newroomid'].astype('float64')
    
    #是否是假日 0:workday 1:holiday
    holiday_list = ['2013-04-14','2013-04-20','2013-04-21','2013-04-27']
    dataset1['is_holiday'] = 0
    dataset1.ix[dataset1['orderdate'].isin(holiday_list),'is_holiday'] = 1
    
    """""""""""""""""""""""""""""""""""""""""""""""""""
          price
    """"""""""""""""""""""""""""""""""""""""""""""""""" 
    #    针对价格创建新特征
    #    与其他各价格的差值
    #    与统一order中最低值的差值
    df1 = dataset1[['orderid','price_deduct']].groupby('orderid',as_index=False).min()
    df1.reset_index(drop=True,inplace=True)
    df1.columns = ['orderid','ordermin']
    df1 = pd.merge(dataset1[['orderid','price_deduct']],df1,on=['orderid'],how='left',suffixes=['','_y'])
    dataset1['price_diff_order'] = df1['price_deduct']-df1['ordermin']
    dataset1['price_diff_order_price_ratio'] = dataset1['price_diff_order'] / dataset1['price_deduct']
    
    #    与统一order中的最小hotel的差值
    del df1
    df2 = dataset1[['orderid','hotelid','price_deduct']].groupby(['orderid','hotelid'],as_index=False).min()
    df2.reset_index(drop=True,inplace=True)
    df2.columns = ['orderid','hotelid','hotelmin']
    df2 = pd.merge(dataset1[['orderid','hotelid','price_deduct',]],df2,on=['orderid','hotelid'],how='left',suffixes=['','_y'])
    dataset1['price_diff_hotel'] = df2['price_deduct']-df2['hotelmin']
    dataset1['price_diff_hotel_price_ratio'] = dataset1['price_diff_hotel'] / dataset1['price_deduct']
    del df2
    
    #    与统一order中的最小basicroom的差值
    df3 = dataset1[['orderid','basicroomid','price_deduct']].groupby(['orderid','basicroomid'],as_index=False).min()
    df3.reset_index(drop=True,inplace=True)
    df3.columns = ['orderid','basicroomid','basicroommin']
    df3 = pd.merge(dataset1[['orderid','basicroomid','price_deduct',]],df3,on=['orderid','basicroomid'],how='left',suffixes=['','_y'])
    dataset1['price_diff_basicroom'] = df3['price_deduct']-df3['basicroommin']
    dataset1['price_diff_basicroom_price_ratio'] = dataset1['price_diff_basicroom'] / dataset1['price_deduct']
    del df3
    
    #    TODO没有考虑差值与房价之间的比率
    #    与给定属性间差距
    dataset1['price_diff_user_avgdealpriceholiday'] = dataset1['price_deduct'] - dataset1['user_avgdealpriceholiday']
    dataset1['price_diff_user_avgdealpriceworkday'] = dataset1['price_deduct'] - dataset1['user_avgdealpriceworkday']
    dataset1['price_diff_user_avgdealprice'] = dataset1['price_deduct'] - dataset1['user_avgdealprice']
    dataset1['price_diff_user_avgprice'] = dataset1['price_deduct'] - dataset1['user_avgprice']
    dataset1['price_diff_user_maxprice'] = dataset1['price_deduct'] - dataset1['user_maxprice']
    dataset1['price_diff_user_minprice'] = dataset1['price_deduct'] - dataset1['user_minprice']
    dataset1['price_diff_user_avgprice_1week'] = dataset1['price_deduct'] - dataset1['user_avgprice_1week']
    dataset1['price_diff_user_medprice_1week'] = dataset1['price_deduct'] - dataset1['user_medprice_1week']
    dataset1['price_diff_user_minprice_1week'] = dataset1['price_deduct'] - dataset1['user_minprice_1week']
    dataset1['price_diff_user_maxprice_1week'] = dataset1['price_deduct'] - dataset1['user_maxprice_1week']
    dataset1['price_diff_user_avgprice_1month'] = dataset1['price_deduct'] - dataset1['user_avgprice_1month']
    dataset1['price_diff_user_medprice_1month'] = dataset1['price_deduct'] - dataset1['user_medprice_1month']
    dataset1['price_diff_user_minprice_1month'] = dataset1['price_deduct'] - dataset1['user_minprice_1month']
    dataset1['price_diff_user_maxprice_1month'] = dataset1['price_deduct'] - dataset1['user_maxprice_1month']
    dataset1['price_diff_user_avgprice_3month'] = dataset1['price_deduct'] - dataset1['user_avgprice_3month']
    dataset1['price_diff_user_medprice_3month'] = dataset1['price_deduct'] - dataset1['user_medprice_3month']
    dataset1['price_diff_user_minprice_3month'] = dataset1['price_deduct'] - dataset1['user_minprice_3month']
    dataset1['price_diff_user_maxprice_3month'] = dataset1['price_deduct'] - dataset1['user_maxprice_3month']
    dataset1['price_diff_hotel_minprice_lastord'] = dataset1['price_deduct'] - dataset1['hotel_minprice_lastord']
    dataset1['price_diff_basic_minprice_lastord'] = dataset1['price_deduct'] - dataset1['basic_minprice_lastord']
    dataset1['price_diff_price_last_lastord'] = dataset1['price_deduct'] - dataset1['price_last_lastord']
    
    
    dataset1['price_diff_user_avgdealpriceholiday_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_avgdealpriceholiday'])/dataset1['price_deduct']
    dataset1['price_diff_user_avgdealpriceworkday_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_avgdealpriceworkday'])/dataset1['price_deduct']
    dataset1['price_diff_user_avgdealprice_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_avgdealprice'])/dataset1['price_deduct']
    dataset1['price_diff_user_avgprice_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_avgprice'])/dataset1['price_deduct']
    dataset1['price_diff_user_maxprice_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_maxprice'])/dataset1['price_deduct']
    dataset1['price_diff_user_minprice_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_minprice'])/dataset1['price_deduct']
    dataset1['price_diff_user_avgprice_1week_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_avgprice_1week'])/dataset1['price_deduct']
    dataset1['price_diff_user_medprice_1week_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_medprice_1week'])/dataset1['price_deduct']
    dataset1['price_diff_user_minprice_1week_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_minprice_1week'])/dataset1['price_deduct']
    dataset1['price_diff_user_maxprice_1week_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_maxprice_1week'])/dataset1['price_deduct']
    dataset1['price_diff_user_avgprice_1month_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_avgprice_1month'])/dataset1['price_deduct']
    dataset1['price_diff_user_medprice_1month_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_medprice_1month'])/dataset1['price_deduct']
    dataset1['price_diff_user_minprice_1month_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_minprice_1month'])/dataset1['price_deduct']
    dataset1['price_diff_user_maxprice_1month_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_maxprice_1month'])/dataset1['price_deduct']
    dataset1['price_diff_user_avgprice_3month_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_avgprice_3month'])/dataset1['price_deduct']
    dataset1['price_diff_user_medprice_3month_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_medprice_3month'])/dataset1['price_deduct']
    dataset1['price_diff_user_minprice_3month_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_minprice_3month'])/dataset1['price_deduct']
    dataset1['price_diff_user_maxprice_3month_price_ratio'] = (dataset1['price_deduct'] - dataset1['user_maxprice_3month'])/dataset1['price_deduct']
    dataset1['price_diff_hotel_minprice_lastord_price_ratio'] = (dataset1['price_deduct'] - dataset1['hotel_minprice_lastord'])/dataset1['price_deduct']
    dataset1['price_diff_basic_minprice_lastord_price_ratio'] = (dataset1['price_deduct'] - dataset1['basic_minprice_lastord'])/dataset1['price_deduct']
    dataset1['price_diff_price_last_lastord_price_ratio'] = (dataset1['price_deduct'] - dataset1['price_last_lastord'])/dataset1['price_deduct']
    
    dataset1['price_diff_last_price_last_hotel'] = dataset1['price_last_lastord'] - dataset1['hotel_minprice_lastord']
    dataset1['price_diff_last_price_last_basic'] = dataset1['price_last_lastord'] - dataset1['basic_minprice_lastord']
    
#    dataset1['diff_price_hotel_ratio'] = dataset1['price_diff_hotel'] / (dataset1['price_diff_last_price_last_hotel']+0.0001)
#    dataset1['diff_price_basic_ratio'] = dataset1['price_diff_basicroom'] / dataset1['price_diff_last_price_last_basic']
    
    dataset1['price_bigger_then_user_max'] = 0
    dataset1.ix[dataset1['price_deduct'] > dataset1['user_maxprice'] ,'price_bigger_then_user_max'] = 1
    dataset1['price_lowwer_then_user_min'] = 0
    dataset1.ix[dataset1['price_deduct'] < dataset1['user_minprice'] ,'price_lowwer_then_user_min'] = 1
    
    dataset1['price_bigger_then_user_maxprice_1week'] = 0
    dataset1.ix[dataset1['price_deduct'] > dataset1['user_maxprice_1week'] ,'price_bigger_then_user_maxprice_1week'] = 1
    dataset1['price_lowwer_then_user_minprice_1week'] = 0
    dataset1.ix[dataset1['price_deduct'] < dataset1['user_minprice_1week'] ,'price_lowwer_then_user_minprice_1week'] = 1
    
    
    dataset1['price_bigger_then_user_maxprice_1month'] = 0
    dataset1.ix[dataset1['price_deduct'] > dataset1['user_maxprice_1month'] ,'price_bigger_then_user_maxprice_1month'] = 1
    dataset1['price_lowwer_then_user_minprice_1month'] = 0
    dataset1.ix[dataset1['price_deduct'] < dataset1['user_minprice_1month'] ,'price_lowwer_then_user_minprice_1month'] = 1
    
    dataset1['price_bigger_then_user_maxprice_3month'] = 0
    dataset1.ix[dataset1['price_deduct'] > dataset1['user_maxprice_3month'] ,'price_bigger_then_user_maxprice_3month'] = 1
    dataset1['price_lowwer_then_user_minprice_3month'] = 0
    dataset1.ix[dataset1['price_deduct'] < dataset1['user_minprice_3month'] ,'price_lowwer_then_user_minprice_3month'] = 1
    
    #与平均返值差距	distance_avg_return
    dataset1['distance_avg_return'] = dataset1['returnvalue'] - dataset1['user_avgpromotion']
    #与上次返值差距	distance_last_return
    dataset1['distance_last_return'] = dataset1['returnvalue'] - dataset1['return_lastord']
    
    #    折扣比率
    dataset1['discount_ratio'] = dataset1['returnvalue'] / dataset1['price_deduct']
    
    dataset1['price_per_area'] = dataset1['price_deduct']/dataset1['basic_minarea']
    #    TODO
    #    price_diff_user_up2std=price_deduct-user_avgprice-2*user_stdprice,
    #    price_diff_user_down2std=price_deduct-user_avgprice+2*user_stdprice
    #    price_diff_user_up2std_yn=if_else(price_diff_user_up2std>0, 1, 0, NA_real_),
    #    price_diff_user_down2std_yn=if_else(price_diff_user_down2std0,1,0,NA_real_),
    
    """""""""""""""""""""""""""""""""""""""""""""""""""
          compare with last time
    """""""""""""""""""""""""""""""""""""""""""""""""""
    ############是否相同 0:same 1:not same############
    #与上次酒店是否相同	same_as_last_hotel  
    dataset1['same_as_last_hotel']=1
    dataset1.ix[dataset1['hotelid'] == dataset1['hotelid_lastord'],'same_as_last_hotel'] = 0
    #与上次物理房型是否相同	same_as_last_basic_room 
    dataset1['same_as_last_basic_room']=1
    dataset1.ix[dataset1['basicroomid'] == dataset1['basicroomid_lastord'],'same_as_last_basic_room'] = 0
    #与上次房型是否相同	same_as_last_room
    dataset1['same_as_last_room']=1
    dataset1.ix[dataset1['newroomid'] == dataset1['roomid_lastord'],'same_as_last_room'] = 0
#    dataset1.ix[dataset1['roomid'] == dataset1['roomid_lastord'],'same_as_last_room'] = 0
    #与上次service2是否相同	same_service2
    dataset1['same_service2']=1
    dataset1.ix[dataset1['roomservice_2'] == dataset1['roomservice_2_lastord'],'same_service2'] = 0
    #与上次service3是否相同	same_service3
    dataset1['same_service3']=1
    dataset1.ix[dataset1['roomservice_3'] == dataset1['roomservice_3_lastord'],'same_service3'] = 0
    #与上次service4是否相同	same_service4
    dataset1['same_service4']=1
    dataset1.ix[dataset1['roomservice_4'] == dataset1['roomservice_4_lastord'],'same_service4'] = 0
    #与上次service5是否相同	same_service5
    dataset1['same_service5']=1
    dataset1.ix[dataset1['roomservice_5'] == dataset1['roomservice_5_lastord'],'same_service5'] = 0
    #与上次service6是否相同	same_service6
    dataset1['same_service6']=1
    dataset1.ix[dataset1['roomservice_6'] == dataset1['roomservice_6_lastord'],'same_service6'] = 0
    #与上次service8是否相同	same_service8
    dataset1['same_service8']=1
    dataset1.ix[dataset1['roomservice_8'] == dataset1['roomservice_8_lastord'],'same_service8'] = 0
    #与上次tag2是否相同	same_tag2
    dataset1['same_tag2']=1
    dataset1.ix[dataset1['roomtag_2'] == dataset1['roomtag_2_lastord'],'same_tag2'] = 0
    #与上次tag3是否相同	same_tag3
    dataset1['same_tag3']=1
    dataset1.ix[dataset1['roomtag_3'] == dataset1['roomtag_3_lastord'],'same_tag3'] = 0
    #与上次tag4是否相同	same_tag4
    dataset1['same_tag4']=1
    dataset1.ix[dataset1['roomtag_4'] == dataset1['roomtag_4_lastord'],'same_tag4'] = 0
    #与上次tag5是否相同	same_tag5
    dataset1['same_tag5']=1
    dataset1.ix[dataset1['roomtag_5'] == dataset1['roomtag_5_lastord'],'same_tag5'] = 0
    #与上次tag6是否相同	same_tag6
    dataset1['same_tag6']=1
    dataset1.ix[dataset1['roomtag_6'] == dataset1['roomtag_6_lastord'],'same_tag6'] = 0
    
    ############差距############
    #与上次tag3差距	distance_last_tag3
    dataset1['distance_last_tag3'] = dataset1['roomtag_3'] - dataset1['roomtag_3_lastord']
    #与上次星级差距	distance_last_star
    dataset1['distance_last_star'] = dataset1['star'] - dataset1['star_lastord']
    #与平均星级差距	distance_avg_star
    dataset1['distance_avg_star'] = dataset1['star'] - dataset1['user_avgstar']
    #与上次消费的时间差TODO
    dataset1['date_from_last'] = (pd.to_datetime(dataset1['orderdate'],format='%Y-%m-%d')-pd.to_datetime(dataset1['orderdate_lastord'],format='%Y-%m-%d')).dt.days
    data_from_last_dict = {
                'date_from_last':dataset1['date_from_last'].max()
            }
    dataset1.fillna(data_from_last_dict,inplace=True)
    
    
    """""""""""""""""""""""""""""""""""""""""""""""""""
          Service
    """""""""""""""""""""""""""""""""""""""""""""""""""
    dataset1['user_roomservice_8_345ratio'] = dataset1['user_roomservice_5_345ratio']
    dataset1.drop(['user_roomservice_5_345ratio'],axis=1,inplace=True)
    dataset1['user_roomservice_8_2ratio'] = 1 - dataset1['user_roomservice_8_345ratio'] - dataset1['user_roomservice_8_1ratio']
    dataset1['user_roomservice_4_1ratio_3month'] =(1 - dataset1['user_roomservice_4_0ratio_3month'] 
                                                     - dataset1['user_roomservice_4_2ratio_3month'] 
                                                     - dataset1['user_roomservice_4_3ratio_3month'] 
                                                     - dataset1['user_roomservice_4_4ratio_3month']
                                                     - dataset1['user_roomservice_4_5ratio_3month'])
    dataset1['user_roomservice_4_1ratio_1month'] =(1 - dataset1['user_roomservice_4_0ratio_1month'] 
                                                     - dataset1['user_roomservice_4_2ratio_1month'] 
                                                     - dataset1['user_roomservice_4_3ratio_1month'] 
                                                     - dataset1['user_roomservice_4_4ratio_1month']
                                                     - dataset1['user_roomservice_4_5ratio_1month'])
    dataset1['user_roomservice_4_1ratio_1week'] =(1  - dataset1['user_roomservice_4_0ratio_1week'] 
                                                     - dataset1['user_roomservice_4_2ratio_1week'] 
                                                     - dataset1['user_roomservice_4_3ratio_1week'] 
                                                     - dataset1['user_roomservice_4_4ratio_1week']
                                                     - dataset1['user_roomservice_4_5ratio_1week'])
    
    """""""""""""""normal"""""""""
    dataset1['match_roomservice_2'] = 0
    dataset1.ix[(dataset1['roomservice_2']==0)&(dataset1['user_roomservice_2_1ratio']<0.5),'match_roomservice_2']=1
    dataset1.ix[(dataset1['roomservice_2']==1)&(dataset1['user_roomservice_2_1ratio']>0.5),'match_roomservice_2']=1
    
    
    dataset1['match_roomservice_3'] = 0
    dataset1.ix[(dataset1['roomservice_3']==0)&(dataset1['user_roomservice_3_123ratio']<0.5),'match_roomservice_3']=1
    dataset1.ix[(dataset1['roomservice_3']==1)&(dataset1['user_roomservice_3_123ratio']>0.5),'match_roomservice_3']=1
    dataset1.ix[(dataset1['roomservice_3']==2)&(dataset1['user_roomservice_3_123ratio']>0.5),'match_roomservice_3']=1
    dataset1.ix[(dataset1['roomservice_3']==3)&(dataset1['user_roomservice_3_123ratio']>0.5),'match_roomservice_3']=1
    
    replace_dict = {
        "user_roomservice_4_0ratio": 0,
        "user_roomservice_4_1ratio": 1,
        "user_roomservice_4_2ratio": 2,
        "user_roomservice_4_3ratio": 3,
        "user_roomservice_4_4ratio": 4,
        "user_roomservice_4_5ratio": 5
        }
    dataset1['user_roomservice_4_max'] = dataset1[[ 'user_roomservice_4_0ratio',
                                                    'user_roomservice_4_1ratio',
                                                    'user_roomservice_4_2ratio',
                                                    'user_roomservice_4_3ratio',
                                                    'user_roomservice_4_4ratio',
                                                    'user_roomservice_4_5ratio'
                                                ]].rename(columns=replace_dict).idxmax(1)
    dataset1['match_roomservice_4'] = 0
    dataset1.ix[(dataset1['roomservice_4']==dataset1['user_roomservice_4_max']),'match_roomservice_4']=1
    
    dataset1['match_roomservice_5'] = 0
    dataset1.ix[(dataset1['roomservice_5']==0)&(dataset1['user_roomservice_5_1ratio']<0.5),'match_roomservice_5']=1
    dataset1.ix[(dataset1['roomservice_5']==1)&(dataset1['user_roomservice_5_1ratio']>0.5),'match_roomservice_5']=1
    
    replace_dict = {
        "user_roomservice_6_0ratio": 0,
        "user_roomservice_6_1ratio": 1,
        "user_roomservice_6_2ratio": 2
        }
    dataset1['user_roomservice_6_max'] = dataset1[[ 'user_roomservice_6_0ratio',
                                                    'user_roomservice_6_1ratio',
                                                    'user_roomservice_6_2ratio'
                                                ]].rename(columns=replace_dict).idxmax(1)
    dataset1['match_roomservice_6'] = 0
    dataset1.ix[(dataset1['roomservice_6']==dataset1['user_roomservice_6_max']),'match_roomservice_6']=1
    
    
    dataset1['match_roomservice_7'] = 0
    dataset1.ix[(dataset1['roomservice_7']==0)&(dataset1['user_roomservice_7_0ratio']>0.5),'match_roomservice_7']=1
    dataset1.ix[(dataset1['roomservice_7']==1)&(dataset1['user_roomservice_7_0ratio']<0.5),'match_roomservice_7']=1
    
    replace_dict = {
        "user_roomservice_8_1ratio": 1,
        "user_roomservice_8_2ratio": 2,
        "user_roomservice_8_345ratio": 3,
        }
    dataset1['user_roomservice_8_max'] = dataset1[[ "user_roomservice_8_1ratio",
                                                    "user_roomservice_8_2ratio",
                                                    "user_roomservice_8_345ratio"
                                                ]].rename(columns=replace_dict).idxmax(1)
    dataset1['match_roomservice_8'] = 0
    dataset1.ix[(dataset1['roomservice_8']==dataset1['user_roomservice_8_max']),'match_roomservice_8']=1
    dataset1.ix[(dataset1['roomservice_8']==4)&(dataset1['user_roomservice_8_max']==3),'match_roomservice_8']=1
    dataset1.ix[(dataset1['roomservice_8']==5)&(dataset1['user_roomservice_8_max']==3),'match_roomservice_8']=1
    
    """""""""""""""1week"""""""""
    dataset1['match_roomservice_3_1week'] = 0
    dataset1.ix[(dataset1['roomservice_3']==0)&(dataset1['user_roomservice_3_123ratio_1week']<0.5),'match_roomservice_3_1week']=1
    dataset1.ix[(dataset1['roomservice_3']==1)&(dataset1['user_roomservice_3_123ratio_1week']>0.5),'match_roomservice_3_1week']=1
    
    replace_dict = {
        "user_roomservice_4_0ratio_1week": 0,
        "user_roomservice_4_1ratio_1week": 1,
        "user_roomservice_4_2ratio_1week": 2,
        "user_roomservice_4_3ratio_1week": 3,
        "user_roomservice_4_4ratio_1week": 4,
        "user_roomservice_4_5ratio_1week": 5
        }
    dataset1['user_roomservice_4_1week_max'] = dataset1[[ 'user_roomservice_4_0ratio_1week',
                                                    'user_roomservice_4_1ratio_1week',
                                                    'user_roomservice_4_2ratio_1week',
                                                    'user_roomservice_4_3ratio_1week',
                                                    'user_roomservice_4_4ratio_1week',
                                                    'user_roomservice_4_5ratio_1week'
                                                ]].rename(columns=replace_dict).idxmax(1)
    dataset1['match_roomservice_4_1week'] = 0
    dataset1.ix[(dataset1['roomservice_4']==dataset1['user_roomservice_4_1week_max']),'match_roomservice_4_1week']=1
    
    dataset1['match_roomservice_7_1week'] = 0
    dataset1.ix[(dataset1['roomservice_7']==0)&(dataset1['user_roomservice_7_0ratio_1week']>0.5),'match_roomservice_7_1week']=1
    dataset1.ix[(dataset1['roomservice_7']==1)&(dataset1['user_roomservice_7_1ratio_1week']>0.5),'match_roomservice_7_1week']=1
    
    """""""""""""""1month"""""""""
    dataset1['match_roomservice_3_1month'] = 0
    dataset1.ix[(dataset1['roomservice_3']==0)&(dataset1['user_roomservice_3_123ratio_1month']<0.5),'match_roomservice_3_1month']=1
    dataset1.ix[(dataset1['roomservice_3']==1)&(dataset1['user_roomservice_3_123ratio_1month']>0.5),'match_roomservice_3_1month']=1
    
    replace_dict = {
        "user_roomservice_4_0ratio_1month": 0,
        "user_roomservice_4_1ratio_1month": 1,
        "user_roomservice_4_2ratio_1month": 2,
        "user_roomservice_4_3ratio_1month": 3,
        "user_roomservice_4_4ratio_1month": 4,
        "user_roomservice_4_5ratio_1month": 5
        }
    dataset1['user_roomservice_4_1month_max'] = dataset1[[ 'user_roomservice_4_0ratio_1month',
                                                           'user_roomservice_4_1ratio_1month',
                                                           'user_roomservice_4_2ratio_1month',
                                                           'user_roomservice_4_3ratio_1month',
                                                           'user_roomservice_4_4ratio_1month',
                                                           'user_roomservice_4_5ratio_1month'
                                                ]].rename(columns=replace_dict).idxmax(1)
    dataset1['match_roomservice_4_1month'] = 0
    dataset1.ix[(dataset1['roomservice_4']==dataset1['user_roomservice_4_1month_max']),'match_roomservice_4_1month']=1    
    
    dataset1['match_roomservice_7_1month'] = 0
    dataset1.ix[(dataset1['roomservice_7']==0)&(dataset1['user_roomservice_7_0ratio_1month']>0.5),'match_roomservice_7_1month']=1
    dataset1.ix[(dataset1['roomservice_7']==1)&(dataset1['user_roomservice_7_1ratio_1month']>0.5),'match_roomservice_7_1month']=1
    
    """""""""""""""3month"""""""""
    dataset1['match_roomservice_3_3month'] = 0
    dataset1.ix[(dataset1['roomservice_3']==0)&(dataset1['user_roomservice_3_123ratio_3month']<0.5),'match_roomservice_3_3month']=1
    dataset1.ix[(dataset1['roomservice_3']==1)&(dataset1['user_roomservice_3_123ratio_3month']>0.5),'match_roomservice_3_3month']=1
    
    replace_dict = {
        "user_roomservice_4_0ratio_3month": 0,
        "user_roomservice_4_1ratio_3month": 1,
        "user_roomservice_4_2ratio_3month": 2,
        "user_roomservice_4_3ratio_3month": 3,
        "user_roomservice_4_4ratio_3month": 4,
        "user_roomservice_4_5ratio_3month": 5
        }
    dataset1['user_roomservice_4_3month_max'] = dataset1[[ 'user_roomservice_4_0ratio_3month',
                                                           'user_roomservice_4_1ratio_3month',
                                                           'user_roomservice_4_2ratio_3month',
                                                           'user_roomservice_4_3ratio_3month',
                                                           'user_roomservice_4_4ratio_3month',
                                                           'user_roomservice_4_5ratio_3month'
                                                ]].rename(columns=replace_dict).idxmax(1)
    dataset1['match_roomservice_4_3month'] = 0
    dataset1.ix[(dataset1['roomservice_4']==dataset1['user_roomservice_4_3month_max']),'match_roomservice_4_3month']=1
    
    dataset1['match_roomservice_7_3month'] = 0
    dataset1.ix[(dataset1['roomservice_7']==0)&(dataset1['user_roomservice_7_0ratio_3month']>0.5),'match_roomservice_7_3month']=1
    dataset1.ix[(dataset1['roomservice_7']==1)&(dataset1['user_roomservice_7_1ratio_3month']>0.5),'match_roomservice_7_3month']=1
    
    """""""""""""""""""""""""""""""""""""""""""""""""""
          order num
    """""""""""""""""""""""""""""""""""""""""""""""""""
    most_popular = dataset1[['orderid','hotelid','basic_comment_ratio']].groupby(['orderid','hotelid'],as_index=False).max()
    most_popular.reset_index(drop=True,inplace=True)
    most_popular.columns = ['orderid','hotelid','basic_comment_ratio_max']
    most_popular = pd.merge(dataset1[['orderid','hotelid','basic_comment_ratio']],most_popular,on=['orderid','hotelid'],how='left',suffixes=['','_y'])
    dataset1['diff_most_popular_basic_comment'] = most_popular['basic_comment_ratio_max'] - most_popular['basic_comment_ratio']
    del most_popular    
    
    most_popular = dataset1[['orderid','hotelid','basic_week_ordernum_ratio']].groupby(['orderid','hotelid'],as_index=False).max()
    most_popular.reset_index(drop=True,inplace=True)
    most_popular.columns = ['orderid','hotelid','basic_week_ordernum_ratio_max']
    most_popular = pd.merge(dataset1[['orderid','hotelid','basic_week_ordernum_ratio']],most_popular,on=['orderid','hotelid'],how='left',suffixes=['','_y'])
    dataset1['diff_most_popular_basicroom_week'] = most_popular['basic_week_ordernum_ratio_max'] - most_popular['basic_week_ordernum_ratio']
    del most_popular
    
    most_popular = dataset1[['orderid','hotelid','basic_recent3_ordernum_ratio']].groupby(['orderid','hotelid'],as_index=False).max()
    most_popular.reset_index(drop=True,inplace=True)
    most_popular.columns = ['orderid','hotelid','basic_recent3_ordernum_ratio_max']
    most_popular = pd.merge(dataset1[['orderid','hotelid','basic_recent3_ordernum_ratio']],most_popular,on=['orderid','hotelid'],how='left',suffixes=['','_y'])
    dataset1['diff_most_popular_basicroom_recent3'] = most_popular['basic_recent3_ordernum_ratio_max'] - most_popular['basic_recent3_ordernum_ratio']
    del most_popular
       
    most_popular = dataset1[['orderid','hotelid','basic_30days_ordnumratio']].groupby(['orderid','hotelid'],as_index=False).max()
    most_popular.reset_index(drop=True,inplace=True)
    most_popular.columns = ['orderid','hotelid','basic_30days_ordnumratio_max']
    most_popular = pd.merge(dataset1[['orderid','hotelid','basic_30days_ordnumratio']],most_popular,on=['orderid','hotelid'],how='left',suffixes=['','_y'])
    dataset1['diff_most_popular_basicroom_30days'] = most_popular['basic_30days_ordnumratio_max'] - most_popular['basic_30days_ordnumratio']
    del most_popular    
    
    most_popular = dataset1[['orderid','hotelid','basic_30days_realratio']].groupby(['orderid','hotelid'],as_index=False).max()
    most_popular.reset_index(drop=True,inplace=True)
    most_popular.columns = ['orderid','hotelid','basic_30days_realratio_max']
    most_popular = pd.merge(dataset1[['orderid','hotelid','basic_30days_realratio']],most_popular,on=['orderid','hotelid'],how='left',suffixes=['','_y'])
    dataset1['diff_most_popular_basicroom_realratio_30days'] = most_popular['basic_30days_realratio_max'] - most_popular['basic_30days_realratio']
    del most_popular    
    
    most_popular = dataset1[['orderid','room_30days_ordnumratio']].groupby(['orderid'],as_index=False).max()
    most_popular.reset_index(drop=True,inplace=True)
    most_popular.columns = ['orderid','room_30days_ordnumratio_max']
    most_popular = pd.merge(dataset1[['orderid','room_30days_ordnumratio']],most_popular,on=['orderid'],how='left',suffixes=['','_y'])
    dataset1['diff_most_popular_room_30days_ordnumratio'] = most_popular['room_30days_ordnumratio_max'] - most_popular['room_30days_ordnumratio']
    del most_popular   
     
    most_popular = dataset1[['orderid','room_30days_realratio']].groupby(['orderid'],as_index=False).max()
    most_popular.reset_index(drop=True,inplace=True)
    most_popular.columns = ['orderid','room_30days_realratio_max']
    most_popular = pd.merge(dataset1[['orderid','room_30days_realratio']],most_popular,on=['orderid'],how='left',suffixes=['','_y'])
    dataset1['diff_most_popular_room_30days_realratio'] = most_popular['room_30days_realratio_max'] - most_popular['room_30days_realratio']
    del most_popular  
        
    #与平均rank的差距	distance_avg_rank
    dataset1['distance_avg_rank'] = dataset1['rank'] - dataset1['user_rank_ratio']
    #与上次rank的差距	distance_last_rank
    dataset1['distance_last_rank'] = dataset1['rank'] - dataset1['rank_lastord']
     
    """
            对定性特征哑编码
    """
    zero_dict = {
             'roomservice_1':0
            ,'roomservice_3':0
            ,'roomservice_4':0
            ,'roomservice_6':0
            ,'roomservice_8':0
            ,'roomservice_3_lastord':0
            ,'roomservice_4_lastord':0
            ,'roomservice_6_lastord':0
            ,'roomservice_8_lastord':0
            }
    dataset1.fillna(zero_dict,inplace=True)
    #哑编码，对IRIS数据集的目标值，返回值为哑编码后的数据
    from sklearn.preprocessing import OneHotEncoder
    #enc = OneHotEncoder(categorical_features=onehot_arr,n_values=[3,4,6,3,5,4,6,3,5],sparse=False)
    enc = OneHotEncoder(categorical_features='all',n_values='auto',sparse=False)
    
    onehot_arr=[
             'roomservice_1'
            ,'roomservice_3'
            ,'roomservice_4'
            ,'roomservice_6'
            ,'roomservice_8'
            ,'roomservice_3_lastord'
            ,'roomservice_4_lastord'
            ,'roomservice_6_lastord'
            ,'roomservice_8_lastord'
            ]
    
    enc.fit(dataset1[onehot_arr].values)
    dataset1_t = enc.transform(dataset1[onehot_arr].values)
    dataset1.drop(onehot_arr,axis=1,inplace=True)
    dataset1 = pd.concat([dataset1,pd.DataFrame(dataset1_t)],axis=1)
    return dataset1