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
,'roomtag_6_lastord'
,'star_lastord'
,'hotel_minprice_lastord'
,'basic_minprice_lastord'
#,'order_index'
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
,'distance_avg_star'
,'distance_last_star'
,'distance_avg_return'
,'distance_last_return'
,'avg_roomarea'
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
,'roomtag_6_lastord'
,'star_lastord'
,'hotel_minprice_lastord'
,'basic_minprice_lastord'
#,'order_index'
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
,'distance_avg_star'
,'distance_last_star'
,'distance_avg_return'
,'distance_last_return'
,'avg_roomarea'
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
#    尝试下return_lastord  returnvalue  user_avgpromotion
    
    dataset1['returnvalue'] = dataset1['returnvalue']-200
    dataset1['return_lastord'] = dataset1['return_lastord']-200
    dataset1['user_avgpromotion'] = dataset1['user_avgpromotion']-200
    
    dataset1.ix[dataset1['basic_minarea']<=0,'basic_minarea'] = np.nan
    dataset1.ix[dataset1['basic_maxarea']<=0,'basic_maxarea'] = np.nan
    
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
            }
    dataset1.fillna(zero_dict,inplace=True)
    #fillna(mean)
    mean_dict={
            'roomtag_3':dataset1['roomtag_3'].mean()
            ,'user_confirmtime':dataset1['user_confirmtime'].mean()
            ,'user_avgdealprice':dataset1['user_avgdealprice'].mean()
            ,'user_avgpromotion':dataset1['user_avgpromotion'].mean()
            ,'user_avgprice_star':dataset1['user_avgprice_star'].mean()
            ,'user_activation':dataset1['user_activation'].mean()
            ,'user_stdprice':dataset1['user_stdprice'].mean()
            ,'user_cvprice':dataset1['user_cvprice'].mean()
            ,'user_avgrecommendlevel':dataset1['user_avgrecommendlevel'].mean()
            }
    
    dataset1.fillna(mean_dict,inplace=True)
    
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
            ,'hotel_minprice_lastord':dataset1['hotel_minprice_lastord'].mean()
            ,'basic_minprice_lastord':dataset1['basic_minprice_lastord'].mean()
            ,'rank_lastord':dataset1['rank_lastord'].mean()
            ,'return_lastord':dataset1['return_lastord'].mean()
            ,'price_last_lastord':dataset1['price_last_lastord'].mean()
            ,'star_lastord':dataset1['star_lastord'].mean()
    #        TODO
            ,'user_rank_ratio':dataset1['user_rank_ratio'].mean()
            ,'basic_minarea':dataset1['basic_minarea'].mean()
            ,'basic_maxarea':dataset1['basic_maxarea'].mean()
    #        TODO
            }
    
    dataset1.fillna(mean_temp_dict,inplace=True)
    
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
    #将平均面积标签化
    dataset1['user_avgroomarea'] = dataset1['user_avgroomarea'].astype('int')
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

    """
            对定性特征哑编码
    """
    #哑编码，对IRIS数据集的目标值，返回值为哑编码后的数据
    from sklearn.preprocessing import OneHotEncoder
    #enc = OneHotEncoder(categorical_features=onehot_arr,n_values=[3,4,6,3,5,4,6,3,5],sparse=False)
    enc = OneHotEncoder(categorical_features='all',n_values='auto',sparse=False)
    
    #onehot_arr=[
    #         'roomservice_1'
    #        ,'roomservice_2'
    #        ,'roomservice_3'
    #        ,'roomservice_4'
    #        ,'roomservice_5'
    #        ,'roomservice_6'
    #        ,'roomservice_7'
    #        ,'roomservice_8'
    #        ,'roomtag_1'
    #        ,'roomtag_4'
    #        ,'roomtag_5'
    #        ]
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
#    dataset1_list = dataset1[onehot_arr]
    
    enc.fit(dataset1[onehot_arr].values)
    dataset1_t = enc.transform(dataset1[onehot_arr].values)
    dataset1.drop(onehot_arr,axis=1,inplace=True)
    dataset1 = pd.concat([dataset1,pd.DataFrame(dataset1_t)],axis=1)
    return dataset1