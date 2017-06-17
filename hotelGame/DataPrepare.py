# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 17:21:45 2017

@author: Chenanyun
"""

import pandas as pd
import numpy as np

select_features1 = [
 'star'
,'rank'
,'returnvalue'
,'price_deduct'
,'basic_minarea'
#,'basic_maxarea'
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
#,'roomtag_6_lastord'
,'star_lastord'
,'hotel_minprice_lastord'
,'basic_minprice_lastord'
#,'order_index'
,'same_as_last_hotel'
,'same_as_last_basic_room'
#,'same_as_last_room'
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
#,'same_tag6'
,'distance_last_tag3'
,'distance_avg_star'
,'distance_last_star'
,'distance_avg_return'
,'distance_last_return'
#,'avg_roomarea'
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
,'price_diff_order'
,'price_diff_hotel'
,'price_diff_basicroom'
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
,'orderbehavior_6_ratio'
,'orderbehavior_7_ratio'
,'orderbehavior_8'
,'orderbehavior_9'
,'bigger_than_min_area'
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
,'confirmtime_positive'
,'advanceddate_positive'
,'roomservice_3_123'
,'roomservice_8_345'
,'total_service_num'
,'total_tag_num'
,'order_price_index'
,'basicroom_price_index'
,'basicroom_rank_index'
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
select_features2 = [
 'star'
,'rank'
,'returnvalue'
,'price_deduct'
,'basic_minarea'
#,'basic_maxarea'
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
#,'roomtag_6_lastord'
,'star_lastord'
,'hotel_minprice_lastord'
,'basic_minprice_lastord'
#,'order_index'
,'same_as_last_hotel'
,'same_as_last_basic_room'
#,'same_as_last_room'
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
#,'same_tag6'
,'distance_last_tag3'
,'distance_avg_star'
,'distance_last_star'
,'distance_avg_return'
,'distance_last_return'
#,'avg_roomarea'
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
,'price_diff_order'
,'price_diff_hotel'
,'price_diff_basicroom'
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
,'orderbehavior_6_ratio'
,'orderbehavior_7_ratio'
,'orderbehavior_8'
,'orderbehavior_9'
,'bigger_than_min_area'
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
,'confirmtime_positive'
,'advanceddate_positive'
,'roomservice_3_123'
,'roomservice_8_345'
,'total_service_num'
,'total_tag_num'
,'order_price_index'
,'basicroom_price_index'
,'basicroom_rank_index'
,'0'
,'1'
,'2'
,'3'
,'4'
,'5'
,'6'
,'7'
,'8'
,'9'
,'10'
,'11'
,'12'
,'13'
,'14'
,'15'
,'16'
,'17'
,'18'
,'19'
,'20'
,'21'
,'22'
,'23'
,'24'
,'25'
,'26'
,'27'
,'28'
,'29'
,'30'
,'31'
,'32'
,'33'
,'34'
,'35'
,'36'
,'37'
,'38'
        ]


def prepareData(dataset1):
    """""""""""""""""""""""""""""""""""""""""""""""""""
          process data
    """""""""""""""""""""""""""""""""""""""""""""""""""
    
    
#    填充房屋面积
    dataset1.ix[dataset1['basic_minarea']<=0,'basic_minarea'] = np.nan
    dataset1.ix[dataset1['basic_maxarea']<=0,'basic_maxarea'] = np.nan
    
    df1 = dataset1[['orderid','price_deduct']].groupby('orderid',as_index=False).min()
    df1.reset_index(drop=True,inplace=True)
    df1.columns = ['orderid','ordermin']
    df1 = pd.merge(dataset1[['orderid','price_deduct']],df1,on=['orderid'],how='left',suffixes=['','_y'])
    dataset1['price_diff_order'] = df1['price_deduct']-df1['ordermin']
    del df1
    
    df2 = dataset1[['orderid','hotelid','price_deduct']].groupby(['orderid','hotelid'],as_index=False).min()
    df2.reset_index(drop=True,inplace=True)
    df2.columns = ['orderid','hotelid','hotelmin']
    df2 = pd.merge(dataset1[['orderid','hotelid','price_deduct',]],df2,on=['orderid','hotelid'],how='left',suffixes=['','_y'])
    dataset1['price_diff_hotel'] = df2['price_deduct']-df2['hotelmin']
    del df2
    
    
    df3 = dataset1[['orderid','basicroomid','price_deduct']].groupby(['orderid','basicroomid'],as_index=False).min()
    df3.reset_index(drop=True,inplace=True)
    df3.columns = ['orderid','basicroomid','basicroommin']
    df3 = pd.merge(dataset1[['orderid','basicroomid','price_deduct',]],df3,on=['orderid','basicroomid'],how='left',suffixes=['','_y'])
    dataset1['price_diff_basicroom'] = df3['price_deduct']-df3['basicroommin']
    del df3
    
    #fillna(0)
    zero_dict = {
             'roomservice_1':0
            ,'roomservice_4':0
            ,'basic_week_ordernum_ratio':0
            ,'basic_recent3_ordernum_ratio':0
            ,'basic_comment_ratio':0
            ,'user_roomservice_4_0ratio':0
            ,'user_roomservice_4_1ratio':0
            ,'user_roomservice_4_5ratio':0
            ,'user_roomservice_6_2ratio':0
            ,'user_roomservice_6_1ratio':0
            ,'user_roomservice_6_0ratio':0
            ,'user_roomservice_2_1ratio':0
            ,'user_roomservice_5_345ratio':0
            
            
            ,'ordertype_2_ratio':0
            ,'ordertype_3_ratio':0
            ,'ordertype_4_ratio':0
            ,'ordertype_5_ratio':0
            }
    dataset1.fillna(zero_dict,inplace=True)
    #fillna(mean)
    mean_dict={
             'user_confirmtime':dataset1['user_confirmtime'].median()
            ,'user_avgdealprice':dataset1['user_avgdealprice'].median()
            ,'user_avgpromotion':dataset1['user_avgpromotion'].median()
            ,'user_avgprice_star':dataset1['user_avgprice_star'].median()
            ,'user_activation':dataset1['user_activation'].median()
            ,'user_stdprice':dataset1['user_stdprice'].median()
            ,'user_cvprice':dataset1['user_cvprice'].median()
            ,'user_avgrecommendlevel':dataset1['user_avgrecommendlevel'].median()
            }
    
    dataset1.fillna(mean_dict,inplace=True)
    #    填充最小值
#    min_dict = {
#            
#            'user_ordnum_1week':dataset1['user_ordnum_1week'].min(),
#            'user_ordnum_1month':dataset1['user_ordnum_1month'].min(),
#            'user_ordnum_3month':dataset1['user_ordnum_3month'].min(),
#            
#            
#            'user_avgprice_1week':dataset1['user_avgprice_1week'].min(),
#            'user_medprice_1week':dataset1['user_medprice_1week'].min(),
#            'user_minprice_1week':dataset1['user_minprice_1week'].min(),
#            'user_maxprice_1week':dataset1['user_maxprice_1week'].min(),
#            
#            'user_avgprice_1month':dataset1['user_avgprice_1month'].min(),
#            'user_medprice_1month':dataset1['user_medprice_1month'].min(),
#            'user_minprice_1month':dataset1['user_minprice_1month'].min(),
#            'user_maxprice_1month':dataset1['user_maxprice_1month'].min(),
#            
#            'user_avgprice_3month':dataset1['user_avgprice_3month'].min(),
#            'user_medprice_3month':dataset1['user_medprice_3month'].min(),
#            'user_minprice_3month':dataset1['user_minprice_3month'].min(),
#            'user_maxprice_3month':dataset1['user_maxprice_3month'].min(),
#            
#            'roomtag_3':dataset1['roomtag_3'].min()
#            }
#    dataset1.fillna(min_dict,inplace=True)
    min_dict = {
            
            'user_ordnum_1week':0,
            'user_ordnum_1month':0,
            'user_ordnum_3month':0,
            
            
            'user_avgprice_1week':0,
            'user_medprice_1week':0,
            'user_minprice_1week':0,
            'user_maxprice_1week':0,
            
            'user_avgprice_1month':0,
            'user_medprice_1month':0,
            'user_minprice_1month':0,
            'user_maxprice_1month':0,
            
            'user_avgprice_3month':0,
            'user_medprice_3month':0,
            'user_minprice_3month':0,
            'user_maxprice_3month':0,
            
            'roomtag_3':dataset1['roomtag_3'].min()
            }
    dataset1.fillna(min_dict,inplace=True)
    
#    临时处理
    dataset1.ix[dataset1['basic_minarea']<=0,'basic_minarea'] = np.nan
    dataset1.ix[dataset1['basic_maxarea']<=0,'basic_maxarea'] = np.nan
    mean_temp_dict={
             'roomservice_2_lastord':0
            ,'roomservice_3_lastord':0
            ,'roomservice_4_lastord':0
            ,'roomservice_5_lastord':0
            ,'roomservice_6_lastord':0
            ,'roomservice_8_lastord':1
            ,'roomtag_3_lastord':0
            ,'roomtag_4_lastord':0
            ,'roomtag_5_lastord':0
            ,'roomtag_6_lastord':0
            ,'hotel_minprice_lastord':dataset1['hotel_minprice_lastord'].median()
            ,'basic_minprice_lastord':dataset1['basic_minprice_lastord'].median()
            ,'rank_lastord':dataset1['rank_lastord'].median()
            ,'return_lastord':dataset1['return_lastord'].median()
            ,'price_last_lastord':dataset1['price_last_lastord'].median()
            ,'star_lastord':dataset1['star_lastord'].median()
    #        TODO
            ,'user_rank_ratio':dataset1['user_rank_ratio'].median()
            ,'basic_minarea':dataset1['basic_minarea'].median()
    #        TODO
            }
    
    dataset1.fillna(mean_temp_dict,inplace=True)
    
#    same order mean
    df4 = dataset1[['orderid','basic_minarea']].groupby(['orderid'],as_index=False).median()
    df4.reset_index(drop=True,inplace=True)
    df4.columns=['orderid','basic_minarea_mean']
    df4 = pd.merge(dataset1.ix[dataset1['basic_minarea'].isnull(),['orderid','roomid']],df4,on=['orderid'],how='left',suffixes=['','_y'])
    dataset1.ix[dataset1['basic_minarea'].isnull(),['basic_minarea']] = df4['basic_minarea_mean']
#    dataset1.fillna({'basic_minarea':dataset1['basic_minarea'].median()},inplace=True)
    del df4

    dataset1['bigger_than_min_area'] = 0
    dataset1.ix[dataset1['basic_maxarea']>dataset1['basic_minarea'],'bigger_than_min_area'] =1
    df5 = dataset1[['orderid','basic_maxarea']].groupby(['orderid'],as_index=False).median()
    df5.reset_index(drop=True,inplace=True)
    df5.columns=['orderid','basic_maxarea_mean']
    df5 = pd.merge(dataset1.ix[dataset1['basic_maxarea'].isnull(),['orderid','roomid']],df5,on=['orderid'],how='left',suffixes=['','_y'])
    dataset1.ix[dataset1['basic_maxarea'].isnull(),['basic_maxarea']] = df5['basic_maxarea_mean']
#    dataset1.fillna({'basic_maxarea':dataset1['basic_maxarea'].median()},inplace=True)
    del df5
    
    #(0,1)处理
    dataset1.ix[dataset1.roomtag_2.notnull(),'roomtag_2'] = 1
    dataset1.ix[dataset1.roomtag_2.isnull(),'roomtag_2'] = 0
    dataset1.ix[dataset1.roomtag_2_lastord.notnull(),'roomtag_2_lastord'] = 1
    dataset1.ix[dataset1.roomtag_2_lastord.isnull(),'roomtag_2_lastord'] = 0
    
    
    #根据平均价格与节假日/工作日的比例填充
    holiday_ratio = dataset1['user_avgdealpriceholiday'].mean()/dataset1['user_avgdealprice'].mean()
    dataset1.ix[dataset1.user_avgdealpriceholiday.isnull(),'user_avgdealpriceholiday'] = dataset1.ix[dataset1['user_avgdealpriceholiday'].isnull(),'user_avgdealprice']*holiday_ratio
    workday_ratio = dataset1['user_avgdealpriceworkday'].mean()/dataset1['user_avgdealprice'].mean()
    dataset1.ix[dataset1.user_avgdealpriceworkday.isnull(),'user_avgdealpriceworkday'] = dataset1.ix[dataset1['user_avgdealpriceworkday'].isnull(),'user_avgdealprice']*workday_ratio
    
#    确认时间不应该有正数
    dataset1['confirmtime_positive'] = 0
    dataset1.ix[dataset1['user_confirmtime']>=0,'confirmtime_positive'] = 1
    dataset1.ix[dataset1['user_confirmtime']>0,'user_confirmtime'] = 0
    
    
    dataset1['advanceddate_positive'] = 0
    dataset1.ix[dataset1['user_avgadvanceddate']>=0,'advanceddate'] = 1
    dataset1.ix[dataset1['user_avgadvanceddate']>0,'user_avgadvanceddate'] = 0

    """""""""""""""""""""""""""""""""""""""""""""""""""
          create feature
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
    dataset1.ix[dataset1['roomid'] == dataset1['roomid_lastord'],'same_as_last_room'] = 0
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
    #与平均星级差距	distance_avg_star
    dataset1['distance_avg_star'] = dataset1['star'] - dataset1['user_avgstar']
    #与上次星级差距	distance_last_star
    dataset1['distance_last_star'] = dataset1['star'] - dataset1['star_lastord']
    #与平均返值差距	distance_avg_return
    dataset1['distance_avg_return'] = dataset1['returnvalue'] - dataset1['user_avgpromotion']
    #与上次返值差距	distance_last_return
    dataset1['distance_last_return'] = dataset1['returnvalue'] - dataset1['return_lastord']
    
    #计算该次平均面积	avg_roomarea
    dataset1['avg_roomarea'] = (dataset1['basic_maxarea'] + dataset1['basic_minarea'])/2
#    #将平均面积标签化
#    dataset1['user_avgroomarea'] = dataset1['user_avgroomarea'].astype('int')
    ##与过去平均面积的差距	distance_avg_roomarea
    #dataset1['distance_avg_roomarea'] = dataset1['avg_roomarea'] - dataset1['user_avgroomnum']
    ##与上次面积的差距	distance_last_roomarea
    #dataset1['distance_last_roomarea'] = (dataset1['avg_roomarea'] - dataset1['user_avgroomnum']).abs()
    
    #与平均价钱的差距	distance_avg_price
    dataset1['distance_avg_price'] = dataset1['price_deduct'] - dataset1['user_avgdealprice']
    #与平均假日的差距	distance_avg_holiday_price
    dataset1['distance_avg_holiday_price'] = dataset1['price_deduct'] - dataset1['user_avgdealpriceholiday']
    #与平日价钱的差距	distance_avg_workday_price
    dataset1['distance_avg_workday_price'] = dataset1['price_deduct'] - dataset1['user_avgdealpriceworkday']
    
    #当前价钱是否在max和min价钱之间	between_max_min   0:out 1:in
    dataset1['between_max_min']=0
    dataset1.ix[(dataset1['price_deduct'] <= dataset1['user_maxprice'])&(dataset1['price_deduct'] >= dataset1['user_minprice']),'between_max_min'] = 1
    
    #与平均rank的差距	distance_avg_rank
    dataset1['distance_avg_rank'] = dataset1['rank'] - dataset1['user_rank_ratio']
    #与上次rank的差距	distance_last_rank
    dataset1['distance_last_rank'] = dataset1['rank'] - dataset1['rank_lastord']
    
    #与上次消费的时间差TODO
    dataset1['date_from_last'] = (pd.to_datetime(dataset1['orderdate'],format='%Y-%m-%d')-pd.to_datetime(dataset1['orderdate_lastord'],format='%Y-%m-%d')).dt.days
    data_from_last_dict = {
            'date_from_last':dataset1['date_from_last'].max()
            }
    dataset1.fillna(data_from_last_dict,inplace=True)
    
    #是否是假日 0:workday 1:holiday
    holiday_list = ['2013-04-14','2013-04-20','2013-04-21','2013-04-27']
    dataset1['is_holiday'] = 0
    dataset1['is_holiday'] = dataset1.ix[dataset1['orderdate'].isin(holiday_list),'is_holiday'] = 1



#    针对后续特征特殊处理
    dataset1['roomservice_3_123'] = 1
    dataset1.ix[dataset1['roomservice_3']==0,'roomservice_3_123'] = 0


    dataset1['roomservice_8_345'] = 1
    dataset1.ix[(dataset1['user_roomservice_5_345ratio']==1)&(dataset1['user_roomservice_5_345ratio']==2),'roomservice_3_123'] = 0
    
#    total_service_num
    dataset1['total_service_num'] = 0
    dataset1.ix[dataset1['roomservice_2']>0,'total_service_num']+=1
    dataset1.ix[dataset1['roomservice_3']>0,'total_service_num']+=1
    dataset1.ix[dataset1['roomservice_4']>0,'total_service_num']+=1
    dataset1.ix[dataset1['roomservice_5']>0,'total_service_num']+=1
    dataset1.ix[dataset1['roomservice_6']>0,'total_service_num']+=1
    dataset1.ix[dataset1['roomservice_7']>0,'total_service_num']+=1
    
    dataset1['total_tag_num'] = 0
    dataset1.ix[dataset1['roomtag_1']>0,'total_tag_num']+=1
    dataset1.ix[dataset1['roomtag_4']>0,'total_tag_num']+=1
    dataset1.ix[dataset1['roomtag_5']>0,'total_tag_num']+=1
    
    
    
    """
            对定性特征哑编码
    """
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