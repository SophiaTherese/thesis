#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 08:32:36 2022

@author: Sophia
"""

import load_utils as lu
import pandas as pd
import numpy as np

#%% ------------- Load alyzer data from DK

# 101 measurements start at 12:00. weekend: 21.-22/11
#            ''' NO CO2 or light DATA'''
#alz_101b = pd.read_csv('../DATA/01_Denmark/BuildingID_101/01_Measured_data/101b_Winter2020_RoomAlyzer_12c40.csv', sep=';')
alz_101b = pd.read_csv('../DATA/01_Denmark/BuildingID_101/01_Measured_data/101b_Winter2020_RoomAlyzer_12c40.csv', sep=';')
# Dropping anything but 17.(tue)-20.(fri), 8:00-17:00
alz_101b = lu.only_work_hours(alz_101b,12)
# make invalid values nan
alz_101b = lu.make_invalid_nan(alz_101b)
alz_101b['CO2 ppm'] = np.nan
alz_101b['Lysniveau lux'] = np.nan
alz_101b['Lys farve K'] = np.nan



alz_101c = pd.read_csv('../DATA/01_Denmark/BuildingID_101/01_Measured_data/101c_Winter2020_RoomAlyzer_12641.csv', sep=';')
alz_101c = lu.only_work_hours(alz_101c,12)
alz_101c = lu.make_invalid_nan(alz_101c)
alz_101c['CO2 ppm'] = np.nan
alz_101c['Lysniveau lux'] = np.nan
alz_101c['Lys farve K'] = np.nan


alz_101d = pd.read_csv('../DATA/01_Denmark/BuildingID_101/01_Measured_data/101d_Winter2020_RoomAlyzer_13d38.csv', sep=';')
alz_101d = lu.only_work_hours(alz_101d,12)
alz_101d = lu.make_invalid_nan(alz_101d)
alz_101d['CO2 ppm'] = np.nan
alz_101d['Lysniveau lux'] = np.nan
alz_101d['Lys farve K'] = np.nan


# 102 measurements start at 12:00. weekend: 21.-22/11
#            ''' NO CO2 or light DATA'''
alz_102a = pd.read_csv('../DATA/01_Denmark/BuildingID_102/01_Measured_data/102a_Winter2020_RoomAlyzer_12640.csv', sep=';')
alz_102a = lu.only_work_hours(alz_102a,12)
alz_102a = lu.make_invalid_nan(alz_102a)
alz_102a['CO2 ppm'] = np.nan
alz_102a['Lysniveau lux'] = np.nan
alz_102a['Lys farve K'] = np.nan

alz_102b1 = pd.read_csv('../DATA/01_Denmark/BuildingID_102/01_Measured_data/102b_Winter2020_RoomAlyzer_12f37.csv', sep=';')
alz_102b1 = lu.only_work_hours(alz_102b1,12)
alz_102b1 = lu.make_invalid_nan(alz_102b1)
alz_102b2 = pd.read_csv('../DATA/01_Denmark/BuildingID_102/01_Measured_data/102b_Winter2020_RoomAlyzer_1362f.csv', sep=';')
alz_102b2 = lu.only_work_hours(alz_102b2,12)
alz_102b2 = lu.make_invalid_nan(alz_102b2)
# Make dataframe
alz_102b_lst = [alz_102b1,alz_102b2]
alz_102b = pd.concat(alz_102b_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
alz_102b['CO2 ppm'] = np.nan
alz_102b['Lysniveau lux'] = np.nan
alz_102b['Lys farve K'] = np.nan


# 103 measurements start at 09:00. weekend: 13.-14/03
# There are extra alyzers for this
# CO2 does not work and no flow data

# CO2 does not work and no flow data
alz_103a1 = pd.read_csv('../DATA/01_Denmark/BuildingID_103/01_Measured_data/103a_01_Spring2021_RoomAlyzer.csv', sep=';')
alz_103a1 = lu.only_work_hours(alz_103a1,0)
alz_103a1 = lu.make_invalid_nan(alz_103a1)
alz_103a3 = pd.read_csv('../DATA/01_Denmark/BuildingID_103/01_Measured_data/103a_03_Spring2021_RoomAlyzer.csv', sep=';')
alz_103a3 = lu.only_work_hours(alz_103a3,0)
alz_103a3 = lu.make_invalid_nan(alz_103a3)
alz_103a8 = pd.read_csv('../DATA/01_Denmark/BuildingID_103/01_Measured_data/103a_08_Spring2021_RoomAlyzer.csv', sep=';')
alz_103a8 = lu.only_work_hours(alz_103a8,0)
alz_103a8 = lu.make_invalid_nan(alz_103a8)
# Make dataframe
alz_103a_lst = [alz_103a1,alz_103a3,alz_103a8]
alz_103a = pd.concat(alz_103a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
alz_103a['CO2 ppm'] = np.nan

# CO2 works but no flow data
alz_103b25 = pd.read_csv('../DATA/01_Denmark/BuildingID_103/01_Measured_data/103b_25_Spring2021_RoomAlyzer.csv', sep=';')
alz_103b25 = lu.only_work_hours(alz_103b25,0)
alz_103b25 = lu.make_invalid_nan(alz_103b25)
# CO2 does not work but there is flow data
alz_103b2 = pd.read_csv('../DATA/01_Denmark/BuildingID_103/01_Measured_data/103b_02_Spring2021_RoomAlyzer.csv', sep=';')
alz_103b2 = lu.only_work_hours(alz_103b2,0)
alz_103b2 = lu.make_invalid_nan(alz_103b2)
alz_103b2['CO2 ppm'] = np.nan
# Make dataframe
alz_103b_lst = [alz_103b25,alz_103b2]
alz_103b = pd.concat(alz_103b_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

# CO2 works
alz_103c22 = pd.read_csv('../DATA/01_Denmark/BuildingID_103/01_Measured_data/103c_22_Spring2021_RoomAlyzer.csv', sep=';')
alz_103c22 = lu.only_work_hours(alz_103c22,0)
alz_103c22 = lu.make_invalid_nan(alz_103c22)
# CO2 does not work but there is flow data'
alz_103c7 = pd.read_csv('../DATA/01_Denmark/BuildingID_103/01_Measured_data/103c_07_Spring2021_RoomAlyzer.csv', sep=';')
alz_103c7 = lu.only_work_hours(alz_103c7,0)
alz_103c7 = lu.make_invalid_nan(alz_103c7)
alz_103c7['CO2 ppm'] = np.nan
# Make dataframe
alz_103c_lst = [alz_103c22,alz_103c7]
alz_103c = pd.concat(alz_103c_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)


alz_103d = pd.read_csv('../DATA/01_Denmark/BuildingID_103/01_Measured_data/103d_12_Spring2021_RoomAlyzer.csv', sep=';')
# CO2 works but no flow data
alz_103d = lu.only_work_hours(alz_103d,0)

alz_103d = lu.make_invalid_nan(alz_103d)

#%%
# 103F measurements start at 00:00. weekend: 
# no light colour. 

#103Fa: 2
alz_103Ea = pd.read_excel('../DATA/01_Denmark/BuildingID_103F/01_Measured_Data/103F_a_10_alz.xlsx')
alz_103Ea = lu.only_work_hours_3(alz_103Ea,0)
alz_103Ea = lu.make_invalid_nan(alz_103Ea)

alz_103Eb = pd.read_excel('../DATA/01_Denmark/BuildingID_103F/01_Measured_Data/103F_b_13_alz.xlsx')
alz_103Eb = lu.only_work_hours_3(alz_103Eb,0)
alz_103Eb = lu.make_invalid_nan(alz_103Eb)

alz_103Ec = pd.read_excel('../DATA/01_Denmark/BuildingID_103F/01_Measured_Data/103F_c_12_alz.xlsx')
alz_103Ec = lu.only_work_hours_3(alz_103Ec,0)
alz_103Ec = lu.make_invalid_nan(alz_103Ec)


#301Ea  move time up 7 hours
alz_301Ea = pd.read_excel('../DATA/01_Denmark/BuildingID_301_E20/01_Measured_Data/301_E2021a_8_alz.xlsx')
alz_301Ea = lu.only_work_hours_3(alz_301Ea,7)
alz_301Ea = lu.make_invalid_nan(alz_301Ea)

#301Eb  move time up 1 hours
alz_301Eb = pd.read_excel('../DATA/01_Denmark/BuildingID_301_E20/01_Measured_Data/301_E2021b_22_alz.xlsx')
alz_301Eb = lu.only_work_hours_3(alz_301Eb,1)
alz_301Eb = lu.make_invalid_nan(alz_301Eb)

#301Ec  move time up 1 hours
alz_301Ec = pd.read_excel('../DATA/01_Denmark/BuildingID_301_E20/01_Measured_Data/301_E2021c_23_alz.xlsx')
alz_301Ec = lu.only_work_hours_3(alz_301Ec,1)
alz_301Ec = lu.make_invalid_nan(alz_301Ec)

#301Ed  move time up 2 hours
alz_301Ed = pd.read_excel('../DATA/01_Denmark/BuildingID_301_E20/01_Measured_Data/301_E2021d_17_alz.xlsx')
alz_301Ed = lu.only_work_hours_3(alz_301Ed,2)
alz_301Ed = lu.make_invalid_nan(alz_301Ed)

#%%

#306a  move time up 0 hours
alz_306oa = pd.read_excel('../DATA/01_Denmark/BuildingID_306/01_Measured_Data/3060A_13_alz.xlsx')
alz_306oa = lu.only_work_hours_3(alz_306oa,0)
alz_306oa = lu.make_invalid_nan(alz_306oa)

alz_306ob = pd.read_excel('../DATA/01_Denmark/BuildingID_306/01_Measured_Data/3060B_11_alz.xlsx')
alz_306ob = lu.only_work_hours_3(alz_306ob,0)
alz_306ob = lu.make_invalid_nan(alz_306ob)

alz_3061a12 = pd.read_excel('../DATA/01_Denmark/BuildingID_306/01_Measured_Data/3061A_12_10_alz.xlsx','12')
alz_3061a12 = lu.only_work_hours_3(alz_3061a12,0)
alz_3061a12 = lu.make_invalid_nan(alz_3061a12)
alz_3061a10 = pd.read_excel('../DATA/01_Denmark/BuildingID_306/01_Measured_Data/3061A_12_10_alz.xlsx','10')
alz_3061a10 = lu.only_work_hours_3(alz_3061a10,0)
alz_3061a10 = lu.make_invalid_nan(alz_3061a10)
alz_3061a_lst = [alz_3061a12,alz_3061a10]
alz_3061a = pd.concat(alz_3061a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)


#%%



#307  move time up 0 hours
alz_307a8 = pd.read_excel('../DATA/01_Denmark/BuildingID_307/01_Measured_Data/307a_8_17_22_23_alz.xlsx','8')
alz_307a8 = lu.only_work_hours_3(alz_307a8,0)
alz_307a8 = lu.make_invalid_nan(alz_307a8)
alz_307a17 = pd.read_excel('../DATA/01_Denmark/BuildingID_307/01_Measured_Data/307a_8_17_22_23_alz.xlsx','17')
alz_307a17 = lu.only_work_hours_3(alz_307a17,0)
alz_307a17 = lu.make_invalid_nan(alz_307a17)
alz_307a22 = pd.read_excel('../DATA/01_Denmark/BuildingID_307/01_Measured_Data/307a_8_17_22_23_alz.xlsx','22')
alz_307a22 = lu.only_work_hours_3(alz_307a22,0)
alz_307a22 = lu.make_invalid_nan(alz_307a22)
alz_307a23 = pd.read_excel('../DATA/01_Denmark/BuildingID_307/01_Measured_Data/307a_8_17_22_23_alz.xlsx','23')
alz_307a23 = lu.only_work_hours_3(alz_307a23,0)
alz_307a23 = lu.make_invalid_nan(alz_307a23)


alz_307a_lst = [alz_307a8,alz_307a17,alz_307a22,alz_307a23]
alz_307a = pd.concat(alz_307a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

#%%

# # 104 measurements start at 00:00. 
alz_104a = pd.read_csv('../DATA/01_Denmark/BuildingID_104/01_Measured_data/104_22_Spring2022_RoomAlyzer.csv', sep=';')
alz_104a = lu.only_work_hours_2(alz_104a,0)
alz_104a = lu.make_invalid_nan(alz_104a)

# der står at det skal være nr24 og ikke 17, så er ikke korrekt til b. 
# alz_104b = pd.read_csv('../DATA/01_Denmark/BuildingID_104/01_Measured_data/104_17_Spring2022_RoomAlyzer.csv', sep=';')
# alz_104b = lu.only_work_hours_2(alz_104b,0)
# alz_104b = lu.make_invalid_nan(alz_104b)


# # 105a measurements start at 00:00. weekwnd: 2-3/4.  10, 22, 24
alz_105a10 = pd.read_csv('../DATA/01_Denmark/BuildingID_105/01_Measured_data/105_10_Spring2022_RoomAlyzer.csv', sep=';')
alz_105a10 = lu.only_work_hours_2(alz_105a10,0)
alz_105a10 = lu.make_invalid_nan(alz_105a10)
alz_105a22 = pd.read_csv('../DATA/01_Denmark/BuildingID_105/01_Measured_data/105_22_Spring2022_RoomAlyzer.csv', sep=';')
alz_105a22 = lu.only_work_hours_2(alz_105a22,0)
alz_105a22 = lu.make_invalid_nan(alz_105a22)
# alz_105a24 = pd.read_csv('../DATA/01_Denmark/BuildingID_105/01_Measured_data/105_24_Spring2022_RoomAlyzer.csv', sep=';')
# alz_105a24 = lu.only_work_hours_2(alz_105a24,0)
# alz_105a24 = lu.make_invalid_nan(alz_105a24)
alz_105a_lst = [alz_105a10,alz_105a22]
alz_105a = pd.concat(alz_105a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

#no measurements from 308a
# 308Ab - 10, 22

alz_308Ab10 = pd.read_csv('../DATA/01_Denmark/BuildingID_308/01_Measured_data/308_10_Spring2022_RoomAlyzer.csv', sep=';')
alz_308Ab10 = lu.only_work_hours_2(alz_308Ab10,0)
alz_308Ab10 = lu.make_invalid_nan(alz_308Ab10)
alz_308Ab22 = pd.read_csv('../DATA/01_Denmark/BuildingID_308/01_Measured_data/308_22_Spring2022_RoomAlyzer.csv', sep=';')
alz_308Ab22 = lu.only_work_hours_2(alz_308Ab22,0)
alz_308Ab22 = lu.make_invalid_nan(alz_308Ab22)

alz_308Ab_lst = [alz_308Ab10,alz_308Ab22]
alz_308Ab = pd.concat(alz_308Ab_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

#309a - 04, 7:
# start at 00:00. 
alz_309a = pd.read_csv('../DATA/01_Denmark/BuildingID_309/01_Measured_data/309_04_Spring2022_RoomAlyzer.csv', sep=';')
alz_309a = lu.only_work_hours_2(alz_309a,0)
alz_309a = lu.make_invalid_nan(alz_309a)

#309b - 2, 15
alz_309b2 = pd.read_csv('../DATA/01_Denmark/BuildingID_309/01_Measured_data/309_02_Spring2022_RoomAlyzer.csv', sep=';')
alz_309b2 = lu.only_work_hours_2(alz_309b2,0)
alz_309b2 = lu.make_invalid_nan(alz_309b2)
alz_309b15 = pd.read_csv('../DATA/01_Denmark/BuildingID_309/01_Measured_data/309_15_Spring2022_RoomAlyzer.csv', sep=';')
alz_309b15 = lu.only_work_hours_2(alz_309b15,0)
alz_309b15 = lu.make_invalid_nan(alz_309b15)
alz_309b_lst = [alz_309b2,alz_309b15]
alz_309b = pd.concat(alz_309b_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
#309c: 17 - no meas



#%%

# 301 measurements start at 09:00. weekend: 13.-14/03 -- NO CO2
# CO2 does not work and no flow data
alz_301a = pd.read_csv('../DATA/01_Denmark/BuildingID_301/01_Measured_data/301a_11_Spring2021_RoomAlyzer.csv', sep=';')
alz_301a = lu.only_work_hours(alz_301a,0)
alz_301a = lu.make_invalid_nan(alz_301a)
alz_301a['CO2 ppm'] = np.nan

alz_301b13 = pd.read_csv('../DATA/01_Denmark/BuildingID_301/01_Measured_data/301b_13_Spring2021_RoomAlyzer.csv', sep=';')
alz_301b13 = lu.only_work_hours(alz_301b13,0)
alz_301b13 = lu.make_invalid_nan(alz_301b13)
alz_301b20 = pd.read_csv('../DATA/01_Denmark/BuildingID_301/01_Measured_data/301b_20_Spring2021_RoomAlyzer.csv', sep=';')
alz_301b20 = lu.only_work_hours(alz_301b20,0)
alz_301b20 = lu.make_invalid_nan(alz_301b20)
# Make dataframe
alz_301b_lst = [alz_301b13,alz_301b20]
alz_301b = pd.concat(alz_301b_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
alz_301b['CO2 ppm'] = np.nan

alz_301c = pd.read_csv('../DATA/01_Denmark/BuildingID_301/01_Measured_data/301c_16_Spring2021_RoomAlyzer.csv', sep=';')
alz_301c = lu.only_work_hours(alz_301c,0)
alz_301c = lu.make_invalid_nan(alz_301c)
alz_301c['CO2 ppm'] = np.nan



# 302 measurements start at 10:00. weekend: 27.-28/03 
alz_302a = pd.read_csv('../DATA/01_Denmark/BuildingID_302/01_Measured_data/302a_05_Spring2021_RoomAlyzer.csv', sep=';')
alz_302a = lu.only_work_hours(alz_302a,0)
# CO2 correction for room alyzer 05: y = 0,9665x + 212,52
alz_302a['CO2 ppm'] *= 0.9665
alz_302a['CO2 ppm'] += 212.52
alz_302a = lu.make_invalid_nan(alz_302a)


alz_302b = pd.read_csv('../DATA/01_Denmark/BuildingID_302/01_Measured_data/302b_02_Spring2021_RoomAlyzer.csv', sep=';')
alz_302b = lu.only_work_hours(alz_302b,0)
# CO2 correction for room alyzer 02: y = 1,0082x + 100,32
alz_302b['CO2 ppm'] *= 1.0082 
alz_302b['CO2 ppm'] += 100.32
alz_302b = lu.make_invalid_nan(alz_302b)

alz_302c = pd.read_csv('../DATA/01_Denmark/BuildingID_302/01_Measured_data/302c_21_Spring2021_RoomAlyzer.csv', sep=';')
alz_302c = lu.only_work_hours(alz_302c,0)
# CO2 correction for room alyzer 21: y = 0,8867x + 158,24
alz_302b['CO2 ppm'] *= 0.8867
alz_302b['CO2 ppm'] += 158.24
alz_302c = lu.make_invalid_nan(alz_302c)

alz_302d = pd.read_csv('../DATA/01_Denmark/BuildingID_302/01_Measured_data/302d_08_Spring2021_RoomAlyzer.csv', sep=';')
alz_302d = lu.only_work_hours(alz_302d,0)
# CO2 correction for room alyzer 08: y = 0,6696x + 9,0723
alz_302d['CO2 ppm'] *= 0.6696
alz_302d['CO2 ppm'] += 9.0723
alz_302d = lu.make_invalid_nan(alz_302d)

alz_302e = pd.read_csv('../DATA/01_Denmark/BuildingID_302/01_Measured_data/302e_11_Spring2021_RoomAlyzer.csv', sep=';')
alz_302e = lu.only_work_hours(alz_302e,0)
# CO2 correction for room alyzer 11: y = 0,9478x + 112,43
alz_302e['CO2 ppm'] *= 0.9478
alz_302e['CO2 ppm'] += 112.43
alz_302e = lu.make_invalid_nan(alz_302e)



#303 measurements start at 10:00. 
"""Målingsperiode:
Start: Tirsdag d. 6. april 2021,  kl. eftermiddag
Slut: Tirsdag d. 13. april 2021, kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag og Søndag d. 10. og 11. april 2021 
"""  #does weekends wrong because of us/eu dates
alz_303a = pd.read_csv('../DATA/01_Denmark/BuildingID_303/01_Measured_data/303a_15_spring2021_RoomAlyzer.csv', sep=';')
alz_303a = lu.only_work_hours(alz_303a,0)
alz_303a = lu.make_invalid_nan(alz_303a)

alz_303b = pd.read_csv('../DATA/01_Denmark/BuildingID_303/01_Measured_data/303b_12_spring2021_RoomAlyzer.csv', sep=';')
alz_303b = lu.only_work_hours(alz_303b,0)
alz_303b = lu.make_invalid_nan(alz_303b)

alz_303c = pd.read_csv('../DATA/01_Denmark/BuildingID_303/01_Measured_data/303c_17_spring2021_RoomAlyzer.csv', sep=';')
alz_303c = lu.only_work_hours(alz_303c,0)
alz_303c = lu.make_invalid_nan(alz_303c)

alz_303d = pd.read_csv('../DATA/01_Denmark/BuildingID_303/01_Measured_data/303d_14_spring2021_RoomAlyzer.csv', sep=';')
alz_303d = lu.only_work_hours(alz_303d,0)
alz_303d = lu.make_invalid_nan(alz_303d)



#303 measurements start at 10:00. 
'''Målingsperiode:
Start: Onsdag d. 14. april 2021, kl. eftermiddag (tjek måleværdierne ud). 
Slut: Onsdag d. 21. april 2021, kl. eftermiddag (tjek måleværdierne ud).
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 17. og 18. april 2021'''
alz_304a = pd.read_csv('../DATA/01_Denmark/BuildingID_304/01_Measured_data/304a_16_Spring2021_RoomAlyzer.csv', sep=';')
alz_304a = lu.only_work_hours(alz_304a,0)
alz_304a = lu.make_invalid_nan(alz_304a)
alz_304a['Lys farve K'] = np.nan

alz_304b = pd.read_csv('../DATA/01_Denmark/BuildingID_304/01_Measured_data/304b_03_Spring2021_RoomAlyzer.csv', sep=';')
alz_304b = lu.only_work_hours(alz_304b,0)
alz_304b = lu.make_invalid_nan(alz_304b)

alz_304c = pd.read_csv('../DATA/01_Denmark/BuildingID_304/01_Measured_data/304c_14_Spring2021_RoomAlyzer.csv', sep=';')
alz_304c = lu.only_work_hours(alz_304c,0)
alz_304c = lu.make_invalid_nan(alz_304c)

alz_304d = pd.read_csv('../DATA/01_Denmark/BuildingID_304/01_Measured_data/304d_13_Spring2021_RoomAlyzer.csv', sep=';')
alz_304d = lu.only_work_hours(alz_304d,0)
alz_304d = lu.make_invalid_nan(alz_304d)

alz_304e = pd.read_csv('../DATA/01_Denmark/BuildingID_304/01_Measured_data/304e_15_Spring2021_RoomAlyzer.csv', sep=';')
alz_304e = lu.only_work_hours(alz_304e,0)
alz_304e = lu.make_invalid_nan(alz_304e)

alz_304f = pd.read_csv('../DATA/01_Denmark/BuildingID_304/01_Measured_data/304f_12_Spring2021_RoomAlyzer.csv', sep=';')
alz_304f = lu.only_work_hours(alz_304f,0)
alz_304f = lu.make_invalid_nan(alz_304f)

alz_304g = pd.read_csv('../DATA/01_Denmark/BuildingID_304/01_Measured_data/304g_17_Spring2021_RoomAlyzer.csv', sep=';')
alz_304g = lu.only_work_hours(alz_304g,0)
alz_304g = lu.make_invalid_nan(alz_304g)

#%%

#alz_305Ab: 1
alz_305Ab = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/01_Measured_Data/All combined spread (user time) sep.xlsx','Sensor 1')
alz_305Ab = lu.only_work_hours_3(alz_305Ab,0)
alz_305Ab = lu.make_invalid_nan(alz_305Ab)
#%%
#alz_305Ac: 2
alz_305Ac = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/01_Measured_Data/All combined spread (user time) sep.xlsx','Sensor 2')
alz_305Ac = lu.only_work_hours_3(alz_305Ac,0)
alz_305Ac = lu.make_invalid_nan(alz_305Ac)

#alz_305Ad: 3
alz_305Ad = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/01_Measured_Data/All combined spread (user time) sep.xlsx','Sensor 3')
alz_305Ad = lu.only_work_hours_3(alz_305Ad,0)
alz_305Ad = lu.make_invalid_nan(alz_305Ad)

#alz_305Ae: 4
alz_305Ae = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/01_Measured_Data/All combined spread (user time) sep.xlsx','Sensor 4')
alz_305Ae = lu.only_work_hours_3(alz_305Ae,0)
alz_305Ae = lu.make_invalid_nan(alz_305Ae)

#alz_305Af: 5
alz_305Af = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/01_Measured_Data/All combined spread (user time) sep.xlsx','Sensor 5')
alz_305Af = lu.only_work_hours_3(alz_305Af,0)
alz_305Af = lu.make_invalid_nan(alz_305Af)

#alz_305Ag: 6
alz_305Ag = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/01_Measured_Data/All combined spread (user time) sep.xlsx','Sensor 6')
alz_305Ag = lu.only_work_hours_3(alz_305Ag,0)
alz_305Ag = lu.make_invalid_nan(alz_305Ag)

#alz_305Ah: 7
alz_305Ah = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/01_Measured_Data/All combined spread (user time) sep.xlsx','Sensor 7')
alz_305Ah = lu.only_work_hours_3(alz_305Ah,0)
alz_305Ah = lu.make_invalid_nan(alz_305Ah)

#alz_305Ai: 9
alz_305Ai = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/01_Measured_Data/All combined spread (user time) sep.xlsx','Sensor 9')
alz_305Ai = lu.only_work_hours_3(alz_305Ai,0)
alz_305Ai = lu.make_invalid_nan(alz_305Ai)

#%%
#310a - 18, 19
alz_310a18 = pd.read_csv('../DATA/01_Denmark/BuildingID_310/01_Measured_data/310_18_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_310a18 = lu.only_work_hours_2(alz_310a18,0)
alz_310a18 = lu.make_invalid_nan(alz_310a18)
alz_310a19 = pd.read_csv('../DATA/01_Denmark/BuildingID_310/01_Measured_data/310_19_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_310a19 = lu.only_work_hours_2(alz_310a19,0)
alz_310a19 = lu.make_invalid_nan(alz_310a19)
alz_310a_lst = [alz_310a18,alz_310a19]
alz_310a = pd.concat(alz_310a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
#310a - 16
alz_310b = pd.read_csv('../DATA/01_Denmark/BuildingID_310/01_Measured_data/310_16_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_310b = lu.only_work_hours_2(alz_310b,0)
alz_310b = lu.make_invalid_nan(alz_310b)


# 311a: 11,12
alz_311a11 = pd.read_csv('../DATA/01_Denmark/BuildingID_311/01_Measured_data/311_11_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_311a11 = lu.only_work_hours_2(alz_311a11,0)
alz_311a11 = lu.make_invalid_nan(alz_311a11)
alz_311a12 = pd.read_csv('../DATA/01_Denmark/BuildingID_311/01_Measured_data/311_12_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_311a12 = lu.only_work_hours_2(alz_311a12,0)
alz_311a12 = lu.make_invalid_nan(alz_311a12)
alz_311a_lst = [alz_311a11,alz_311a12]
alz_311a = pd.concat(alz_311a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
# 3011b: 8
alz_311b = pd.read_csv('../DATA/01_Denmark/BuildingID_311/01_Measured_data/311_08_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_311b = lu.only_work_hours_2(alz_311b,0)
alz_311b = lu.make_invalid_nan(alz_311b)


# 312a: 20, 21
alz_312a20 = pd.read_csv('../DATA/01_Denmark/BuildingID_312/01_Measured_data/312_20_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_312a20 = lu.only_work_hours_2(alz_312a20,0)
alz_312a20 = lu.make_invalid_nan(alz_312a20)
alz_312a21 = pd.read_csv('../DATA/01_Denmark/BuildingID_312/01_Measured_data/312_21_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_312a21 = lu.only_work_hours_2(alz_312a21,0)
alz_312a21 = lu.make_invalid_nan(alz_312a21)
alz_312a_lst = [alz_312a20,alz_312a21]
alz_312a = pd.concat(alz_312a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
# 312b: 23
alz_312b = pd.read_csv('../DATA/01_Denmark/BuildingID_312/01_Measured_data/312_23_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_312b = lu.only_work_hours_2(alz_312b,0)
alz_312b = lu.make_invalid_nan(alz_312b)
# 312c: 25
alz_312c = pd.read_csv('../DATA/01_Denmark/BuildingID_312/01_Measured_data/312_25_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_312c = lu.only_work_hours_2(alz_312c,0)
alz_312c = lu.make_invalid_nan(alz_312c)

# 313a: 11(no Co2), 12, 13
alz_313a11 = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_11_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313a11 = lu.only_work_hours_2(alz_313a11,0)
alz_313a11 = lu.make_invalid_nan(alz_313a11)
alz_313a12 = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_12_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313a12 = lu.only_work_hours_2(alz_313a12,0)
alz_313a12 = lu.make_invalid_nan(alz_313a12)
alz_313a13 = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_13_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313a13 = lu.only_work_hours_2(alz_313a13,0)
alz_313a13 = lu.make_invalid_nan(alz_313a13)
alz_313a_lst = [alz_313a11,alz_313a12,alz_313a13]
alz_313a = pd.concat(alz_313a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
# 313b: 14, 16
alz_313b14 = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_14_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313b14 = lu.only_work_hours_2(alz_313b14,0)
alz_313b14 = lu.make_invalid_nan(alz_313b14)
alz_313b16 = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_16_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313b16 = lu.only_work_hours_2(alz_313b16,0)
alz_313b16 = lu.make_invalid_nan(alz_313b16)
alz_313b_lst = [alz_313b14,alz_313b16]
alz_313b = pd.concat(alz_313b_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
# 313c: 18, 19
alz_313c18 = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_18_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313c18 = lu.only_work_hours_2(alz_313c18,0)
alz_313c18 = lu.make_invalid_nan(alz_313c18)
alz_313c19 = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_19_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313c19 = lu.only_work_hours_2(alz_313c19,0)
alz_313c19 = lu.make_invalid_nan(alz_313c19)
alz_313c_lst = [alz_313c18,alz_313c19]
alz_313c = pd.concat(alz_313c_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
# 313d: 8
alz_313d = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_08_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313d = lu.only_work_hours_2(alz_313d,0)
alz_313d = lu.make_invalid_nan(alz_313d)
# 313e: 20
alz_313e = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_20_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313e = lu.only_work_hours_2(alz_313e,0)
alz_313e = lu.make_invalid_nan(alz_313e)

# 313f:23, 25
alz_313f23 = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_23_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313f23 = lu.only_work_hours_2(alz_313f23,0)
alz_313f23 = lu.make_invalid_nan(alz_313f23)
alz_313f25 = pd.read_csv('../DATA/01_Denmark/BuildingID_313/01_Measured_data/313_25_Spring2022_RoomAlyzer.csv', sep=';',encoding='latin-1')
alz_313f25 = lu.only_work_hours_2(alz_313f25,0)
alz_313f25 = lu.make_invalid_nan(alz_313f25)
alz_313f_lst = [alz_313f23,alz_313f25]
alz_313f = pd.concat(alz_313f_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)


#%% ------------- Make alyzer dataframe for dk

alz_dk = [lu.summary_meas(alz_101b,101,'101b') , lu.summary_meas(alz_101c,101,'101c'), lu.summary_meas(alz_101d,101,'101d'),
          lu.summary_meas(alz_102a,102,'102a'),lu.summary_meas(alz_102b,102,'102b'),
          lu.summary_meas(alz_103a,103,'103a'),lu.summary_meas(alz_103b,103,'103b'),lu.summary_meas(alz_103c,103,'103c'),lu.summary_meas(alz_103d,103,'103d'),
          
          lu.summary_meas(alz_103Ea,'103_E2021','103_E2021a'),lu.summary_meas(alz_103Eb,'103_E2021','103_E2021b'),lu.summary_meas(alz_103Ec,'103_E2021','103_E2021c'),
          lu.summary_meas(alz_103Ea,104,'104a'),lu.summary_meas(alz_105a,105,'105a'),
          
          
          lu.summary_meas(alz_301a,301,'301a'),lu.summary_meas(alz_301b,301,'301b'),lu.summary_meas(alz_301c,301,'301c'),
          lu.summary_meas(alz_301Ea,'301_E2021','301_E2021a'),lu.summary_meas(alz_301Eb,'301_E2021','301_E2021b'),lu.summary_meas(alz_301Ec,'301_E2021','301_E2021c'),lu.summary_meas(alz_301Ed,'301_E2021','301_E2021d'),
          
          
          
          lu.summary_meas(alz_302a,302,'302a'),lu.summary_meas(alz_302b,302,'302b'),lu.summary_meas(alz_302c,302,'302c'),
          lu.summary_meas(alz_302e,302,'302d'),lu.summary_meas(alz_302e,302,'302e'), lu.summary_meas(alz_303a,303,'303a'),lu.summary_meas(alz_303b,303,'303b'),lu.summary_meas(alz_303c,303,'303c'),lu.summary_meas(alz_303d,303,'303d'),
          lu.summary_meas(alz_304a,304,'304a'),lu.summary_meas(alz_304b,304,'304b'),lu.summary_meas(alz_304c,304,'304c'),lu.summary_meas(alz_304d,304,'304d'),
          lu.summary_meas(alz_304e,304,'304e'),lu.summary_meas(alz_304f,304,'304f'),lu.summary_meas(alz_304g,304,'304g'),
          
          lu.summary_meas(alz_305Ab,305,'305b'),lu.summary_meas(alz_305Ac,305,'305c'),lu.summary_meas(alz_305Ad,305,'305d'),lu.summary_meas(alz_305Ae,305,'305e'),
          lu.summary_meas(alz_305Af,305,'305f'),lu.summary_meas(alz_305Ag,305,'305g'),lu.summary_meas(alz_305Ah,305,'305h'),lu.summary_meas(alz_305Ai,305,'305i'),
                                                 
          lu.summary_meas(alz_306oa,'306','3060A'),lu.summary_meas(alz_306ob,'306','3060B'),lu.summary_meas(alz_3061a,'306','3061A'),
                    
          lu.summary_meas(alz_307a,'307','307a'),
                        
          lu.summary_meas(alz_308Ab,'308A','308Ab'),
          lu.summary_meas(alz_309a,309,'309a'),lu.summary_meas(alz_309b,309,'309b'),
          lu.summary_meas(alz_310a,310,'310a'),lu.summary_meas(alz_310b,310,'310b'),
          lu.summary_meas(alz_311a,311,'311a'),lu.summary_meas(alz_311b,311,'311b'),
          lu.summary_meas(alz_312a,312,'312a'),lu.summary_meas(alz_312b,312,'312b'),lu.summary_meas(alz_312c,312,'312c'),
          lu.summary_meas(alz_313a,313,'313a'),lu.summary_meas(alz_313b,313,'313b'),lu.summary_meas(alz_313c,313,'313c'),
          lu.summary_meas(alz_313d,313,'313d'),lu.summary_meas(alz_313e,313,'313e'),lu.summary_meas(alz_313f,313,'313f')]

#alz_305Ab
# Make dataframe
df_alz_dk = pd.concat(alz_dk, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)



df_alz_dk['location'] = 'Denmark'



#%% ------------- Load alyzer data from GL

# 401 
''' Start: tirsdag d. 23. marts 2021 kl. middag
    Slut: tirsdag d. 31. marts 2021 kl. aften
    Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 27. og 28. marts 2021 '''
    
alz_401b = pd.read_excel('../DATA/02_Greenland/Building_ID_401/01_Measured_data/401b_07_Spring2021_Hobo_Alldata.xls.xlsx')
alz_401b = lu.only_work_hours_GL(alz_401b,0)
# make invalid values nan
alz_401b = lu.make_invalid_nan_GL(alz_401b)

alz_401c = pd.read_excel('../DATA/02_Greenland/Building_ID_401/01_Measured_data/401c_05_Spring2021_Hobo_Alldata.xlsx')
alz_401c = lu.only_work_hours_GL(alz_401c,0)
# make invalid values nan
alz_401c = lu.make_invalid_nan_GL(alz_401c)

alz_401d = pd.read_excel('../DATA/02_Greenland/Building_ID_401/01_Measured_data/401d_03_Spring2021_Hobo_Alldata.xlsx')
alz_401d = lu.only_work_hours_GL(alz_401d,0)
# make invalid values nan
alz_401d = lu.make_invalid_nan_GL(alz_401d)

alz_401e = pd.read_excel('../DATA/02_Greenland/Building_ID_401/01_Measured_data/401e_06_Spring2021_Hobo_Alldata.xlsx')
alz_401e = lu.only_work_hours_GL(alz_401e,0)
# make invalid values nan
alz_401e = lu.make_invalid_nan_GL(alz_401e)


# 402
''' Start: tirsdag d. 23. marts 2021 kl. sen aften (virker til at tider allerede er justeret)
    Slut: tirsdag d. 31. marts 2021 kl. sen aften
    Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 27. og 28. marts 2021'''

alz_402a = pd.read_excel('../DATA/02_Greenland/Building_ID_402/01_Measured_data/402a_09_Spring2021_Hobo_Alldata.xlsx')
alz_402a = lu.only_work_hours_GL(alz_402a,0)
alz_402a = lu.make_invalid_nan_GL(alz_402a)

alz_402b = pd.read_excel('../DATA/02_Greenland/Building_ID_402/01_Measured_data/402b_08_Spring2021_Hobo_Alldata.xlsx')
alz_402b = lu.only_work_hours_GL(alz_402b,0)
# make invalid values nan
alz_402b = lu.make_invalid_nan_GL(alz_402b)

alz_402c = pd.read_excel('../DATA/02_Greenland/Building_ID_402/01_Measured_data/402c_10_Spring2021_Hobo_Alldata.xlsx')
alz_402c = lu.only_work_hours_GL(alz_402c,0)
# make invalid values nan
alz_402c = lu.make_invalid_nan_GL(alz_402c)

alz_402d = pd.read_excel('../DATA/02_Greenland/Building_ID_402/01_Measured_data/402d_04_Spring2021_Hobo_Alldata.xlsx')
alz_402d = lu.only_work_hours_GL(alz_402d,0)
# make invalid values nan
alz_402d = lu.make_invalid_nan_GL(alz_402d)

alz_402e = pd.read_excel('../DATA/02_Greenland/Building_ID_402/01_Measured_data/402e_11_Spring2021_Hobo_Alldata.xlsx')
alz_402e = lu.only_work_hours_GL(alz_402e,0)
# make invalid values nan
alz_402e = lu.make_invalid_nan_GL(alz_402e)


# 403
''' Start: tirsdag d. 23. marts 2021 kl. sen aften
    Slut: tirsdag d. 31. marts 2021 kl. eftermiddag
    Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 27. og 28. marts 2021'''
alz_403a_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/01_Measured_data/403a_13_co2_kombo.xlsx')
alz_403a_co2 = lu.only_work_hours_GL(alz_403a_co2,0)
alz_403a_co2 = lu.make_invalid_nan_GL(alz_403a_co2)
alz_403a_light = pd.read_excel('../DATA/02_Greenland/Building_ID_403/01_Measured_data/403a_13_light_kombo.xlsx')
alz_403a_light = lu.only_work_hours_GL(alz_403a_light,0)
alz_403a_light = lu.make_invalid_nan_GL(alz_403a_light)
# Make dataframe
alz_403a_lst = [alz_403a_co2,alz_403a_light]
alz_403a = pd.concat(alz_403a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

alz_403b_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/01_Measured_data/403b_12_co2.xlsx')
alz_403b_co2 = lu.only_work_hours_GL(alz_403b_co2,0)
alz_403b_co2 = lu.make_invalid_nan_GL(alz_403b_co2)
alz_403b_light = pd.read_excel('../DATA/02_Greenland/Building_ID_403/01_Measured_data/403b_12_light.xlsx')
alz_403b_light = lu.only_work_hours_GL(alz_403b_light,0)
alz_403b_light = lu.make_invalid_nan_GL(alz_403b_light)
# Make dataframe
alz_403b_lst = [alz_403b_co2,alz_403b_light]
alz_403b = pd.concat(alz_403b_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

alz_403c_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/01_Measured_data/403c_14_co2.xlsx')
alz_403c_co2 = lu.only_work_hours_GL(alz_403c_co2,0)
alz_403c_co2 = lu.make_invalid_nan_GL(alz_403c_co2)
alz_403c_light = pd.read_excel('../DATA/02_Greenland/Building_ID_403/01_Measured_data/403c_14_light.xlsx')
alz_403c_light = lu.only_work_hours_GL(alz_403c_light,0)
alz_403c_light = lu.make_invalid_nan_GL(alz_403c_light)
# Make dataframe
alz_403c_lst = [alz_403c_co2,alz_403c_light]
alz_403c = pd.concat(alz_403c_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

alz_403d_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/01_Measured_data/403c_14_co2.xlsx')
alz_403d_co2 = lu.only_work_hours_GL(alz_403d_co2,0)
alz_403d_co2 = lu.make_invalid_nan_GL(alz_403d_co2)
alz_403d_light = pd.read_excel('../DATA/02_Greenland/Building_ID_403/01_Measured_data/403c_14_light.xlsx')
alz_403d_light = lu.only_work_hours_GL(alz_403d_light,0)
alz_403d_light = lu.make_invalid_nan_GL(alz_403d_light)
# Make dataframe
alz_403d_lst = [alz_403d_co2,alz_403d_light]
alz_403d = pd.concat(alz_403d_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)



# 404
''' Start: tirsdag d. 23. marts 2021 kl. sen aften
Slut: tirsdag d. 31. marts 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 27. og 28. marts 2021'''
alz_404a = pd.read_excel('../DATA/02_Greenland/Building_ID_404/01_Measured_data/404_Alldata.xlsx','A')
alz_404a = lu.only_work_hours_GL(alz_404a,0)
alz_404a = lu.make_invalid_nan_GL(alz_404a)

alz_404b = pd.read_excel('../DATA/02_Greenland/Building_ID_404/01_Measured_data/404_Alldata.xlsx','B')
alz_404b = lu.only_work_hours_GL(alz_404b,0)
alz_404b = lu.make_invalid_nan_GL(alz_404b)

# 405
''' Start: tirsdag d. 23. marts 2021 kl. sen aften
Slut: tirsdag d. 31. marts 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 27. og 28. marts 2021'''
alz_405a = pd.read_excel('../DATA/02_Greenland/Building_ID_405/01_Measured_data/405_alldata.xlsx','a')
alz_405a = lu.only_work_hours_GL(alz_405a,0)
alz_405a = lu.make_invalid_nan_GL(alz_405a)

alz_405b = pd.read_excel('../DATA/02_Greenland/Building_ID_405/01_Measured_data/405_alldata.xlsx','b')
alz_405b = lu.only_work_hours_GL(alz_405b,0)
alz_405b = lu.make_invalid_nan_GL(alz_405b)

alz_405c = pd.read_excel('../DATA/02_Greenland/Building_ID_405/01_Measured_data/405_alldata.xlsx','c')
alz_405c = lu.only_work_hours_GL(alz_405c,0)
alz_405c = lu.make_invalid_nan_GL(alz_405c)

alz_405d = pd.read_excel('../DATA/02_Greenland/Building_ID_405/01_Measured_data/405_alldata.xlsx','d')
alz_405d = lu.only_work_hours_GL(alz_405d,0)
alz_405d = lu.make_invalid_nan_GL(alz_405d)


# 406  venter med at loade ind, da der ikke er nogen questionarires

# 407 
''' Start: tirsdag d. 6. april 2021 kl. sen aften
Slut: onsdag d. 14. april 2021 kl. formiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021'''
alz_407a = pd.read_excel('../DATA/02_Greenland/Building_ID_407/01_Measured_data/407a_18_Spring2021_Hobo.xlsx')
alz_407a = lu.only_work_hours_GL(alz_407a,0)
alz_407a = lu.make_invalid_nan_GL(alz_407a)

alz_407b = pd.read_excel('../DATA/02_Greenland/Building_ID_407/01_Measured_data/407b_19_Spring2021_Hobo.xlsx')
alz_407b = lu.only_work_hours_GL(alz_407b,0)
alz_407b = lu.make_invalid_nan_GL(alz_407b)

alz_407c = pd.read_excel('../DATA/02_Greenland/Building_ID_407/01_Measured_data/407c_17_Spring2021_Hobo.xlsx')
alz_407c = lu.only_work_hours_GL(alz_407c,0)
alz_407c = lu.make_invalid_nan_GL(alz_407c)


# 408  venter med at loade ind, da der ikke er nogen questionarires

# 409
''' Start: onsdag d. 7. april 2021 kl. aften
Slut: torsdag d. 15. april 2021 kl. middag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021
'''
alz_409a_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/01_Measured_data/409a_09_Spring2021_Hobo.xlsx')
alz_409a_co2 = lu.only_work_hours_GL(alz_409a_co2,0)
alz_409a_co2 = lu.make_invalid_nan_GL(alz_409a_co2)
alz_409a_light = pd.read_excel('../DATA/02_Greenland/Building_ID_409/01_Measured_data/409a_Hobolight09_Spring2021_Hobo.xlsx')
alz_409a_light = lu.only_work_hours_GL(alz_409a_light,0)
alz_409a_light = lu.make_invalid_nan_GL(alz_409a_light)
# Make dataframe
alz_409a_lst = [alz_409a_co2,alz_409a_light]
alz_409a = pd.concat(alz_409a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

alz_409b_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/01_Measured_data/409b_11_Spring2021_Hobo.xlsx')
alz_409b_co2 = lu.only_work_hours_GL(alz_409b_co2,0)
alz_409b_co2 = lu.make_invalid_nan_GL(alz_409b_co2)
alz_409b_light = pd.read_excel('../DATA/02_Greenland/Building_ID_409/01_Measured_data/409b_Hobolight11_Spring2021_Hobo.xlsx')
alz_409b_light = lu.only_work_hours_GL(alz_409b_light,0)
alz_409b_light = lu.make_invalid_nan_GL(alz_409b_light)
# Make dataframe
alz_409b_lst = [alz_409b_co2,alz_409b_light]
alz_409b = pd.concat(alz_409b_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

alz_409c_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/01_Measured_data/409c_12_Spring2021_Hobo.xlsx')
alz_409c_co2 = lu.only_work_hours_GL(alz_409c_co2,0)
alz_409c_co2 = lu.make_invalid_nan_GL(alz_409c_co2)
alz_409c_light = pd.read_excel('../DATA/02_Greenland/Building_ID_409/01_Measured_data/409c_Hobolight12_Spring2021_Hobo.xlsx')
alz_409c_light = lu.only_work_hours_GL(alz_409c_light,0)
alz_409c_light = lu.make_invalid_nan_GL(alz_409c_light)
# Make dataframe
alz_409c_lst = [alz_409c_co2,alz_409c_light]
alz_409c = pd.concat(alz_409c_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

''' Start: onsdag d. 7. april 2021 kl. sen aften
Slut: torsdag d. 15. april 2021 kl. middag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021
'''
alz_410a_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/01_Measured_data/410a_03_Spring2021_Hobo.xlsx')
alz_410a_co2 = lu.only_work_hours_GL(alz_410a_co2,0)
alz_410a_co2 = lu.make_invalid_nan_GL(alz_410a_co2)
alz_410a_light = pd.read_excel('../DATA/02_Greenland/Building_ID_410/01_Measured_data/410a_Hobolight03_Spring2021_Hobo.xlsx')
alz_410a_light = lu.only_work_hours_GL(alz_410a_light,0)
alz_410a_light = lu.make_invalid_nan_GL(alz_410a_light)
# Make dataframe
alz_410a_lst = [alz_410a_co2,alz_410a_light]
alz_410a = pd.concat(alz_410a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

alz_410b_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/01_Measured_data/410b_02_Spring2021_Hobo.xlsx')
alz_410b_co2 = lu.only_work_hours_GL(alz_410b_co2,0)
alz_410b_co2 = lu.make_invalid_nan_GL(alz_410b_co2)
alz_410b_light = pd.read_excel('../DATA/02_Greenland/Building_ID_410/01_Measured_data/410b_Hobolight02_Spring2021_Hobo.xlsx')
alz_410b_light = lu.only_work_hours_GL(alz_410b_light,0)
alz_410b_light = lu.make_invalid_nan_GL(alz_410b_light)
# Make dataframe
alz_410b_lst = [alz_410b_co2,alz_410b_light]
alz_410b = pd.concat(alz_410b_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

alz_410c_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/01_Measured_data/410c_04_Spring2021_Hobo.xlsx')
alz_410c_co2 = lu.only_work_hours_GL(alz_410c_co2,0)
alz_410c_co2 = lu.make_invalid_nan_GL(alz_410c_co2)
alz_410c_light = pd.read_excel('../DATA/02_Greenland/Building_ID_410/01_Measured_data/410c_Hobolight04_Spring2021_Hobo.xlsx')
alz_410c_light = lu.only_work_hours_GL(alz_410c_light,0)
alz_410c_light = lu.make_invalid_nan_GL(alz_410c_light)
# Make dataframe
alz_410c_lst = [alz_410c_co2,alz_410c_light]
alz_410c = pd.concat(alz_410c_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

#411
''' Start: torsdag d. 8. april 2021 kl. eftermiddag
Slut: fredag d. 16. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021
'''
alz_411a_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/01_Measured_data/411a_06_Spring2021_Hobo.xlsx')
alz_411a_co2 = lu.only_work_hours_GL(alz_411a_co2,0)
alz_411a_co2 = lu.make_invalid_nan_GL(alz_411a_co2)
alz_411a_light = pd.read_excel('../DATA/02_Greenland/Building_ID_411/01_Measured_data/411a_Hobolight06_Spring2021_Hobo.xlsx')
alz_411a_light = lu.only_work_hours_GL(alz_411a_light,0)
alz_411a_light = lu.make_invalid_nan_GL(alz_411a_light)
# Make dataframe
alz_411a_lst = [alz_411a_co2,alz_411a_light]
alz_411a = pd.concat(alz_411a_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

alz_411b_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/01_Measured_data/411b_05_Spring2021_Hobo.xlsx')
alz_411b_co2 = lu.only_work_hours_GL(alz_411b_co2,0)
alz_411b_co2 = lu.make_invalid_nan_GL(alz_411b_co2)
alz_411b_light = pd.read_excel('../DATA/02_Greenland/Building_ID_411/01_Measured_data/411b_Hobolight05_Spring2021_Hobo.xlsx')
alz_411b_light = lu.only_work_hours_GL(alz_411b_light,0)
alz_411b_light = lu.make_invalid_nan_GL(alz_411b_light)
# Make dataframe
alz_411b_lst = [alz_411b_co2,alz_411b_light]
alz_411b = pd.concat(alz_411b_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

alz_411c_co2 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/01_Measured_data/411c_08_Spring2021_Hobo.xlsx')
alz_411c_co2 = lu.only_work_hours_GL(alz_411c_co2,0)
alz_411c_co2 = lu.make_invalid_nan_GL(alz_411c_co2)
alz_411c_light = pd.read_excel('../DATA/02_Greenland/Building_ID_411/01_Measured_data/411c_Hobolight08_Spring2021_Hobo.xlsx')
alz_411c_light = lu.only_work_hours_GL(alz_411c_light,0)
alz_411c_light = lu.make_invalid_nan_GL(alz_411c_light)
# Make dataframe
alz_411c_lst = [alz_411c_co2,alz_411c_light]
alz_411c = pd.concat(alz_411c_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)



#412
''' Start: torsdag d. 8. april 2021 kl. eftermiddag
Slut: fredag d. 16. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021
'''
alz_412a = pd.read_excel('../DATA/02_Greenland/Building_ID_412/01_Measured_data/412a_20_Spring2021_Hobo.xlsx')
alz_412a = lu.only_work_hours_GL(alz_412a,0)
alz_412a = lu.make_invalid_nan_GL(alz_412a)

alz_412b = pd.read_excel('../DATA/02_Greenland/Building_ID_412/01_Measured_data/412b_23_Spring2021_Hobo.xlsx')
alz_412b = lu.only_work_hours_GL(alz_412b,0)
alz_412b = lu.make_invalid_nan_GL(alz_412b)

alz_412c = pd.read_excel('../DATA/02_Greenland/Building_ID_412/01_Measured_data/412c_21_Spring2021_Hobo.xlsx')
alz_412c = lu.only_work_hours_GL(alz_412c,0)
alz_412c = lu.make_invalid_nan_GL(alz_412c)


#413
''' Start: torsdag d. 8. april 2021 kl. eftermiddag
Slut: fredag d. 16. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021
'''
alz_413a = pd.read_excel('../DATA/02_Greenland/Building_ID_413/01_Measured_data/413a_29_Spring2021_Hobo.xlsx')
alz_413a = lu.only_work_hours_GL(alz_413a,0)
alz_413a = lu.make_invalid_nan_GL(alz_413a)

alz_413b = pd.read_excel('../DATA/02_Greenland/Building_ID_413/01_Measured_data/413b_33_Spring2021_Hobo.xlsx')
alz_413b = lu.only_work_hours_GL(alz_413b,0)
alz_413b = lu.make_invalid_nan_GL(alz_413b)

alz_413c = pd.read_excel('../DATA/02_Greenland/Building_ID_413/01_Measured_data/413c_35_Spring2021_Hobo.xlsx')
alz_413c = lu.only_work_hours_GL(alz_413c,0)
alz_413c = lu.make_invalid_nan_GL(alz_413c)


#414
'''Start: torsdag d. 8. april 2021 kl. eftermiddag
Slut: fredag d. 16. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021
'''
alz_414a = pd.read_excel('../DATA/02_Greenland/Building_ID_414/01_Measured_data/414a_31_Spring2021_Hobo.xlsx')
alz_414a = lu.only_work_hours_GL(alz_414a,0)
alz_414a = lu.make_invalid_nan_GL(alz_414a)

alz_414b = pd.read_excel('../DATA/02_Greenland/Building_ID_414/01_Measured_data/414b_32_Spring2021_Hobo.xlsx')
alz_414b = lu.only_work_hours_GL(alz_414b,0)
alz_414b = lu.make_invalid_nan_GL(alz_414b)

alz_414c = pd.read_excel('../DATA/02_Greenland/Building_ID_414/01_Measured_data/414c_24_Spring2021_Hobo.xlsx')
alz_414c = lu.only_work_hours_GL(alz_414c,0)
alz_414c = lu.make_invalid_nan_GL(alz_414c)


#415
'''Start: torsdag d. 8. april 2021 kl. aften
Slut: fredag d. 16. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021
'''
alz_415a = pd.read_excel('../DATA/02_Greenland/Building_ID_415/01_Measured_data/415a_30_Spring2021_Hobo.xlsx')
alz_415a = lu.only_work_hours_GL(alz_415a,0)
alz_415a = lu.make_invalid_nan_GL(alz_415a)

alz_415b = pd.read_excel('../DATA/02_Greenland/Building_ID_415/01_Measured_data/415b_25_Spring2021_Hobo.xlsx')
alz_415b = lu.only_work_hours_GL(alz_415b,0)
alz_415b = lu.make_invalid_nan_GL(alz_415b)

alz_415c = pd.read_excel('../DATA/02_Greenland/Building_ID_415/01_Measured_data/415c_28_Spring2021_Hobo.xlsx')
alz_415c = lu.only_work_hours_GL(alz_415c,0)
alz_415c = lu.make_invalid_nan_GL(alz_415c)


#416
'''Start: torsdag d. 8. april 2021 kl. aften
Slut: fredag d. 16. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021
'''
alz_416a = pd.read_excel('../DATA/02_Greenland/Building_ID_416/01_Measured_data/416a_34_Spring2021_Hobo.xlsx')
alz_416a = lu.only_work_hours_GL(alz_416a,0)
alz_416a = lu.make_invalid_nan_GL(alz_416a)

alz_416b = pd.read_excel('../DATA/02_Greenland/Building_ID_416/01_Measured_data/416b_26_Spring2021_Hobo.xlsx')
alz_416b = lu.only_work_hours_GL(alz_416b,0)
alz_416b = lu.make_invalid_nan_GL(alz_416b)

alz_416c = pd.read_excel('../DATA/02_Greenland/Building_ID_416/01_Measured_data/416c_27_Spring2021_Hobo.xlsx')
alz_416c = lu.only_work_hours_GL(alz_416c,0)
alz_416c = lu.make_invalid_nan_GL(alz_416c)


#417 - no co2
'''Start: fredag d. 9. april 2021 kl. eftermiddag (?)
Slut: mandag d. 19. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021 + Lørdag + Søndag d. 17. + 18. april 2021.
'''
alz_417a = pd.read_excel('../DATA/02_Greenland/Building_ID_417/01_Measured_data/417a_CO2-07_Spring2021_Hobo.xlsx')
alz_417a = lu.only_work_hours_GL(alz_417a,0)
alz_417a = lu.make_invalid_nan_GL(alz_417a)

alz_417b = pd.read_excel('../DATA/02_Greenland/Building_ID_417/01_Measured_data/417b_CO2-10_Spring2021_Hobo.xlsx')
alz_417b = lu.only_work_hours_GL(alz_417b,0)
alz_417b = lu.make_invalid_nan_GL(alz_417b)

alz_417c = pd.read_excel('../DATA/02_Greenland/Building_ID_417/01_Measured_data/417c_CO2-12_Spring2021_Hobo.xlsx')
alz_417c = lu.only_work_hours_GL(alz_417c,0)
alz_417c = lu.make_invalid_nan_GL(alz_417c)


#418 - no co2
'''Start: fredag d. 9. april 2021 kl. eftermiddag (?)
Slut: mandag d. 19. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021 + Lørdag + Søndag d. 17. + 18. april 2021.
'''
alz_418a = pd.read_excel('../DATA/02_Greenland/Building_ID_418/01_Measured_data/418a_CO2-01_Spring2021_Hobo.xlsx')
alz_418a = lu.only_work_hours_GL(alz_418a,0)
alz_418a = lu.make_invalid_nan_GL(alz_418a)

alz_418b = pd.read_excel('../DATA/02_Greenland/Building_ID_418/01_Measured_data/418b_CO2-06_Spring2021_Hobo.xlsx')
alz_418b = lu.only_work_hours_GL(alz_418b,0)
alz_418b = lu.make_invalid_nan_GL(alz_418b)

alz_418c = pd.read_excel('../DATA/02_Greenland/Building_ID_418/01_Measured_data/418c_CO2-11_Spring2021_Hobo.xlsx')
alz_418c = lu.only_work_hours_GL(alz_418c,0)
alz_418c = lu.make_invalid_nan_GL(alz_418c)


#419 - no co2
'''Start: fredag d. 9. april 2021 kl. eftermiddag (?)
Slut: mandag d. 19. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 10. og 11. april 2021 + Lørdag + Søndag d. 17. + 18. april 2021.
'''
alz_419a = pd.read_excel('../DATA/02_Greenland/Building_ID_419/01_Measured_data/419a_CO2-09_Spring2021_Hobo.xlsx')
alz_419a = lu.only_work_hours_GL(alz_419a,0)
alz_419a = lu.make_invalid_nan_GL(alz_419a)

alz_419b = pd.read_excel('../DATA/02_Greenland/Building_ID_419/01_Measured_data/419b_CO2-08_Spring2021_Hobo.xlsx')
alz_419b = lu.only_work_hours_GL(alz_419b,0)
alz_419b = lu.make_invalid_nan_GL(alz_419b)

alz_419c = pd.read_excel('../DATA/02_Greenland/Building_ID_419/01_Measured_data/419c_CO2-03_Spring2021_Hobo.xlsx')
alz_419c = lu.only_work_hours_GL(alz_419c,0)
alz_419c = lu.make_invalid_nan_GL(alz_419c)


#420 - no co2 in 420b
'''Start: tirsdag d. 13. april 2021 kl. eftermiddag (?)
Slut: onsdag d. 21. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 17. + 18. april 2021.
'''
alz_420a = pd.read_excel('../DATA/02_Greenland/Building_ID_420/01_Measured_data/420_alldata.xlsx','A')
alz_420a = lu.only_work_hours_GL(alz_420a,0)
alz_420a = lu.make_invalid_nan_GL(alz_420a)

alz_420b = pd.read_excel('../DATA/02_Greenland/Building_ID_420/01_Measured_data/420_alldata.xlsx','B')
alz_420b = lu.only_work_hours_GL(alz_420b,0)
alz_420b = lu.make_invalid_nan_GL(alz_420b)

alz_420c = pd.read_excel('../DATA/02_Greenland/Building_ID_420/01_Measured_data/420_alldata.xlsx','C')
alz_420c = lu.only_work_hours_GL(alz_420c,0)
alz_420c = lu.make_invalid_nan_GL(alz_420c)


#421 
'''Start: onsdag d. 14. april 2021 kl. eftermiddag
Slut: torsdag d. 22. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 17. + 18. april 2021.
'''
alz_421a = pd.read_excel('../DATA/02_Greenland/Building_ID_421/01_Measured_data/421a_17_Spring2021_Hobo.xlsx')
alz_421a = lu.only_work_hours_GL(alz_421a,0)
alz_421a = lu.make_invalid_nan_GL(alz_421a)

alz_421b = pd.read_excel('../DATA/02_Greenland/Building_ID_421/01_Measured_data/421b_18_Spring2021_Hobo.xlsx')
alz_421b = lu.only_work_hours_GL(alz_421b,0)
alz_421b = lu.make_invalid_nan_GL(alz_421b)

alz_421c = pd.read_excel('../DATA/02_Greenland/Building_ID_421/01_Measured_data/421c_19_Spring2021_Hobo.xlsx')
alz_421c = lu.only_work_hours_GL(alz_421c,0)
alz_421c = lu.make_invalid_nan_GL(alz_421c)


#422 
'''Start: onsdag d. 14. april 2021 kl. eftermiddag
Slut: torsdag d. 22. april 2021 kl. eftermiddag
Evt. weekend (evt. fratrækkes): Lørdag + Søndag d. 17. + 18. april 2021.
'''
alz_422a = pd.read_excel('../DATA/02_Greenland/Building_ID_422/01_Measured_data/422a_22_Spring2021_Hobo.xlsx')
alz_422a = lu.only_work_hours_GL(alz_422a,0)
alz_422a = lu.make_invalid_nan_GL(alz_422a)

alz_422b = pd.read_excel('../DATA/02_Greenland/Building_ID_422/01_Measured_data/422b_01_Spring2021_Hobo.xlsx')
alz_422b = lu.only_work_hours_GL(alz_422b,0)
alz_422b = lu.make_invalid_nan_GL(alz_422b)

alz_422c = pd.read_excel('../DATA/02_Greenland/Building_ID_422/01_Measured_data/422c_15_Spring2021_Hobo.xlsx')
alz_422c = lu.only_work_hours_GL(alz_422c,0)
alz_422c = lu.make_invalid_nan_GL(alz_422c)


#%%
# #%% ------------- Make alyzer dataframe

alz_GL = [lu.summary_meas_GL(alz_401b,401,'401b'),lu.summary_meas_GL(alz_401c,401,'401c'),
          lu.summary_meas_GL(alz_401d,401,'401d'),lu.summary_meas_GL(alz_401e,401,'401e'),
          
          lu.summary_meas_GL(alz_402a,402,'402a'),lu.summary_meas_GL(alz_402b,402,'402b'),
          lu.summary_meas_GL(alz_402c,402,'402c'),lu.summary_meas_GL(alz_402d,402,'402d'),
          lu.summary_meas_GL(alz_402e,402,'402e'),
          
          lu.summary_meas_GL(alz_403a,403,'403a'),lu.summary_meas_GL(alz_403b,403,'403b'),
          lu.summary_meas_GL(alz_403c,403,'403c'),lu.summary_meas_GL(alz_403d,403,'403d'),
          
          lu.summary_meas_GL(alz_404a,404,'404a'),lu.summary_meas_GL(alz_404b,404,'404b'),
          
          lu.summary_meas_GL(alz_405a,405,'405a'),lu.summary_meas_GL(alz_405b,405,'405b'),
          lu.summary_meas_GL(alz_405c,405,'405c'),lu.summary_meas_GL(alz_405d,405,'405d'),
          
          lu.summary_meas_GL(alz_407a,407,'407a'),lu.summary_meas_GL(alz_407b,407,'407b'),
          lu.summary_meas_GL(alz_407c,407,'407c'),
          
          lu.summary_meas_GL(alz_409a,409,'409a'),lu.summary_meas_GL(alz_409b,409,'409b'),
          lu.summary_meas_GL(alz_409c,409,'409c'),
          
          lu.summary_meas_GL(alz_410a,410,'410a'),lu.summary_meas_GL(alz_410b,410,'410b'),
          lu.summary_meas_GL(alz_410c,410,'410c'),
          
          lu.summary_meas_GL(alz_411a,411,'411a'),lu.summary_meas_GL(alz_411b,411,'411b'),
          lu.summary_meas_GL(alz_411c,411,'411c'),
          
          lu.summary_meas_GL(alz_412a,412,'412a'),lu.summary_meas_GL(alz_412b,412,'412b'),
          lu.summary_meas_GL(alz_412c,412,'412c'),
          
          lu.summary_meas_GL(alz_413a,413,'413a'),lu.summary_meas_GL(alz_413b,413,'413b'),
          lu.summary_meas_GL(alz_413c,413,'413c'),
          
          lu.summary_meas_GL(alz_414a,414,'414a'),lu.summary_meas_GL(alz_414b,414,'414b'),
          lu.summary_meas_GL(alz_414c,414,'414c'),
          
          lu.summary_meas_GL(alz_415a,415,'415a'),lu.summary_meas_GL(alz_415b,415,'415b'),
          lu.summary_meas_GL(alz_415c,415,'415c'),
          
          lu.summary_meas_GL(alz_416a,416,'416a'),lu.summary_meas_GL(alz_416b,416,'416b'),
          lu.summary_meas_GL(alz_416c,416,'416c'),
          
          lu.summary_meas_GL(alz_417a,417,'417a'),lu.summary_meas_GL(alz_417b,417,'417b'),
          lu.summary_meas_GL(alz_417c,417,'417c'),
          
          lu.summary_meas_GL(alz_418a,418,'418a'),lu.summary_meas_GL(alz_418b,418,'418b'),
          lu.summary_meas_GL(alz_418c,418,'418c'),
          
          lu.summary_meas_GL(alz_419a,419,'419a'),lu.summary_meas_GL(alz_419b,419,'419b'),
          lu.summary_meas_GL(alz_419c,419,'419c'),
          
          lu.summary_meas_GL(alz_420a,420,'420a'),lu.summary_meas_GL(alz_420b,420,'420b'),
          lu.summary_meas_GL(alz_420c,420,'420c'),
          
          lu.summary_meas_GL(alz_421a,421,'421a'),lu.summary_meas_GL(alz_421b,421,'421b'),
          lu.summary_meas_GL(alz_421c,421,'421c'),
          
          lu.summary_meas_GL(alz_422a,422,'422a'),lu.summary_meas_GL(alz_422b,422,'422b'),
          lu.summary_meas_GL(alz_422c,422,'422c')]

# # Make dataframe
df_alz_GL = pd.concat(alz_GL, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)
df_alz_GL['location'] = 'Greenland'


df_alz = pd.concat([df_alz_dk,df_alz_GL], axis=0, join='outer', ignore_index=True,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

df_alz = df_alz.set_index('officeID',drop=False)
#%% ------------- Make df of means



print("Top absolute correlation")
print(lu.get_top_abs_correlation(df_alz[['T_75p','T_25p','CO2_25p','CO2_75p','light_25p','light_75p','RH_25p','RH_75p','sound_75p','sound_25p']],10))




df_alz_means = df_alz.drop(['VOC_median','VOC_75p','VOC_25p','VOC_max','VOC_min',
                          'CO2_75p','CO2_median','CO2_25p','CO2_max','CO2_min',
                          'RH_median','RH_75p','RH_25p','RH_min','RH_max',
                          'T_median','T_75p','T_25p','T_min','T_max',
                          'sound_75p','sound_median','sound_25p','sound_min','sound_max',
                          'light_max','light_25p','light_75p','light_min','light_median'],axis=1)

df_alz_means = df_alz_means.set_index('officeID',drop=False)


#%% - Delete unwanted dataframes

del [alz_dk, alz_GL,
     
     alz_101b, alz_101c, alz_101d,
     
     alz_102a ,alz_102b,alz_102b1, alz_102b2, alz_102b_lst,
     
     alz_103a,alz_103a1,alz_103a3, alz_103a8, alz_103a_lst, alz_103b, alz_103b2, 
     alz_103b25, alz_103b_lst, alz_103c, alz_103c7, alz_103c22,alz_103c_lst, alz_103d, 
     
     alz_103Ea, alz_103Eb, alz_103Ec,
     
     alz_104a, alz_105a, alz_105a10, alz_105a22, alz_105a_lst,
     
     alz_301Ea, alz_301Eb, alz_301Ec, alz_301Ed,
     
     alz_301a,alz_301b, alz_301b13, alz_301b20,alz_301b_lst, alz_301c,
     
     alz_302a,alz_302b,alz_302c, alz_302d, alz_302e,
     
     alz_303a,alz_303b,alz_303c,alz_303d,
     
     alz_304a,alz_304b,alz_304c,alz_304d,
     
     alz_304e,alz_304f,alz_304g,
     
     alz_305Ab, alz_305Ac, alz_305Ad, alz_305Ae, alz_305Af, alz_305Ag, alz_305Ah, alz_305Ai,
     
     
     alz_3061a,alz_3061a10,alz_3061a12, alz_3061a_lst, alz_306oa, alz_306ob, 
     alz_307a23, alz_307a22,alz_307a17, alz_307a8, alz_307a_lst, alz_307a,
     
     
     alz_308Ab_lst, alz_308Ab, alz_308Ab10, alz_308Ab22,
     
     alz_309a, alz_309b, alz_309b2, alz_309b15, alz_309b_lst,
     
     alz_310a, alz_310a_lst, alz_310a18, alz_310a19, alz_310b,
     
     alz_311a, alz_311a11, alz_311a12, alz_311a_lst, alz_311b,
     
     alz_312a, alz_312a20, alz_312a21, alz_312a_lst, alz_312b, alz_312c,
     
     alz_313a, alz_313a11, alz_313a12, alz_313a13, alz_313a_lst, 
     alz_313b, alz_313b14, alz_313b16, alz_313b_lst, 
     alz_313c, alz_313c18, alz_313c19, alz_313c_lst, alz_313d, alz_313e, 
     alz_313f, alz_313f23, alz_313f25, alz_313f_lst, 
     
     
     alz_401b,alz_401c,alz_401d,alz_401e,
     alz_402a, alz_402b, alz_402c, alz_402d, alz_402e,
     alz_403a, alz_403b, alz_403a_lst,alz_403a_co2,alz_403a_light,
     alz_403b_co2,alz_403b_light, alz_403b_lst,alz_403c_lst,alz_403d_lst,
     alz_403c_co2,alz_403c_light,alz_403d_co2,alz_403d_light,
     
     alz_403c,alz_403d,
     
     alz_404a,alz_404b,
     
     alz_405a,alz_405b,alz_405c,alz_405d,
     
     alz_407a,alz_407b,alz_407c,
     
     alz_409a_co2,alz_409a_light,alz_409a_lst,alz_409a,
     alz_409b_co2,alz_409b_light,alz_409b_lst,alz_409b,
     alz_409c_co2,alz_409c_light,alz_409c_lst,alz_409c,
     
     alz_410a_co2,alz_410a_light,alz_410a_lst,alz_410a,
     alz_410b_co2,alz_410b_light,alz_410b_lst,alz_410b,
     alz_410c_co2,alz_410c_light,alz_410c_lst,alz_410c,
     
     alz_411a_co2,alz_411a_light,alz_411a_lst,alz_411a,
     alz_411b_co2,alz_411b_light,alz_411b_lst,alz_411b,
     alz_411c_co2,alz_411c_light,alz_411c_lst,alz_411c,
     
     alz_412a,alz_412b,alz_412c,
     
     alz_413a,alz_413b,alz_413c,
     
     alz_414a,alz_414b,alz_414c,
     
     alz_415a,alz_415b,alz_415c,
     
     alz_416a,alz_416b,alz_416c,
     
     alz_417a,alz_417b,alz_417c,
     
     alz_418a,alz_418b,alz_418c,
     
     alz_419a,alz_419b,alz_419c,
     
     alz_420a,alz_420b,alz_420c,
     
     alz_421a,alz_421b,alz_421c,
     
     alz_422a,alz_422b,alz_422c]
    

# %%

df_alz_means.to_csv("../temp_data/df_alz_means.csv", index=False)