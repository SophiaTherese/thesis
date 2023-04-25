#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:01:24 2022

@author: Sophia Wesche

CATEGORICAL FEATURESELECTION

Input:  Relevant dataframe for specific model and target label.

Output: Chi2 values prited for each feature in relation to target

"""
# tutorial used: 
# https://datascienceplus.com/selecting-categorical-features-in-customer-attrition-prediction-using-python/


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import prince # for multiple correspondence analysis
from sklearn.feature_selection import SelectKBest, chi2 # for chi-squared feature selection
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
import matplotlib.pyplot as plt
import fs_utils as fu

#load cleaned data frame
df_all = pd.read_csv("../temp_data/df_all_catClean.csv")



  #%%%
''' select df:
    Uncomment the section relevant to your model, to make the 
    appropriate dataframe. Rememebr to comment out the previously 
    selected section, so only one data frame is assessed.'''
 
# #indoor climate 
# df_cat = df_all.drop(['buildingID', 'officeID',
    
#                       'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
#                       'O2_winArea','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                      
#                       'performanceOverall','symp1', 'betterorworse1','symp0', 'betterorworse0','symp3', 'betterorworse3','symp7', 'betterorworse7',
#                       'symptabilitywork','symptstayhome',
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['indoorClimate'])


#performance
# df_cat = df_all.drop(['buildingID', 'officeID',
    
#                       'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
#                       'O2_winArea','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
#                       'performanceOverall','symp1', 'betterorworse1','symp0', 'betterorworse0','symp3', 'betterorworse3','symp7', 'betterorworse7',
#                       'symptabilitywork','symptstayhome',],axis=1).copy()

# df_cat = df_cat.dropna(subset=['performanceOverall'])


# s1: headache
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
                   
#                       'O2_winArea','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                      
#                       'performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
#                       'symp0', 'betterorworse0','symp3', 'betterorworse3','symp7', 'betterorworse7',
                     
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['s1_better'])


# # s0: Dry or irritated eyes
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
                   
#                       'O2_winArea','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                      
#                       'performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
#                       'symp1', 'betterorworse1','symp3', 'betterorworse3','symp7', 'betterorworse7',
                     
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['s0_better'])


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
                   
#                       'O2_winArea','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                      
#                       'performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
#                       'symp1', 'betterorworse1','symp0', 'betterorworse0','symp7', 'betterorworse7',
                     
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['s3_better'])



# # s7: Difficult to concentrate
# df_all['symp7'] = df_all['symp7'].apply(fu.reduce_s)
# df_all['betterorworse7'] = df_all['betterorworse7'].map({"worse":0,
#                                                          "nochange":0,
#                                                          "better":1, 
#                                                          np.nan:0})


# df_all['s7_better'] = ''
# fu.sBetter(df_all,'symp7','betterorworse7','s7_better')
# df_all = df_all.drop(['betterorworse7','symp7'],axis=1)


# df_cat = df_all.drop(['buildingID', 'officeID',
    
#                     'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
#                       'O2_winArea','O2_winShadePercentage','O2_opWin','Office volume',
#                       'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
#                       'area_det_floor', 'month',
                      
#                       'performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
#                       'symp1', 'betterorworse1','symp0', 'betterorworse0','symp3', 'betterorworse3',
                     
#                       ],axis=1).copy()

# df_cat = df_cat.dropna(subset=['s7_better'])


# df_cat = df_cat.applymap(str)
 

# building-related symptoms dataframe: 
df_cat = df_all.drop(['performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
                     's0_better','s1_better','s3_better','s7_better','SBS1',
                     'buildingID','officeID',
    
                      'CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                      'Window Area','O2_winShadePercentage','O2_opWin','Office volume',
                      'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
                      'area_det_floor', 'month',
                      
                      ],axis=1).copy()

df_cat = df_cat.dropna(subset=['SBS2'])
 
 
#%%%

''' COMPARING FEATURES 
    Input: target label relevant for the data frame tested'''


X1 = df_cat.drop('SBS2', axis=1) # input features
y1 = df_cat['SBS2'] # target variable


# X1 = df_cat.drop('performanceOverall', axis=1) # input features
# y1 = df_cat['performanceOverall'] # target variable


#%%%

'''Prints chi2 value of each categorical feature in relation to target'''

#Because it can't work with nan
X1.fillna('', inplace=True)

# prepare input features
oe = OrdinalEncoder()
oe.fit(X1)
X_enc = oe.transform(X1)

# prepare target variable
le = LabelEncoder()
le.fit(y1)
y_enc = le.transform(y1)


# feature selection
sf = SelectKBest(chi2, k='all')
sf_fit1 = sf.fit(X_enc, y_enc)
# print feature scores
for i in range(len(sf_fit1.scores_)):
    print(' %s: %f' % (X1.columns[i], sf_fit1.scores_[i]))



# #If plots of feature importance is wanted, the following can be uncommented. 
# #plot the scores of features
# datset1 = pd.DataFrame()
# datset1['feature'] = X1.columns[ range(len(sf_fit1.scores_))]
# datset1['scores'] = sf_fit1.scores_
# datset1 = datset1.sort_values(by='scores', ascending=True)
# sns.barplot(datset1['scores'], datset1['feature'], color='green')
# sns.set_style('whitegrid')
# plt.rcParams["figure.figsize"] = (10,20)
# plt.ylabel('Categorical feature', fontsize=18)
# plt.xlabel('Chi2 Score', fontsize=18)
# plt.show()



#%%%
''' Dividing into categories of each feature
    Does the same as the previous, but for each of the specific categories 
    in a 1-hot-encoded nominal feature.'''

# df_cat = df_cat.dropna(subset=['indoorClimate'])
# df_cat_dum = pd.get_dummies(df_cat,dummy_na=True, drop_first=True)

# print(df_cat_dum.shape)
# print("The data set contains: {} rows and {} columns".format(df_cat_dum.shape[0], df_cat_dum.shape[1]))
# print("Features after get_dummies:\n", list(df_cat_dum.columns))

# # X = df_cat_dum.drop('indoorClimate', axis=1) # input categorical features
# # y = df_cat_dum['indoorClimate'] # target variable

# X = df_cat_dum.drop('performanceOverall', axis=1) # input categorical features
# y = df_cat_dum['performanceOverall'] # target variable



# # categorical feature selection
# sf = SelectKBest(chi2, k='all')
# sf_fit = sf.fit(X, y)
# # print feature scores
# for i in range(len(sf_fit.scores_)):
#     print(' %s: %f' % (X.columns[i], sf_fit.scores_[i]))

# import matplotlib.pyplot as plt

# # plot the scores
# datset = pd.DataFrame()
# datset['feature'] = X.columns[ range(len(sf_fit.scores_))]
# datset['scores'] = sf_fit.scores_
# datset = datset.sort_values(by='scores', ascending=True)
# sns.barplot(datset['scores'], datset['feature'], color='blue')
# sns.set_style('whitegrid')
# plt.rcParams["figure.figsize"] = (10,10)
# plt.ylabel('Categorical Feature', fontsize=18)
# plt.xlabel('Score', fontsize=18)
# plt.show()






#%%% https://towardsdatascience.com/chi-square-test-for-feature-selection-in-machine-learning-206b1f0b8223

# #test significance: 
# chi_scores = chi2(X,y)

# p_values = pd.Series(chi_scores[1],index = X.columns)
# p_values.sort_values(descending = False , inplace = True)

# # plot p-values
# p_values.plot.bar()


# # print(p_values(<0,05))


