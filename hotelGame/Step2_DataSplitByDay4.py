@@ -0,0 +1,136 @@
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:20:35 2017

@author: Chenanyun
"""
import numpy as np

path = 'F:\\MyPython\\resource\\ctrip\\'
#path = 'E:\\cay\\resource\\'

#path_train = path+'competition_train.txt'
path_train = path+'train_1_sorted.csv'

path_train_list = [
#        path+'train_1_sorted.csv'
       path+'train_2_sorted.csv'
       ,path+'train_3_sorted.csv'
       ,path+'train_4_sorted.csv'
       ,path+'train_5_sorted.csv'
        ]


path_out = path+'train_total.csv';
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
line += '	order_index'

fout = open(path_out,'w',buffering=4096000)
fout.write(line+'\n')

orderid = ''
lastorderid = ''
order_index =0
sameorders=[]
r_l=''
zeronum = 3
def addindex():
    addstr = '	'+str(order_index)
    return addstr

def writeout(orders,num,label):
    words = label.split('\t')
    if words[2] not in jump:
        orderlen = len(orders)
        if orderlen <= num:
            fout.write(label+'\n')
            fout.writelines(orders)
        else:
            orders = np.random.shuffle(orders)
            fout.write(label+'\n')
            fout.writelines(sameorders[0:num])
    

line = f.readline().strip('\n')
line = f.readline().strip('\n')
num_line = 0
#while num_line < 1000 and line:
while line:
    num_line += 1
    words = line.split('\t')
    orderid = words[0]
    orderlabel = words[6]
    if orderid == lastorderid:
        order_index += 1
    else:
        if num_line!=1:
            writeout(sameorders,zeronum,r_l)
            sameorders.clear()
            r_l=''
        order_index = 1
    line += addindex()
    if orderlabel == '1':
        r_l = line
    else:
        sameorders.append(line+'\n')
    
    lastorderid = orderid
    if num_line % 10000 ==0:
        print(num_line)
    line = f.readline().strip('\n')
    
f.close()

for p in path_train_list:
    f = open(p, 'r',buffering=4096000)
    line = f.readline().strip('\n')
    while line:
        num_line += 1
        words = line.split('\t')
        orderid = words[0]
        orderlabel = words[6]
        if orderid == lastorderid:
            order_index += 1
        else:
            writeout(sameorders,zeronum,r_l)
            sameorders.clear()
            r_l=''
            order_index = 1
        line += addindex()
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