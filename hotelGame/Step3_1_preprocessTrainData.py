@@ -0,0 +1,237 @@
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:09:03 2017

@author: Chenanyun
"""
import pandas as pd
import numpy as np
import DataPrepare as DP

path = 'F:\\MyPython\\resource\\ctrip\\'
#path = 'E:\\cay\\resource\\temp\\'

#path_train = path+'train_1.csv'
#path_train = path+'train_1_sorted.csv'
path_train = path+'train_total.csv'
#path_test = path+'test_1.csv'


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
dataset1 = DP.prepareData(dataset1)
#dataset1.dropna(axis=1,how='all',inplace=True)
#dataset1.dropna(axis=0,how='any',inplace=True)
#dataset2 = read_data(path_test)
#dataset1.describe(percentiles=[.05,.25,.75,.95,.99],include='all').to_csv(path+'describe.csv')
#dataset1.describe(percentiles=[.05,.25,.75,.95,.99],include='all')
#dataset1.info(verbose=True,null_counts=True)


"""""""""""""""""""""""""""""""""""""""""""""""""""
      predict
"""""""""""""""""""""""""""""""""""""""""""""""""""

#room_order_num=pd.read_csv(path+'room_order_num.csv')
#basicroom_order_num=pd.read_csv(path+'basicroom_order_num.csv')
#hotel_order_num=pd.read_csv(path+'hotel_order_num.csv')
#room_order_num.columns=['roomid','room_order_num']
#basicroom_order_num.columns=['basicroomid','basicroom_order_num']
#hotel_order_num.columns=['hotelid','hotel_order_num']
#
#dataset1 = pd.merge(dataset1, room_order_num, on='roomid',how='left')
#dataset1 = pd.merge(dataset1, basicroom_order_num, on='basicroomid',how='left')
#dataset1 = pd.merge(dataset1, hotel_order_num, on='hotelid',how='left')


dataset1.fillna(0,inplace=True)

dataset1[DP.select_features1].to_csv('preprocessed_train.csv',index=False)
dataset1[['orderlabel']].to_csv('preprocessed_train_Y.csv',index=False)

#trainY = dataset1['orderlabel']
#dataset1 = dataset1[select_features]
#
#
##compare_train = trainX[['orderid','roomid']]
##result_train = trainX.ix[trainX['orderlabel']==1,['orderid','roomid']]
##
##compare_test = testX[['orderid','roomid']]
##result_test = testX.ix[testX['orderlabel']==1,['orderid','roomid']]
#
#
##from sklearn.preprocessing import StandardScaler
##sc = StandardScaler()
##sc.fit(trainX)
##trainX_std = sc.transform(trainX)
##testX_std = sc.transform(testX)
#
##from sklearn.preprocessing import Normalizer
##sc = Normalizer()
##sc.fit(trainX)
##trainX_std = sc.transform(trainX)
##testX_std = sc.transform(testX)
#
#
##def printScore(compare,result,predict):
###    combine = pd.concat([compare,pd.DataFrame(predict[:,1])],axis=1)
##    combine = pd.concat([compare,pd.DataFrame(predict)],axis=1)
##    maxr = combine.loc[combine.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax())]
##    maxr = pd.merge(maxr,result,on=['orderid'])
##    print(len(maxr[maxr['roomid_x']==maxr['roomid_y']])/len(maxr))
##    
#
#
#
#import xgboost as xgb
#param = {'bst:max_depth':5, 'bst:eta':0.3, 'silent':1, 'objective':'binary:logistic' }
##param['nthread'] = 4
#plst = param.items()
##plst += [('eval_metric', 'auc')] # Multiple evals can be handled in this way
##plst += [('eval_metric', 'ams@0')]
##evallist  = [(trainY.values.ravel(),'eval'), (dataset1.values,'train')]
#num_round = 10
#xg_train = xgb.DMatrix( dataset1.values, label=trainY)
##bst = xgb.train( plst, xg_train, num_round, evallist )
#bst = xgb.train( plst, xg_train, num_round )
#
#bst.save_model('0001.model')

#preds2 = bst.predict(xg_train,ntree_limit=bst.best_iteration)  
#
#compare_train = dataset1[['orderid','roomid']]
#result_train = dataset1.ix[dataset1['orderlabel']==1,['orderid','roomid']]
#del dataset1
#
#combine = pd.concat([compare_train,pd.DataFrame(preds2)],axis=1)
#maxr = combine.loc[combine.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax())]
#maxr = pd.merge(maxr,result_train,on=['orderid'])
#x = len(maxr[maxr['roomid_x']==maxr['roomid_y']])/float(len(maxr))
#print x
#
#printScore(compare_train,result_train,preds2)
"""""""""""""""""""""""""""""""""""""""""""""""""""
      gbdt
"""""""""""""""""""""""""""""""""""""""""""""""""""

#from sklearn.ensemble import GradientBoostingClassifier
#
##from sklearn.grid_search import GridSearchCV
##from sklearn import cross_validation,metrics
##param_test1={'n_estimators':[80,90,100,110,120,130,140]}
##param_test2 = {'max_depth':[3,5,7,9,11], 'min_samples_split':[100,300,500,700]}
##gsearch1 = GridSearchCV(
##        estimator =  GradientBoostingClassifier(
##                      n_estimators = 120,
##                      learning_rate=0.1,max_features='sqrt',
##                      criterion='friedman_mse', init=None,
##                      loss='deviance', max_depth=3,
##                      max_leaf_nodes=None,
##                      min_impurity_split=1e-07, min_samples_leaf=1,
##                      min_samples_split=2, min_weight_fraction_leaf=0.0,
##                      presort='auto', random_state=None,
##                      subsample=1.0, verbose=0, warm_start=False),
##        param_grid=param_test2,scoring='roc_auc',iid=False,cv=5)
##gsearch1.fit(trainX,trainY.values.ravel())
##gsearch1.grid_scores_,gsearch1.best_estimator_,gsearch1.best_score_
#
#
#gbc = GradientBoostingClassifier(
#              n_estimators=120, learning_rate=0.1,
#              max_depth=9, min_samples_split=100, min_samples_leaf=5, max_leaf_nodes=None,
#              max_features='sqrt',
#              subsample=1.0,
#              loss='deviance', criterion='friedman_mse', init=None,
#              min_impurity_split=1e-07, min_weight_fraction_leaf=0.0,
#              presort='auto', random_state=None,
#               verbose=0, warm_start=False)
#gbc.fit(dataset1,trainY.values.ravel())
##predict_train = gbc.predict_proba(trainX)
##predict_test = gbc.predict_proba(testX)
##printScore(compare_train,result_train,predict_train)
##printScore(compare_test,result_test,predict_test)
#
#from sklearn.externals.joblib import dump,load
##持久化数据
##第一个参数为内存中的对象
##第二个参数为保存在文件系统中的名称
##第三个参数为压缩级别，0为不压缩，3为合适的压缩级别
#dump(gbc, 'gbc_total.dmp', compress=3)
##从文件系统中加载数据到内存中
##gbc = load('gbc.dmp')



"""""""""""""""""""""""""""""""""""""""""""""""""""
      logistic
"""""""""""""""""""""""""""""""""""""""""""""""""""

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
"""""""""""""""""""""""""""""""""""""""""""""""""""
      RandomForest
"""""""""""""""""""""""""""""""""""""""""""""""""""
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
"""""""""""""""""""""""""""""""""""""""""""""""""""
      AdaBoost
"""""""""""""""""""""""""""""""""""""""""""""""""""
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
