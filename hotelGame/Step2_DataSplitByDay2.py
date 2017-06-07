# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:26:22 2017

@author: Chenanyun
"""


import pandas as pd

path = 'F:\\MyPython\\resource\\ctrip\\'
#path = 'E:\\cay\\resource\\'

path_train = path+'competition_train.txt'
#path_train = path+'competition_test.txt'
path_out = path+'train_';

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

date_arr = date_train

f = open(path_train, 'r',buffering=1024000)
line = f.readline().strip('\n')

#fout_list = []
#for i in [1,2,3,4,5,6,7]:
#    fout = open(path_out+str(i)+'.csv','w')
#    fout.write(line+'\n')
#    fout_list.append(fout)
f1 = open(path_out+'01.csv','w',buffering=1024000)
f2 = open(path_out+'02.csv','w',buffering=1024000)
f3 = open(path_out+'03.csv','w',buffering=1024000)
f4 = open(path_out+'04.csv','w',buffering=1024000)
f5 = open(path_out+'05.csv','w',buffering=1024000)
f6 = open(path_out+'06.csv','w',buffering=1024000)
f7 = open(path_out+'07.csv','w',buffering=1024000)


num_line = 0
while line:
    num_line += 1
    line = f.readline().strip('\n')
    words = line.split('\t')
#    fout = fout_list[date_arr.index(words[2])]
#    fout.write(line+'\n')
    if words[2] == date_arr[0]:
        f1.write(line+'\n')
    elif words[2] == date_arr[1]:
        f2.write(line+'\n')
    elif words[2] == date_arr[2]:
        f3.write(line+'\n')
    elif words[2] == date_arr[3]:
        f4.write(line+'\n')
    elif words[2] == date_arr[4]:
        f5.write(line+'\n')
    elif words[2] == date_arr[5]:
        f6.write(line+'\n')
    elif words[2] == date_arr[6]:
        f7.write(line+'\n')
    else:
        print ('error')
    if num_line % 10000 ==0:
        print(num_line)

f.close()
#for i in [1,2,3,4,5,6,7]:
#    fout = fout_list[i-1]
#    fout.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
