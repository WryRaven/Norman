# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:05:11 2018

@author: ckwil
"""

import os
import pandas as pd
import numpy as np
os.chdir('C:\\Users\ckwil\desktop\\norming')

#%% Read and parse source
df = pd.read_excel('numbers.xlsx')

#%% Norming function
def norm(x):
    for i in x:
        str(i)
        if i[0] == '+':
            i = i[1:]
        if i[0:1] == '00':
            i = i[2:]
    return x

#%%
df['Normalized'] = df['Raw'].apply(lambda x: norm(x))
df