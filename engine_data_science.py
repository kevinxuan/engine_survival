#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:56:43 2018

# 
"""

import pandas as pd
import numpy as np
import os
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
os.chdir('/users/apple/Downloads/CMAPSSData/csv/')

train1 = pd.read_csv('t1.csv')
'''
train2 = pd.read_csv('t2.csv')
train3 = pd.read_csv('t3.csv')
train4 = pd.read_csv('t4.csv')
'''

life = train1.unit_number.value_counts().sort_index()

train = pd.DataFrame()
test = pd.DataFrame()
c = 0 
for a in life:
    if c == 0:
        start = 0
        end = life.iloc[0]
    # set training set and dataset
    indice = int(life.iloc[c]*0.8)
    train = train.append(train1.iloc[start:start+indice,:])
    test = test.append(train1.iloc[start+indice:end,:])
    start += life.iloc[c]
    c += 1
    if c == len(life):
        break
    end += life.iloc[c] 
    
# train test
train_y = train.target
test_y = test.target
train = train.drop(['target','unit_number','time_in_cycle'],axis = 1)
test = test.drop(['target','unit_number','time_in_cycle'],axis = 1)
sc=  StandardScaler()
train = sc.fit_transform(train)
test = sc.transform(test)

# classifier 
import lightgbm as lgb
dataset = lgb.Dataset(train,label = train_y)
params = {}
params['learning_rate'] = 0.001
params['boosting_type'] = 'gbdt'
params['objective'] = 'regression'
params['num_leaves'] = 100

clf = lgb.train(params,dataset, 500)
y_pred = clf.predict(test)
r2_score(test_y,y_pred)

# r^2 = 0.04