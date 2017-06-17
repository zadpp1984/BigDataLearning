# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 18:30:54 2017

@author: user
"""
import numpy as np


arr = [
       ['A1','B1',3],
       ['A1','B1',5],
       ['A1','B2',2],
       ['A2','B1',3],
       ['A2','B1',3],
       ['A2','B1',2]
       ]

mynp = np.array(arr)

np.random.shuffle(mynp)


import pandas as pd

mypd = pd.DataFrame(arr)


mypd2 = mypd.loc[mypd[0]=='A1']

mypd.append(mypd2,ignore_index=True)