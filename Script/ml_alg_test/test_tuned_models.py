#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:10:32 2022

@author: Sophia
"""


import pandas as pd

import util_ml as mu

from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


#load dataframes of each model: 
df_perf = pd.read_csv("../temp_data/df_perf.csv")
df_ic = pd.read_csv("../temp_data/df_ic.csv")
df_s1 = pd.read_csv("../temp_data/df_s1.csv")
df_s0 = pd.read_csv("../temp_data/df_s0.csv")
df_s3 = pd.read_csv("../temp_data/df_s3.csv")
df_s7 = pd.read_csv("../temp_data/df_s7.csv")
df_SBS2 = pd.read_csv("../temp_data/df_SBS2.csv")





#%% ---------office-related symptoms

# Logistic regression model: 
logreg_model_SBS = LogisticRegression(solver='lbfgs', max_iter=100)

mu.norm_models(df_SBS2,'SBS2',logreg_model_SBS)

# accuracy: 0.8444444444444444
# F1 score: 0.5333333333333333
# auc: 0.6944444444444444

#%%
param_dist_SBS ={"objective": "binary:logistic",
                #"n_estimators": 100,
                "random_state": 42,
                 "max_depth":4,
                 "learning_rate":0.1,
                 "gamma": 1,
                 'lambda': 1,
               # # "reg_lambda": 0,
                #"scale_pos_weight":1,
                "eval_metric":"auc"}

mu.xgboost_classifier(df_SBS2,'SBS2',param_dist_SBS)

# {'gamma': 1, 'learning_rate': 0.1, 'max_depth': 4}
# XGBoost accuracy: 0.8444444444444444
# XGBoost F1: 0.5333333333333333
# XGBoost auc: 0.6944444444444444

#%%
rf_model_SBS = RandomForestClassifier(random_state= 42,
                                     max_depth = 4, 
                                     min_samples_leaf = 2,
                                     min_samples_split= 5,
                                     n_estimators=100,
                                     max_features= 12,
                                     class_weight='balanced_subsample'
                                     )

mu.tree_model(df_SBS2,'SBS2',rf_model_SBS)

# {'class_weight': 'balanced_subsample, 'max_depth': 4, 'min_samples_leaf': 2, 'min_samples_split': 5}
# Random Forest accuracy: 0.8444444444444444
# Random Forest F1 score: 0.5882352941176471
# Random Forrest auc: 0.736111111111111


#%%
param_SBS = GaussianNB(priors=None, 
                       var_smoothing=1.519911082952933e-08)

mu.norm_models(df_SBS2,'SBS2',param_SBS)

# Gausian Naive Bayes accuracy: 0.8444444444444444
# Gausian Naive Bayes F1 score: 0.5882352941176471
# Gausian Naive Bayes auc: 0.736111111111111


#%% ------ Indoor climate

# XGB
param_dist_ic ={"objective": "binary:logistic",
                #"n_estimators": 100,
                "random_state": 42,
                "max_depth":3,
                "learning_rate":0.1,
                "gamma": 0.5,
                "lambda":1,
               # "reg_lambda": 0,
                #"scale_pos_weight":1,
                "eval_metric":"auc"
                }

mu.xgboost_classifier(df_ic,'indoorClimate',param_dist_ic)

#Best:
#{'gamma': 0.5, 'lambda': 1, 'learning_rate': 0.1, 'max_depth': 3}
# XGBoost accuracy: 0.6341463414634146
# XGBoost F1: 0.6341463414634146
# XGBoost auc: 0.6345238095238095

#%%
rf_model_IC = RandomForestClassifier(random_state= 42,
                                     max_depth = 8, 
                                     min_samples_leaf = 4,
                                     min_samples_split= 3,
                                     n_estimators=100,
                                     #min_weight_fraction_leaf = 0.1,
                                     #max_features= 7,
                                     # class_weight="balanced_subsample"
                                     )

mu.tree_model(df_ic,'indoorClimate',rf_model_IC)


#{'max_depth': 8, 'min_samples_leaf': 4, 'min_samples_split': 3}
# Random Forest accuracy: 0.5609756097560976
# Random Forest F1 score: 0.5714285714285713
# Random Forrest auc: 0.5619047619047619


#%%

# Support vector machine:
SVC_model_ic = SVC(kernel='sigmoid',
                   # C= 1, 
                   # gamma = 0.1
                   )

mu.norm_models(df_ic,'indoorClimate',SVC_model_ic)

# sigmoid, with deafult hyper-parameters
# accuracy: 0.7073170731707317
# F1 score: 0.7142857142857143
# auc: 0.7083333333333334

#%% ------ Performance


#xgb: 
param_dist_Perf ={#"objective": "binary:logistic",
                  # "n_estimators": 100,
                  "random_state": 42,
                  "max_depth":2,
                  "learning_rate":0.1,
                  "gamma": 0.1,
                  # "reg_lambda": 0,
                  # "scale_pos_weight":1,
                  # "eval_metric":"logloss"
                  }
mu.xgboost_classifier(df_perf,'performanceOverall',param_dist_Perf)

# {'gamma': 0.1, 'learning_rate': 0.1, 'max_depth': 2}
# XGBoost accuracy: 0.7142857142857143
# XGBoost F1: 0.793103448275862
# XGBoost auc: 0.6749999999999999

#%%

#random forest
rf_model_perf = RandomForestClassifier(random_state=42,
                                       n_estimators= 100,
                                        max_depth =6, 
                                        min_samples_leaf = 1,
                                        min_samples_split= 3,
                                        #max_features= 8,
                                        class_weight=None
                                       )


mu.tree_model(df_perf,'performanceOverall',rf_model_perf)

# Accuracy: 0.7380952380952381
# F1 score: 0.8135593220338982
# AUC: 0.6916666666666667

#%%
# logistic reg:
lReg_p = LogisticRegression()

mu.norm_models(df_perf,'performanceOverall',lReg_p)

# Logistic Regression accuracy: 0.6904761904761905
# Logistic Regression F1 score: 0.7868852459016393
# Logistic Regression auc: 0.6083333333333334

#%%
# support vector machine

SVC_model_p = SVC(kernel='sigmoid', probability=True)

mu.norm_models(df_perf,'performanceOverall',SVC_model_p)

# SVC accuracy: 0.7619047619047619
# SVC F1 score: 0.84375
# SVC auc: 0.6583333333333332

#%% ------ 0: Dry or irritated eyes

#xgBoost
param_dist_0 ={#"objective": "binary:logistic",
                  #"n_estimators": 100,
                  "random_state": 1,
                  "max_depth":3,
                  "learning_rate":0.01,
                  "gamma": 0.25,
                  #"reg_lambda": 0,
                 # "scale_pos_weight":1,
                  #"eval_metric":"auc"
                  }

mu.xgboost_classifier(df_s0,'s0_better',param_dist_0)

#{'gamma': 0.25, 'learning_rate': 0.01, 'max_depth': 3}
# XGBoost accuracy: 0.8444444444444444
# XGBoost F1: 0.0
# XGBoost auc: 0.5

#%%
#GausianNB
param_grid_nb_0 = GaussianNB(priors=None, 
                             var_smoothing=0.0008111308307896872)

mu.norm_models(df_s0,'s0_better',param_grid_nb_0)

#var_smoothing=0.0008111308307896872
# Gausian Naive Bayes accuracy: 0.8444444444444444
# Gausian Naive Bayes F1 score: 0.22222222222222224
# Gausian Naive Bayes auc: 0.5582706766917293

#%%
rf_model_s0 = RandomForestClassifier(random_state= 42,
                                     max_depth = 4, 
                                     min_samples_leaf = 7,
                                     min_samples_split= 9,
                                     class_weight="balanced")
mu.tree_model(df_s0,'s0_better',rf_model_s0)

# {'class_weight': 'balanced', 'max_depth': 4, 'min_samples_leaf': 7, 'min_samples_split': 9}
# Random Forest accuracy: 0.8
# Random Forest F1 score: 0.47058823529411764
# Random Forrest auc: 0.706766917293233

#%% ------ 1: Headache

#GausianNB
param_grid_nb_1 = GaussianNB(priors=None, var_smoothing=0.0008111308307896872)

mu.norm_models(df_s1,'s1_better',param_grid_nb_1)

#var_smoothing=0.0008111308307896872
# Gausian Naive Bayes accuracy: 0.8444444444444444
# Gausian Naive Bayes F1 score: 0.4615384615384615
# Gausian Naive Bayes auc: 0.6604729729729729

#%%
# decision tree
param_dt_s1 = DecisionTreeClassifier(random_state= 42,
                                      max_depth=15,
                                      min_samples_leaf=7,
                                      min_samples_split= 4,
                                      class_weight="balanced")

mu.tree_model(df_s1,'s1_better',param_dt_s1)

# {'class_weight': 'balanced', 'max_depth': 4, 'min_samples_leaf': 9, 'min_samples_split': 2}
# Decision Tree accuracy: 0.7111111111111111
# Decision Tree F1: 0.5185185185185185
# Decision Tree auc: 0.7753378378378378



#%%
# random forest
rf_model_s1 = RandomForestClassifier(random_state= 42,
                                     max_depth = 10, 
                                     min_samples_leaf = 10,
                                     min_samples_split= 8,
                                     class_weight="balanced")
mu.tree_model(df_s1,'s1_better',rf_model_s1)

#{'class_weight': 'balanced', 'max_depth': 10, 'min_samples_leaf': 10, 'min_samples_split': 8}
# Random Forest accuracy: 0.7777777777777778
# Random Forest F1 score: 0.5
# Random Forrest auc: 0.7179054054054054


#%% ------ 3: Tiredness or fatigue

# Performs best: decision tree and GNB
param_dt_s3 = DecisionTreeClassifier(random_state= 42,
                                     max_depth=5,
                                     min_samples_leaf=10,
                                     min_samples_split=2,
                                     #max_features= 12,
                                     class_weight='balanced'
                                     )

mu.tree_model(df_s3,'s3_better',param_dt_s3)

#{'class_weight': 'balanced', 'max_depth': 5, 'min_samples_leaf': 10, 'min_samples_split': 2}
# Accuracy: 0.6444444444444445
# F1 score: 0.27272727272727276
# AUC: 0.5563909774436091


#%%
# random forest

rf_model_s3 = RandomForestClassifier(random_state= 42,
                                     max_depth = 10, 
                                     min_samples_leaf = 10,
                                     min_samples_split= 8,
                                     class_weight="balanced")
mu.tree_model(df_s3,'s3_better',rf_model_s3)

#{'class_weight': 'balanced', 'max_depth': 10, 'min_samples_leaf': 10, 'min_samples_split': 8}
# Accuracy: 0.7777777777777778
# F1 score: 0.4444444444444444
# AUC: 0.6936090225563909
#%%

# GNB
param_grid_nb_3 = GaussianNB(priors=None, 
                             var_smoothing=6.579332246575683e-06)

mu.norm_models(df_s3,'s3_better',param_grid_nb_3)

#{'var_smoothing': 6.579332246575683e-06}
# Gausian Naive Bayes accuracy: 0.8222222222222222
# Gausian Naive Bayes F1 score: 0.5
# Gausian Naive Bayes auc: 0.7199248120300752

#%% ------ 7: Difficult to concentrate


#GNB
param_grid_nb_7 = GaussianNB(priors=None, 
                             var_smoothing=5.336699231206313e-07)

mu.norm_models(df_s7,'s7_better',param_grid_nb_7)

#5.336699231206313e-07
# Gausian Naive Bayes accuracy: 0.8
# Gausian Naive Bayes F1 score: 0.47058823529411764
# Gausian Naive Bayes auc: 0.6666666666666666


#%%
rf_model_s7 = RandomForestClassifier(random_state= 42,
                                     max_depth = 2, 
                                     min_samples_leaf = 8,
                                     min_samples_split= 2,
                                     n_estimators=100,
                                     class_weight="balanced_subsample")
mu.tree_model(df_s7,'s7_better',rf_model_s7)

#{'class_weight': 'balanced_subsample', 'max_depth': 2, 'min_samples_leaf': 8, 'min_samples_split': 2}
# Random Forest accuracy: 0.8444444444444444
# Random Forest F1 score: 0.631578947368421
# Random Forrest auc: 0.7777777777777777


#%%
param_dist_7 ={"objective": "binary:logistic",
               "n_estimators": 100,
               "random_state": 42,
               "max_depth":4,
               "learning_rate":0.01,
               "gamma": 1}

mu.xgboost_classifier(df_s7,'s7_better',param_dist_7)

#{'gamma': 1, 'learning_rate': 0.01, 'max_depth': 4, 'reg_lambda': 2, 'scale_pos_weight': 1}
# XGBoost accuracy: 0.8
# XGBoost F1: 0.1818181818181818
# XGBoost auc: 0.5416666666666667
