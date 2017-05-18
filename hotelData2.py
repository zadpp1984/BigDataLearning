# -*- coding: utf-8 -*-
"""
Created on Wed May 17 23:55:20 2017

@author: Chenanyun
"""
#path_train, path_test = ['../input/ctrip/' + x for x in os.listdir('../input/ctrip')]

import pandas as pd

path_train = 'F:\\MyPython\\resource\\ctrip\\competition_train.txt'
usecols='orderid uid orderlabel star returnvalue price_deduct'.split()
#x_train是读取块，循环是对读取块的遍历
x_train = pd.read_table(path_train,sep='\t',chunksize=100000,usecols=usecols,low_memory=False)
orderid, uid = [],[]
data_order = pd.DataFrame()
total_train,j = 0,1
for data_i in x_train:
    data_temp = data_i[data_i.orderlabel==1]
    data_order = pd.concat((data_order,data_temp),axis=0,ignore_index=True)
    orderid.extend(data_i.orderid.unique())
    uid.extend(data_i.uid.unique())
    total_train += data_i.shape[0]
    print(j,end=',')
    j+=1
order_num = len(set(orderid))
u_num = len(set(uid))
print('\n\n训练集一共有{}条记录，{}份订单,{}个用户，成功预订{}份订单'.format(total_train,order_num,u_num,data_order.shape[0]))

print(type(x_train))


from matplotlib import pyplot as plt
plt.hist(data_order.price_deduct.values); plt.show()




hist_data = data_order.price_deduct.values
hist_data = hist_data[hist_data<5000]
plt.figure(figsize=(12,5))
plt.hist(hist_data,bins=100,)
plt.show()



plt.hist(data_order.star.values); plt.show()