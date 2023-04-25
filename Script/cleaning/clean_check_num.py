#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:12:04 2022

@author: Sophia

Clean numerical features from checklist
"""

import numpy as np
import pandas as pd
import seaborn as sns
import clean_utils as cu

from numpy import isnan
from pandas import read_csv
from sklearn.impute import KNNImputer

df_all = pd.read_csv("../temp_data/df_all.csv")


# plots
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
#sns.set(style="darkgrid")


#%% --------- measurement data

# Histograms and box plots of measurement data used in the final models. 
# These plots shows the data before missing values are replaced. 
df_all.reset_index(inplace=True, drop=True)
fig, axs = plt.subplots(2, 5, figsize=(20, 8))

sns.histplot(data=df_all, x="T_mean", color="white", ax=axs[0, 0])
sns.histplot(data=df_all, x="RH_mean", color="white", ax=axs[0, 1])
sns.histplot(data=df_all, x="sound_mean", color="white", ax=axs[0, 2])
sns.histplot(data=df_all, x="CO2_mean", color="white", ax=axs[0, 3])
sns.histplot(data=df_all, x="light_mean", color="white", ax=axs[0, 4])

sns.boxplot(data=df_all, x="T_mean", color="white", ax=axs[1, 0])
sns.boxplot(data=df_all, x="RH_mean", color="white", ax=axs[1, 1])
sns.boxplot(data=df_all, x="sound_mean", color="white", ax=axs[1, 2])
sns.boxplot(data=df_all, x="CO2_mean", color="white", ax=axs[1, 3])
sns.boxplot(data=df_all, x="light_mean", color="white", ax=axs[1, 4])

plt.show()

#check correlation: 
print("Top absolute correlation")
print(cu.get_top_abs_correlation(df_all[['T_mean','RH_mean','sound_mean','CO2_mean','light_mean','VOC_mean','light_col_mean']],10))

#%%


    
# Replace missing values with median
df_all['CO2_mean']= df_all['CO2_mean'].fillna(df_all['CO2_mean'].median())
df_all['sound_mean'] = df_all['sound_mean'].fillna(df_all['sound_mean'].median())
df_all['light_mean'] = df_all['light_mean'].fillna(df_all['light_mean'].median())
df_all['T_mean'] = df_all['T_mean'].fillna(df_all['T_mean'].median())
df_all['RH_mean'] = df_all['RH_mean'].fillna(df_all['RH_mean'].median())

df_all.reset_index(inplace=True, drop=True)
fig, axs = plt.subplots(2, 5, figsize=(20, 8))


# print plots again of how the data looks now
sns.histplot(data=df_all, x="T_mean", color="white", ax=axs[0, 0])
sns.histplot(data=df_all, x="RH_mean", color="white", ax=axs[0, 1])
sns.histplot(data=df_all, x="sound_mean", color="black", ax=axs[0, 2])
sns.histplot(data=df_all, x="CO2_mean", color="white", ax=axs[0, 3])
sns.histplot(data=df_all, x="light_mean", color="white", ax=axs[0, 4])

sns.boxplot(data=df_all, x="T_mean", color="white", ax=axs[1, 0])
sns.boxplot(data=df_all, x="RH_mean", color="white", ax=axs[1, 1])
sns.boxplot(data=df_all, x="sound_mean", color="white", ax=axs[1, 2])
sns.boxplot(data=df_all, x="CO2_mean", color="white", ax=axs[1, 3])
sns.boxplot(data=df_all, x="light_mean", color="white", ax=axs[1, 4])

plt.show()


#%% 
#notice light_mean and light_col_mean has a correllation of 0.76 -> drop light colour
#notice RH_mean and VOC have a correlation of 0.94 -> drop VOC
#notice VOC_mean and CO2_mean have a correlation of 0.70 -> drop VOC mean
"""Theis means VOC and light colour are redundent is redundant because ventilation will influence both"""

df_all = df_all.drop(['VOC_mean','light_col_mean'],axis=1)


#%% ------------ checklists

'''Make numerical features written as strings numerical'''

# window stuff
df_all['Window Area'] = df_all['O2_winArea'].apply(float)
df_all['O2_winShadePercentage'] = df_all['O2_winShadePercentage'].apply(float)
df_all['O2_opWin'] = df_all['O2_opWin'].apply(float)
df_all['O2_noOpWin'] = df_all['O2_noOpWin'].apply(float)
df_all['O2_noWinExt'] = df_all['O2_noWinExt'].apply(float)

#office dimesnion stuff
df_all['O2_floorArea'] = df_all['O2_floorArea'].apply(float)
df_all['O2_ceilHeight'] = df_all['O2_ceilHeight'].apply(float)
df_all['Office volume'] = df_all['O2_ceilHeight']*df_all['O2_floorArea']
df_all['O2_noOccupiedWorkstations'] = df_all['O2_noOccupiedWorkstations'].apply(float)
df_all['O2_noWorkstations'] = df_all['O2_noWorkstations'].apply(float)



#building type
df_all['Construction year'] = df_all['O1_constructionYear'].apply(float)

df_all['O1_renovationYear'].replace(to_replace=['None'], value=np.nan, inplace=True)
df_all['O1_renovationYear'] = df_all['O1_renovationYear'].fillna(0)
 # df_all['O1_renovationYear'] = df_all['O1_renovationYear'].map({'None': np.nan})
df_all['O1_renovationYear'] = df_all['O1_renovationYear'].apply(float)


#HVAC
df_all['O2_noSupplyDevices'].replace(to_replace=['None'], value=0, inplace=True)
df_all['O2_noSupplyDevices'] = df_all['O2_noSupplyDevices'].apply(float)
df_all['Number of supply devices'] = df_all['O2_noSupplyDevices'].apply(float)

df_all['O2_noSpaceHeatersInUse'].replace(to_replace=['2. intelligent house'], value=np.nan, inplace=True)
df_all['O2_noSpaceHeatersInUse'] = df_all['O2_noSpaceHeatersInUse'].apply(float)

df_all['O2_noSpaceHeaters'].replace(to_replace=['Most likely'], value=np.nan, inplace=True)
df_all['O2_noSpaceHeaters'] = df_all['O2_noSpaceHeaters'].apply(float)

df_all['O2_noHumidifiersInUse'] = df_all['O2_noHumidifiersInUse'].apply(float)
df_all['O2_noDehumidifiersInUse'] = df_all['O2_noDehumidifiersInUse'].apply(float)
df_all['O2_noDeskfansInUse'] = df_all['O2_noDeskfansInUse'].apply(float)



#damages
df_all['O2_wallMoistureWidth'] = df_all['O2_wallMoistureWidth'].apply(float)
df_all['O2_wallMoistureHeight'] = df_all['O2_wallMoistureHeight'].apply(float)


df_all['O2_ceilingMoistureWidth'] = df_all['O2_ceilingMoistureWidth'].apply(float)
df_all['O2_ceilingMoistureHeight'] = df_all['O2_ceilingMoistureHeight'].apply(float)


df_all['O2_wallMouldWidth'] = df_all['O2_wallMouldWidth'].apply(float)
df_all['O2_wallMouldHeight'] = df_all['O2_wallMouldHeight'].apply(float)

df_all['O2_floorDetachWidth'] = df_all['O2_floorDetachWidth'].apply(float)
df_all['O2_floorDetachHeight'] = df_all['O2_floorDetachHeight'].apply(float)

df_all['O2_floorDiscolorHeight'] = df_all['O2_floorDiscolorHeight'].apply(float)
df_all['O2_floorDiscolorWidth'] = df_all['O2_floorDiscolorWidth'].apply(float)

df_all['O2_floorScratchHeight'] = df_all['O2_floorScratchHeight'].apply(float)
df_all['O2_floorScratchWidth'] = df_all['O2_floorScratchWidth'].apply(float)

lst_dam = ['O2_wallMoistureWidth','O2_wallMoistureHeight',
           'O2_ceilingMoistureWidth','O2_ceilingMoistureHeight',
                     
           'O2_wallMouldWidth','O2_wallMouldHeight', 
           'O2_ceilingMouldWidth','O2_ceilingMouldHeight',
          
           'O2_floorDetachWidth','O2_floorDetachHeight',
           'O2_floorDiscolorHeight','O2_floorDiscolorWidth',
           'O2_floorScratchHeight','O2_floorScratchWidth']

# lav nan -> 0
df_all[lst_dam]= df_all[lst_dam].fillna(0)


df_all['area_moist'] = df_all['O2_wallMoistureWidth']*df_all['O2_wallMoistureHeight'] + df_all['O2_ceilingMoistureWidth']*df_all['O2_ceilingMoistureHeight'] 
df_all['area_mould'] = df_all['O2_wallMouldWidth']*df_all['O2_wallMouldHeight'] + df_all['O2_ceilingMouldWidth']*df_all['O2_ceilingMouldHeight'] 
df_all['area_det_floor'] = df_all['O2_floorDetachWidth']*df_all['O2_floorDetachHeight'] + df_all['O2_floorDiscolorHeight']*df_all['O2_floorDiscolorWidth'] + df_all['O2_floorScratchHeight']*df_all['O2_floorScratchWidth']

df_all.reset_index(inplace=True, drop=True)


#drop feature names that are not used anymore
df_all = df_all.drop(['O2_winArea','O1_constructionYear'],axis=1)


#%% plots of numerical featuresfor before replacement of missing values for report

fig, axs = plt.subplots(2, 3, figsize=(15, 7))
sns.histplot(data=df_all, x="Window Area",  color="white", ax=axs[0, 0])
sns.histplot(data=df_all, x="Office volume", color="white", ax=axs[0, 1])
sns.histplot(data=df_all, x="Number of supply devices", color="white", ax=axs[0, 2])

sns.boxplot(data=df_all, x="Window Area", color="white", ax=axs[1, 0])
sns.boxplot(data=df_all, x="Office volume", color="white", ax=axs[1, 1])
sns.boxplot(data=df_all, x="Number of supply devices", color="white", ax=axs[1, 2])
plt.show()



#%% ------------ window stuff

'''Assessment of window related features. How many missing values are there. 
    Should feature be dropped or missing values be replaced'''

fig, axs = plt.subplots(2, 5, figsize=(30, 10))

sns.histplot(data=df_all, x="Window Area", kde=True, color="skyblue", ax=axs[0, 0])
#sns.histplot(data=df_all, x="O2_floorArea", kde=True, color="olive", ax=axs[0, 1])
sns.histplot(data=df_all, x="O2_noWinExt", kde=True, color="teal", ax=axs[0, 1])
sns.histplot(data=df_all, x="O2_winShadePercentage", kde=True, color="gold", ax=axs[0, 2])
sns.histplot(data=df_all, x="O2_opWin", kde=True, color="red", ax=axs[0, 3])
sns.histplot(data=df_all, x="O2_noOpWin", kde=True, color="red", ax=axs[0, 4])

sns.boxplot(data=df_all, x="Window Area", color="skyblue", ax=axs[1, 0])
#sns.boxplot(data=df_all, x="O2_floorArea", color="olive", ax=axs[1, 1])
sns.boxplot(data=df_all, x="O2_noWinExt", color="teal", ax=axs[1, 1])
sns.boxplot(data=df_all, x="O2_winShadePercentage", color="gold", ax=axs[1, 2])
sns.boxplot(data=df_all, x="O2_opWin", color="red", ax=axs[1, 3])
sns.boxplot(data=df_all, x="O2_noOpWin", color="red", ax=axs[1, 4])

plt.show()



# O2_opWin (percent of operable windows)  and O2_winShadePercentage - erstat missing med 0
df_all['O2_opWin']= df_all['O2_opWin'].fillna(0)
df_all['O2_winShadePercentage']= df_all['O2_winShadePercentage'].fillna(0)

#create df to better see window features
df_win = df_all[['Window Area','O2_noWinExt','O2_winShadePercentage','O2_opWin','O2_noOpWin','O2_floorArea']]
#O2_noWinExt data ser mystisk ud, så drop til fordel for Window Area

fig, axs = plt.subplots(2, 4, figsize=(30, 10))

sns.histplot(data=df_all, x="Window Area", kde=True, color="skyblue", ax=axs[0, 0])
#sns.histplot(data=df_all, x="O2_floorArea", kde=True, color="olive", ax=axs[0, 1])
sns.histplot(data=df_all, x="O2_noWinExt", kde=True, color="teal", ax=axs[0, 1])
sns.histplot(data=df_all, x="O2_winShadePercentage", kde=True, color="gold", ax=axs[0, 2])
sns.histplot(data=df_all, x="O2_opWin", kde=True, color="red", ax=axs[0, 3])

sns.boxplot(data=df_all, x="Window Area", color="skyblue", ax=axs[1, 0])
#sns.boxplot(data=df_all, x="O2_floorArea", color="olive", ax=axs[1, 1])
sns.boxplot(data=df_all, x="O2_noWinExt", color="teal", ax=axs[1, 1])
sns.boxplot(data=df_all, x="O2_winShadePercentage", color="gold", ax=axs[1, 2])
sns.boxplot(data=df_all, x="O2_opWin", color="red", ax=axs[1, 3])

plt.show()


# Window Area and O2_noWinExt have a 0,66 correlation, and no windows have no missing values
# drop O2_noWinExt
#
#check correlation: 
print("Top absolute correlation")
print(cu.get_top_abs_correlation(df_all[['Window Area','O2_noWinExt','O2_winShadePercentage','O2_opWin','O2_noOpWin']],10))

#Drop 
df_all = df_all.drop(['O2_noWinExt','O2_noOpWin'],axis=1)

del df_win

#%%%% #office dimesnion stuff


df_all.reset_index(inplace=True, drop=True)
fig, axs = plt.subplots(2, 4, figsize=(30, 10))

sns.histplot(data=df_all, x="O2_floorArea", kde=True, color="skyblue", ax=axs[0, 0])
sns.histplot(data=df_all, x="O2_ceilHeight", kde=True, color="olive", ax=axs[0, 1])
sns.histplot(data=df_all, x="Office volume", kde=True, color="teal", ax=axs[0, 2])
sns.histplot(data=df_all, x="O2_noOccupiedWorkstations", kde=True, color="teal", ax=axs[0, 3])

sns.boxplot(data=df_all, x="O2_floorArea", color="skyblue", ax=axs[1, 0])
sns.boxplot(data=df_all, x="O2_ceilHeight", color="olive", ax=axs[1, 1])
sns.boxplot(data=df_all, x="Office volume", color="teal", ax=axs[1, 2])
sns.boxplot(data=df_all, x="O2_noOccupiedWorkstations", color="teal", ax=axs[1, 3])

plt.show()

#create df to better see window features
df_dim = df_all[['O2_floorArea','Window Area','O2_ceilHeight','Office volume','O2_noWorkstations','O2_noOccupiedWorkstations','O2_ceilHeight']]

#%%% - replace missing values related to office dimenaions based on KNN

# A data frame made of the features we want the missing values to be replaced 
# based on, is set up: 
X= df_all[['Office volume','Window Area','O2_noWorkstations','O2_floorArea','O2_ceilHeight']]

# define KKN imputer
imputer = KNNImputer()
# fit on the mini-dataset
imputer.fit(X)
# transform the dataset based on KKN imputer
Xtrans = imputer.transform(X)

# Replace original feature columns with the transformed columns where missing
# values are replaced based on KNN.
df_all['Office volume'] = Xtrans[:,0]
df_all['Window Area'] = Xtrans[:,1]
df_all['O2_noWorkstations'] = Xtrans[:,2]
df_all['O2_floorArea'] = Xtrans[:,3]
df_all['O2_ceilHeight'] = Xtrans[:,4]


# plot dimension features after missing values are replaced.
fig, axs = plt.subplots(2, 4, figsize=(30, 10))

sns.histplot(data=df_all, x="O2_floorArea", kde=True, color="skyblue", ax=axs[0, 0])
sns.histplot(data=df_all, x="O2_ceilHeight", kde=True, color="olive", ax=axs[0, 1])
sns.histplot(data=df_all, x="Office volume", kde=True, color="teal", ax=axs[0, 2])
sns.histplot(data=df_all, x="O2_noOccupiedWorkstations", kde=True, color="teal", ax=axs[0, 3])

sns.boxplot(data=df_all, x="O2_floorArea", color="skyblue", ax=axs[1, 0])
sns.boxplot(data=df_all, x="O2_ceilHeight", color="olive", ax=axs[1, 1])
sns.boxplot(data=df_all, x="Office volume", color="teal", ax=axs[1, 2])
sns.boxplot(data=df_all, x="O2_noOccupiedWorkstations", color="teal", ax=axs[1, 3])

plt.show()

del df_dim

# print total missing
#print('Missing: %d' % sum(isnan(Xtrans).flatten()))

#%%%
#Drop features that are not useful anymore. 
df_all = df_all.drop(['O2_floorArea','O2_ceilHeight'],axis=1)


#%%%% building type 
# plot building-related info to ge overview
fig, axs = plt.subplots(2, 2, figsize=(30, 10))

sns.histplot(data=df_all, x="Construction year", kde=True, color="skyblue", ax=axs[0, 0])
sns.histplot(data=df_all, x="O1_renovationYear", kde=True, color="olive", ax=axs[0, 1])

sns.boxplot(data=df_all, x="Construction year", color="skyblue", ax=axs[1, 0])
sns.boxplot(data=df_all, x="O1_renovationYear", color="olive", ax=axs[1, 1])

plt.show()



#%%%%

fig=plt.figure(figsize=(15,4))
sns.histplot(data=df_all, x="month", kde=False,color="white").set(title='Month')
plt.show()

fig=plt.figure(figsize=(15,4))
sns.histplot(data=df_all, x="Construction year", color="white").set(title='Month')
plt.show()
#%%

# Renovation Year is made into a cetegorical feature, because it was so 
# unevenly distributed

df_all['Renovation Year'] = ''
for i in range(len(df_all)): 
    if ((df_all['O1_renovationYear'][i] >= 1990) & (df_all['O1_renovationYear'][i] < 2010)): 
        df_all['Renovation Year'][i] = '1990-2009'
    elif df_all['O1_renovationYear'][i] >= 2010: 
        df_all['Renovation Year'][i] = '2010<'
    else: 
        df_all['Renovation Year'][i] = 'noRenovation'

#%%
# Make data frame to better see building-related features
df_all_bType= df_all[['Construction year','O1_renovationYear','Renovation Year']]

df_all = df_all.drop(['O1_renovationYear'],axis=1)


#%% HVAC

df_HVAC = df_all[['O2_noSupplyDevices','O2_noReturnDevices','O2_noSpaceHeatersInUse',
                  'O2_noHumidifiersInUse','O2_noDehumidifiersInUse','O2_noDeskfansInUse']]


''' Drop no space heaters that are noot in use
    otherwise make nan = 0'''

# Replace missing values with 0: 
df_all['Number of supply devices']= df_all['Number of supply devices'].fillna(0)
df_all['O2_noReturnDevices']= df_all['O2_noReturnDevices'].fillna(0)
df_all['O2_noSpaceHeatersInUse']= df_all['O2_noSpaceHeatersInUse'].fillna(0)
df_all['O2_noHumidifiersInUse']= df_all['O2_noHumidifiersInUse'].fillna(0)
df_all['O2_noDehumidifiersInUse']= df_all['O2_noDehumidifiersInUse'].fillna(0)
df_all['O2_noDeskfansInUse']= df_all['O2_noDeskfansInUse'].fillna(0)

#%% 

# fig, axs = plt.subplots(2, 3, figsize=(30, 10))
# sns.histplot(data=df_all, x="Number of supply devices", kde=True, color="skyblue", ax=axs[0, 0])
# sns.histplot(data=df_all, x="O2_noReturnDevices", kde=True, color="olive", ax=axs[0, 1])
# sns.histplot(data=df_all, x="O2_noSpaceHeatersInUse", kde=True, color="teal", ax=axs[0, 2])
# # sns.histplot(data=df_all, x="O2_noSpaceHeaters", kde=True, color="red", ax=axs[0, 3])

# sns.boxplot(data=df_all, x="Number of supply devices", color="skyblue", ax=axs[1, 0])
# sns.boxplot(data=df_all, x="O2_noReturnDevices", color="olive", ax=axs[1, 1])
# sns.boxplot(data=df_all, x="O2_noSpaceHeatersInUse", color="teal", ax=axs[1, 2])
# # sns.boxplot(data=df_all, x="O2_noSpaceHeaters", color="red", ax=axs[1, 3])
# plt.show()


#%% 

fig, axs = plt.subplots(2, 3, figsize=(15, 5))
sns.histplot(data=df_all, x="O2_noHumidifiersInUse", kde=True, color="skyblue", ax=axs[0, 0])
sns.histplot(data=df_all, x="O2_noDehumidifiersInUse", kde=True, color="olive", ax=axs[0, 1])
sns.histplot(data=df_all, x="O2_noDeskfansInUse", kde=True, color="teal", ax=axs[0, 2])

sns.boxplot(data=df_all, x="O2_noHumidifiersInUse", color="skyblue", ax=axs[1, 0])
sns.boxplot(data=df_all, x="O2_noDehumidifiersInUse", color="olive", ax=axs[1, 1])
sns.boxplot(data=df_all, x="O2_noDeskfansInUse", color="teal", ax=axs[1, 2])
plt.show()

# No dehumidifyers - drop 
# Only 2 desk fan in used - drop
# Only 5 humidifyers in used in total - drop


fig, axs = plt.subplots(2, 2, figsize=(30, 10))

sns.histplot(data=df_all, x="Number of supply devices", kde=True, color="skyblue", ax=axs[0, 0])
sns.histplot(data=df_all, x="O2_noSpaceHeatersInUse", kde=True, color="olive", ax=axs[0, 1])

sns.boxplot(data=df_all, x="Number of supply devices", color="skyblue", ax=axs[1, 0])
sns.boxplot(data=df_all, x="O2_noSpaceHeatersInUse", color="olive", ax=axs[1, 1])
plt.show()
#%% 
#Drop
df_all = df_all.drop(['O2_noSpaceHeaters','O2_noHumidifiersInUse','O2_noDehumidifiersInUse',
                      'O2_noDeskfansInUse','O2_noSupplyDevices','O2_noReturnDevices'],axis=1)

#O2_noSupplyDevices and O2_noReturnDevices has correlation of 1 -> removing one

del df_HVAC
#%% 
# #%% damages to office


#make nan 0 :
df_all['area_moist']= df_all['area_moist'].fillna(0)
df_all['area_mould']= df_all['area_mould'].fillna(0)
df_all['area_det_floor']= df_all['area_det_floor'].fillna(0)


df_dam = df_all[['area_moist','area_mould','area_det_floor']]



fig, axs = plt.subplots(2, 3, figsize=(30, 10))

sns.histplot(data=df_all, x="area_moist", kde=True, color="skyblue", ax=axs[0, 0])
sns.histplot(data=df_all, x="area_mould", kde=True, color="olive", ax=axs[0, 1])
sns.histplot(data=df_all, x="area_det_floor", kde=True, color="teal", ax=axs[0, 2])


sns.boxplot(data=df_all, x="area_moist", color="skyblue", ax=axs[1, 0])
sns.boxplot(data=df_all, x="area_mould", color="olive", ax=axs[1, 1])
sns.boxplot(data=df_all, x="area_det_floor", color="teal", ax=axs[1, 2])

plt.show()


#no mold - should drop
# moist, only few, med stor spredning (ser ud som om man har brugt forskellige dimensioner) - drop


# keep deteriation





#%%
#Now drop the original features
df_all = df_all.drop(['O2_wallMoistureWidth','O2_wallMoistureHeight',
                'O2_ceilingMoistureWidth','O2_ceilingMoistureHeight',
                'O2_paintDetachWidth','O2_paintDetachHeight',
                
                'O2_wallMouldWidth','O2_wallMouldHeight', 
                'O2_ceilingMouldWidth','O2_ceilingMouldHeight',       
                
                'O2_floorDetachWidth','O2_floorDetachHeight',
                'O2_floorDiscolorHeight','O2_floorDiscolorWidth',
                'O2_floorScratchHeight','O2_floorScratchWidth',
                
                'area_moist','area_mould'

                ],axis=1)

del df_dam


#%% questionnaire

sns.histplot(data=df_all, x="month", kde=True, color="skyblue")
plt.show()

print(df_all['month'].value_counts())
#%% -- correlation



print("Top absolute correlation")
print(cu.get_top_abs_correlation(df_all[['Window Area','O2_winShadePercentage','O2_opWin',
                                         'Office volume','O2_noOccupiedWorkstations','O2_noWorkstations',
                                         'Construction year','O2_noSpaceHeatersInUse','Number of supply devices',
                                         'area_det_floor']],10))
#%% 
#del [axs, fig] 


# correlation between O2_noWorkstations and office volume = 0.92
# correlation between O2_noOccupiedWorkstations and office_volume = 0.78

# drop these as we have more accurate info about how many people are in the room.
df_all = df_all.drop(['O2_noOccupiedWorkstations','O2_noWorkstations'],axis=1)
#%% 
print(cu.get_top_abs_correlation(df_all[['CO2_mean','RH_mean','T_mean','light_mean','sound_mean',
                   
                                         'Window Area','O2_winShadePercentage','O2_opWin',
                                         'Office volume',
                                         'Construction year',
                                         'O2_noSpaceHeatersInUse','Number of supply devices',
                                         'area_det_floor', 'month',]],10))

#%% -- correlation

df_all.to_csv("../temp_data/df_all_numClean.csv", index=False)






#%% plots for report

# Construction year, office volume, window area, month, number of diffusers



fig, axs = plt.subplots(2, 3, figsize=(15, 7))

sns.histplot(data=df_all, x="Window Area", color="white", ax=axs[0, 0])
sns.histplot(data=df_all, x="Office volume", color="white", ax=axs[0, 1])
sns.histplot(data=df_all, x="Number of supply devices", color="white", ax=axs[0, 2])


sns.boxplot(data=df_all, x="Window Area", color="white", ax=axs[1, 0])
sns.boxplot(data=df_all, x="Office volume", color="white", ax=axs[1, 1])
sns.boxplot(data=df_all, x="Number of supply devices", color="white", ax=axs[1, 2])

plt.show()



