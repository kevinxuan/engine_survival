#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:07:44 2018

engine_survival_method 1
"""

import pandas as pd
import numpy as np

import os
from sklearn.metrics import mean_squared_error, r2_score
os.chdir('/users/apple/Downloads/CMAPSSData/csv/')

# all training data

train = pd.read_csv('train_FD004.csv')
life = train.unit_number.value_counts().sort_index()
train['target'] = 0

c = 0 
for a in life:
    if c == 0:
        start = 0
        end = life.iloc[0]
    train.iloc[start:end,train.columns.get_loc('target')] = a
    start += life.iloc[c]
    c += 1
    if c == len(life):
        break
    end += life.iloc[c] 
train.to_csv('t4.csv',index = 0)

#################################################################################
    
# read in data
train = pd.read_csv('test_FD001.csv')
life = train.unit_number.value_counts().sort_index()
out = pd.read_csv('FD001.csv')
data_out = pd.read_csv('RUL_FD001.csv',header = None,names = ['real_out'])

c = 0 
finallist = []
for a in life:
    if c == 0:
        start = 0
        end = life.iloc[0]
    finallist.append(np.average(out.iloc[start:end,out.columns.get_loc('pred')])-life.iloc[c]) 
    start += life.iloc[c]
    c += 1
    if c == len(life):
        break
    end += life.iloc[c] 
    
finallist = pd.Series(finallist)

''' or use out.groupby('unit_number')['pred'].mean() '''
data_out['pred'] =finallist
data_out['pred'] = pd.Series(np.where(data_out['pred']<0,0,data_out['pred']))

# mean squared error
rmse = np.sqrt(mean_squared_error(data_out.real_out,data_out.pred))
r2 = r2_score(data_out.real_out,data_out.pred)
'''  RMSE: 38.186 ''' 