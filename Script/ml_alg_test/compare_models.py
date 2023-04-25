# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import util_ml as mu



#%% -  Office-related symptoms
# load df
df_SBS = pd.read_csv("../temp_data/df_SBS2.csv")


# comparing models based on target. Output: box plots ofperformance of each algorithm, and mean + (STD)
mu.compare_mlAlg(df_SBS,'SBS2')
# output: ROC curve of each algorithm
mu.roc_curve_models(df_SBS,'SBS2')

#%% -  Indoor Climate
# load df
df_ic = pd.read_csv("../temp_data/df_ic.csv")


# comparing models based on target. Output: box plots ofperformance of each algorithm and mean + (STD)
mu.compare_mlAlg(df_ic,'indoorClimate')
# output: ROC curve of each algorithm
mu.roc_curve_models(df_ic,'indoorClimate')



    

#%% -  Performance

# load df
df_perf = pd.read_csv("../temp_data/df_perf.csv")
df_perf = df_perf.reset_index(drop=True)



# comparing models based on target. Output: box plots ofperformance of each algorithm  and mean + (STD)
mu.compare_mlAlg(df_perf,'performanceOverall')
mu.roc_curve_models(df_perf,'performanceOverall')




#%% Headache

# load df
df_s1 = pd.read_csv("../temp_data/df_s1.csv")


# comparing models based on target. Output: box plots ofperformance of each algorithm  and mean + (STD)
mu.compare_mlAlg(df_s1,'s1_better')

# output: ROC curve of each algorithm
mu.roc_curve_models(df_s1,'s1_better')

#%% 0: Dry or irritated eyes
# load df
df_s0 = pd.read_csv("../temp_data/df_s0.csv")


# comparing models based on target. Output: box plots ofperformance of each algorithm  and mean + (STD)
mu.compare_mlAlg(df_s0,'s0_better')

# output: ROC curve of each algorithm
mu.roc_curve_models(df_s0,'s0_better')

#%% 3: Tiredness or fatigue
# load df
df_s3 = pd.read_csv("../temp_data/df_s3.csv")

# comparing models based on target. Output: box plots ofperformance of each algorithm  and mean + (STD)
mu.compare_mlAlg(df_s3,'s3_better')

# output: ROC curve of each algorithm
mu.roc_curve_models(df_s3,'s3_better')



#%% 7: Difficult to concentrate
# load df
df_s7 = pd.read_csv("../temp_data/df_s7.csv")


# comparing models based on target. Output: box plots ofperformance of each algorithm  and mean + (STD)
mu.compare_mlAlg(df_s7,'s7_better')

# output: ROC curve of each algorithm
mu.roc_curve_models(df_s7,'s7_better')
