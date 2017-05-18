# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:06:56 2017

@author: Chenanyun
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
from matplotlib import pyplot as plt

path_train = 'E:\\cay\\resource\\competition_train.txt'
usecols='uid orderlabel hotelid basicroomid roomid star rank returnvalue price_deduct basic_minarea basic_maxarea roomservice_1 roomservice_2 roomservice_3 roomservice_4 roomservice_5 roomservice_6 roomservice_7 roomservice_8 roomtag_1 roomtag_2 roomtag_3 roomtag_4 roomtag_5 roomtag_6 basic_week_ordernum_ratio basic_recent3_ordernum_ratio basic_comment_ratio basic_30days_ordnumratio basic_30days_realratio room_30days_ordnumratio room_30days_realratio '.split()
#x_train是读取块，循环是对读取块的遍历
x_train = pd.read_table(path_train,sep='\t',chunksize=100000,usecols=usecols,low_memory=False)
data_hotel = pd.DataFrame()
total_train,j = 0,1
for data_i in x_train:
    data_hotel = pd.concat((data_hotel,data_i),axis=0,ignore_index=True)
    total_train += data_i.shape[0]
    print(j,end=',')
    j+=1
    if total_train >= 1000000:
        break 
print(total_train)

datacopy = data_hotel.copy()
datacopy.head()
datacopy.dropna(axis=1)
datacopy.describe()
data_hotel.describe()

datacopy = datacopy.fillna(0)
datacopy = datacopy.dropna()

datacopy100 = data_hotel.head(100)
#datacopy100 = datacopy100.iloc[:,4:]
datacopy100 = datacopy100.dropna()


datacopy100.describe()
datacopy100.dtypes

#
from sklearn import preprocessing
datacopy_np = datacopy.ix[:,5:].values
X_scaled = preprocessing.scale(datacopy_np)
print(X_scaled[1:5])
myFA(X_scaled)
myPCA(X_scaled)


from sklearn import decomposition
#FactorAnalysis FA
def myFA(scaledData):
    pca = decomposition.FactorAnalysis(n_components=2)
    X = pca.fit_transform(scaledData)
    pos = pd.DataFrame()
    pos['X'] = X[:,0]
    pos['Y'] = X[:,1]
    
    ax = pos.plot(kind='scatter',x='X',y='Y',color='blue',label='0')
#    ax = pos.ix[pos['type']==0].plot(kind='scatter',x='X',y='Y',color='blue',label='0')
#    ax = pos.ix[pos['type']==1].plot(kind='scatter',x='X',y='Y',color='red',label='1',ax=ax)
    pos.head()

#PCA
def myPCA(scaledData):
    pca = decomposition.PCA(n_components=2)
    X = pca.fit_transform(scaledData)
    pos = pd.DataFrame()
    pos['X'] = X[:,0]
    pos['Y'] = X[:,1]
    
    ax = pos.plot(kind='scatter',x='X',y='Y',color='blue',label='0')
#    ax1 = pos1.ix[pos1['type']==0].plot(kind='scatter',x='X',y='Y',color='blue',label='0')
#    ax2 = pos1.ix[pos1['type']==1].plot(kind='scatter',x='X',y='Y',color='red',label='1')
    pos.head()


#ICA
pca2 = decomposition.FastICA(n_components=2)
X2 = pca2.fit_transform(datacopy100.ix[:,5:].values)
pos2 = pd.DataFrame()
pos2['X'] = X2[:,0]
pos2['Y'] = X2[:,1]
pos2['type'] = datacopy100['orderlabel']

ax3 = pos2.ix[pos2['type']==0].plot(kind='scatter',x='X',y='Y',color='blue',label='0')
ax4 = pos2.ix[pos2['type']==1].plot(kind='scatter',x='X',y='Y',color='red',label='1')

pos2.head()



#MDS
from sklearn import manifold
from sklearn.metrics import euclidean_distances
similarities = euclidean_distances(datacopy100.ix[:,5:].values)
mds = manifold.MDS(n_components=2,max_iter=3000,eps=1e-9,dissimilarity="precomputed",n_jobs=1)
XX = mds.fit(similarities).embedding_

pos3 = pd.DataFrame(XX,columns=['X','Y'])
pos3['X'] = XX[:,0]
pos3['Y'] = XX[:,1]
pos3['type'] = datacopy100['orderlabel']

ax5 = pos2.ix[pos2['type']==0].plot(kind='scatter',x='X',y='Y',color='blue',label='0')
ax6 = pos2.ix[pos2['type']==1].plot(kind='scatter',x='X',y='Y',color='red',label='1')

pos3.head()
# see data
#from pandas.tools.plotting import andrews_curves
#from pandas.tools.plotting import radviz
#plt.figure()
#andrews_curves(datacopy100,'orderlabel')
#radviz(datacopy100,'orderlabel')


#
##pandas DataFrame -> numpy ndarray
#data_hotel_np = data_hotel.values
#type(data_hotel)
#type(data_hotel_np)
#
#
##numric data select
#data_hotel_np_temp = data_hotel_np[:,4:]
#print (data_hotel_np_temp)
#
## nan
#imp = Imputer(missing_values="NaN",strategy="mean",axis=0)
#print(imp.transform(data_hotel_np_temp))
#
