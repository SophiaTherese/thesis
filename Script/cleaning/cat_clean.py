#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:19:25 2022

@author: Sophia

Categorial cleaning
"""
import numpy as np
import pandas as pd
import seaborn as sns

import clean_utils as cu

df_all = pd.read_csv("../temp_data/df_all_1hot.csv")

# sns.set(rc={'figure.figsize':(10,20)})

#%% 

# drop features without useful categorical information
df_all = df_all.drop(['O1_insulationOther','O2_otherCeilingComment', 'O2_otherWallCovComment', 
                      'O2_suspendedCeilingComment','O2_winShades',
                      
                      'building','OO_buildingID'],axis=1)



#%%
''' Building Checklist'''

# ----------------Site

sns.catplot(data=df_all, x="building_site", kind="count", palette="Greys",aspect=40/10)

print(df_all['building_site'].value_counts())

#merge categories
df_all['Site'] = df_all['building_site'].map({" O1urb_com":"urban",
                                                                    " O1urb_res":"urban",
                                                                    " O1urb_indus":"urban",
                                                                    " O1urb_com O1urb_res":"urban",
                                                                    " O1suburb_indus O1suburb_com":"suburban",
                                                                    " O1suburb_com":"suburban",
                                                                    " O1suburb_res":"suburban",
                                                                    " O1suburb_indus":"suburban",
                                                                    '':"none"
                                                                    })

sns.catplot(data=df_all, x="Site", kind="count", palette="Greys",height=4,aspect=1).set(title='Site')

print(df_all['Site'].value_counts())


df_all = df_all.drop(['O1rur_nurb','O1urb_com', 'O1urb_res', 'O1rur_agr','O1urb_indus','O1suburb_indus',
                      'O1suburb_res','O1suburb_com','O1rur_com','O1rur_ind','building_site'],axis=1)
#%% 

sns.catplot(data=df_all, x="Site", kind="count", palette='Greys',height=3,aspect=3/2).set(title='Site')

#%% ----------------building_ventType

sns.catplot(data=df_all, x="building_ventType", kind="count", palette="Greys",aspect=50/10)

print(df_all['building_ventType'].value_counts())

# da der for det meste også vil være naturlig vent, lader jeg den kun fremgå som enestående. 
# O1_exhaustSupplyHeat gælder over både exhaust og heat recovery, exhaust, og exhaust supply, 
# dem der har checket dem alle er derfor kun i den sidste kategori. 
df_all['bVentType'] = df_all['building_ventType'].map({" O1_natVentman O1_exhaust":"exhaust",
                                                                    " O1_natVentman O1_exhaustSupplyHeat":"exhaustSupplyHeat",
                                                                    " O1_natVentman O1_exhaustSupply":"exhaustSupply",
                                                                    " O1_natVentman":"natVentman",
                                                                    " O1_exhaustSupplyHeat":"exhaustSupplyHeat",
                                                                    " O1_exhaustSupply":"exhaustSupply",
                                                                    " O1_natVentman O1_exhaust O1_exhaustSupply O1_exhaustSupplyHeat":"exhaustSupplyHeat",
                                                                    '':"noAnswer"
                                                                    })
sns.catplot(data=df_all, x="bVentType", kind="count", palette="Greys",aspect=20/10)

print(df_all['bVentType'].value_counts())

df_all = df_all.drop(['O1_natVentman','O1_exhaustSupplyHeat','O1_exhaustSupply',
                      'O1_exhaust','building_ventType','O1_natVentAut'],axis=1)



#%% ----------------building_heatType


sns.catplot(data=df_all, x="building_heatType", kind="count", palette="Greys",aspect=50/10)


print(df_all['building_heatType'].value_counts())


df_all['b_heatT'] = df_all['building_heatType'].map({" O1_radiators":"radiators",
                                                     " O1_airHeatWater":"airHeat",
                                                     " O1_airHeatEl O1_radiators":"radiatorAirHeat",
                                                     " O1_airHeatWater O1_radiators":"radiatorAirHeat",
                                                     " O1_airHeatEl":"airHeat"})

sns.catplot(data=df_all, x="b_heatT", kind="count", palette="Greys",aspect=50/10)
print(df_all['b_heatT'].value_counts())



# combine electric and water air heating - in 1-hot
cu.merge_binary(df_all,'O1_airHeatEl','O1_airHeatWater','airHeat')
df_all['radiatorHeat'] = df_all['O1_radiators'].map({1:"True",0:"False"})

print(df_all['airHeat'].value_counts())


# no examples of floor heating - so drop

# Drop gathered category
df_all = df_all.drop(['b_heatT','building_heatType','O1_floorHeat','O1_radiators','O1_airHeatWater','O1_airHeatEl'],axis=1)


#%% ----------------building_coolType


sns.catplot(data=df_all, x="building_coolType", kind="count", palette="Greys",aspect=50/10)

#'building_coolType',['O1_individualCooling', 'O1_centralCooling','O1_noCooling'

# Drop 
df_all = df_all.drop(['O1_individualCooling','O1_centralCooling','O1_noCooling'],axis=1)


#%% ----------------building_facadeType

sns.catplot(data=df_all, x="building_facadeType", kind="count", palette="Greys",aspect=50/10)
print(df_all['building_facadeType'].value_counts())

'''combine asbestos cement and concrete'
    concrete + brick -> brick
    asbestos + wood -> wood'''

df_all['building_facadeType'] = df_all['building_facadeType'].map({" O1_facadeConcrete":"concrete",
                                                                   " O1_facadeBrick":"brick",
                                                                   " O1_facadeWood":"wood",
                                                                   " O1_facadeAsbest":"concrete",
                                                                   " O1_facadeWood O1_facadeAsbest":"wood",
                                                                   " O1_facadeBrick O1_facadeConcrete":"brick"})

print(df_all['building_facadeType'].value_counts())


sns.catplot(data=df_all, x="building_facadeType", kind="count", palette="Greys",aspect=50/10)
#building_facadeType',['O1_facadeBrick', 'O1_facadeConcrete','O1_facadeWood','O1_facadeAsbest'

df_all = df_all.drop(['O1_facadeBrick','O1_facadeConcrete','O1_facadeWood','O1_facadeAsbest'],axis=1)


#%% ----------------building_intWallType - drop instead of office checklist

sns.catplot(data=df_all, x="building_intWallType", kind="count", palette="Greys",aspect=50/10)
print(df_all['building_intWallType'].value_counts())


df_all = df_all.drop(['O1_intWallBrick','O1_intWallGypsum','O1_intWallWood','O1_intWallConcrete','building_intWallType'],axis=1)

#%% ----------------building_extWallType

sns.catplot(data=df_all, x="building_extWallType", kind="count", palette="Greys",aspect=50/10)
print(df_all['building_extWallType'].value_counts())

df_all['building_extWallType'] = df_all['building_extWallType'].map({" O1_extWallWood":"wood",
                                                                     " O1_extWallConcrete":"concrete",
                                                                     " O1_extWallConcrete O1_extWallBrick":"brick",
                                                                     " O1_extWallBrick":"brick",
                                                                     " O1_extWallConcrete O1_extWallWood":"wood"})

sns.catplot(data=df_all, x="building_extWallType", kind="count", palette="Greys",aspect=50/10)
print(df_all['building_extWallType'].value_counts())

df_all = df_all.drop(['O1_extWallConcrete','O1_extWallBrick','O1_extWallWood'],axis=1)

#'O1_extWallConcrete','O1_extWallBrick','O1_extWallWood'

#%% ----------------building_insType

sns.catplot(data=df_all, x="building_insType", kind="count", palette="Greys",aspect=50/10)
print(df_all['building_insType'].value_counts())

df_all['building_insType'] = df_all['building_insType'].map({" O1_exteriorInsulation":"exteriorInsulation",
                                                             " O1_interiorInsulation":"O1_interiorInsulation",
                                                             " O1_cavityInsulation":"cavityInsulation"})

#'O1_exteriorInsulation','O1_interiorInsulation','O1_cavityInsulation'
df_all = df_all.drop(['O1_exteriorInsulation','O1_interiorInsulation','O1_cavityInsulation'],axis=1)


#%% ----------------OO_buildingTypology  - drop

sns.catplot(data=df_all, x="OO_buildingTypology", kind="count", palette="Greys",aspect=50/10)
print(df_all['OO_buildingTypology'].value_counts())

#%%
sns.catplot(data=df_all, x="Renovation Year", kind="count", palette="Greys",aspect=50/10)
print(df_all['Renovation Year'].value_counts())

#  - mapping ordinal
df_all['Renovation Year'] = df_all['Renovation Year'].map({"noRenovation":0,
                                                         "1990-2009":1,
                                                         "2010<":2})

print(df_all['Renovation Year'].value_counts())
#%%
sns.catplot(data=df_all, x="Renovation Year", kind="count", palette="Greys",height=4,aspect=3/2).set(title='Renovation year')

#%%
df_all = df_all.drop(['OO_buildingTypology'],axis=1)

#too many nan

#%% ----------------manage_outdoorCont
''' Building Checklist'''

sns.catplot(data=df_all, x="manage_outdoorCont", kind="count", palette="Greys",aspect=50/10)
print(df_all['manage_outdoorCont'].value_counts())

# df_all['manage_outdoorCont'] = df_all['manage_outdoorCont'].map({" O2_garbageDumpsters":"garbageDumpsters",
#                                                              " O2_heavyTraffic":"heavyTraffic",
#                                                              " O2_garbageDumpsters O2_heavyTraffic":"multiple",
#                                                              " O2_heavyTraffic O2_constructionActivities":"multiple",
#                                                              " O2_garbageDumpsters O2_smokeStack":"multiple",
#                                                              " O2_noOutdoorContSources":"noOutdoorContSources",
#                                                              " O2_garbageDumpsters O2_powerPlants O2_heavyTraffic O2_emergencyGenerators O2_smokeStack":"multiple",
#                                                              " O2_garbageDumpsters O2_emergencyGenerators O2_smokeStack":"multiple",
#                                                              " O2_garbageDumpsters O2_heavyTraffic O2_constructionActivities":"multiple",
#                                                              " O2_garbageDumpsters O2_constructionActivities":"multiple"})


cu.merge_binary(df_all,'O2_smokeStack','O2_emergencyGenerators','outdoorCont_smokeGenerators')

df_all['outdoorCont_heavyTraffic'] = df_all['O2_heavyTraffic'].map({1:"True",0:"False"})
df_all['outdoorCont_garbageDumpsters'] = df_all['O2_garbageDumpsters'].map({1:"True",0:"False"})
df_all['outdoorCont_powerPlants'] = df_all['O2_powerPlants'].map({1:"True",0:"False"})
df_all['outdoorCont_constructionActivities'] = df_all['O2_constructionActivities'].map({1:"True",0:"False"})

df_all['noOutdoorContSources'] = df_all['O2_noOutdoorContSources'].map({1:"True",0:"False"})


#'manage_outdoorCont',['O2_garbageDumpsters','O2_powerPlants','O2_heavyTraffic','O2_constructionActivities','O2_emergencyGenerators','O2_smokeStack','O2_noOutdoorContSources'
df_all = df_all.drop(['O2_garbageDumpsters','O2_powerPlants','O2_heavyTraffic','O2_constructionActivities','O2_emergencyGenerators','O2_smokeStack','O2_noOutdoorContSources','manage_outdoorCont'],axis=1)
#%% cleaning

sns.catplot(data=df_all, x="O3_deskWash", kind="count", palette="Greys",aspect=50/10)
print(df_all['O3_deskWash'].value_counts())

#  - mapping ordinal
df_all['deskWash'] = df_all['O3_deskWash'].map({"never":0,
                                                "onceWeek":4,
                                                "2-4":5,
                                                "everyDay":6})

print(df_all['deskWash'].value_counts())

#%%
sns.catplot(data=df_all, x="O3_floorMope", kind="count", palette="Greys",aspect=50/10)
print(df_all['O3_floorMope'].value_counts())

#  - mapping ordinal
df_all['Floor mopping frequency'] = df_all['O3_floorMope'].map({"never":0,
                                                              "lessFreq":1,
                                                              "onceMonth":2,
                                                              "secondWeek":3,                                        
                                                              "onceWeek":4,
                                                              "2-4":5,
                                                              "everyDay":6})

print(df_all['Floor mopping frequency'].value_counts())
#%%
sns.catplot(data=df_all, x="Floor mopping frequency", kind="count", palette="Greys",height=4,aspect=3/1).set(title='Frequency of floor mopping')

#%%
sns.catplot(data=df_all, x="O3_floorVacuum", kind="count", palette="Greys",aspect=50/10)
print(df_all['O3_floorVacuum'].value_counts())

#  - mapping ordinal
df_all['floorVacuum'] = df_all['O3_floorVacuum'].map({"never":0,
                                                      "lessFreq":1,
                                                      "onceMonth":2,
                                                      "secondWeek":3,
                                                      "onceWeek":4,
                                                      "2-4":5,
                                                      "everyDay":6})

print(df_all['floorVacuum'].value_counts())


#%%
sns.catplot(data=df_all, x="O3_winWash", kind="count", palette="Greys",aspect=50/10)
print(df_all['O3_winWash'].value_counts())


#  - mapping ordinal
df_all['winWash'] = df_all['O3_winWash'].map({"never":0,
                                              "lessFreq":1,
                                              "onceMonth":2,
                                              "secondWeek":3,
                                              "onceWeek":4,
                                              "2-4":5,
                                              "everyDay":6})

print(df_all['winWash'].value_counts())


#%% replace nan in cleaning  with mode
lst_ordinal_clean = [['deskWash','Floor mopping frequency','floorVacuum','winWash']]
for column in lst_ordinal_clean: 
    df_all[column] = df_all[column].fillna(df_all[column].median())


#%% cleaning materials
sns.catplot(data=df_all, x="O3_envMat", kind="count", palette="Greys",aspect=50/10)
print(df_all['O3_envMat'].value_counts())
#%%
#  - mapping ordinal
df_all['envMat_clean'] = df_all['O3_envMat'].map({"none":0,
                                                  "lessThan50%":1,
                                                  "moreThan50%":1,
                                                  "1":np.nan,
                                                  "100%":2})

#fill nan with 0. 
df_all['envMat_clean'] = df_all['envMat_clean'].fillna(0)
print(df_all['envMat_clean'].value_counts())

df_all = df_all.drop(['O3_deskWash','O3_floorMope','O3_floorVacuum','O3_winWash','O3_envMat'],axis=1)

#%%
''' office 1'''

#office type - office
sns.catplot(data=df_all, x="O2_officeType", kind="count", palette="Greys",aspect=50/10)
print(df_all['O2_officeType'].value_counts())

# drops this office description as the occupant version is more accurtate
df_all = df_all.drop(['O2_officeType'],axis=1)

#%% officetype  - ocupant
sns.catplot(data=df_all, x="officeInterior", kind="count", palette="Greys",aspect=50/10)
print(df_all['officeInterior'].value_counts())

#%%
sns.catplot(data=df_all, x="officeInterior", kind="count", palette="Greys",height=4,aspect=3/2).set(title='Office interior')

#%% windows - office
sns.catplot(data=df_all, x="O2_windowOrientation", kind="count", palette="Greys",aspect=50/10)
print(df_all['O2_windowOrientation'].value_counts())
df_all['office_windowOrientation'] = df_all['O2_windowOrientation'].map({"West":"West",
                                                                         "Northeast":"Northeast",
                                                                         "East":"East",
                                                                         "South":"South",
                                                                         "North":"North",
                                                                         "Southwest":"Southwest",
                                                                         "Northwest":"Northwest",
                                                                         "Southeast":"Southeast",
                                                                         "0":np.nan})

print(df_all['office_windowOrientation'].value_counts())



#%% windows - occupant
sns.catplot(data=df_all, x="windowOrientation", kind="count", palette="Greys",aspect=50/10)
print(df_all['windowOrientation'].value_counts())

df_all['occupant_windowOrientation'] = df_all['windowOrientation'].map({"west":"west",
                                                                         "norhteast":"norhteast",
                                                                         "east":"east",
                                                                         "south":"south",
                                                                         "north":"north",
                                                                         "southwest":"southwest",
                                                                         "northwest":"northwest",
                                                                         "southeast":"southeast",
                                                                         "---":np.nan})
print(df_all['occupant_windowOrientation'].value_counts())

df_all = df_all.drop(['O2_windowOrientation','windowOrientation'],axis=1)
#%%----------------office_exteriorView'
sns.catplot(data=df_all, x="office_exteriorView", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_exteriorView'].value_counts())

# combine road parking and other buildings
cu.merge_binary(df_all,'O2_viewRoadParking','O2_viewOtherBuildings','viewRoadBuildings')

df_all['viewGreenNature'] = df_all['O2_viewGreenNature'].map({1:True,0:False})


df_all = df_all.drop(['O2_viewGreenNature','O2_viewRoadParking','O2_viewOtherBuildings','office_exteriorView'],axis=1)

#,['O2_viewGreenNature','O2_viewRoadParking','O2_viewOtherBuildings'],df_all)

#%%
sns.catplot(data=df_all, x="viewGreenNature", kind="count", palette="Greys",height=3,aspect=3/2).set(title='View of green nature')
#%%----------------office_wallFinish

sns.catplot(data=df_all, x="office_wallFinish", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_wallFinish'].value_counts())


df_all['office_wallFinish'] = df_all['office_wallFinish'].map({" O2_paintWallboard":"paintWallboard",
                                                               " O2_paintWallboard O2_otherWallCov":"paintWallboard",
                                                               " O2_wallpaper":"wallpaper",
                                                               " O2_paintWallboard O2_wallpaper":"paintWallboard",
                                                               " O2_fabric":"fabric",
                                                               " O2_wallpaper O2_otherWallCov ":"wallpaper"})

sns.catplot(data=df_all, x="office_wallFinish", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_wallFinish'].value_counts())
#'O2_paintWallboard','O2_fabric','O2_metal','O2_wallpaper','O2_otherWallCov','O2_woodPanels'


df_all = df_all.drop(['O2_paintWallboard','O2_fabric','O2_metal','O2_wallpaper','O2_otherWallCov','O2_woodPanels'],axis=1)


#%%----------------office_ceilingFinish

sns.catplot(data=df_all, x="office_ceilingFinish", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_ceilingFinish'].value_counts())

#cu.merge_binary(df_all,'O1_airHeatEl','O1_airHeatWater','airHeat')

# making O2_ceilingWoodPanels into other

df_all['office_ceilingFinish'] = df_all['office_ceilingFinish'].map({" O2_ceilingBoards":"ceilingBoards",
                                                                     " O2_ceilingWoodPanels":"otherCeiling",
                                                                     " O2_otherCeiling":"otherCeiling",
                                                                     " O2_ceilingMetal":"otherCeiling",
                                                                     " O2_ceilingConcrete":"ceilingConcrete",
                                                                     
                                                                     " O2_ceilingBoards O2_ceilingWoodPanels":"ceilingBoards",
                                                                     
                                                                     " O2_ceilingBoards O2_otherCeiling":"ceilingBoards"})

sns.catplot(data=df_all, x="office_ceilingFinish", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_ceilingFinish'].value_counts())
#'O2_suspendedCeiling','O2_ceilingFabric','O2_ceilingMetal','O2_ceilingConcrete','O2_ceilingBoards','O2_ceilingWoodPanels','O2_otherCeiling'

#df_all = df_all.drop(['O2_ceilingFabric','office_ceilingFinish'],axis=1)

# efterlader O2_suspendedCeiling som binær
df_all['suspendedCeiling'] = df_all['O2_suspendedCeiling'].map({1:"True",0:"False"})

df_all = df_all.drop(['O2_ceilingFabric','O2_ceilingMetal','O2_ceilingConcrete','O2_ceilingBoards','O2_ceilingWoodPanels','O2_otherCeiling','O2_suspendedCeiling'],axis=1)


#%%----------------office_floorFinish

sns.catplot(data=df_all, x="office_floorFinish", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_floorFinish'].value_counts())


df_all['floorCarpet'] = df_all['O2_floorCarpet'].map({1:"True",0:"False"})
df_all['floorWood'] = df_all['O2_floorWood'].map({1:"True",0:"False"})
df_all['floorPlastic'] = df_all['O2_floorPlastic'].map({1:"True",0:"False"})


#'O2_floorCarpet','O2_floorWood','O2_floorConcrete','O2_floorPlastic'

df_all = df_all.drop(['O2_floorConcrete','office_floorFinish',
                      'O2_floorCarpet','O2_floorWood','O2_floorPlastic'],axis=1)

# keeping O2_floorCarpet, O2_floorPlastic, O2_floorWood as binary


#%% - deterioration
sns.catplot(data=df_all, x="O2_crackWinPaint", kind="count", palette="Greys",aspect=50/10)
print(df_all['O2_crackWinPaint'].value_counts())

df_all['office_crackWinPaint'] = df_all['O2_crackWinPaint'].map({"no":0,
                                                                 "little":1,
                                                                 "lot":2})

df_all['office_crackWinPaint'] = df_all['office_crackWinPaint'].fillna(0)

print(df_all['office_crackWinPaint'].value_counts())
df_all = df_all.drop(['O2_crackWinPaint'],axis=1)




#%%----------------office_lightType

#light type
sns.catplot(data=df_all, x="office_lightType", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_lightType'].value_counts())

# keep as binary


#'O2_lightLED','O2_lightIncan','O2_lightFlour'



df_all['lightLED'] = df_all['O2_lightLED'].map({1:"True",0:"False"})
df_all['lightIncan'] = df_all['O2_lightIncan'].map({1:"True",0:"False"})
df_all['lightFlour'] = df_all['O2_lightFlour'].map({1:"True",0:"False"})

df_all = df_all.drop(['office_lightType','O2_lightLED','O2_lightIncan','O2_lightFlour'],axis=1)
#%%
# desk lights
sns.catplot(data=df_all, x="O2_desklight", kind="count", palette="Greys",aspect=50/10)
print(df_all['O2_desklight'].value_counts())

df_all['office_desklights'] = df_all['O2_desklight'].map({"none":0,
                                                          "<50%":1,
                                                          "0.5":2,
                                                          ">50%":3,
                                                          "all":4})

df_all['office_desklights'] = df_all['office_desklights'].fillna(0)


sns.catplot(data=df_all, x="office_desklights", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_desklights'].value_counts())

df_all = df_all.drop(['O2_desklight'],axis=1)

#%%----------------office_supplyAir

sns.catplot(data=df_all, x="office_supplyAir", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_supplyAir'].value_counts())

# combining different ceiling diffueser

df_all['office_supplyAir'] = df_all['office_supplyAir'].map({" O2_ventNoSupply":"ventNoSupply",
                                                             " O2_ventLinCeilDif":"ventCeilDif",
                                                             " O2_ventPerfCeiling":"ventPerfCeiling",
                                                             " O2_ventRoundDif":"ventCeilDif",
                                                             " O2_ventSideWallDif O2_ventRoundDif":"ventWallVeilDif",
                                                             " O2_ventFancoil O2_ventNoSupply":"ventFancoil",
                                                             " O2_ventSideWallDif":"ventWallDif",
                                                             " O2_ventLinCeilDif O2_ventNoSupply":"ventCeilDif"})

sns.catplot(data=df_all, x="office_supplyAir", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_supplyAir'].value_counts())



#'O2_ventWallGrill','O2_ventLinCeilDif','O2_ventLowFloorGrill','O2_ventLuminaires','O2_ventSideWallDif','O2_ventPerfCeiling','O2_ventFloorReg','O2_ventFloorDif','O2_ventFancoil','O2_ventRoundDif','O2_ventOther','O2_ventNoSupply'

df_all = df_all.drop(['O2_ventWallGrill','O2_ventLowFloorGrill','O2_ventLuminaires','O2_ventFloorReg','O2_ventFloorDif','O2_ventOther',
                      'O2_ventLinCeilDif','O2_ventSideWallDif','O2_ventPerfCeiling','O2_ventFancoil','O2_ventRoundDif','O2_ventNoSupply'],axis=1)




#%%----------------office_returnAir

sns.catplot(data=df_all, x="office_returnAir", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_returnAir'].value_counts())

#O2_ventReturnSideGrill are placed high up on the wall and i will merge them with ceiling grills

df_all['office_returnAir'] = df_all['office_returnAir'].map({" O2_ventNoReturn":"ventNoReturn",
                                                             " O2_ventReturnCeilGrill":"O2_ventReturnGrill",
                                                             " O2_ventReturnOther":"ventReturnOther",
                                                             " O2_ventReturnSideGrill":"O2_ventReturnGrill",
                                                             " O2_ventReturnCeilSlot":"ventReturnCeilSlot",
                                                             " O2_ventReturnCeilGrill O2_ventReturnSideGrill":"O2_ventReturnGrill",
                                                             " O2_ventReturnOther O2_ventNoReturn":"ventReturnOther"})


sns.catplot(data=df_all, x="office_returnAir", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_returnAir'].value_counts())



df_all = df_all.drop(['O2_ventReturnCeilGrill','O2_ventReturnCeilSlot','O2_ventReturnSlotsLum','O2_ventReturnFloorGrill',
                      'O2_ventReturnSideGrill','O2_ventReturnOther','O2_ventNoReturn'],axis=1)

#'O2_ventReturnCeilGrill','O2_ventReturnCeilSlot','O2_ventReturnSlotsLum','O2_ventReturnFloorGrill','O2_ventReturnSideGrill','O2_ventReturnOther','O2_ventNoReturn'

#%%----------------office_niceThings

sns.catplot(data=df_all, x="office_niceThings", kind="count", palette="Greys",aspect=50/10)
print(df_all['office_niceThings'].value_counts())

#'O2_otherGreenPlants','O2_otherArt','O2_otherWallColor','O2_otherWaterEl','O2_otherLounge','O2_otherOther'

cu.merge_binary(df_all,'O2_otherGreenPlants','O2_otherWaterEl','otherPlantWater')
cu.merge_binary(df_all,'O2_otherArt','O2_otherWallColor','otherColArt')

df_all['otherLounge'] = df_all['O2_otherLounge'].map({1:"True",0:"False"})

#df_other = df_all[['O2_otherGreenPlants','O2_otherArt','O2_otherWallColor','O2_otherWaterEl','O2_otherLounge','O2_otherOther']]

df_all = df_all.drop(['office_niceThings','O2_otherGreenPlants','O2_otherWaterEl',
                      'O2_otherArt','O2_otherWallColor','O2_otherOther','O2_otherLounge'],axis=1)


#%%
''' questionnaire'''


#----------------occupant_odour

sns.catplot(data=df_all, x="occupant_odour", kind="count", palette="Greys",aspect=50/10)
print(df_all['occupant_odour'].value_counts())


cu.merge_binary(df_all,'photocopier','printer','tech')


df_all['food'] = df_all['food'].map({1:"True",0:"False"})
df_all['perfume'] = df_all['perfume'].map({1:"True",0:"False"})
df_all['tobaccoSmoke'] = df_all['tobaccoSmoke'].map({1:"True",0:"False"})

df_all['cleaningProd'] = df_all['cleaningProd'].map({1:"True",0:"False"})
df_all['carpet'] = df_all['carpet'].map({1:"True",0:"False"})
df_all['smells_outside'] = df_all['outside'].map({1:"True",0:"False"})



df_all = df_all.drop(['photocopier','printer','occupant_odour','outside'],axis=1)
#%%
sns.catplot(data=df_all, x="smells_outside", kind="count", palette="Greys",height=3,aspect=3/2).set(title='Odours from outside')

#%%----------------occupant_noise

sns.catplot(data=df_all, x="occupant_noise", kind="count", palette="Greys",aspect=50/10)
print(df_all['occupant_noise'].value_counts())


cu.merge_binary_3(df_all,'noisePhoneTalk','noiseOverhearing','noiseNeighborTalk','talk')
cu.merge_binary(df_all,'noiseTraffic','noisemechanical','noiseExterior')

df_all['noiseOfficeEquipment'] = df_all['noiseOfficeEquipment'].map({1:"True",0:"False"})
df_all['noiseTelephones'] = df_all['noiseTelephones'].map({1:"True",0:"False"})


#'noiseTraffic','noiseOverhearing','noiseOfficeEquipment','noisePhoneTalk','noiseNeighborTalk','noisemechanical','noiseTelephones'


df_all = df_all.drop(['noisePhoneTalk','noiseOverhearing','noiseNeighborTalk',
                      'noiseTraffic','noisemechanical','occupant_noise'],axis=1)
#%%
sns.catplot(data=df_all, x="noiseTelephones", kind="count", palette="Greys",height=3,aspect=3/2).set(title='Noise from telephones')
sns.catplot(data=df_all, x="noiseOfficeEquipment", kind="count", palette="Greys",height=3,aspect=3/2).set(title='Noise from office equipment')
sns.catplot(data=df_all, x="noiseExterior", kind="count", palette="Greys",height=3,aspect=3/2).set(title='Noises from traffic or machinery')
sns.catplot(data=df_all, x="talk", kind="count", palette="Greys",height=3,aspect=3/2).set(title='Noise from overhearing, neighbours talking or phone talk')


#%%----------------occupant light

sns.catplot(data=df_all, x="occupant_light_level", kind="count", palette="Greys",aspect=50/10)
print(df_all['occupant_light_level'].value_counts())

sns.catplot(data=df_all, x="occupant_light_other", kind="count", palette="Greys",aspect=50/10)
print(df_all['occupant_light_other'].value_counts())

#%%
sns.catplot(data=df_all, x="occupant_daylight", kind="count", palette="Greys",aspect=50/10)
print(df_all['occupant_daylight'].value_counts())

df_all['lightTooLittleDaylight'] = df_all['lightTooLittleDaylight'].map({1:"True",0:"False"})
df_all['lightTooMuchDaylight'] = df_all['lightTooMuchDaylight'].map({1:"True",0:"False"})


#%%

#ordinal:
df_all['daylight'] = df_all['occupant_daylight'].map({" lightTooLittleDaylight":0," lightTooMuchDaylight":2,np.nan:1})
print(df_all['daylight'].value_counts())


#%%
sns.catplot(data=df_all, x="daylight", kind="count", palette="Greys",height=4,aspect=3/1).set(title='Daylight')

#%%

df_light = df_all[['lightReflections','lightNoTask','lightFlicker']]

df_all['lightTooDark'] = df_all['lightTooDark'].map({1:"True",0:"False"})
df_all['lightTooBright'] = df_all['lightTooBright'].map({1:"True",0:"False"})



#dropping light colour as it is only nan

#Merge disturbing light features like reflections, flicker into one, and inability to perform tasks
#cu.merge_binary_3(df_all,'lightReflections','lightNoTask','lightFlicker','light_other')


df_all['lightReflections'] = df_all['lightReflections'].map({1:"True",0:"False"})
df_all['lightNoTask'] = df_all['lightNoTask'].map({1:"True",0:"False"})
df_all['lightFlicker'] = df_all['lightFlicker'].map({1:"True",0:"False"})



df_all = df_all.drop(['occupant_light_level','lightColor','occupant_light_other'],axis=1)


print(df_all['daylight'].value_counts())
df_all = df_all.drop(['occupant_daylight'],axis=1)


#%%
'''occupant specific'''

#sex
sns.catplot(data=df_all, x="sex", kind="count", palette="Greys",aspect=50/10)
print(df_all['sex'].value_counts())


df_all['sex'] = df_all['sex'].map({"Male":"Male",
                                   "Female":"Female",
                                   "NoReponse":np.nan,
                                   '':np.nan})
print(df_all['sex'].value_counts())


#%%
sns.catplot(data=df_all, x="sex", kind="count", palette="Greys",height=3,aspect=3/2).set(title='Sex')


#%%
#age
sns.catplot(data=df_all, x="age", kind="count", palette="Greys",aspect=50/10)
print(df_all['age'].value_counts())

df_all['age'] = df_all['age'].map({"_20-29":0,
                                   "_30-39":1,
                                   "_40-49":2,
                                   "_50-60":3,
                                   "_>60":4,
                                   "----":np.nan})

df_all['age'] = df_all['age'].fillna(df_all['age'].median())

print(df_all['age'].value_counts())
#%%
sns.catplot(data=df_all, x="age", kind="count", palette="Greys",height=4,aspect=3/1).set(title='Age')

#%%
#job
sns.catplot(data=df_all, x="job", kind="count", palette="Greys",aspect=50/10)
print(df_all['job'].value_counts())

df_all['job'] = df_all['job'].map({"Administrative":"Administrative",
                                   "Technical":"Technical",
                                   "Managerial":"Managerial",
                                   "Professional":"Professional"})
print(df_all['job'].value_counts())
#%%


#contacts
sns.catplot(data=df_all, x="contacts", kind="count", palette="Greys",aspect=50/10)
print(df_all['contacts'].value_counts())

df_all['eyeWear'] = df_all['contacts'].map({"Glasses":"Glasses_contacts",
                                            "Contacts":"Glasses_contacts",
                                            "None":"None"})

df_all = df_all.drop(['contacts'],axis=1)

#%%
sns.catplot(data=df_all, x="eyeWear", kind="count", palette="Greys",height=3,aspect=3/2).set(title='Eye wear')


#%% smoker
sns.catplot(data=df_all, x="smoker", kind="count", palette="Greys",aspect=50/10)
print(df_all['smoker'].value_counts())

#%% Distance to window
sns.catplot(data=df_all, x="distToWindow", kind="count", palette="Greys",aspect=50/10)
print(df_all['distToWindow'].value_counts())

df_all['distToWindow'] = df_all['distToWindow'].map({"0-2":0,
                                                     "2-3":1,
                                                     "2-4":2,
                                                     ">4":3})

df_all['distToWindow'] = df_all['distToWindow'].fillna(df_all['distToWindow'].median())

print(df_all['distToWindow'].value_counts())

#%% persons in office
sns.catplot(data=df_all, x="personsInOffice", kind="count", palette="Greys",aspect=50/10)
print(df_all['personsInOffice'].value_counts())
#%%
df_all['personsInOffice'] = df_all['personsInOffice'].map({"1":0,
                                                           "2021-03-02 00:00:00":1,
                                                           "2-3":1,
                                                           "4-5":2,
                                                           ">5":3})
#%%
df_all['personsInOffice'] = df_all['personsInOffice'].fillna(df_all['personsInOffice'].median())

print(df_all['personsInOffice'].value_counts())

#%% hours at desk
sns.catplot(data=df_all, x="hoursatdesk", kind="count", palette="Greys",aspect=50/10)
print(df_all['hoursatdesk'].value_counts())

df_all['hoursatdesk'] = df_all['hoursatdesk'].map({"1-2":0,"3-5":1,">5":2})

df_all['hoursatdesk'] = df_all['hoursatdesk'].fillna(df_all['hoursatdesk'].median())

print(df_all['hoursatdesk'].value_counts())

#%%

# saves cleaned data frame as the final data frame
df_all.to_csv("../temp_data/df_all_catClean.csv", index=False)
