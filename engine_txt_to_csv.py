#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:51:30 2018

@author: apple
"""

import numpy as np
import pandas as pd
import csv
import os

path = '/users/apple/Downloads/CMAPSSDATA/text/'
b = 0
allfiles = os.listdir(path)[0:]
# create folder

for a in allfiles:
    file = path+a
    out = '/users/apple/Downloads/CMAPSSDATA/csv/'+a.replace('txt','csv')
    b +=1
    inp = csv.reader(open(file,'r'),delimiter = ' ')
    out = csv.writer(open(out,'w'))
    out.writerows(inp)
    
path2 = '/users/apple/Downloads/CMAPSSDATA/csv/'
allfiles2 = os.listdir(path2)[1:]

colnames = ['unit_number','time_in_cycle','os1','os2','os3']
sm = ['sm%g'%i for i in range(0,21)]
colnames = colnames + sm

for a in allfiles2:
    data = pd.read_csv(path2+a,header = None)
    data = data.iloc[:,0:26]
    data.columns = colnames
    data.to_csv(path2+a,index= 0)
    