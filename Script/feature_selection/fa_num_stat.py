#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 12:57:12 2022

@author: Sophia Wesche

Input:  dataframe with only numerical features and target, 
        dataframe with numerical and ordinal features and target
    
Output: Dataframe of tau, kendall's tau p-value, F-score, ANOVA p-value,
        The same dataframe but only with features with tau p-value < 0.05. 
        The same dataframe but only with features with ANOVA p-value < 0.05. 
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import f_classif
from sklearn.preprocessing import StandardScaler
from scipy import stats

import fs_utils as fu


"load cleaned dataframe"
df_all = pd.read_csv("../temp_data/df_all_catClean.csv")


#%%
'''Multiple office-related symptoms'''

#make df of only numerical features and the target
df_all_num = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                      'Window Area','O2_winShadePercentage','O2_opWin',
                      'Office volume',
                      'Construction year',
                      'O2_noSpaceHeatersInUse','Number of supply devices',
                      'area_det_floor', 'month',
                      'SBS2']].copy()

#make df of numerical and ordinal features and the target
df_all_num_ord = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                          'Window Area','O2_winShadePercentage','O2_opWin',
                          'Office volume',
                          'Construction year',
                          'O2_noSpaceHeatersInUse','Number of supply devices',
                          'area_det_floor', 'month',
                          
                          'personsInOffice','hoursatdesk','age','Floor mopping frequency',
                          'Renovation Year','deskWash','floorVacuum','winWash',
                          'envMat_clean','office_crackWinPaint','office_desklights',
                          'distToWindow','daylight',
                          'SBS2']].copy()


# create output data frames accordig to kendall's tau and ANOVA tests. 
SBS_df,tauSBS_df,ANOVASBS_df = fu.tau_ANOVA(df_all_num,df_all_num_ord,'SBS2')


#%%
 
'''indoor climate '''
# reduce to 0 = bad building performance, 1 = good performance
df_all['indoorClimate'] = df_all['indoorClimate'].apply(fu.reduce_ic)

#make df of only numerical features and the target
df_all_num = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                      'Window Area','O2_winShadePercentage','O2_opWin',
                      'Office volume',
                      'Construction year',
                      'O2_noSpaceHeatersInUse','Number of supply devices',
                      'area_det_floor', 'month',
                      'indoorClimate']].copy()

#make df of numerical and ordinal features and the target
df_all_num_ord = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                          'Window Area','O2_winShadePercentage','O2_opWin',
                          'Office volume',
                          'Construction year',
                          'O2_noSpaceHeatersInUse','Number of supply devices',
                          'area_det_floor', 'month',
                          
                          'personsInOffice','hoursatdesk','age','Floor mopping frequency',
                          'Renovation Year','deskWash','floorVacuum','winWash',
                          'envMat_clean','office_crackWinPaint','office_desklights',
                          'distToWindow','daylight',
                          'indoorClimate']].copy()

# create output data frames accordig to kendall's tau and ANOVA tests. 
ic_df,tauIC_df,ANOVAic_df = fu.tau_ANOVA(df_all_num,df_all_num_ord,'indoorClimate')


#%%

'''Performance '''
df_all['performanceOverall'] = df_all['performanceOverall'].apply(fu.reduce_perf)

#make df of only numerical features and the target
df_all_num = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                     'Window Area','O2_winShadePercentage','O2_opWin',
                     'Office volume',
                     'Construction year',
                     'O2_noSpaceHeatersInUse','Number of supply devices',
                     'area_det_floor', 'month',
                     'performanceOverall']].copy()

#make df of numerical and ordinal features and the target
df_all_num_ord = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                         'Window Area','O2_winShadePercentage','O2_opWin',
                         'Office volume',
                         'Construction year',
                         'O2_noSpaceHeatersInUse','Number of supply devices',
                         'area_det_floor', 'month',
                         'personsInOffice','hoursatdesk','age','Floor mopping frequency',
                         'Renovation Year','deskWash','floorVacuum','winWash',
                         'envMat_clean','office_crackWinPaint','office_desklights',
                         'distToWindow','daylight',
                         
                         'performanceOverall']].copy()

# create output data frames accordig to kendall's tau and ANOVA tests. 
perf_df,tauP_df,ANOVAP_df = fu.tau_ANOVA(df_all_num,df_all_num_ord,'performanceOverall')


#%% s1: headache

'''Headahe '''


#make df of only numerical features and the target
dfs1_num = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                     'Window Area','O2_winShadePercentage','O2_opWin',
                     'Office volume',
                     'Construction year',
                     'O2_noSpaceHeatersInUse','Number of supply devices',
                     'area_det_floor', 'month',
                     's1_better']].copy()

#make df of numerical and ordinal features and the target
dfs1_num_ord = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                     'Window Area','O2_winShadePercentage','O2_opWin',
                     'Office volume',
                     'Construction year',
                     'O2_noSpaceHeatersInUse','Number of supply devices',
                     'area_det_floor', 'month',
                     'hoursatdesk','age','Floor mopping frequency',
                     'Renovation Year','deskWash','floorVacuum','winWash',
                     'envMat_clean','office_desklights',
                     'distToWindow','daylight',
                         
                     's1_better']].copy()

# create output data frames accordig to kendall's tau and ANOVA tests. 
s1_df,taus1_df,ANOVA_s1_df = fu.tau_ANOVA(dfs1_num,dfs1_num_ord,'s1_better')


#%% s0: Dry or irritated eyes

'''Dry or irritated eyes '''

#make df of only numerical features and the target
dfs0_num = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                     'Window Area','O2_winShadePercentage','O2_opWin',
                     'Office volume',
                     'Construction year',
                     'O2_noSpaceHeatersInUse','Number of supply devices',
                     'area_det_floor', 'month',
                     's0_better']].copy()

#make df of numerical and ordinal features and the target
dfs0_num_ord = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                     'Window Area','O2_winShadePercentage','O2_opWin',
                     'Office volume',
                     'Construction year',
                     'O2_noSpaceHeatersInUse','Number of supply devices',
                     'area_det_floor', 'month',
                     'hoursatdesk','age','Floor mopping frequency',
                     'Renovation Year','deskWash','floorVacuum','winWash',
                     'envMat_clean','office_desklights',
                     'distToWindow','daylight',
                         
                     's0_better']].copy()

# create output data frames accordig to kendall's tau and ANOVA tests. 
s0_df,taus0_df,ANOVA_s0_df = fu.tau_ANOVA(dfs0_num,dfs0_num_ord,'s0_better')


#%% s3: Tiredness or fatigue

'''Tiredness or fatigue'''

#make df of only numerical features and the target
dfs3_num = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                     'Window Area','O2_winShadePercentage','O2_opWin',
                     'Office volume',
                     'Construction year',
                     'O2_noSpaceHeatersInUse','Number of supply devices',
                     'area_det_floor', 'month',
                     's3_better']].copy()

#make df of numerical and ordinal features and the target
dfs3_num_ord = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                     'Window Area','O2_winShadePercentage','O2_opWin',
                     'Office volume',
                     'Construction year',
                     'O2_noSpaceHeatersInUse','Number of supply devices',
                     'area_det_floor', 'month',
                     'hoursatdesk','age','Floor mopping frequency',
                     'Renovation Year','deskWash','floorVacuum','winWash',
                     'envMat_clean','office_desklights',
                     'distToWindow','daylight',
                         
                     's3_better']].copy()

# create output data frames accordig to kendall's tau and ANOVA tests. 
s3_df,taus3_df,ANOVA_s3_df = fu.tau_ANOVA(dfs3_num,dfs3_num_ord,'s3_better')


#%% s7: Difficult to concentrate

'''Difficult to concentrate'''

#make df of only numerical features and the target
dfs7_num = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                     'Window Area','O2_winShadePercentage','O2_opWin',
                     'Office volume',
                     'Construction year',
                     'O2_noSpaceHeatersInUse','Number of supply devices',
                     'area_det_floor', 'month',
                     's7_better']].copy()

#make df of numerical and ordinal features and the target
dfs7_num_ord = df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                     'Window Area','O2_winShadePercentage','O2_opWin',
                     'Office volume',
                     'Construction year',
                     'O2_noSpaceHeatersInUse','Number of supply devices',
                     'area_det_floor', 'month',
                     'hoursatdesk','age','Floor mopping frequency',
                     'Renovation Year','deskWash','floorVacuum','winWash',
                     'envMat_clean','office_desklights',
                     'distToWindow','daylight',
                         
                     's7_better']].copy()

# create output data frames accordig to kendall's tau and ANOVA tests. 
s7_df,taus7_df,ANOVA_s7_df = fu.tau_ANOVA(dfs7_num,dfs7_num_ord,'s7_better')