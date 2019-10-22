#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:07:19 2018

# engine flatten
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
train2['engine'] = 1
train3['engine'] = 1
train4['engine'] = 1
train1 = train1.drop(['target'],axis = 1)
train2 = train2.drop(['target'],axis = 1)
train3 = train3.drop(['target'],axis = 1)
train4 = train4.drop(['target'],axis = 1)

final = pd.concat([train1,train2,train3,train4],axis = 0)

from lifelines import CoxPHFitter
cph = CoxPHFitter()
cph.fit(final, 'time_in_cycle', event_col='engine')
cph.print_summary()

new_final = final.drop(['time_in_cycle','engine'],axis=1)
'''
lis = [50,140,380,500]
#plt.plot(cph.predict_survival_function(new_final.iloc[lis,:]),label = '1')
plt.plot(cph.predict_survival_function(new_final.iloc[50:51,:]),label = 'engine 1')
plt.plot(cph.predict_survival_function(new_final.iloc[140:141,:]),label = 'engine 2')
plt.plot(cph.predict_survival_function(new_final.iloc[380:381,:]),label = 'engine 3')
plt.plot(cph.predict_survival_function(new_final.iloc[500:501,:]),label = 'engine 4')
plt.xlabel('Remaining Life Cycle')
plt.ylabel('Probability')
plt.legend()
plt.axvline(x=150)
plt.grid()
'''

# randomize 10
new_lis = [18,20,55,61,86,124,168,229,260,269,362,387,390,437,458,\
           519,530,618,656,667]
mat = cph.predict_survival_function(new_final.iloc[new_lis,:])
mat = mat.round(decimals = 4)

for xxx in [60,  71, 159, 197, 208]:
    print('%g \n' %xxx)
    print(mat[xxx].iloc[np.where(np.logical_and(mat[xxx]>0.48, mat[xxx]< 0.52))])
    
for bbb in new_lis:
    print('%g' %bbb)
    print(final.iloc[bbb,:].time_in_cycle)
    print('\n')
    
plt.scatter(a,b,label = 'real engine life cycle')
plt.scatter(a,c,label = 'Predicted to Breakdown Soon')