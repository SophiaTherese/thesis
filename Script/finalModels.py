# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

#import util_ml as mu
import util_finalModel as ufm

# from sklearn.dummy import DummyClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.linear_model import LogisticRegression


#Loading dataframes
df_perf = pd.read_csv("./temp_data/df_perf.csv")
df_ic = pd.read_csv("./temp_data/df_ic.csv")
df_s1 = pd.read_csv("./temp_data/df_s1.csv")
df_s0 = pd.read_csv("./temp_data/df_s0.csv")
df_s3 = pd.read_csv("./temp_data/df_s3.csv")
df_s7 = pd.read_csv("./temp_data/df_s7.csv")
df_SBS2 = pd.read_csv("./temp_data/df_SBS2.csv")



#%%-------- Model training and performance

# Function to train the indoor climate climate model. Input: Data frame for indoor climate
ufm.indoorClimate(df_ic)
#ufm.indoorClimate_model(df_ic,182)

# accuracy: 0.7073170731707317
# F1 score: 0.7142857142857143
# auc: 0.7083333333333334

#%%

# Function to train performance model. Input: Data frame for performance
ufm.performance(df_perf)

# Random Forest accuracy: 0.7380952380952381
# Random Forest F1 score: 0.8135593220338982
# Random Forrest auc: 0.6916666666666667
#%%
# Function to train performance model. Input: Data frame for symptoms
ufm.symptoms(df_SBS2)

# Random Forest accuracy: 0.8444444444444444
# Random Forest F1 score: 0.5882352941176471
# Random Forrest auc: 0.736111111111111


#%% 0: Dry or irritated eyes
ufm.s0(df_s0)
# Random Forest accuracy: 0.8
# Random Forest F1 score: 0.47058823529411764
# Random Forrest auc: 0.706766917293233

#%% 1: Headache
ufm.s1(df_s1)
# Random Forest accuracy: 0.7111111111111111
# Random Forest F1 score: 0.5185185185185185
# Random Forrest auc: 0.7753378378378378

#%% 3: Tiredness or fatigue
ufm.s3(df_s3)

# Accuracy: 0.82
# F1 score: 0.5
# AUC: 0.72

#%% 7: Difficult to concentrate
ufm.s7(df_s7)
# Random Forest accuracy: 0.8444444444444444
# Random Forest F1 score: 0.631578947368421
# Random Forrest auc: 0.7777777777777777

#%% use case: 
    
"""Shap force plots as seen in use case
    input: dataframe of the target, select nr. observation (nr. row)
    output: prediction (1 or 0) + print forceplot"""
    
# occupant 1:
ufm.performance_model(df_perf,182)
ufm.model_indoorClimate(df_ic,df_ic,182)
ufm.symptoms_model(df_SBS2,195)



#occupant 2
ufm.performance_model(df_perf,183)
#ufm.indoorClimate_model(df_ic,183)
ufm.model_indoorClimate(df_ic,df_ic,183)
ufm.symptoms_model(df_SBS2,196)



#occupant 3
ufm.performance_model(df_perf,184)
#ufm.indoorClimate_model(df_ic,184)
ufm.model_indoorClimate(df_ic,df_ic,184)
ufm.symptoms_model(df_SBS2,197)

#%% Make changes to input for performance model:

#occupant 1
df_perf.at[182,'CO2_mean']=750
df_perf.at[182,'T_mean']=23
df_perf.at[182,'RH_mean']=20
df_perf.at[182,'talk']=False
#df_perf.at[182,'Floor mopping frequency']=0
df_perf.at[182,'Number of supply devices']=6



#occupant 2
df_perf.at[183,'CO2_mean']=750
df_perf.at[183,'T_mean']=23
df_perf.at[183,'RH_mean']=20
df_perf.at[183,'talk']=False
#df_perf.at[183,'Floor mopping frequency']=0
df_perf.at[183,'Number of supply devices']=6



#occupant 3
df_perf.at[184,'CO2_mean']=750
df_perf.at[183,'T_mean']=23
df_perf.at[183,'RH_mean']=20
df_perf.at[184,'talk']=False
#df_perf.at[184,'Floor mopping frequency']=0
df_perf.at[184,'Number of supply devices']=6


# shorten feature name to avoid text overlapping in force plots.
df_perf.rename(columns = {'Number of supply devices':'Nr devices', 
                          'Floor mopping frequency':'Floor mopping'
                          }, inplace = True)

#%% # change values in rows of indoor climate df as seen in use case

#occupant 1
df_ic.at[182,'CO2_mean']=750
df_ic.at[182,'T_mean']=23
#df_ic.at[182,'light_mean']=500
df_ic.at[182,'RH_mean']=20
df_ic.at[182,'talk']=False
#df_ic.at[182,'Floor mopping frequency']=0
df_ic.at[182,'Number of supply devices']=6


#occupant2
df_ic.at[183,'CO2_mean']=750
df_ic.at[183,'T_mean']=23
#df_ic.at[183,'light_mean']=500
df_ic.at[183,'RH_mean']=20
df_ic.at[183,'talk']=False
#df_ic.at[183,'Floor mopping frequency']=0
df_ic.at[183,'Number of supply devices']=6

#occupant 3
df_ic.at[184,'CO2_mean']=750
df_ic.at[184,'T_mean']=23
#df_ic.at[184,'light_mean']=500
df_ic.at[184,'RH_mean']=20
df_ic.at[184,'talk']=False
#df_ic.at[184,'Floor mopping frequency']=0
df_ic.at[184,'Number of supply devices']=6

# shorten feature name to avoid text overlapping in force plots.
df_ic.rename(columns = {'Number of supply devices':'Nr devices', 
                        'Floor mopping frequency':'Floor mopping'
                        }, inplace = True)

#%% # change symptoms obs
#occupant 1
df_SBS2.at[195,'CO2_mean']=750
df_SBS2.at[195,'T_mean']=23
df_perf.at[195,'RH_mean']=20
df_SBS2.at[195,'talk']=False
#df_SBS2.at[195,'Floor mopping frequency']=0
df_SBS2.at[195,'Number of supply devices']=6


#occupant 2
df_SBS2.at[196,'CO2_mean']=750
df_SBS2.at[196,'T_mean']=23
df_perf.at[196,'RH_mean']=20
df_SBS2.at[196,'talk']=False
#df_SBS2.at[196,'Floor mopping frequency']=0
df_SBS2.at[196,'Number of supply devices']=6


#occupant 3
df_SBS2.at[197,'CO2_mean']=750
df_SBS2.at[197,'T_mean']=23
df_perf.at[197,'RH_mean']=20
df_SBS2.at[197,'talk']=False
df_SBS2.at[197,'noiseOfficeEquipment']=False
#df_SBS2.at[197,'Floor mopping frequency']=0
df_SBS2.at[197,'Number of supply devices']=6

#%%
""" force plots after input is changed in use case"""


# performance
#occupant 1
ufm.performance_model(df_perf,182)
# Performance prediction:  [0]
# Performance after prediction:  [1]

#occupant 2
ufm.performance_model(df_perf,183)
# Performance prediction:  [1]
# Performance after prediction:  [1]
#occupant 3
ufm.performance_model(df_perf,184)
# Performance prediction:  [0]
# Performance after prediction:  [1]


#%% indoor climate 

#occupant 1
ufm.model_indoorClimate(df_ic,df_ic,182)
#Indoor climate prediction:  [0.]
# Indoor climate prediction after:  [1.]

#occupant 2
ufm.model_indoorClimate(df_ic,df_ic,183)
# Indoor climate prediction:  [1.]
# Indoor climate prediction after:  [1.]
#occupant 3
ufm.model_indoorClimate(df_ic,df_ic,184)
# Indoor climate prediction:  [0.]
# Indoor climate prediction after:  [1.]

#%% symptoms
#occupant 1
ufm.symptoms_model(df_SBS2,195)
# Symptoms prediction:  [1]

#occupant 2
ufm.symptoms_model(df_SBS2,196)
# Symptoms prediction:  [1]

#occupant 3
ufm.symptoms_model(df_SBS2,197)
# Symptoms prediction:  [1]






