#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:04:16 2022

@author: Sophia Wesche

documentation: 
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html

"""
import numpy as np
import pandas as pd
# load functions in from "util_ml.py"
import util_ml as mu

#import impoer dataframes for each target: 
df_perf = pd.read_csv("../temp_data/df_perf.csv")
df_perf = df_perf.reset_index(drop=True)
df_ic = pd.read_csv("../temp_data/df_ic.csv")
df_s1 = pd.read_csv("../temp_data/df_s1.csv")
df_s0 = pd.read_csv("../temp_data/df_s0.csv")
df_s3 = pd.read_csv("../temp_data/df_s3.csv")
df_s7 = pd.read_csv("../temp_data/df_s7.csv")
df_SBS2 = pd.read_csv("../temp_data/df_SBS2.csv")




#%% -------- Tune office-related symptom models

# tune XGB model: 
param_SBS = {"gamma": [0.7,1,1.5],
             "max_depth":[2,3,4,5,7],
             "learning_rate":[0.07,0.1,0.2],
            # "lambda":[1,10],
                #'n_estimators': [50,100, 200, 300],
                }

mu.tune_xgBoost(df_SBS2,'SBS2',param_SBS)


#%%
# Tune random forest model: 
param_rf_SBS = {'max_depth': [3,4,5,6,8,9],
                'min_samples_leaf': [1,2,3,4,10],
                'min_samples_split': [2,3,4,5,6,7],
                #'n_estimators': [50,100, 200, 300],
                'max_features':[4,6,7,8,10,12],
                #"class_weight":["balanced_subsample","balanced",None]
                }

mu.tune_randomF(df_SBS2,'SBS2',param_rf_SBS)


#%%
# Tune GNB model:  
param_SBS = {'var_smoothing': np.logspace(0,-9, num=100)}
#best: {'var_smoothing': 1.519911082952933e-08}

mu.tune_GNB(df_SBS2,'SBS2',param_SBS)




#%%  -------- Tune Indoor climate models:
    
# XGB model: 
param_grid_1 = {"gamma": [0.25,1,1.5,2],}

param_grid_2 = {"gamma": [0.4,0.5,0.6],
                "max_depth":[3,4],
                "learning_rate":[0.25,0.2,0.1],
                "lambda":[1,2],
                #"scale_pos_weight": [1,3,5],
                #'n_estimators': [50,100, 200, 300],
                }

mu.tune_xgBoost(df_ic,'indoorClimate',param_grid_2)


#%%
# SVC model: 
grid_svc = {'C': [0.1,1, 10, 100], 
            'gamma': [1,0.1,0.01],
            #'kernel': ['linear','rbf', 'poly', 'sigmoid']
            }

mu.tune_svc(df_ic,'indoorClimate',grid_svc)


#%% 

# random forrest
paramIC_rF_2 = {'max_depth': [7,8,9,None],
                'min_samples_leaf': [4,5,6],
                'min_samples_split': [3,4,5],
                #'n_estimators': [50,100, 200, 300],
                #'max_features':[16,13,12,11,10,9,8,7],
               # "class_weight":["balanced_subsample","balanced",None]
                }
mu.tune_randomF(df_ic,'indoorClimate',paramIC_rF_2)

#%% ------- Tune Performance models


# XGB:
param_grid_1 = {"max_depth":[2,3,4,5],}

param_grid_2 = {"gamma": [0.1,0.2],
                "max_depth":[2,3,None],
                "learning_rate":[0.05,0.1,0.15],
                #"reg_lambda": [0,0.01,0.1,1,10],
                # "scale_pos_weight": [1,3,5],
                }

mu.tune_xgBoost(df_perf,'performanceOverall',param_grid_2)


#%%  - random forest

param_rF_p = {'max_depth': [3,4,5,6],
              'min_samples_leaf': [1,2],
              'min_samples_split': [3,5,6,7,8],
              }

#Bedst: {'max_depth': 6, 'min_samples_leaf': 1, 'min_samples_split': 3}

mu.tune_randomF(df_perf,'performanceOverall',param_rF_p)

#%% ------  Tune model 0: Dry or irritated eyes

#GNB tune: 
param_grid_GNB0 = {'var_smoothing': np.logspace(0,-9, num=100)}

mu.tune_GNB(df_s0,'s0_better',param_grid_GNB0)

#%%
# XGB:
param_xgb0 = {"gamma": [0,0.05,0.1,0.25],
              "max_depth":[2,3,4,5,6,7,8,9],
              "learning_rate":[0.01,0.04,0.05,0.06,0.7,0.1],
               # "reg_lambda": [0,0.01,0.1,1,10],
                # "scale_pos_weight": [1,3,5],
                #"eval_metric":["logloss","error","auc"]
                }

mu.tune_xgBoost(df_s0,'s0_better',param_xgb0)

#%%
# random forest: 
param_rF_s0 = {'max_depth': [4,5,8,10,12,15],
                   'min_samples_leaf': [2,5,7,8,9,10],
                   'min_samples_split': [2,5,7,8,9],
                   #'n_estimators': [100, 200, 300],
                   #'max_features':[13,10,9,8],
                   "class_weight":["balanced"]
                   }


mu.tune_randomF(df_s0,'s0_better',param_rF_s0)


#%% s1: headache
# random forest:
param_grid_rF_2 = {'max_depth': [4,5,10,15],
                   'min_samples_leaf': [2,7,8,9,10],
                   'min_samples_split': [2,7,8,9],
                   #'n_estimators': [100, 200, 300],
                   #'max_features':[13,10,9,8],
                   "class_weight":["balanced_subsample","balanced",None]}


mu.tune_randomF(df_s1,'s1_better',param_grid_rF_2)

#%%
# decision tree
param_grid_dt1_1 = {"class_weight":["balanced_subsample","balanced"],
                   'max_features':[12,11,10,9,8,7],}

param_grid_dt1_2 = {'max_depth': [4,6,8,10,12],
                   'min_samples_leaf': [1,2,5,6,7,9],
                   'min_samples_split': [2,3,4,5,8],
                   "class_weight":[None,"balanced"]}
mu.tune_dt(df_s1,'s1_better',param_grid_dt1_2)

#%% 
#GNB: 
param_grid_GNB1 = {'var_smoothing': np.logspace(0,-9, num=100)}
#best: var_smoothing': 4.3287612810830526e-07

mu.tune_GNB(df_s1,'s1_better',param_grid_GNB1)
#%% ------ 3: Tiredness or fatigue

# Decision tree: 
param_grid_dt3_1 = {'max_depth': [1,2,3,4,5,6,8]}

param_grid_dt3_2 = {'max_depth': [4,5,6,7],
                    'min_samples_leaf': [11,12,13],
                    'min_samples_split': [2,3,4],
                  #  'max_features':[17,15,13,12,11,10,9,8,7],
                    'class_weight':["balanced",None]}


mu.tune_dt(df_s3,'s3_better',param_grid_dt3_2)

#{'class_weight': 'balanced', 'max_depth': 5, 'min_samples_leaf': 8, 'min_samples_split': 2}

#%%
# random forest
param_rF_s3 = {'max_depth': [4,5,10,15],
                   'min_samples_leaf': [2,7,8,9,10],
                   'min_samples_split': [2,7,8,9],
                   #'n_estimators': [100, 200, 300],
                   #'max_features':[13,10,9,8],
                   "class_weight":["balanced_subsample","balanced"]}


mu.tune_randomF(df_s3,'s3_better',param_rF_s3)
#%%
# GNB:
param_grid_GNB0 = {'var_smoothing': np.logspace(0,-9, num=100)}
#best: {'var_smoothing': 6.579332246575683e-06}

mu.tune_GNB(df_s3,'s3_better',param_grid_GNB0)





#%% ------ 7: Difficult to concentrate

# GNB model tuning:
param_grid_GNB7 = {'var_smoothing': np.logspace(0,-9, num=100)}
#best: 

mu.tune_GNB(df_s7,'s7_better',param_grid_GNB7)
# {'var_smoothing': 1.232846739442066e-08}
#%%
#xgb: 
param_xgb7_1 = {"gamma": [0,0.25,1,1.5,2],}

param_xgb7_2 = {"gamma": [0,0.25,1,1.5,2],
                "max_depth":[2,3,4,5],
                "learning_rate":[0.01,0.05,0.1,0.2],
                "reg_lambda": [0,1,2],
                "scale_pos_weight": [1,3,5]}

mu.tune_xgBoost(df_s7,'s7_better',param_xgb7_2)

#{'gamma': 1, 'learning_rate': 0.01, 'max_depth': 4, 'reg_lambda': 2, 'scale_pos_weight': 1}

