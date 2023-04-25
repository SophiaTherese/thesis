#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:11:55 2022

@author: Sophia
"""
import numpy as np
import pandas as pd
import datetime
import seaborn as sns


from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay


# correlation

def redundant_pairs(df):
    """ Get digonal and lower triangular pairs of correlation matrix"""
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range (0,i + 1):
            pairs_to_drop.add((cols[i],cols[j]))
            
    return pairs_to_drop

def get_top_abs_correlation(df, n = 5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = redundant_pairs(df)
    au_corr = au_corr.drop(labels = labels_to_drop).sort_values(ascending = False)
    return au_corr[0:n]




"""correlation of meassurement df"""

#Dropping non-nimerical values
def num(df):
    df_num = df.drop(['buildingID','officeID'],axis=1)
    
    return df_num

# reverse 1-hot encoding function

#df_predictors_cat.reset_index(inplace=True, drop=True)

def get_cat(feat_name,cols,df):
    
    df[feat_name]='' # to create an empty column
    
    for col_name in df[cols].columns:
        new_df = df.loc[df[col_name]==1,feat_name]= df[feat_name]+' '+col_name
        
    return new_df


# - function for merging two binary features

def merge_binary(df,feature1,feature2,mergedFeature):
    df[mergedFeature] = ''
    for i in range(len(df)):
        if (df[feature1][i] + df[feature2][i] >= 1): 
            df[mergedFeature][i] = "True"
        else:
            df[mergedFeature][i] = "False"
            df_merged = df
    return df_merged

# - function for merging 3 binary features

def merge_binary_3(df,feature1,feature2,feature3,mergedFeature):
    df[mergedFeature] = ''
    for i in range(len(df)):
        if (df[feature1][i] + df[feature2][i] + df[feature3][i]>= 1): 
            df[mergedFeature][i] = "True"
        else:
            df[mergedFeature][i] = "False"
            df_merged = df
    return df_merged

