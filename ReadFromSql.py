# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:08:08 2017

@author: Chenanyun
"""

import pandas as pd
import MySQLdb

conn = MySQLdb.connect(host="localhost:3306",user="cay",passwd="cay",db="cay",charset="utf8")

sql = "select * from competition_train_1 limit 100000"

df = pd.read_sql(sql,conn,index_col="orderid")

print (df)