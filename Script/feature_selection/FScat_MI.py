#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:33:57 2022

@author: Sophia Wesche

Input: Relevant dataframe for specific model and target label.

Output: Mutual information (number between 0 and 1) between each feature and target

"""

#load libraries
import numpy as np
import pandas as pd
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
from matplotlib import pyplot
import matplotlib.pyplot as plt
import seaborn as sns
import fs_utils as fu

#load cleaned dataframe
df_all = pd.read_csv("../temp_data/df_all_catClean.csv")



#%%

''' select df:
    Uncomment the section relevant to your model, to make the 
    appropriate dataframe. Rememebr to comment out the previously 
    selected section, so only one data frame is assessed.'''
 
# #indoor climate 
# df_cat = df_all.drop(['buildingID', 'officeID',
    
#                       'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
#                       'Window Area','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
#                       'symp1','betterorworse1','performanceOverall',
                     
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['indoorClimate'])


# performance
# df_cat = df_all.drop(['buildingID', 'officeID',
    
#                       'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
#                       'Window Area','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                        # 'indoorClimate','symp1', 'betterorworse1','symp0', 'betterorworse0','symp3', 'betterorworse3','symp7', 'betterorworse7',
                                             # 'symptabilitywork','symptstayhome',],axis=1).copy()
# df_cat = df_cat.dropna(subset=['performanceOverall'])


# # s1: headache
# df_all['symp1'] = df_all['symp1'].apply(fu.reduce_s)
# df_all['betterorworse1'] = df_all['betterorworse1'].map({"worse":0,
#                                                          "nochange":0,
#                                                          "better":1, 
#                                                          np.nan:0})


# df_all['s1_better'] = ''
# fu.sBetter(df_all,'symp1','betterorworse1','s1_better')
# df_all = df_all.drop(['betterorworse1','symp1'],axis=1)


# df_cat = df_all.drop(['buildingID', 'officeID',
    
#                     'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
#                       'Window Area','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                      
#                       'performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
#                       'symp0', 'betterorworse0','symp3', 'betterorworse3','symp7', 'betterorworse7',
                     
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['s1_better'])

# s0: Dry or irritated eyes
# df_all['symp0'] = df_all['symp0'].apply(fu.reduce_s)
# df_all['betterorworse0'] = df_all['betterorworse0'].map({"worse":0,
#                                                          "nochange":0,
#                                                          "better":1, 
#                                                          np.nan:0})


# df_all['s0_better'] = ''
# fu.sBetter(df_all,'symp0','betterorworse0','s0_better')
# df_all = df_all.drop(['betterorworse0','symp0'],axis=1)


# df_cat = df_all.drop(['buildingID', 'officeID',
    
#                     'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
#                       'Window Area','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                      
#                       'performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
#                       'symp1', 'betterorworse1','symp3', 'betterorworse3','symp7', 'betterorworse7',
                     
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['s0_better'])



# s3: Tiredness or fatigue
# df_all['symp3'] = df_all['symp3'].apply(fu.reduce_s)
# df_all['betterorworse3'] = df_all['betterorworse3'].map({"worse":0,
#                                                          "nochange":0,
#                                                          "better":1, 
#                                                          np.nan:0})


# df_all['s3_better'] = ''
# fu.sBetter(df_all,'symp3','betterorworse3','s3_better')
# df_all = df_all.drop(['betterorworse3','symp3'],axis=1)


# df_cat = df_all.drop(['buildingID', 'officeID',
    
#                     'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
#                       'Window Area','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                      
#                       'performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
#                       'symp1', 'betterorworse1','symp0', 'betterorworse0','symp7', 'betterorworse7',
                     
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['s3_better'])


# s7: Difficult to concentrate
# df_all['symp7'] = df_all['symp7'].apply(fu.reduce_s)
# df_all['betterorworse7'] = df_all['betterorworse7'].map({"worse":0,
#                                                          "nochange":0,
#                                                          "better":1, 
#                                                          np.nan:0})

# df_all['s7_better'] = ''
# fu.sBetter(df_all,'symp7','betterorworse7','s7_better')
# df_all = df_all.drop(['betterorworse7','symp7'],axis=1)


# df_cat = df_all.drop(['buildingID', 'officeID',
    
#                       'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
#                       'Window Area','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                      
#                       'performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
#                       'symp1', 'betterorworse1','symp0', 'betterorworse0','symp3', 'betterorworse3',
                     
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['s7_better'])


#SBS; 
df_cat = df_all.drop(['performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
                     's0_better','s1_better','s3_better','s7_better','SBS1',
                     'buildingID','officeID',
    
                      'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                      'Window Area','O2_winShadePercentage','O2_opWin','Office volume',
                      'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
                      'area_det_floor', 'month',
                      
                      ],axis=1).copy()

df_cat = df_cat.dropna(subset=['SBS2'])



# make everything strings
df_cat = df_cat.applymap(str)


#%%
 
'''Input: target label relevant for the data frame tested'''

X = df_cat.drop('SBS2', axis=1) # input features
y = df_cat['SBS2'] # target variable

# X = df_cat.drop('performanceOverall', axis=1) # input features
# y = df_cat['performanceOverall'] # target variable

#Because it can't work with nan, replacing nan with empty cell
X.fillna('', inplace=True)



#%%
'''Prints chi2 value of each categorical feature in relation to target'''

# prepare input features
oe = OrdinalEncoder()
oe.fit(X)
X_enc = oe.transform(X)

# prepare target variable
le = LabelEncoder()
le.fit(y)
y_enc = le.transform(y)

# feature selection



# feature selection
sf = SelectKBest(score_func=mutual_info_classif, k='all')
sf_fit1 = sf.fit(X_enc, y_enc)
# print feature scores
for i in range(len(sf_fit1.scores_)):
    print(' %s: %f' % (X.columns[i], sf_fit1.scores_[i]))


# #If plots of feature importance is wanted, the following can be uncommented. 
# # plot the scores
# pyplot.bar([i for i in range(len(sf_fit1.scores_))], sf_fit1.scores_)
# pyplot.show()



# plot the scores of features
# datset1 = pd.DataFrame()
# datset1['feature'] = X.columns[ range(len(sf_fit1.scores_))]
# datset1['scores'] = sf_fit1.scores_
# datset1 = datset1.sort_values(by='scores', ascending=True)
# sns.barplot(datset1['scores'], datset1['feature'], color='green')
# sns.set_style('whitegrid')
# plt.rcParams["figure.figsize"] = (10,20)
# plt.ylabel('Categorical feature', fontsize=18)
# plt.xlabel('Mutual Info Score', fontsize=18)
# plt.show()


