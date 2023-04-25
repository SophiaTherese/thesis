# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import datetime
import seaborn as sns


from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay






# ------------- Definition for DK alyzer dataframe 

def summary_meas(office_df,buildingID,officeID):
    '''Makes a 1-line dataframe out of the summary-stats of 
       each of the '''

    lst = {'buildingID':[buildingID],'officeID':[officeID],
           
           'T_mean':[office_df['Temperatur°C'].mean()],
           'T_min':[office_df['Temperatur°C'].min()],
           'T_max':[office_df['Temperatur°C'].max()],
           'T_25p':[np.nanpercentile(office_df['Temperatur°C'], 25, axis=0)],
           'T_median':[office_df['Temperatur°C'].median()],
           'T_75p':[np.nanpercentile(office_df['Temperatur°C'], 75, axis=0)],
           
           'RH_mean':[office_df['Luftfugtighed (RH%)%'].mean()],
           'RH_min':[office_df['Luftfugtighed (RH%)%'].min()],
           'RH_max':[office_df['Luftfugtighed (RH%)%'].max()],
           'RH_25p':[np.nanpercentile(office_df['Luftfugtighed (RH%)%'], 25)],
           'RH_median':[office_df['Luftfugtighed (RH%)%'].median()],
           'RH_75p':[np.nanpercentile(office_df['Luftfugtighed (RH%)%'], 75)],
           
           'CO2_mean':[office_df['CO2 ppm'].mean()],
           'CO2_min':[office_df['CO2 ppm'].min()],
           'CO2_max':[office_df['CO2 ppm'].max()],
           'CO2_25p':[np.nanpercentile(office_df['CO2 ppm'], 25, axis=0)],
           'CO2_median':[office_df['CO2 ppm'].median()],
           'CO2_75p':[np.nanpercentile(office_df['CO2 ppm'], 75, axis=0)],
           
           'VOC_mean':[office_df['VOC ppb'].mean()],
           'VOC_min':[office_df['VOC ppb'].min()],
           'VOC_max':[office_df['VOC ppb'].max()],
           'VOC_25p':[np.nanpercentile(office_df['VOC ppb'], 25)],
           'VOC_median':[office_df['VOC ppb'].median()],
           'VOC_75p':[np.nanpercentile(office_df['VOC ppb'], 75)],
           
           'sound_mean':[office_df['Lydniveau dB'].mean()],
           'sound_min':[office_df['Lydniveau dB'].min()],
           'sound_max':[office_df['Lydniveau dB'].max()],
           'sound_25p':[np.nanpercentile(office_df['Lydniveau dB'], 25)],
           'sound_median':[office_df['Lydniveau dB'].median()],
           'sound_75p':[np.nanpercentile(office_df['Lydniveau dB'], 75)],
           
           'light_mean':[office_df['Lysniveau lux'].mean()],
           'light_min':[office_df['Lysniveau lux'].min()],
           'light_max':[office_df['Lysniveau lux'].max()],
           'light_25p':[np.nanpercentile(office_df['Lysniveau lux'], 25)],
           'light_median':[office_df['Lysniveau lux'].median()],
           'light_75p':[np.nanpercentile(office_df['Lysniveau lux'], 75)],
           
           'light_col_mean':[office_df['Lys farve K'].mean()]}
    
#brug max og min farve
    
    
    mini_df = pd.DataFrame(lst)
    
    
    # mini_df['light_col_neutral'] = 1-( mini_df['light_col_cold'] + mini_df['light_col_warm'])
    # 'light_col_warm':[office_df['Lys farve K'][office_df['Lys farve K'] < 3300].count()/office_df['Lys farve K'].count()],
    # 'light_col_cold':[office_df['Lys farve K'][office_df['Lys farve K'] > 5300].count()/office_df['Lys farve K'].count()]
    return mini_df

def only_work_hours(office_df,h):
    ''''Removes part of time series outside workhours 
        and potentially shifting start time.'''
    if h > 0:
        office_df['date'] = pd.to_datetime(pd.Series(office_df['Dato']),dayfirst=True)+ pd.offsets.Hour(h)
        office_df = office_df[(office_df['date'].dt.dayofweek <5)]
        office_df = office_df[(office_df['date'].dt.hour >= 8) & (office_df['date'].dt.hour < 17)]
        # office_df['Temperatur°C'] = pd.to_numeric(office_df['Temperatur°C'].str.slice(0,5))
        # office_df['Luftfugtighed (RH%)%'] = pd.to_numeric(office_df['Luftfugtighed (RH%)%'].str.slice(0,5))
        new_office_df = office_df
    
    else:
        office_df['date'] = pd.to_datetime(pd.Series(office_df['Dato']),dayfirst=True)
        office_df = office_df[(office_df['date'].dt.dayofweek <5)]
        office_df = office_df[(office_df['date'].dt.hour >= 8) & (office_df['date'].dt.hour < 17)]
        # office_df['Temperatur°C'] = pd.to_numeric(office_df['Temperatur°C'].str.slice(0,5))
        # office_df['Luftfugtighed (RH%)%'] = pd.to_numeric(office_df['Luftfugtighed (RH%)%'].str.slice(0,5))
        new_office_df = office_df
    
    return new_office_df


def only_work_hours_2(office_df,h):
    ''''Removes part of time series outside workhours 
        and potentially shifting start time.'''
    if h > 0:
        office_df['date'] = pd.to_datetime(pd.Series(office_df['Dato']),dayfirst=True)+ pd.offsets.Hour(h)
        office_df = office_df[(office_df['date'].dt.dayofweek <5)]
        office_df = office_df[(office_df['date'].dt.hour >= 8) & (office_df['date'].dt.hour < 17)]
        office_df['Temperatur°C'] = pd.to_numeric(office_df['Temperatur°C'].str.slice(0,5))
        office_df['Luftfugtighed (RH%)%'] = pd.to_numeric(office_df['Luftfugtighed (RH%)%'].str.slice(0,5))
        new_office_df = office_df
    
    else:
        office_df['date'] = pd.to_datetime(pd.Series(office_df['Dato']),dayfirst=True)
        office_df = office_df[(office_df['date'].dt.dayofweek <5)]
        office_df = office_df[(office_df['date'].dt.hour >= 8) & (office_df['date'].dt.hour < 17)]
        office_df['Temperatur°C'] = pd.to_numeric(office_df['Temperatur°C'].str.slice(0,5))
        office_df['Luftfugtighed (RH%)%'] = pd.to_numeric(office_df['Luftfugtighed (RH%)%'].str.slice(0,5))
        new_office_df = office_df
    
    return new_office_df

def only_work_hours_3(office_df,h):
    ''''Removes part of time series outside workhours 
        and potentially shifting start time.'''
    if h > 0:
        office_df['date'] = pd.to_datetime(pd.Series(office_df['Dato']),dayfirst=True)+ pd.offsets.Hour(h)
        office_df = office_df[(office_df['date'].dt.dayofweek <5)]
        office_df = office_df[(office_df['date'].dt.hour >= 8) & (office_df['date'].dt.hour < 17)]
        office_df['Temperatur°C'] = pd.to_numeric(office_df['Temperatur°C'])
        office_df['Luftfugtighed (RH%)%'] = pd.to_numeric(office_df['Luftfugtighed (RH%)%'])
        new_office_df = office_df
    
    else:
        office_df['date'] = pd.to_datetime(pd.Series(office_df['Dato']),dayfirst=True)
        office_df = office_df[(office_df['date'].dt.dayofweek <5)]
        office_df = office_df[(office_df['date'].dt.hour >= 8) & (office_df['date'].dt.hour < 17)]
        office_df['Temperatur°C'] = pd.to_numeric(office_df['Temperatur°C'])
        office_df['Luftfugtighed (RH%)%'] = pd.to_numeric(office_df['Luftfugtighed (RH%)%'])
        new_office_df = office_df
        
    return new_office_df


def make_invalid_nan(office_df):
    '''Remove outliers'''
 
    office_df.loc[office_df['Temperatur°C']<15, 'Temperatur°C'] = np.nan
    office_df.loc[office_df['Temperatur°C']>35, 'Temperatur°C'] = np.nan
    
    office_df.loc[office_df['Luftfugtighed (RH%)%']<0, 'Luftfugtighed (RH%)%'] = np.nan
    office_df.loc[office_df['Luftfugtighed (RH%)%']>100, 'Luftfugtighed (RH%)%'] = np.nan
    
    office_df.loc[office_df['Lysniveau lux']<0, 'Lysniveau lux'] = np.nan
    office_df.loc[office_df['Lys farve K']<0, 'Lys farve K'] = np.nan
    
    office_df.loc[office_df['CO2 ppm']<380, 'CO2 ppm'] = np.nan
    office_df.loc[office_df['VOC ppb']<0, 'VOC ppb'] = np.nan
    
    office_df.loc[office_df['Lydniveau dB']<0, 'Lydniveau dB'] = np.nan
    
    nan_df = office_df
    
    return nan_df

def make_invalid_nan_2(office_df):
    '''Remove outliers'''
 
    office_df.loc[office_df['Temperatur°C']<15, 'Temperatur°C'] = np.nan
    office_df.loc[office_df['Temperatur°C']>35, 'Temperatur°C'] = np.nan
    
    office_df.loc[office_df['LuftfugtighedRH%']<0, 'LuftfugtighedRH%'] = np.nan
    office_df.loc[office_df['LuftfugtighedRH%']>100, 'LuftfugtighedRH%'] = np.nan
    
    office_df.loc[office_df['Lysniveau lux']<0, 'Lysniveau lux'] = np.nan
    office_df.loc[office_df['Lys farve K']<0, 'Lys farve K'] = np.nan
    
    office_df.loc[office_df['CO2 ppm']<380, 'CO2 ppm'] = np.nan
    office_df.loc[office_df['VOC ppb']<0, 'VOC ppb'] = np.nan
    
    office_df.loc[office_df['Lydniveau dB']<0, 'Lydniveau dB'] = np.nan
    
    nan_df = office_df
    
    return nan_df




# ------------- Definition for GL alyzer dataframe 

def summary_meas_GL(office_df,buildingID,officeID):
    '''Makes a 1-line dataframe out of the summary-stats of 
       each of the '''

    lst_GL = {'buildingID':[buildingID],'officeID':[officeID],
           
           'T_mean':[office_df['TEMP'].mean()],
           'T_min':[office_df['TEMP'].min()],
           'T_max':[office_df['TEMP'].max()],
           'T_25p':[np.nanpercentile(office_df['TEMP'], 25, axis=0)],
           'T_median':[office_df['TEMP'].median()],
           'T_75p':[np.nanpercentile(office_df['TEMP'], 75, axis=0)],
           
           'RH_mean':[office_df['RH'].mean()],
           'RH_min':[office_df['RH'].min()],
           'RH_max':[office_df['RH'].max()],
           'RH_25p':[np.nanpercentile(office_df['RH'], 25)],
           'RH_median':[office_df['RH'].median()],
           'RH_75p':[np.nanpercentile(office_df['RH'], 75)],
           
           'CO2_mean':[office_df['CO2'].mean()],
           'CO2_min':[office_df['CO2'].min()],
           'CO2_max':[office_df['CO2'].max()],
           'CO2_25p':[np.nanpercentile(office_df['CO2'], 25, axis=0)],
           'CO2_median':[office_df['CO2'].median()],
           'CO2_75p':[np.nanpercentile(office_df['CO2'], 75, axis=0)],
           
           'VOC_mean':np.nan,
           'VOC_min':np.nan,
           'VOC_max':np.nan,
           'VOC_25p':np.nan,
           'VOC_median':np.nan,
           'VOC_75p':np.nan,
           
           'sound_mean':np.nan,
           'sound_min':np.nan,
           'sound_max':np.nan,
           'sound_25p':np.nan,
           'sound_median':np.nan,
           'sound_75p':np.nan,
           
           'light_mean':[office_df['Intensity'].mean()],
           'light_min':[office_df['Intensity'].min()],
           'light_max':[office_df['Intensity'].max()],
           'light_25p':[np.nanpercentile(office_df['Intensity'], 25)],
           'light_median':[office_df['Intensity'].median()],
           'light_75p':[np.nanpercentile(office_df['Intensity'], 75)],
           
           'light_col_mean':np.nan}
    

    
    
    mini_df_GL = pd.DataFrame(lst_GL)
    return mini_df_GL

def only_work_hours_GL(office_df,h):
    ''''Removes part of time series outside workhours 
        and potentially shifting start time.'''
    if h > 0:
        office_df['date'] = pd.to_datetime(pd.Series(office_df['Dato']),dayfirst=True)+ pd.offsets.Hour(h)
        office_df = office_df[(office_df['date'].dt.dayofweek <5)]
        office_df = office_df[(office_df['date'].dt.hour >= 8) & (office_df['date'].dt.hour < 17)]
        new_office_df_GL = office_df
    
    else:
        office_df['date'] = pd.to_datetime(pd.Series(office_df['Dato']),dayfirst=True)
        office_df = office_df[(office_df['date'].dt.dayofweek <5)]
        office_df = office_df[(office_df['date'].dt.hour >= 8) & (office_df['date'].dt.hour < 17)]
        new_office_df_GL = office_df
    
    return new_office_df_GL



def make_invalid_nan_GL(office_df):
    '''Remove outliers'''
 
    office_df.loc[office_df['TEMP']<15, 'TEMP'] = np.nan
    office_df.loc[office_df['TEMP']>35, 'TEMP'] = np.nan
    
    office_df.loc[office_df['RH']<0, 'RH'] = np.nan
    office_df.loc[office_df['RH']>100, 'RH'] = np.nan
    
    office_df.loc[office_df['Intensity']<0, 'Intensity'] = np.nan
    office_df.loc[office_df['Intensity']<0, 'Intensity'] = np.nan
    
    office_df.loc[office_df['CO2']<380, 'CO2'] = np.nan

    nan_df_GL = office_df
    
    return nan_df_GL



# reverse 1-hot encoding function

#df_predictors_cat.reset_index(inplace=True, drop=True)

def get_cat(feat_name,cols,df):
    
    df[feat_name]='' # to create an empty column
    
    for col_name in df[cols].columns:
        new_df = df.loc[df[col_name]==1,feat_name]= df[feat_name]+' '+col_name
        
    return new_df

# sym: reduce into two groups
def reduce_s(data):
    if 1 <= data  <= 3:
        return 1
    else:
        return 0



# symptoms that got better
def sBetter(df,col1,col2,label):
    p = len(df)
    for i in range(p):
        if (df[col1][i] == 1 & df[col2][i] == 1):
            df[label][i] = 1
        else:
            df[label][i] = 0
            
            
def SBS_1(df,f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,SBS):
    df[SBS] = ''
    for i in range(len(df)):
        if (df[f0][i] + df[f1][i] + df[f2][i] + df[f3][i] + df[f4][i] + df[f5][i] + df[f6][i] + df[f7][i] + df[f8][i] + df[f9][i]>= 1): 
            df[SBS][i] = 1
        else:
            df[SBS][i] = 0
            df_new = df
    return df_new

            
def SBS_2(df,f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,SBS):
    df[SBS] = ''
    
    df['s0'] = df[f0]
    df['s1'] = df[f1]
    df['s2'] = df[f2]
    df['s3'] = df[f3]
    df['s4'] = df[f4]
    df['s5'] = df[f5]
    df['s6'] = df[f6]
    df['s7'] = df[f7]
    df['s8'] = df[f8]
    df['s9'] = df[f9]
    
    for i in range(len(df)):
        if (df[f0][i] + df[f1][i] + df[f2][i] + df[f3][i] + df[f4][i] + df[f5][i] + df[f6][i] + df[f7][i] + df[f8][i] + df[f9][i]>= 2): 
            df[SBS][i] = 1
     
           
        else:
            df[SBS][i] = 0
            
            df['s0'][i] = 0
            df['s1'][i] = 0
            df['s2'][i] = 0
            df['s3'][i] = 0
            df['s4'][i] = 0
            df['s5'][i] = 0
            df['s6'][i] = 0
            df['s7'][i] = 0
            df['s8'][i] = 0
            df['s9'][i] = 0
            
   
        df_new = df
    return df_new

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

