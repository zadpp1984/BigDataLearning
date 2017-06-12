# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:43:05 2017

@author: Chenanyun
"""


import pandas as pd

path = 'F:\\MyPython\\resource\\ctrip\\'
#path = 'E:\\cay\\resource\\temp\\'

#path_train = path+'competition_train.txt'
#path_out = path+'train_';
path_train = path+'competition_test.txt'
path_out = path+'test_';

date_train = ['2013-04-14',
              '2013-04-15',
              '2013-04-16',
              '2013-04-17',
              '2013-04-18',
              '2013-04-19',
              '2013-04-20']
date_test = ['2013-04-21',
              '2013-04-22',
              '2013-04-23',
              '2013-04-24',
              '2013-04-25',
              '2013-04-26',
              '2013-04-27']


date_arr = date_test

f = open(path_train, 'r',buffering=4096000)
line = f.readline()

fout_list = []
for i in [1,2,3,4,5,6,7]:
    fout = open(path_out+str(i)+'.csv','w',buffering=4096000)
    fout.write(line)
    fout_list.append(fout)

num_line = 0
#while num_line < 10000 and line:
while line:
    num_line += 1
    line = f.readline()
    if line:
        words = line.split('\t')
        fout = fout_list[date_arr.index(words[2])]
        fout.write(line)
        if num_line % 10000 ==0:
            print(num_line)

f.close()
for i in [1,2,3,4,5,6,7]:
    fout = fout_list[i-1]
    fout.close()