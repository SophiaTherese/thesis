#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:33:05 2022

@author: Sophia
"""
import numpy as np
import pandas as pd
from sklearn.feature_selection import f_classif
from sklearn.preprocessing import StandardScaler
from scipy import stats

# performanceOverall: reduce into two groups
def reduce_perf(data):
    if 0 <= data  <= 2:
        return 0
   
    if data == 3:
        return 1
    
    if 3 <= data  <= 6:
        return 1
    else:
        return np.nan

# indoorClimate: reduce into two groups
def reduce_ic(data):
    if 0 <= data  <= 2:
        return 0
    
    if 3 <= data  <= 5:
        return 1
    else:
        return np.nan

# sym: reduce into two groups
def reduce_s(data):
    if 1 <= data  <= 3:
        return 1
    else:
        return 0
    
# symptoms that got better
def sBetter(df,col1,col2,label):
    p = len(df)
    for i in range(p):
        if (df[col1][i] == 1 & df[col2][i] == 1):
            df[label][i] = 1
        else:
            df[label][i] = 0




 
# test num stat
def tau_ANOVA(df,df_ord,label):
    
    df = df.dropna(subset=[label])
    df_ord = df_ord.dropna(subset=[label])

    cols = [x for x in df.columns if x != label]
    cols_ord = [x for x in df_ord.columns if x != label]

    X = df[cols]
    X_ord = df_ord[cols_ord]

    y = df[label]
    
    
    lst = list(X_ord)
    print(lst)
    
    Tau = []
    p_tau = []

    for column in lst:
        tau, p_value = stats.kendalltau(X_ord[column], y, nan_policy='omit', variant='b')
        Tau.append(tau)
        p_tau.append(p_value)
    


    F_score, p_value = f_classif(X, y)



    df_stats = pd.DataFrame([Tau,p_tau,F_score,p_value], index=['tau','p_tau','F_score','p_ANOVA'], columns=X_ord.columns).T
    
    df_tau = df_stats[df_stats['p_tau']  <= 0.05]  
    
    df_ANOVA = df_stats[df_stats['p_ANOVA']  <= 0.05] 
    
    return df_stats,df_tau,df_ANOVA
