# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:09:03 2017

@author: Chenanyun
"""
import pandas as pd
import numpy as np

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\temp\\'

path_train = path+'train_1.csv'
path_test = path+'test_1.csv'

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
        print(i,end=',')
        i+=1

    del data_i
    return dataset

dataset1 = read_data(path_train)

dataset1.dropna(axis=1,how='all',inplace=True)
#
#
#dataset1.dropna(axis=0,how='any',inplace=True)
#dataset2 = read_data(path_test)
#dataset1.describe(percentiles=[.05,.25,.75,.95,.99],include='all').to_csv(path+'describe.csv')
#dataset1.describe(percentiles=[.05,.25,.75,.95,.99],include='all')
#dataset1.info(verbose=True,null_counts=True)

"""""""""""""""""""""""""""""""""""""""""""""""""""
      process data
"""""""""""""""""""""""""""""""""""""""""""""""""""
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
        }

dataset1.fillna(mean_dict,inplace=True)

mean_temp_dict={
         'roomservice_2_lastord':dataset1['roomservice_2_lastord'].mean()
        ,'roomservice_3_lastord':dataset1['roomservice_3_lastord'].mean()
        ,'roomservice_4_lastord':dataset1['roomservice_4_lastord'].mean()
        ,'roomservice_5_lastord':dataset1['roomservice_5_lastord'].mean()
        ,'roomservice_6_lastord':dataset1['roomservice_6_lastord'].mean()
        ,'roomservice_8_lastord':dataset1['roomservice_8_lastord'].mean()
        ,'roomtag_3_lastord':dataset1['roomtag_3_lastord'].mean()
        ,'roomtag_4_lastord':dataset1['roomtag_4_lastord'].mean()
        ,'roomtag_5_lastord':dataset1['roomtag_5_lastord'].mean()
        ,'roomtag_6_lastord':dataset1['roomtag_6_lastord'].mean()
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
zeroone_arr=[
        'roomtag_2'
        ,'roomtag_2_lastord'
        ]

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
#与过去平均面积的差距	distance_avg_roomarea
dataset1['distance_avg_roomarea'] = dataset1['avg_roomarea'] - dataset1['user_avgroomnum']
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
"""
        对定性特征哑编码
"""
#哑编码，对IRIS数据集的目标值，返回值为哑编码后的数据
from sklearn.preprocessing import OneHotEncoder
#enc = OneHotEncoder(categorical_features=[0,1],n_values=[3,4],sparse=False)
enc = OneHotEncoder(categorical_features='all',n_values='auto',sparse=False)

onehot_arr=[
         'roomservice_1'
        ,'roomservice_2'
        ,'roomservice_3'
        ,'roomservice_4'
        ,'roomservice_5'
        ,'roomservice_6'
        ,'roomservice_7'
        ,'roomservice_8'
        ,'roomtag_1'
        ,'roomtag_4'
        ,'roomtag_5'
        ]
dataset1_list = dataset1[onehot_arr]

enc.fit(dataset1_list.values)
dataset1_t = enc.transform(dataset1_list.values)


dataset1.drop(onehot_arr,axis=1,inplace=True)

dataset1 = pd.concat([dataset1,pd.DataFrame(dataset1_t)],axis=1)

del dataset1_list
del dataset1_t

"""""""""""""""""""""""""""""""""""""""""""""""""""
      predict
"""""""""""""""""""""""""""""""""""""""""""""""""""
dataset1.fillna(0,inplace=True)

select_features = [
 'star'
,'rank'
,'returnvalue'
,'price_deduct'
,'basic_minarea'
,'basic_maxarea'
,'roomtag_2'
,'roomtag_3'
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
,'roomservice_3_lastord'
,'roomservice_4_lastord'
,'roomservice_5_lastord'
,'roomservice_6_lastord'
,'roomservice_8_lastord'
,'roomtag_2_lastord'
,'roomtag_3_lastord'
,'roomtag_4_lastord'
,'roomtag_5_lastord'
,'roomtag_6_lastord'
,'star_lastord'
,'hotel_minprice_lastord'
,'basic_minprice_lastord'
,'order_index'
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
,'distance_avg_roomarea'
,'distance_avg_price'
,'distance_avg_holiday_price'
,'distance_avg_workday_price'
,'between_max_min'
,'distance_avg_rank'
,'distance_last_rank'
,'date_from_last'
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
        ]

trainX = dataset1.ix[:100000,select_features].reset_index(drop=True)
trainY = dataset1.ix[:100000,'orderlabel'].reset_index(drop=True)
#trainY = trainX[['orderlabel']]

testX = dataset1.ix[100000:200000,select_features].reset_index(drop=True)
testY = dataset1.ix[100000:200000,'orderlabel'].reset_index(drop=True)

compare_train = dataset1.ix[:100000,['orderid','roomid','orderlabel']].reset_index(drop=True)
result_train = compare_train.ix[compare_train['orderlabel']==1,['orderid','roomid']].reset_index(drop=True)
compare_train.drop('orderlabel',axis=1,inplace=True)

compare_test = dataset1.ix[100000:200000,['orderid','roomid','orderlabel']].reset_index(drop=True)
result_test = compare_test.ix[compare_test['orderlabel']==1,['orderid','roomid']].reset_index(drop=True)
compare_test.drop('orderlabel',axis=1,inplace=True)

#compare_train = trainX[['orderid','roomid']]
#result_train = trainX.ix[trainX['orderlabel']==1,['orderid','roomid']]
#
#compare_test = testX[['orderid','roomid']]
#result_test = testX.ix[testX['orderlabel']==1,['orderid','roomid']]


#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#sc.fit(trainX)
#trainX_std = sc.transform(trainX)
#testX_std = sc.transform(testX)

#from sklearn.preprocessing import Normalizer
#sc = Normalizer()
#sc.fit(trainX)
#trainX_std = sc.transform(trainX)
#testX_std = sc.transform(testX)


def printScore(compare,result,predict):
    combine = pd.concat([compare,pd.DataFrame(predict[:,1])],axis=1)
    maxr = combine.loc[combine.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax())]
    maxr = pd.merge(maxr,result,on=['orderid'])
    print(len(maxr[maxr['roomid_x']==maxr['roomid_y']])/len(maxr))
    del combine
    del maxr
    


from sklearn.ensemble import GradientBoostingClassifier
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation,metrics
param_test1={'n_estimators':range(20,81,10)}
param_test1={'n_estimators':range(20,81,10)}
gsearch1 = GridSearchCV(
        estimator =  GradientBoostingClassifier(
                      learning_rate=0.1,max_features='sqrt',
                      criterion='friedman_mse', init=None,
                      loss='deviance', max_depth=3,
                      max_leaf_nodes=None,
                      min_impurity_split=1e-07, min_samples_leaf=1,
                      min_samples_split=2, min_weight_fraction_leaf=0.0,
                      presort='auto', random_state=None,
                      subsample=1.0, verbose=0, warm_start=False),
        param_grid=param_test1,scoring='roc_auc',iid=False,cv=5)
gsearch1.fit(trainX,trainY.values.ravel())

gsearch1.grid_scores_,gsearch1.best_estimator_,gsearch1.best_score_

#gbc = GradientBoostingClassifier(criterion='friedman_mse', init=None,
#              learning_rate=0.1, loss='deviance', max_depth=3,
#              max_features='sqrt', max_leaf_nodes=None,
#              min_impurity_split=1e-07, min_samples_leaf=1,
#              min_samples_split=2, min_weight_fraction_leaf=0.0,
#              n_estimators=200, presort='auto', random_state=None,
#              subsample=1.0, verbose=0, warm_start=False)
#gbc.fit(trainX,trainY.values.ravel())
#predict_train = gbc.predict_proba(trainX)
#predict_test = gbc.predict_proba(testX)
#printScore(compare_train,result_train,predict_train)
#printScore(compare_test,result_test,predict_test)



#from sklearn.linear_model import LogisticRegression
#lr = LogisticRegression(C=1, random_state=0,class_weight='balanced')
#lr.fit(trainX_std,trainY.values.ravel())
#
#predict_train1 = lr.predict_proba(trainX_std)
#predict_test1 = lr.predict_proba(testX_std)
#
#
#
#printScore(compare_train,result_train,predict_train1)
#printScore(compare_test,result_test,predict_test1)
#
#
#
#from sklearn.ensemble import RandomForestClassifier
#clf = RandomForestClassifier(n_estimators=1000)
#clf.fit(trainX,trainY.values.ravel())
#
#predict_train2 = clf.predict_proba(trainX)
#predict_test2 = clf.predict_proba(testX)
#
#printScore(compare_train,result_train,predict_train2)
#printScore(compare_test,result_test,predict_test2)
#
#
#
#
#from sklearn.ensemble import AdaBoostClassifier
#from sklearn.tree import DecisionTreeClassifier
#abc = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),algorithm="SAMME",n_estimators=200)
#abc.fit(trainX_std,trainY.values.ravel())
#
#predict_train3 = abc.predict_proba(trainX_std)
#predict_test3 = abc.predict_proba(testX_std)
#
#
#
#printScore(compare_train,result_train,predict_train3)
#printScore(compare_test,result_test,predict_test3)
#
#
#predict_test_total = predict_test1[:,1]+predict_test2[:,1]+predict_test3[:,1]
#total_test = pd.concat([compare_train,pd.DataFrame(predict_test_total)],axis=1)