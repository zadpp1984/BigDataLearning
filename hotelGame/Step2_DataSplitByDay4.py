# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:20:35 2017

@author: Chenanyun
"""
import numpy as np

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\temp\\'

#path_train = path+'competition_train.txt'
#path_train = path+'train_1_sorted.csv'
path_train = path+'train_3_sorted.csv'

path_train_list = [
#        path+'train_1_sorted.csv'
        path+'train_2_sorted.csv'
#       ,path+'train_3_sorted.csv'
#       ,path+'train_4_sorted.csv'
       ,path+'train_5_sorted.csv'
       ,path+'train_6_sorted.csv'
       ,path+'train_7_sorted.csv'
        ]


zeronum = 10
index =4
path_out = path+'train_total'+str(zeronum)+'_'+str(index)+'.csv';
#path_train = path+'competition_test.txt'
#path_out = path+'temp\\test_';

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

jump = ['2013-04-19','2013-04-20']

date_arr = date_train

f = open(path_train, 'r',buffering=4096000)
line = f.readline().strip('\n')

fout = open(path_out,'w',buffering=4096000)
fout.write(line+'\n')

orderid = ''
lastorderid = ''
sameorders=[]
r_l=''

def writeout(orders,num,label):
    words = label.split('\t')
    if len(words) < 2 :
        print orders
        print label
    if words[2] not in jump:
        orderlen = len(orders)
        if orderlen <= num:
            fout.write(label+'\n')
            fout.writelines(orders)
        else:
            np.random.shuffle(orders)
            fout.write(label+'\n')
            fout.writelines(orders[0:num])
    

line = f.readline().strip('\n')
#line = f.readline().strip('\n')
num_line = 0
#while num_line < 1000 and line:
while line:
    num_line += 1
    words = line.split('\t')
    orderid = words[0]
    orderlabel = words[6]
    if orderid == lastorderid:
        pass
    else:
        if num_line!=1:
            writeout(sameorders,zeronum,r_l)
            sameorders = []
            r_l=''
    if orderlabel == '1':
        r_l = line
    else:
        sameorders.append(line+'\n')
    
    lastorderid = orderid
    if num_line % 10000 ==0:
        print(num_line)
    line = f.readline().strip('\n')
    
writeout(sameorders,zeronum,r_l)
sameorders = []
r_l=''
f.close()

new_num_line = 0
for p in path_train_list:
    f = open(p, 'r',buffering=4096000)
    line = f.readline().strip('\n')
    line = f.readline().strip('\n')
    while line:
        num_line += 1
        words = line.split('\t')
        orderid = words[0]
        orderlabel = words[6]
        if orderid == lastorderid:
            pass
        else:
            if new_num_line == 0:
                new_num_line =1
            else:
                writeout(sameorders,zeronum,r_l)
                sameorders=[]
                r_l=''
        if orderlabel == '1':
            r_l = line
        else:
            sameorders.append(line+'\n')
        
        lastorderid = orderid
        if num_line % 10000 ==0:
            print(num_line)
        line = f.readline().strip('\n')
    f.close()



fout.close()