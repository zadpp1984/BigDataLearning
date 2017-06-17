# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:52:11 2017

@author: user
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

i=8

Y1 = read_data(path+'preprocessed_train_Y'+str(i)+'.csv').values.ravel()
dataset1 = read_data(path+'preprocessed_train'+str(i)+'.csv').values
dataset2 = read_data(path+'preprocessed_test.csv').values
compare_test = read_data(path+'preprocessed_test_compare.csv')
result_test = compare_test.ix[compare_test['orderlabel']==1,['orderid','roomid']]


"""""""""""""""""""""""""""""""""""""""""""""""""""
      RandomForest
"""""""""""""""""""""""""""""""""""""""""""""""""""
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=1000)
clf.fit(dataset1,Y1)

#predict_train2 = clf.predict_proba(dataset1)
predict_test2 = clf.predict_proba(dataset2)

printScore(compare_test,result_test,predict_test2[:,1])






#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#sc.fit(dataset1)
#trainX_std = sc.transform(dataset1)
#testX_std = sc.transform(dataset2)
#
#
#from sklearn.linear_model import LogisticRegression
#lr = LogisticRegression(C=1, random_state=0,class_weight='balanced')
#lr.fit(trainX_std,Y1)
#
#predict_train1 = (lr.predict_proba(trainX_std))[:,1]
#predict_test1 = (lr.predict_proba(testX_std))[:,1]


#printScore(compare_test,result_test,predict_test1)



#bst.save_model('xgboost.model')