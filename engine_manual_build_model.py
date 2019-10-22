#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:50:59 2018

@author: apple
"""


import pandas as pd
import numpy as np

import os
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt
os.chdir('/users/apple/Downloads/CMAPSSData/csv/')


train1 = pd.read_csv('t1.csv')
train2 = pd.read_csv('t2.csv')
train3 = pd.read_csv('t3.csv')
train4 = pd.read_csv('t4.csv')

train1 = train1.groupby('unit_number').mean()
train2 = train2.groupby('unit_number').mean()
train3 = train3.groupby('unit_number').mean()
train4 = train4.groupby('unit_number').mean()
train1['engine'] = 1
train2['engine'] = 2
train3['engine'] = 3
train4['engine'] = 4

final = pd.concat([train1,train2,train3,train4],axis = 0)

final = pd.concat([final.drop(['engine'],axis = 1),\
                   pd.get_dummies(final.engine,prefix = 'engine')],axis = 1)


test1 = pd.read_csv('test_FD001.csv')
test2 = pd.read_csv('test_FD002.csv')
test3 = pd.read_csv('test_FD003.csv')
test4 = pd.read_csv('test_FD004.csv')

ans1 = pd.read_csv('RUL_FD001.csv')
ans2 = pd.read_csv('RUL_FD002.csv')
ans3 = pd.read_csv('RUL_FD003.csv')
ans4 = pd.read_csv('RUL_FD004.csv')
test1 = test1.groupby('unit_number').mean()
test2 = test2.groupby('unit_number').mean()
test3 = test3.groupby('unit_number').mean()
test4 = test4.groupby('unit_number').mean()
test1['engine'] = 1
test2['engine'] = 2
test3['engine'] = 3
test4['engine'] = 4
test1['real'] = ans1
test2['real'] = ans2
test3['real'] = ans3
test4['real'] = ans4

test = pd.concat([test1,test2,test3,test4],axis = 0)
test = pd.concat([test.drop(['engine'],axis = 1),\
                   pd.get_dummies(test.engine,prefix = 'engine')],axis = 1)