# -*- coding: utf-8 -*-

"""
Created on Tue Oct 25 09:33:57 2022

@author: Sophia Wesche

In this document features are manually removed according to the filter selection
and the correlation between the features. 

Input: Cleaned dataframe.

Output: Heat maps of correlation between features kept in model dataframe
        Plot of target balance
        Dataframes for each model saved after feature selection is performed. 
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Import association_metric for categorical correlation
import association_metrics as am
import pandas as pd
from dython.nominal import associations
from dython.nominal import identify_nominal_columns
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

import fs_utils as fu

df_all = pd.read_csv("../temp_data/df_all_catClean.csv")

#%%
# make feature of window area per office volume
df_all['winA_perVol'] = df_all['Window Area']/df_all['Office volume']


#%% -  Indoor climate data frame
# drop features based on feature selection: 
df_ic = df_all.drop(['performanceOverall','s0_better','s1_better','s3_better','s7_better','SBS1','SBS2',
                     'symptabilitywork','symptstayhome',
                     'buildingID','officeID',
                     
                     #general
                     'location','month','Renovation Year','Construction year',
                     
                     'lightTooMuchDaylight','lightTooLittleDaylight',
                     'lightNoTask','lightReflections','lightFlicker',
                     'lightTooMuchDaylight','lightTooLittleDaylight','lightTooBright',
                     'lightLED','lightIncan','lightFlour','lightTooDark','office_desklights',
                     'daylight',
                     
                     #windows
                     'occupant_windowOrientation',#'Window Area',
                     'winA_perVol',
                     'O2_winShadePercentage','O2_opWin','office_windowOrientation',
                     
                     
                     
                     #envelope
                     'building_extWallType','building_insType','building_facadeType',
                     
                     #office surfaces
                     'floorPlastic','office_crackWinPaint','otherColArt',
                     'office_ceilingFinish','floorCarpet','office_wallFinish',
                     'suspendedCeiling','floorWood','floorPlastic','area_det_floor',
                     
                     #cleaning 
                     'deskWash','winWash','floorVacuum','envMat_clean',
                     
                     #HVAC
                     'radiatorHeat','airHeat','building_coolType',
                     'bVentType','office_returnAir','office_supplyAir',
                     'O2_noSpaceHeatersInUse','O2_noSpaceHeatersInUse', 
                     
                     
                     
                     #exterior
                     'Site',
                     'viewRoadBuildings',
                     'outdoorCont_powerPlants',
                     'outdoorCont_constructionActivities',
                     'noOutdoorContSources','outdoorCont_smokeGenerators',
                     'outdoorCont_garbageDumpsters','outdoorCont_heavyTraffic',
                     
                     #noise:
                     'noiseExterior','noiseOfficeEquipment','noiseTelephones',
                     
                     #odours:
                     'carpet','perfume','food','smells_outside','tobaccoSmoke','tech','cleaningProd',
                     
                     #office
                     'otherLounge','otherPlantWater','personsInOffice','officeInterior',#'Office volume',
                     
                     #occupant:
                     'age','job','distToWindow','hoursatdesk','smoker','eyeWear',
                     
                     ],axis=1)

#%%

# reduce to 0 = bad building performance, 1 = good performance
df_ic['indoorClimate'] = df_ic['indoorClimate'].apply(fu.reduce_ic)

df_ic = df_ic.dropna(subset=['indoorClimate'])

#sns.catplot(data=df_ic, x="indoorClimate", kind="count", palette="ch:.25",aspect=40/10)


#%%

'''It calculates the correlation/strength-of-association of 
    features in the data-set with both categorical and continuous 
    features using: Pearson’s R for continuous-continuous cases, 
    Correlation Ratio for categorical-continuous cases, Cramer’s 
    V or Theil’s U for categorical-categorical cases.'''
# Make correlation plot between features in final dataframe 
categorical_features=identify_nominal_columns(df_ic)
complete_correlation= associations(df_ic, filename= 'complete_correlation.png', figsize=(30,10))
df_complete_corr=complete_correlation['corr']
df_complete_corr.dropna(axis=1, how='all').dropna(axis=0, how='all').style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)

#%% plot target classes 
sns.catplot(data=df_ic, x="indoorClimate", kind="count", palette="ch:.25",height=4,aspect=3/2).set(title='Occupant satisfaction with indoor climate')
plt.show()

#%%
# save final data frame for indoor climate
df_ic = df_ic.reset_index(drop=True)
df_ic.to_csv("../temp_data/df_ic.csv", index=False)

#%% -  performance df

# drop features based on feature selection

df_perf = df_all.drop(['indoorClimate', 's0_better','s1_better','s3_better','s7_better','SBS1','SBS2',
                       'symptabilitywork','symptstayhome',
                       'buildingID','officeID',
                       
                       #general
                        'month','location','Renovation Year',#'Construction year'
                       
                        
                        
                        #light
                        'lightTooLittleDaylight','lightTooMuchDaylight','lightNoTask','daylight',
                        'lightReflections','lightTooDark','lightTooBright','lightFlicker',
                        'lightFlour','lightLED','lightIncan','office_desklights',
                        
                        #windows
                        'occupant_windowOrientation',#'Window Area',
                        'winA_perVol',
                        'O2_winShadePercentage','O2_opWin','office_windowOrientation',
                       
                        
                        #envelope
                        'building_extWallType','building_insType','building_facadeType',
                        
                        # office surfaces
                        'office_wallFinish',
                        'office_ceilingFinish',
                        'otherColArt','office_crackWinPaint','floorPlastic',
                        'area_det_floor','suspendedCeiling','floorCarpet','floorWood',
                       
                        
                        #Office setup/facilities
                        'personsInOffice','Office volume',
                        'otherLounge','otherPlantWater',
                       
                        #cleaning
                        'deskWash','winWash','floorVacuum','envMat_clean',
                        
                        # occupant
                        'smoker','distToWindow','hoursatdesk','job',
                       
                        #HVAC
                        'airHeat','radiatorHeat','bVentType','building_coolType','O2_noSpaceHeatersInUse',
                        'office_supplyAir','office_returnAir',#'Number of supply devices',
                        
                        # exterior
                        'Site','viewRoadBuildings','viewGreenNature',
                        'outdoorCont_powerPlants','outdoorCont_constructionActivities',
                        'noOutdoorContSources','outdoorCont_heavyTraffic','outdoorCont_smokeGenerators',
                        'outdoorCont_garbageDumpsters','outdoorCont_garbageDumpsters',
                        
                        #noise
                        'noiseOfficeEquipment','noiseExterior','sound_mean','noiseTelephones',
                       
                        #odour
                        'carpet','perfume','food','tobaccoSmoke','cleaningProd','smells_outside','tech',
                        
                        
                        ],axis=1)


df_perf = df_perf.dropna(subset=['performanceOverall'])

#%%
# reduce target classes to two classes. 
df_perf['performanceOverall'] = df_perf['performanceOverall'].apply(fu.reduce_perf)

#%% plot classes
sns.catplot(data=df_perf, x="performanceOverall", kind="count", palette="ch:.25",height=4,aspect=3/2).set(title='Occupant performance')
plt.show()


#%% 
# Make correlation plot between features in final dataframe 
categorical_features=identify_nominal_columns(df_perf)
complete_correlation= associations(df_perf, filename= 'complete_correlation.png', figsize=(30,10))

df_complete_corr=complete_correlation['corr']
df_complete_corr.dropna(axis=1, how='all').dropna(axis=0, how='all').style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)


# ligthTooBright and Daylight: 0.71 - > drop ligthTooBright


# renovation year and outdoorCont_garbagedispenser: 0.83
# Renovation Year and floorCarpet : 0.82
#  outdoorCont_garbageDumpsters and floorCarpet: 0.73
#  Renovation Year and outdoorCont_emergencyGenerators : 0.83
#  outdoorCont_smokeStack and outdoorCont_emergencyGenerators : 0.73
 #-----> drop outdoorCont_garbageDumpsters, floorCarpet, outdoorCont_emergencyGenerators
 
# suspended ceiling and buildingFacadeType: 0.79

#....> drop buildingFacadeType

# officeSupplyAir and Number of supply devices - >below 0.7 so keep for now


# PersonsInOffice and officeInterior - > 0.81 - >drop personsInOffice

# area_det_floor and officereturnAir - > 0.78 - > drop area_det_floor



#%%

#save final performance df. 
df_perf.to_csv("../temp_data/df_perf.csv", index=False)




#%% -  symptom 1: headache df
df_s1 = df_all.drop(['performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
                     's0_better','s3_better','s7_better','SBS1','SBS2',
                     'buildingID','officeID',
                     
                     #General
                     'Renovation Year','month',
                     'location',
                    
                     
                     #light
                     'lightFlicker','lightReflections','lightTooDark',
                     'lightTooBright','light_mean','lightNoTask',
                     'lightTooLittleDaylight','lightTooMuchDaylight','daylight',
                     'lightLED','lightIncan','lightFlour','office_desklights',
                    
                     #windows
                     'occupant_windowOrientation','O2_winShadePercentage',
                     'O2_opWin','Window Area','winA_perVol','office_windowOrientation',
                     
                     #building envelope
                     'building_extWallType','building_insType','building_facadeType',
                    
                     # office surfaces
                     'office_wallFinish','office_ceilingFinish','suspendedCeiling',
                     'floorCarpet','floorWood','floorPlastic','otherColArt',
                     'office_crackWinPaint','area_det_floor',
                     
                     #Office setup/facilities
                     'personsInOffice','otherPlantWater','otherLounge',
                     'Office volume','officeInterior',
                    
                     #clean
                     'deskWash','envMat_clean','winWash','floorVacuum',
                     'Floor mopping frequency',
                     
                     #Occupant
                     'job','smoker','distToWindow','hoursatdesk','eyeWear',
                    
                     # HVAC
                     'airHeat','radiatorHeat','bVentType',
                     'office_returnAir','office_supplyAir','bVentType',
                     'O2_noSpaceHeatersInUse','RH_mean','building_coolType',
                     'Number of supply devices','T_mean',
                    
                     #exterior
                     'viewRoadBuildings','viewGreenNature',
                     'outdoorCont_heavyTraffic','outdoorCont_garbageDumpsters',
                     'outdoorCont_powerPlants','outdoorCont_constructionActivities',
                     'outdoorCont_smokeGenerators','noOutdoorContSources',
                     'Site',
                    
                     # noise
                     'sound_mean','noiseOfficeEquipment','noiseTelephones',
                     'talk','noiseExterior',
                     
                     #Odours occupants
                     'cleaningProd','perfume','food','tobaccoSmoke','tech',
                     'carpet','smells_outside',
                     ],axis=1)


#%%

sns.catplot(data=df_s1, x="s1_better", kind="count", palette="ch:.25",height=4,aspect=1).set(title='Headache')
print(df_s1['s1_better'].value_counts())
#df_s1 = df_s1.dropna(subset=['symp1'])

#%%
# Make correlation plot between features in final dataframe 
categorical_features=identify_nominal_columns(df_s1)
complete_correlation= associations(df_s1, filename= 'complete_correlation.png', figsize=(30,10))
df_complete_corr=complete_correlation['corr']
df_complete_corr.dropna(axis=1, how='all').dropna(axis=0, how='all').style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)



df_s1.to_csv("../temp_data/df_s1.csv", index=False)


#%% -  symptom 0: Dry or irritated eyes
df_s0 = df_all.drop(['performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
                     's1_better','s3_better','s7_better','SBS1','SBS2',
                     'buildingID','officeID',
                     
                     #General
                     'Renovation Year','month',
                     'location','Construction year',
                    
                     
                     #light
                     'lightFlicker','lightReflections','lightTooDark',
                     'lightTooBright','lightNoTask',
                     'lightTooLittleDaylight','lightTooMuchDaylight','daylight',
                     'lightLED','lightIncan','lightFlour','office_desklights',
                    
                     #windows
                     'occupant_windowOrientation','O2_winShadePercentage',
                     'O2_opWin','Window Area','winA_perVol','office_windowOrientation',
                     
                     #building envelope
                     'building_extWallType','building_insType','building_facadeType',
                    
                     # office surfaces
                     'office_wallFinish','office_ceilingFinish','suspendedCeiling',
                     'floorCarpet','floorWood','floorPlastic','otherColArt',
                     'office_crackWinPaint','area_det_floor',
                     
                     #Office setup/facilities
                     'personsInOffice','otherPlantWater','otherLounge',
                     'officeInterior',
                    
                     #clean
                     'deskWash','envMat_clean','winWash','floorVacuum',
                     'Floor mopping frequency',
                     
                     #Occupant
                     'job','age','smoker','distToWindow','hoursatdesk',
                    
                     # HVAC
                     'airHeat','radiatorHeat','bVentType',
                     'office_returnAir','office_supplyAir','bVentType',
                     'O2_noSpaceHeatersInUse','building_coolType','Number of supply devices',
                    
                     #exterior
                     'viewRoadBuildings','viewGreenNature',
                     'outdoorCont_heavyTraffic','outdoorCont_garbageDumpsters',
                     'outdoorCont_powerPlants','outdoorCont_constructionActivities',
                     'outdoorCont_smokeGenerators','noOutdoorContSources','Site',
                     
                    
                     # noise
                     'sound_mean','noiseOfficeEquipment','noiseTelephones',
                     'talk','noiseExterior',
                     
                     #Odours occupants
                     'tech', 'carpet','perfume','smells_outside','cleaningProd','food','tobaccoSmoke'
                     
                     ],axis=1)



#%%
sns.catplot(data=df_s0, x="s0_better", kind="count", palette="ch:.25",height=4,aspect=1).set(title='Dry or irritated eyes')
print(df_s0['s0_better'].value_counts())

#%%
# Make correlation plot between features in final dataframe 
categorical_features=identify_nominal_columns(df_s0)
complete_correlation= associations(df_s0, filename= 'complete_correlation.png', figsize=(30,10))
df_complete_corr=complete_correlation['corr']
df_complete_corr.dropna(axis=1, how='all').dropna(axis=0, how='all').style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)

#%%


df_s0.to_csv("../temp_data/df_s0.csv", index=False)


#%% -  symptom 3: Tiredness or fatigue
df_s3 = df_all.drop(['performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
                     's0_better','s1_better','s7_better','SBS1','SBS2',
                     'buildingID','officeID',
                     
                     #General
                     #
                     'month',
                     'location','Renovation Year',#'Construction year',
                    
                     
                     #light
                     'lightFlicker','lightReflections','lightTooDark',
                     'lightTooBright','lightNoTask',
                     'lightTooLittleDaylight','lightTooMuchDaylight','daylight',
                     'lightLED','lightIncan','lightFlour','office_desklights',
                     
                    
                     #windows
                     'occupant_windowOrientation',
                     'O2_winShadePercentage',
                     'O2_opWin','Window Area','winA_perVol','office_windowOrientation',
                     
                     #building envelope
                     'building_extWallType','building_insType','building_facadeType',
                    
                     # office surfaces
                     'office_wallFinish','suspendedCeiling',
                     'floorCarpet','floorWood','floorPlastic','otherColArt',
                     'office_crackWinPaint','area_det_floor',
                     'office_ceilingFinish',
                     
                     #Office setup/facilities
                     'personsInOffice',
                     'otherPlantWater','otherLounge','Office volume',
                     'officeInterior',
                    
                     #clean
                     'deskWash','envMat_clean','winWash','floorVacuum',
                     'Floor mopping frequency',
                     
                     #Occupant
                     'job','sex','smoker','distToWindow','hoursatdesk','eyeWear',
                    
                     # HVAC
                     'airHeat','radiatorHeat','bVentType','RH_mean',
                     'office_returnAir','office_supplyAir','bVentType',
                     'O2_noSpaceHeatersInUse','building_coolType','Number of supply devices',
                    
                     #exterior
                     'viewRoadBuildings','viewGreenNature',
                     'outdoorCont_heavyTraffic','outdoorCont_garbageDumpsters',
                     'outdoorCont_powerPlants','outdoorCont_constructionActivities',
                     'outdoorCont_smokeGenerators','noOutdoorContSources',#'Site',
                     
                    
                     # noise
                     'sound_mean',#'noiseOfficeEquipment','noiseTelephones',
                     #'talk','noiseExterior',
                     
                     #Odours occupants
                     #'smells_outside',
                     'perfume','cleaningProd','food',
                     'tobaccoSmoke','tech', 'carpet',
                     ],axis=1)



#%%
sns.catplot(data=df_s3, x="s3_better", kind="count", palette="ch:.25",height=4,aspect=1).set(title='Tiredness or fatigue')
print(df_s3['s3_better'].value_counts())

# Make correlation plot between features in final dataframe 
categorical_features=identify_nominal_columns(df_s3)
complete_correlation= associations(df_s3, filename= 'complete_correlation.png', figsize=(30,10))
df_complete_corr=complete_correlation['corr']
df_complete_corr.dropna(axis=1, how='all').dropna(axis=0, how='all').style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)

#%%

df_s3.to_csv("../temp_data/df_s3.csv", index=False)




#%% -  symptom 7: Difficult to concentrate
df_s7 = df_all.drop(['performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
                     's0_better','s1_better','s3_better','SBS1','SBS2',
                     'buildingID','officeID',
                     
                     #General
                     'month',
                     'location','Renovation Year',#'Construction year',
                    
                     
                     #light
                     'lightFlicker','lightTooDark','lightReflections','lightTooBright',#'light_mean'
                     'lightNoTask',
                     'lightTooLittleDaylight','lightTooMuchDaylight','daylight',
                     'lightLED','lightIncan','lightFlour','office_desklights',
                     
                    
                     #windows
                     'occupant_windowOrientation',
                     'O2_winShadePercentage',
                     'O2_opWin','Window Area','winA_perVol','office_windowOrientation',
                     
                     #building envelope
                     'building_extWallType','building_insType','building_facadeType',
                    
                     # office surfaces
                     'office_wallFinish','suspendedCeiling',
                     'floorCarpet','floorWood','floorPlastic','otherColArt',
                     'office_crackWinPaint','area_det_floor',
                     'office_ceilingFinish',
                     
                     #Office setup/facilities
                     'personsInOffice',
                     'otherPlantWater','Office volume','otherLounge',
                     'officeInterior',
                    
                     #clean
                     'deskWash','envMat_clean','winWash','floorVacuum',
                     'Floor mopping frequency',
                     
                     #Occupant
                     'job','distToWindow','eyeWear',
                     'smoker','hoursatdesk',#'age','sex',
                    
                     # HVAC
                     'airHeat','radiatorHeat','bVentType',
                     'office_returnAir','office_supplyAir','bVentType',
                     'O2_noSpaceHeatersInUse','building_coolType',
                     'Number of supply devices','RH_mean','T_mean',
                    
                     #exterior
                     'viewRoadBuildings','viewGreenNature',
                     'outdoorCont_heavyTraffic',
                     'outdoorCont_garbageDumpsters',
                     'outdoorCont_powerPlants','outdoorCont_constructionActivities',
                     'outdoorCont_smokeGenerators','noOutdoorContSources','Site',
                     
                    
                     # noise
                     #'sound_mean','noiseOfficeEquipment','noiseTelephones',
                     #'talk','noiseExterior',
                     
                     #Odours occupants
                     'smells_outside',
                     'perfume','cleaningProd','food',
                     'tobaccoSmoke','tech', 'carpet',
                     
                     ],axis=1)


#%%
sns.catplot(data=df_s7, x="s7_better", kind="count", palette="ch:.25",height=4,aspect=1).set(title='Difficult to concentrate')
print(df_s7['s7_better'].value_counts())


# Make correlation plot between features in final dataframe 
categorical_features=identify_nominal_columns(df_s7)
complete_correlation= associations(df_s7, filename= 'complete_correlation.png', figsize=(30,10))
df_complete_corr=complete_correlation['corr']
df_complete_corr.dropna(axis=1, how='all').dropna(axis=0, how='all').style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)

#%%

df_s7.to_csv("../temp_data/df_s7.csv", index=False)


#%% -  SBS2
df_SBS2 = df_all.drop(['performanceOverall','indoorClimate','symptabilitywork','symptstayhome',
                     's0_better','s1_better','s3_better','s7_better','SBS1',
                     'buildingID','officeID',
                     
                     #General
                     'month','location','Renovation Year',#'Construction year',
                    
                     
                     #light
                     'lightFlicker',
                     'lightReflections',
                     'lightTooBright',
                     'lightNoTask',#'lightTooDark',
                     'lightTooLittleDaylight','lightTooMuchDaylight','daylight',
                     'lightLED','lightIncan','lightFlour','office_desklights',
                     
                    
                     #windows
                     'occupant_windowOrientation',
                     'O2_winShadePercentage',
                     'O2_opWin','Window Area','winA_perVol','office_windowOrientation',
                     
                     #building envelope
                     'building_extWallType','building_insType','building_facadeType',
                    
                     # office surfaces
                     'office_wallFinish','suspendedCeiling',
                     'floorCarpet','floorWood','floorPlastic','otherColArt',
                     'office_crackWinPaint','area_det_floor',
                     'office_ceilingFinish',
                     
                     #Office setup/facilities
                     'personsInOffice',
                     'otherPlantWater','otherLounge','Office volume',
                     'officeInterior',
                    
                     #clean
                     'deskWash','envMat_clean','winWash','floorVacuum',
                     #'Floor mopping frequency',
                     
                     #Occupant
                     'job',#'sex',
                     'smoker','distToWindow','hoursatdesk','eyeWear',
                    
                     # HVAC
                     'airHeat','radiatorHeat','bVentType',
                     'office_returnAir','office_supplyAir','bVentType',
                     'O2_noSpaceHeatersInUse',
                     'building_coolType',#'Number of supply devices',
                    
                     #exterior
                     'viewRoadBuildings','viewGreenNature',
                     'outdoorCont_heavyTraffic','outdoorCont_garbageDumpsters',
                     'outdoorCont_powerPlants','outdoorCont_constructionActivities',
                     'outdoorCont_smokeGenerators','noOutdoorContSources','Site',
                     
                    
                     # noise
                     'noiseTelephones','noiseExterior','sound_mean',
                     #'talk','noiseOfficeEquipment',
                     
                     #Odours occupants
                     'smells_outside',
                     'perfume','cleaningProd','food',
                     'tobaccoSmoke','tech', 'carpet',
                     ],axis=1)



#%%
sns.catplot(data=df_SBS2, x="SBS2", kind="count", palette="ch:.25",height=4,aspect=1).set(title='SBS')
print(df_SBS2['SBS2'].value_counts())

categorical_features=identify_nominal_columns(df_SBS2)

#print(categorical_features)


#associations(df_perf, nominal_columns='auto', numerical_columns=None, mark_columns=False, nom_nom_assoc='cramer', num_num_assoc='pearson', bias_correction=True, nan_strategy=_REPLACE, nan_replace_value=_DEFAULT_REPLACE_VALUE, ax=None, figsize=None, annot=True, fmt='.2f', cmap=None, sv_color='silver', cbar=True, vmax=1.0, vmin=None, plot=True, compute_only=False, clustering=False, title=None, filename=None)


complete_correlation= associations(df_SBS2, filename= 'complete_correlation.png', figsize=(30,10))
df_complete_corr=complete_correlation['corr']
df_complete_corr.dropna(axis=1, how='all').dropna(axis=0, how='all').style.background_gradient(cmap='coolwarm', axis=None).set_precision(2)



df_SBS2.to_csv("../temp_data/df_SBS2.csv", index=False)



