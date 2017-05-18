# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:36:30 2017

@author: Chenanyun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename='F:\\MyPython\\resource\\ctrip\\competition_train.txt'

#with open(filename, 'r') as f:
#    columns = f.readline().strip('\n').split('\t') 
#columns[:5]

f = open(filename, 'r')
line = f.readline().strip('\n')
columns = line.split('\t') 
datas = pd.DataFrame(columns=columns); 

num_line = 0
while num_line < 10000 and line:
    num_line += 1
    line = f.readline().strip('\n')
    row = pd.DataFrame([line.split('\t')], columns=columns)
    datas = datas.append(row)
    
print(datas.head())

# 一万条数据中成交的订单数
print(len(datas[datas.orderlabel== '1']))

#将object类型转换成float  否则无法画图
datas.price_deduct = datas.price_deduct.apply(lambda x: float(x))

import matplotlib.pyplot as plt
%matplotlib inline
plt.hist(datas[datas.orderlabel== '1'].price_deduct.values, bins=20, alpha=0.5)
plt.xlabel('price_deduct')
plt.ylabel('num')

plt.hist([float(i) for i in datas[(datas.orderlabel== '1') & (datas.price_deduct < 8000)].price_deduct.values], bins=50, alpha=0.5)
plt.xlabel('price_deduct')
plt.ylabel('num')


