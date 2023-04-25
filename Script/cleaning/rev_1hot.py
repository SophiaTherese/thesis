#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:41:30 2022

@author: Sophia
"""
import numpy as np
import pandas as pd
import clean_utils as cu

df_all = pd.read_csv("../temp_data/df_all_numClean.csv")



# List of all binary features, that could be combined into nominal features. 
bi_lst = [#Building check
          'O1rur_nurb','O1urb_com', 'O1urb_res', 'O1rur_agr','O1urb_indus','O1suburb_indus',
          'O1suburb_res','O1suburb_com','O1rur_com','O1rur_ind',
            
          'O1_natVentman','O1_natVentAut', 'O1_exhaust','O1_exhaustSupply','O1_exhaustSupplyHeat',
            
          'O1_airHeatEl','O1_airHeatWater', 'O1_radiators', 'O1_floorHeat',
          
          'O1_individualCooling', 'O1_centralCooling','O1_noCooling',
            
          'O1_facadeBrick', 'O1_facadeConcrete','O1_facadeWood','O1_facadeAsbest',
          'O1_intWallBrick','O1_intWallGypsum','O1_intWallWood','O1_intWallConcrete',
          'O1_extWallConcrete','O1_extWallBrick','O1_extWallWood',
          'O1_exteriorInsulation','O1_interiorInsulation','O1_cavityInsulation',
          
          #Manager
          'O2_garbageDumpsters','O2_powerPlants', 'O2_heavyTraffic', 
          'O2_constructionActivities', 'O2_emergencyGenerators', 
          'O2_smokeStack','O2_noOutdoorContSources',
          
          #office1
          'O2_viewGreenNature','O2_viewRoadParking','O2_viewOtherBuildings',
                        
          'O2_paintWallboard','O2_fabric','O2_metal','O2_wallpaper','O2_otherWallCov','O2_woodPanels',
          'O2_suspendedCeiling','O2_ceilingFabric','O2_ceilingMetal','O2_ceilingConcrete','O2_ceilingBoards','O2_ceilingWoodPanels','O2_otherCeiling',
          'O2_floorCarpet','O2_floorWood','O2_floorConcrete','O2_floorPlastic',
          
          'O2_lightLED','O2_lightIncan','O2_lightFlour',
          
          'O2_ventWallGrill','O2_ventLinCeilDif','O2_ventLowFloorGrill','O2_ventLuminaires','O2_ventSideWallDif','O2_ventPerfCeiling','O2_ventFloorReg',
          'O2_ventFloorDif','O2_ventFancoil','O2_ventRoundDif','O2_ventOther','O2_ventNoSupply',
                        
          'O2_ventReturnCeilGrill','O2_ventReturnCeilSlot','O2_ventReturnSlotsLum','O2_ventReturnFloorGrill',
          'O2_ventReturnSideGrill','O2_ventReturnOther','O2_ventNoReturn',
          
          'O2_otherGreenPlants','O2_otherArt','O2_otherWallColor','O2_otherWaterEl','O2_otherLounge','O2_otherOther',
          
          #questionaires
          'photocopier', 'outside', 'printer',
          'perfume','food','tobaccoSmoke','cleaningProd','carpet',
                            
          'noiseTraffic','noiseOverhearing','noiseOfficeEquipment',
          'noisePhoneTalk','noiseNeighborTalk','noisemechanical',
          'noiseTelephones',
                            
          'lightTooDark','lightTooBright','lightTooLittleDaylight','lightTooMuchDaylight',
          'lightFlicker', 'lightReflections','lightColor',
          'lightColor', 'lightNoTask']

for column in bi_lst:
    df_all[column] = df_all[column].map({True:1, False:0, "True":1, "False":0})


#%% Building

#make site into one feature
cu.get_cat('building_site',['O1rur_nurb','O1urb_com', 'O1urb_res', 'O1rur_agr','O1urb_indus','O1suburb_indus','O1suburb_res','O1suburb_com','O1rur_com','O1rur_ind'],df_all)

#make ventilation type into one feature
cu.get_cat('building_ventType',['O1_natVentman','O1_natVentAut','O1_exhaust','O1_exhaustSupply','O1_exhaustSupplyHeat'],df_all)

#make heating system type into one feature
cu.get_cat('building_heatType',['O1_airHeatEl','O1_airHeatWater', 'O1_radiators', 'O1_floorHeat'],df_all)


#make cooling system type into one feature
cu.get_cat('building_coolType',['O1_individualCooling', 'O1_centralCooling','O1_noCooling'],df_all)


#'O1_individualCooling', 'O1_centralCooling','O1_otherCool',O1_noCooling

    
#make facade system  into one feature
cu.get_cat('building_facadeType',['O1_facadeBrick', 'O1_facadeConcrete','O1_facadeWood','O1_facadeAsbest'],df_all)

# #make interior wall type into one feature
cu.get_cat('building_intWallType',['O1_intWallBrick','O1_intWallGypsum','O1_intWallWood','O1_intWallConcrete'],df_all)


#make exterior wall type into one feature
cu.get_cat('building_extWallType',['O1_extWallConcrete','O1_extWallBrick','O1_extWallWood'],df_all)

#make wall insulation type into one feature
cu.get_cat('building_insType',['O1_exteriorInsulation','O1_interiorInsulation','O1_cavityInsulation'],df_all)


#%% Manager


#make Outdoor contaminant sources into one feature
cu.get_cat('manage_outdoorCont',['O2_garbageDumpsters','O2_powerPlants','O2_heavyTraffic','O2_constructionActivities','O2_emergencyGenerators','O2_smokeStack','O2_noOutdoorContSources'],df_all)



# #make Outdoor contaminant sources into one feature
# manager_checklist['manage_outdoorCont']='' # to create an empty column
# for col_name in manager_checklist[['O2_garbageDumpsters','O2_powerPlants','O2_heavyTraffic','O2_constructionActivities','O2_emergencyGenerators','O2_smokeStack','O2_noOutdoorContSources']].columns:
#     manager_checklist.loc[manager_checklist[col_name]==1,'manage_outdoorCont']= manager_checklist['manage_outdoorCont']+' '+col_name

# manager_checklist = manager_checklist.drop(['O2_garbageDumpsters','O2_powerPlants','O2_heavyTraffic','O2_constructionActivities','O2_emergencyGenerators','O2_smokeStack','O2_noOutdoorContSources'],axis=1)


#%% Office 1


#make exterior view into one feature
cu.get_cat('office_exteriorView',['O2_viewGreenNature','O2_viewRoadParking','O2_viewOtherBuildings'],df_all)


#make office wall finish into one feature
cu.get_cat('office_wallFinish',['O2_paintWallboard','O2_fabric','O2_metal','O2_wallpaper','O2_otherWallCov','O2_woodPanels'],df_all)
#make office ceiling finish into one feature
cu.get_cat('office_ceilingFinish',['O2_ceilingFabric','O2_ceilingMetal','O2_ceilingConcrete','O2_ceilingBoards','O2_ceilingWoodPanels','O2_otherCeiling'],df_all)
#make office floor finish into one feature
cu.get_cat('office_floorFinish',['O2_floorCarpet','O2_floorWood','O2_floorConcrete','O2_floorPlastic'],df_all)
 


#make lighting into one feature
cu.get_cat('office_lightType',['O2_lightLED','O2_lightIncan','O2_lightFlour'],df_all)
 


#make office supply air into one feature
cu.get_cat('office_supplyAir',['O2_ventWallGrill','O2_ventLinCeilDif','O2_ventLowFloorGrill','O2_ventLuminaires','O2_ventSideWallDif','O2_ventPerfCeiling','O2_ventFloorReg','O2_ventFloorDif','O2_ventFancoil','O2_ventRoundDif','O2_ventOther','O2_ventNoSupply'],df_all)
 

#make office return air into one feature
cu.get_cat('office_returnAir',['O2_ventReturnCeilGrill','O2_ventReturnCeilSlot','O2_ventReturnSlotsLum','O2_ventReturnFloorGrill','O2_ventReturnSideGrill','O2_ventReturnOther','O2_ventNoReturn'],df_all)
 


#make nice things air into one feature
cu.get_cat('office_niceThings',['O2_otherGreenPlants','O2_otherArt','O2_otherWallColor','O2_otherWaterEl','O2_otherLounge','O2_otherOther'],df_all)


#%%%


#make occupant_odour into one feature
cu.get_cat('occupant_odour',['photocopier', 'outside', 'printer','perfume','food','tobaccoSmoke','cleaningProd','carpet'],df_all)

#make occupant_odour into one feature
cu.get_cat('occupant_noise',['noiseTraffic','noiseOverhearing','noiseOfficeEquipment','noisePhoneTalk','noiseNeighborTalk','noisemechanical','noiseTelephones'],df_all)

#make light into fewer eature
cu.get_cat('occupant_light_level',['lightTooDark','lightTooBright'],df_all)
cu.get_cat('occupant_light_other',['lightFlicker', 'lightReflections','lightColor','lightNoTask'],df_all)

cu.get_cat('occupant_daylight',['lightTooMuchDaylight','lightTooLittleDaylight'],df_all)





#%%

# the data frame is saved
df_all.to_csv("../temp_data/df_all_1hot.csv", index=False)

