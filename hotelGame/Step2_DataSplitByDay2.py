# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:26:22 2017

@author: Chenanyun
"""


import pandas as pd

#path = 'F:\\MyPython\\resource\\ctrip\\'
path = 'E:\\cay\\resource\\'

path_train = path+'competition_train.txt'
path_out = path+'temp\\train_';
#path_train = path+'competition_test.txt'
#path_out = path+'test_';

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

f = open(path_train, 'r',buffering=4096000)
line = f.readline().strip('\n')
line += '	order_index	hotel_order_index	basicroom_hotel_index	basicroom_order_index	room_hotel_index	room_basicroom_index'

fout_list = []
for i in [1,2,3,4,5,6,7]:
    fout = open(path_out+str(i)+'.csv','w')
    fout.write(line+'\n')
    fout_list.append(fout)


orderid = hotelid = basicroomid = roomid = ''
lastorderid = lasthotelid = lastbasicroomid = lastroomid = ''

order_index =0
hotel_order_index =0
basicroom_hotel_index = 0
basicroom_order_index = 0
room_hotel_index = 0
room_basicroom_index =  0

def addindex():
    addstr = '	'+str(order_index)
    addstr +='	'+str(hotel_order_index)
    addstr +='	'+str(basicroom_hotel_index)
    addstr +='	'+str(basicroom_order_index)
    addstr +='	'+str(room_hotel_index)
    addstr +='	'+str(room_basicroom_index)
    return addstr

num_line = 0
while num_line < 10000 and line:
#while line:
    num_line += 1
    line = f.readline().strip('\n')
    if line:
        words = line.split('\t')
        orderid = words[0]
        hotelid = words[3]
        basicroomid = words[4]
        roomid = words[5]
        if orderid != lastorderid:
            order_index = 1
            hotel_order_index = 1
            basicroom_hotel_index = 1
            basicroom_order_index = 1
            room_hotel_index= 1
            room_basicroom_index=1
        else:
            order_index += 1
            if hotelid != lasthotelid:
                hotel_order_index += 1
                basicroom_order_index += 1
                basicroom_hotel_index = 1
                room_hotel_index = 1
                room_basicroom_index = 1
            else:
                room_hotel_index += 1
                if basicroomid != lastbasicroomid:
                    basicroom_order_index += 1
                    basicroom_hotel_index += 1
                    room_basicroom_index = 1
                else:
                    room_basicroom_index += 1
        line += addindex()
        
        lastorderid = orderid
        lasthotelid = hotelid
        lastbasicroomid = basicroomid
        lastroomid = roomid
        
        fout = fout_list[date_arr.index(words[2])]
        fout.write(line+'\n')
        if num_line % 10000 ==0:
            print(num_line)

f.close()
for i in [1,2,3,4,5,6,7]:
    fout = fout_list[i-1]
    fout.close()
