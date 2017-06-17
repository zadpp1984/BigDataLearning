# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 21:23:30 2017

@author: Chenanyun
"""
import pandas as pd
import xgboost as xgb

def printScore(compare,result,predict):
    combine = pd.concat([compare,pd.DataFrame(predict)],axis=1)
    maxr = combine.loc[combine.groupby('orderid',as_index=False).apply(lambda x:x[0].argmax())]
    maxr = pd.merge(maxr,result,on=['orderid'])
    print len(maxr[maxr['roomid_x']==maxr['roomid_y']])/float(len(maxr))

def read_data(file):
    
    with open(file, 'r') as f:
        columns = f.readline().strip('\n').split(',') 
    
    dataset = pd.DataFrame()
    file_handler = pd.read_table(file,
                                 sep=',',
                                 
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

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\temp\\'

i=10
index=2

Y1 = read_data(path+'preprocessed_train_Y'+str(i)+'_'+str(index)+'.csv').values.ravel()
dataset1 = read_data(path+'preprocessed_train'+str(i)+'_'+str(index)+'.csv')


dataset2 = read_data(path+'preprocessed_test.csv')

#xg_train = xgb.DMatrix(dataset1.drop(['order_price_index','basicroom_price_index','basicroom_rank_index'],axis=1).values, label=Y1.ravel())
#xg_test = xgb.DMatrix(dataset2.drop(['order_price_index','basicroom_price_index','basicroom_rank_index'],axis=1).values)


drop_list=[
            'confirmtime_positive'
            ,'advanceddate_positive'
            ,'roomservice_3_123'
            ,'roomservice_8_345'
            ,'total_service_num'
            ,'total_tag_num'
            ,'order_price_index'
            ,'basicroom_price_index'
            ,'basicroom_rank_index'
        ]
xg_train = xgb.DMatrix(dataset1.drop(drop_list,axis=1).values, label=Y1.ravel())
xg_test = xgb.DMatrix(dataset2.drop(drop_list,axis=1).values)


#xg_train = xgb.DMatrix(dataset1.values, label=Y1.ravel())
#xg_test = xgb.DMatrix(dataset2.values)

compare_test = read_data(path+'preprocessed_test_compare.csv')
result_test = compare_test.ix[compare_test['orderlabel']==1,['orderid','roomid']]



##num_round = 140
num_round = 160
param = {
        'booster':'gbtree',
        'objective':'binary:logistic',
        'eval_metric':'auc',
        'bst:eta':0.3,
        'bst:max_depth':3,
#        'subsample':0.8, #从数据集中选择数据的比例
#        'colsample_bytree':0.7, #建立树时对特征随即采样的比例
#        'min_child_weight':5,
#        'max_delta_step':1,  #通常不被调查
        'scale_pos_weight':0.9,
#        'gamma':1,
#        'lambda':300,
        'silent':0
        
        }
watchlist = [(xg_train,'train')]
plst = param.items()
bst = xgb.train(plst, xg_train, num_round ,evals=watchlist)
predict_test = bst.predict(xg_test) 
printScore(compare_test,result_test,predict_test)

#xgb.plot_importance(bst,max_num_features=100)
#xgb.plot_tree(bst)
#bst.get_fscore()
#bst.get_score()
#bst.get_split_value_histogram('f80')
#bst.attributes()
bst.save_model('xgboost10_2.model')
#bst.save_model('xgboost11_2.model')
#bst.save_model('xgboost.model')






