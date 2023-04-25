#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 08:42:07 2022

@author: Sophia
"""

import pandas as pd
import numpy as np

# Import data sheets to python with pandas

#%%%
#-------------------------- CHECKLISTS --------------------

""" LOADING BUILDING CHECKLISTS"""

# Load in building  checklists from excel to pandas
building_checklist_101 = pd.read_excel('../DATA/01_Denmark/BuildingID_101/02_Checklists/101_Winter2020_Buildingchecklist.xlsx')
building_checklist_102 = pd.read_excel('../DATA/01_Denmark/BuildingID_102/02_Checklists/102_Winter2020_Buildingchecklist.xlsx')
building_checklist_103 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103_Spring2021_Buildingchecklist.xlsx')

building_checklist_103E = pd.read_excel('../DATA/01_Denmark/BuildingID_103F/02_Checklists/K&L_Albertslund_Checklister.xlsx','Building checklist')
building_checklist_104 = pd.read_excel('../DATA/01_Denmark/BuildingID_104/02_Checklists/104_Checklister.xlsx','Building checklist')
building_checklist_105 = pd.read_excel('../DATA/01_Denmark/BuildingID_105/02_Checklists/105_Checklister.xlsx','Building checklist')


building_checklist_301 = pd.read_excel('../DATA/01_Denmark/BuildingID_301/02_Checklists/301_Spring2021_Buildingchecklist.xlsx')
building_checklist_302 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302_Spring2021_Buildingchecklist.xlsx')
building_checklist_303 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303_Spring2021_Buildingchecklist.xlsx')
building_checklist_304 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304_Spring2021_Buildingchecklist.xlsx')

building_checklist_301E = pd.read_excel('../DATA/01_Denmark/BuildingID_301_E20/02_Checklists/K&LHvidovreChecklister.xlsx','Building Checklist')
building_checklist_305A = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/02_Checklists/305A_Checklister.xlsx','Building checklist')
building_checklist_306 = pd.read_excel('../DATA/01_Denmark/BuildingID_306/02_Checklists/Vingmed_Checklister.xlsx','Building checklist')
building_checklist_307 = pd.read_excel('../DATA/01_Denmark/BuildingID_307/02_Checklists/VentekAirChecklister.xlsx','Building checklist')
building_checklist_308 = pd.read_excel('../DATA/01_Denmark/BuildingID_308/02_Checklists/308_Checklister.xlsx','Building checklist')
building_checklist_309 = pd.read_excel('../DATA/01_Denmark/BuildingID_309/02_Checklists/309_Checklister.xlsx','Building checklist')
building_checklist_310 = pd.read_excel('../DATA/01_Denmark/BuildingID_310/02_Checklists/310_Checklister.xlsx','Building checklist')
building_checklist_311 = pd.read_excel('../DATA/01_Denmark/BuildingID_311/02_Checklists/311_Checklister.xlsx','Building checklist')
building_checklist_312 = pd.read_excel('../DATA/01_Denmark/BuildingID_312/02_Checklists/312_Checklister.xlsx','Building checklist')
building_checklist_313 = pd.read_excel('../DATA/01_Denmark/BuildingID_313/02_Checklists/313_Checklister.xlsx','Building checklist')

building_checklist_401 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401_Spring2021_Buildingchecklist.xlsx')
building_checklist_402 = pd.read_excel('../DATA/02_Greenland/Building_ID_402/02_Checklists/402_Spring2021_Buildingchecklist.xlsx')
building_checklist_403 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/02_Checklists/403_Spring2021_Buildingchecklist.xlsx')
building_checklist_404 = pd.read_excel('../DATA/02_Greenland/Building_ID_404/02_Checklists/404_Spring2021_Buildingchecklist.xlsx')
building_checklist_405 = pd.read_excel('../DATA/02_Greenland/Building_ID_405/02_Checklists/405_Spring2021_Buildingchecklist.xlsx')
building_checklist_406 = pd.read_excel('../DATA/02_Greenland/Building_ID_406/02_Checklists/406_Spring2021_Buildingchecklist.xlsx')
building_checklist_407 = pd.read_excel('../DATA/02_Greenland/Building_ID_407/02_Checklists/407_Spring2021_Buildingchecklist.xlsx')
building_checklist_408 = pd.read_excel('../DATA/02_Greenland/Building_ID_408/02_Checklists/408_Spring2021_Buildingchecklist.xlsx')
building_checklist_409 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/02_Checklists/409_Spring2021_Buildingchecklist.xlsx')
building_checklist_410 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/02_Checklists/410_Spring2021_Buildingchecklist.xlsx')
building_checklist_411 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/02_Checklists/411_Spring2021_Buildingchecklist.xlsx')
building_checklist_412 = pd.read_excel('../DATA/02_Greenland/Building_ID_412/02_Checklists/412_Spring2021_Buildingchecklist.xlsx')
building_checklist_413 = pd.read_excel('../DATA/02_Greenland/Building_ID_413/02_Checklists/413_Spring2021_Buildingchecklist.xlsx')
building_checklist_414 = pd.read_excel('../DATA/02_Greenland/Building_ID_414/02_Checklists/414_Spring2021_Buildingchecklist.xlsx')
building_checklist_415 = pd.read_excel('../DATA/02_Greenland/Building_ID_415/02_Checklists/415_Spring2021_Buildingchecklist.xlsx')
building_checklist_416 = pd.read_excel('../DATA/02_Greenland/Building_ID_416/02_Checklists/416_Spring2021_Buildingchecklist.xlsx')
building_checklist_417 = pd.read_excel('../DATA/02_Greenland/Building_ID_417/02_Checklists/417_Spring2021_Buildingchecklist.xlsx')
building_checklist_418 = pd.read_excel('../DATA/02_Greenland/Building_ID_418/02_Checklists/418_Spring2021_Buildingchecklist.xlsx')
building_checklist_419 = pd.read_excel('../DATA/02_Greenland/Building_ID_419/02_Checklists/419_Spring2021_Buildingchecklist.xlsx')
building_checklist_420 = pd.read_excel('../DATA/02_Greenland/Building_ID_420/02_Checklists/420_Spring2021_Buildingchecklist.xlsx')
building_checklist_421 = pd.read_excel('../DATA/02_Greenland/Building_ID_421/02_Checklists/421_Spring2021_Buildingchecklist.xlsx')
building_checklist_422 = pd.read_excel('../DATA/02_Greenland/Building_ID_422/02_Checklists/422_Spring2021_Buildingchecklist.xlsx')

# Make dataframe of each checklist
building_checklist = [building_checklist_101 , building_checklist_102, building_checklist_103,
          building_checklist_301,building_checklist_302,building_checklist_303,
          building_checklist_304,
          
          building_checklist_103E, building_checklist_104, building_checklist_105,
          
          building_checklist_301E, building_checklist_305A, building_checklist_306,
          building_checklist_307,building_checklist_308,
          building_checklist_309, building_checklist_310, building_checklist_311,
          building_checklist_312,building_checklist_313,
          
          building_checklist_401, building_checklist_402, building_checklist_403,
          building_checklist_404, building_checklist_405, building_checklist_406,
          building_checklist_407, building_checklist_408, 
          building_checklist_409,building_checklist_410,building_checklist_411,
          building_checklist_412,building_checklist_413,building_checklist_414,
          building_checklist_415,building_checklist_416,building_checklist_417,
          building_checklist_418,building_checklist_419,building_checklist_420,
          building_checklist_421,building_checklist_422]


building_checklist = pd.concat(building_checklist, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

#Drop features not used
building_checklist = building_checklist.drop(['ID','OO_officeName','completed','OO_BBR1','OO_BBR2','OO_BBR3','OO_BNR',
                                              'OO_buildingID','OO_inspectors','OO_submitDate','OO_submitTime','OO_address',
                                              
                                              'O1_floorsAboveGrade','O1_floorsBelowGrade','O1_grossFloorArea',
                                              'O1_netFloorArea','O1_submitDate','O1_submitTime','O1a_submitDate',
                                              'O1a_SubmitTime','O1b_SubmitDate','O1b_SubmitTime','O1bb_submitDate',
                                              'O1bb_submitTime','O1e_submitDate','O1e_submitTime','O2_submitDate',
                                              'O2_submitTime'],axis=1)

# Make new data frame that drops patterns of ventilation in the rest of the building
bc_nSpeVent = building_checklist.drop(['O1_filterSchedule','O1_tempControl','O1_CO2control','O1_ventSchedule','O1_otherVent',
                                       'O1_manControl', 'O1_notPossible',
                                       
                                       'O2_kitchenette','O2_kitchenetteFloor1','O2_kitchenetteFloor2','O2_kitchenetteFloor3',
                                       'O2_kitchenetteFloor4','O2_kitchenetteFloor5','O2_kitchenetteVent1','O2_kitchenetteVent2',
                                       'O2_kitchenetteVent3','O2_kitchenetteVent4','O2_kitchenetteVent5',
                                       
                                       'O2_laboratories','O2_labFloor1','O2_labFloor2','O2_labFloor3','O2_labFloor4','O2_labFloor5',
                                       'O2_labVent1','O2_labVent2','O2_labVent3','O2_labVent4','O2_labVent5',
                                       
                                       'O2_workshops','O2_workshopFloor1','O2_workshopFloor2','O2_workshopFloor3','O2_workshopFloor4',
                                       'O2_workshopFloor5','O2_workshopVent1','O2_workshopVent2','O2_workshopVent3','O2_workshopVent4',
                                       'O2_workshopVent5',
                                       
                                       'O2_printshops','O2_printshopFloor1','O2_printshopFloor2','O2_printshopFloor3','O2_printshopFloor4',
                                       'O2_printshopFloor5','O2_printshopVent1','O2_printshopVent2','O2_printshopVent3','O2_printshopVent4',
                                       'O2_printshopVent5',
                                       
                                       'O2_kitchens','O2_kitchenFloor1','O2_kitchenFloor2','O2_kitchenFloor3','O2_kitchenFloor4','O2_kitchenFloor5',
                                       'O2_kitchenVent1','O2_kitchenVent2','O2_kitchenVent3','O2_kitchenVent4','O2_kitchenVent5',
                                       
                                       'O2_garages','O2_garageFloor1','O2_garageFloor2','O2_garageFloor3','O2_garageFloor4','O2_garageFloor5',
                                       'O2_garageVent1','O2_garageVent2','O2_garageVent3','O2_garageVent4','O2_garageVent5',
                                       
                                       'O2_cleaning','O2_cleaningFloor1','O2_cleaningFloor2','O2_cleaningFloor3','O2_cleaningFloor4',
                                       'O2_cleaningFloor5','O2_cleaningVent1','O2_cleaningVent2','O2_cleaningVent3','O2_cleaningVent4','O2_cleaningVent5',
                                       
                                       'O2_restroom','O2_restroomFloor1','O2_restroomFloor2','O2_restroomFloor3','O2_restroomFloor4','O2_restroomFloor5',
                                       'O2_restroomVent1','O2_restroomVent2','O2_restroomVent3','O2_restroomVent4','O2_restroomVent5',
                                       
                                       'O1_floorDes1','O1_floorDes2','O1_floorDes3','O1_floorDes4','O1_floorDes5','O1_floorDes6','O1_floorDes7','O1_floorDes8',
                                       'O1_primAct1','O1_primAct2','O1_primAct3','O1_primAct4','O1_primAct5','O1_primAct6','O1_primAct7','O1_primAct8',
                                       'O1_secAct1','O1_secAct2','O1_secAct3','O1_secAct4','O1_secAct5','O1_secAct6','O1_secAct7','O1_secAct8',
                                       'O1_comments1','O1_comments2','O1_comments3','O1_comments4','O1_comments5','O1_comments6','O1_comments7','O1_comments8',
                                       
                                       #deleting other comments
                                       'O1_otherHeat','O1_otherCool','O1_envelopeOther','O1_intWallOther','O1_extWallOther' ],axis=1)


# make comment/nan into true/false
# bi_lst = ['O1_otherCool']
# for column in bi_lst:
#     bc_nSpeVent[column][bc_nSpeVent[column].isna() == False] = True
#     bc_nSpeVent[column] = bc_nSpeVent[column].fillna(False)



building_checklist = building_checklist.set_index('buildingID')
bc_nSpeVent = bc_nSpeVent.set_index('buildingID')
#%%%#%%%

""" LOADING MANAGER CHECKLISTS"""

# Load in building  checklists from excel to pandas
mc_101 = pd.read_excel('../DATA/01_Denmark/BuildingID_101/02_Checklists/101_Winter2020_Managerchecklist.xlsx')
mc_102 = pd.read_excel('../DATA/01_Denmark/BuildingID_102/02_Checklists/102_Winter2020_Managerchecklist.xlsx')
mc_103 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103_Spring2021_Managerchecklist.xlsx')

mc_103E = pd.read_excel('../DATA/01_Denmark/BuildingID_103F/02_Checklists/K&L_Albertslund_Checklister.xlsx','Manager checklist')
mc_104 = pd.read_excel('../DATA/01_Denmark/BuildingID_104/02_Checklists/104_Checklister.xlsx','Manager checklist')
mc_105 = pd.read_excel('../DATA/01_Denmark/BuildingID_105/02_Checklists/105_Checklister.xlsx','Manager checklist')


mc_301 = pd.read_excel('../DATA/01_Denmark/BuildingID_301/02_Checklists/301_Spring2021_Managerchecklist.xlsx')
mc_302 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302_Spring2021_Managerchecklist.xlsx')
mc_303 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303_Spring2021_Managerchecklist.xlsx')
mc_304 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304_Spring2021_Mangerchecklist.xlsx')

mc_301E = pd.read_excel('../DATA/01_Denmark/BuildingID_301_E20/02_Checklists/K&LHvidovreChecklister.xlsx','Manager Checklist')
mc_305A = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/02_Checklists/305A_Checklister.xlsx','Manager checklist')
mc_306 = pd.read_excel('../DATA/01_Denmark/BuildingID_306/02_Checklists/Vingmed_Checklister.xlsx','Manager checklist')
mc_307 = pd.read_excel('../DATA/01_Denmark/BuildingID_307/02_Checklists/VentekAirChecklister.xlsx','Manager checklist')
mc_308 = pd.read_excel('../DATA/01_Denmark/BuildingID_308/02_Checklists/308_Checklister.xlsx','Manager checklist')
mc_309 = pd.read_excel('../DATA/01_Denmark/BuildingID_309/02_Checklists/309_Checklister.xlsx','Manager checklist')
mc_310 = pd.read_excel('../DATA/01_Denmark/BuildingID_310/02_Checklists/310_Checklister.xlsx','Manager checklist')
mc_311 = pd.read_excel('../DATA/01_Denmark/BuildingID_311/02_Checklists/311_Checklister.xlsx','Manager checklist')
mc_312 = pd.read_excel('../DATA/01_Denmark/BuildingID_312/02_Checklists/312_Checklister.xlsx','Manager checklist')
mc_313 = pd.read_excel('../DATA/01_Denmark/BuildingID_313/02_Checklists/313_Checklister.xlsx','Manager checklist')



mc_401 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401_Spring2021_Managerchecklist.xlsx')
mc_402 = pd.read_excel('../DATA/02_Greenland/Building_ID_402/02_Checklists/402_Spring2021_Managerchecklist.xlsx')
mc_403 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/02_Checklists/403_Spring2021_Managerchecklist.xlsx')
mc_404 = pd.read_excel('../DATA/02_Greenland/Building_ID_404/02_Checklists/404_Spring2021_Managerchecklist.xlsx')
mc_405 = pd.read_excel('../DATA/02_Greenland/Building_ID_405/02_Checklists/405_Spring2021_Managerchecklist.xlsx')
mc_406 = pd.read_excel('../DATA/02_Greenland/Building_ID_406/02_Checklists/406_Spring2021_Managerchecklist.xlsx')
mc_407 = pd.read_excel('../DATA/02_Greenland/Building_ID_407/02_Checklists/407_Spring2021_Managerchecklist.xlsx')
mc_408 = pd.read_excel('../DATA/02_Greenland/Building_ID_408/02_Checklists/408_Spring2021_Managerchecklist.xlsx')
mc_409 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/02_Checklists/409_Spring2021_Managerchecklist.xlsx')
mc_410 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/02_Checklists/410_Spring2021_Managerchecklist.xlsx')
mc_411 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/02_Checklists/411_Spring2021_Managerchecklist.xlsx')
mc_412 = pd.read_excel('../DATA/02_Greenland/Building_ID_412/02_Checklists/412_Spring2021_Managerchecklist.xlsx')
mc_413 = pd.read_excel('../DATA/02_Greenland/Building_ID_413/02_Checklists/413_Spring2021_Managerchecklist.xlsx')
mc_414 = pd.read_excel('../DATA/02_Greenland/Building_ID_414/02_Checklists/414_Spring2021_Managerchecklist.xlsx')
mc_415 = pd.read_excel('../DATA/02_Greenland/Building_ID_415/02_Checklists/415_Spring2021_Managerchecklist.xlsx')
mc_416 = pd.read_excel('../DATA/02_Greenland/Building_ID_416/02_Checklists/416_Spring2021_Managerchecklist.xlsx')
mc_417 = pd.read_excel('../DATA/02_Greenland/Building_ID_417/02_Checklists/417_Spring2021_Managerchecklist.xlsx')
mc_418 = pd.read_excel('../DATA/02_Greenland/Building_ID_418/02_Checklists/418_Spring2021_Managerchecklist.xlsx')
mc_419 = pd.read_excel('../DATA/02_Greenland/Building_ID_419/02_Checklists/419_Spring2021_Managerchecklist.xlsx')
mc_420 = pd.read_excel('../DATA/02_Greenland/Building_ID_420/02_Checklists/420_Spring2021_Managerchecklist.xlsx')
mc_421 = pd.read_excel('../DATA/02_Greenland/Building_ID_421/02_Checklists/421_Spring2021_Managerchecklist.xlsx')
mc_422 = pd.read_excel('../DATA/02_Greenland/Building_ID_422/02_Checklists/422_Spring2021_Managerchecklist.xlsx')

# Make dataframe of each checklist
manager_checklist = [mc_101 , mc_102, mc_103,mc_301,mc_302,mc_303,mc_304,
                     
                     mc_103E,mc_104, mc_105, mc_301E, mc_305A, mc_306, mc_307,
                     mc_308,mc_309, mc_310, mc_311, mc_312, mc_313,
                     
                     
                     mc_401,mc_402,mc_403,mc_404,mc_405,mc_406,mc_407,mc_408,mc_409,mc_410,
                     mc_411,mc_412,mc_413,mc_414,mc_415,mc_416,mc_417,mc_418,mc_419,
                     mc_420, mc_421, mc_422]

# Make dataframe
manager_checklist = pd.concat(manager_checklist, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

#%%%
#Drop unnecessary features
manager_checklist = manager_checklist.drop(['ID','OO_officeName', 'OO_address','completed','OO_BBR1','OO_BBR2','OO_BBR3','OO_Bnr','OO_inspectors',
                                            
                                            'OO_submitDate','O1_submitDate','O1a_submitDate','O2_submitDate','O3a_submitDate',
                                            'O3b_submitDate','O3c_submitDate','O3d_submitDate',
                                            
                                            'OO_submitTime','O1_submitTime','O1a_submitTime','O2_submitTime','O3a_submitTime',
                                            'O3b_submitTime','O3c_submitTime','O3d_submitTime',
                                            
                                            'O1_noEmployees', 'O1_covidNoEmployees', 'O1_generalWeekendsOccupied','O1_normalNoEmployees',
                                            
                                            'O1_floorsBelowGrade','O1_floorsAboveGrade','O1_grossFloorArea','O1_netFloorArea',
                                            
                                            'O1_ownership','O1_otherPublicOwner','O1_whichPublicOwner',
                                            'O1_otherPrivateOwner','O1_whichPrivateOwner',
                                            'O1_daysPerWeekOccupied','O1_generalWeekdaysOccupied',
                                            
                                            'O2_curWaterDamageBasement', 'O2_curWaterDamageRoof', 'O2_curWaterDamageMechSpace',
                                            'O2_curWaterDamageOccupiedFloor', 'O2_curWaterDamage',
                                            
                                            'O2_waterDamage', 'O2_waterDamageBasement', 'O2_waterDamageRoof', 'O2_waterDamageBasement',
                                            'O2_waterDamageRoof', 'O2_waterDamageBasement', 'O2_waterDamageMechSpace','O2_waterDamageOccupiedFloor',
                                            
                                            'O2_fireDamage', 'O2_fireDamageWhen', 'O2_fireDamageExtent',
                                            
                                            'O3_cleanStoreText', 'O3_genClean','O3_genCleanText','O3_cleanStore','O3_floorBroom'
                                            
                                            
                                            ],axis=1)




#%%% 

    
# make 'on' true and nan false in binary features:
m_bi_lst = ['O2_garbageDumpsters','O2_powerPlants', 'O2_heavyTraffic', 
            'O2_constructionActivities', 'O2_emergencyGenerators', 'O2_smokeStack','O2_noOutdoorContSources']
  
for column in m_bi_lst:
    manager_checklist[column] = manager_checklist[column].map({'on': True, np.nan:False})


#%%%

manager_checklist = manager_checklist.set_index('buildingID')

"""MERGING MANAGER AND BUILDIGN CHECKLISTS"""
mb_checklists = building_checklist.combine_first(manager_checklist)
mb_non_sVent_checklists = bc_nSpeVent.combine_first(manager_checklist)

#pd.concat([building_checklist, manager_checklist], axis=1)

#%%%

""" LOADING OFFICE CHECKLISTS"""
#%%% --------- LOAD OFFICE CHECKLIST 1s 

#101
oc_101b1 = pd.read_excel('../DATA/01_Denmark/BuildingID_101/02_Checklists/101b_Winter2020_Officechecklist1.xlsx')
oc_101c1 = pd.read_excel('../DATA/01_Denmark/BuildingID_101/02_Checklists/101c_Winter2020_Officechecklist1.xlsx')
oc_101d1 = pd.read_excel('../DATA/01_Denmark/BuildingID_101/02_Checklists/101d_Winter2020_Officechecklist1.xlsx')
#102
oc_102a1 = pd.read_excel('../DATA/01_Denmark/BuildingID_102/02_Checklists/102a_Winter2020_Officechecklist1.xlsx')
oc_102b1 = pd.read_excel('../DATA/01_Denmark/BuildingID_102/02_Checklists/102b_Winter2020_Officechecklist1.xlsx')
#103
oc_103a1 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103a_Spring2021_Officechecklist_1.xlsx')
oc_103b1 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103b_Spring2021_Officechecklist_1.xlsx')
oc_103c1 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103c_Spring2021_Officechecklist_1.xlsx')
oc_103d1 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103(d)_Spring2021_Officechecklist_1.xlsx')

#103E- oc105
oc_103E = pd.read_excel('../DATA/01_Denmark/BuildingID_103F/02_Checklists/K&L_Albertslund_Checklister.xlsx','Office checklists')
oc_104 = pd.read_excel('../DATA/01_Denmark/BuildingID_104/02_Checklists/104_Checklister.xlsx','Office checklist 1')
oc_105 = pd.read_excel('../DATA/01_Denmark/BuildingID_105/02_Checklists/105_Checklister.xlsx','Office checklist 1')



#301
oc_301a1 = pd.read_excel('../DATA/01_Denmark/BuildingID_301/02_Checklists/301a_Spring2021_Officechecklist1.xlsx')
oc_301b1 = pd.read_excel('../DATA/01_Denmark/BuildingID_301/02_Checklists/301b_Spring2021_Officechecklist1.xlsx')
oc_301c1 = pd.read_excel('../DATA/01_Denmark/BuildingID_301/02_Checklists/301c_Spring2021_Officechecklist1.xlsx')
#302
oc_302a1 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302a_Spring2021_Officechecklist1.xlsx')
oc_302b1 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302b_Spring2021_Officechecklist1.xlsx')
oc_302c1 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302c_Spring2021_Officechecklist1.xlsx')
oc_302d1 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302d_Spring2021_Officechecklist1.xlsx')
oc_302e1 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302(e)_Spring2021_Officechecklist1.xlsx')
#303
oc_303a1 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303a_Spring2021_Officechecklist1.xlsx')
oc_303b1 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303b_Spring2021_Officechecklist1.xlsx')
oc_303c1 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303c_Spring2021_Officechecklist1.xlsx')
oc_303d1 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303(d)_Spring2021_Officechecklist1.xlsx')
#304
oc_304a1 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304(a)_Spring2021_Officechecklist1.xlsx')
oc_304b1 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304b_Spring2021_Officechecklist1.xlsx')
oc_304c1 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304c_Spring2021_Officechecklist1.xlsx')
oc_304d1 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304d_Spring2021_Officechecklist1.xlsx')
oc_304e1 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304e_Spring2021_Officechecklist1.xlsx')
oc_304f1 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304f_Spring2021_Officechecklist1.xlsx')
oc_304g1 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304g_Spring2021_Officechecklist1.xlsx')


oc_301E = pd.read_excel('../DATA/01_Denmark/BuildingID_301_E20/02_Checklists/K&LHvidovreChecklister.xlsx','Office checklist 1')
oc_305A = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/02_Checklists/305A_Checklister.xlsx','Office checklist 1')
oc_306 = pd.read_excel('../DATA/01_Denmark/BuildingID_306/02_Checklists/Vingmed_Checklister.xlsx','Office checklist 1')
oc_307 = pd.read_excel('../DATA/01_Denmark/BuildingID_307/02_Checklists/VentekAirChecklister.xlsx','Office checklist 1')
oc_308 = pd.read_excel('../DATA/01_Denmark/BuildingID_308/02_Checklists/308_Checklister.xlsx','Office checklist 1')
oc_309 = pd.read_excel('../DATA/01_Denmark/BuildingID_309/02_Checklists/309_Checklister.xlsx','Office checklist 1')
oc_310 = pd.read_excel('../DATA/01_Denmark/BuildingID_310/02_Checklists/310_Checklister.xlsx','Office checklist 1')
oc_311 = pd.read_excel('../DATA/01_Denmark/BuildingID_311/02_Checklists/311_Checklister.xlsx','Office checklist 1')
oc_312 = pd.read_excel('../DATA/01_Denmark/BuildingID_312/02_Checklists/312_Checklister.xlsx','Office checklist 1')
oc_313 = pd.read_excel('../DATA/01_Denmark/BuildingID_313/02_Checklists/313_Checklister.xlsx','Office checklist 1')






#401 Greenland
oc_401b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401a_Spring2021_Officechecklist1.xlsx')
oc_401c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401b_Spring2021_Officechecklist1.xlsx')
oc_401d1 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401c_Spring2021_Officechecklist1.xlsx')
oc_401e1 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401d_Spring2021_Officechecklist1.xlsx')

#402
oc_402a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_402/02_Checklists/402a_Spring2021_Officechecklist1.xlsx')
oc_402b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_402/02_Checklists/402b_Spring2021_Officechecklist1.xlsx')
oc_402c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_402/02_Checklists/402c_Spring2021_Officechecklist1.xlsx')
oc_402d1 = pd.read_excel('../DATA/02_Greenland/Building_ID_402/02_Checklists/402d_Spring2021_Officechecklist1.xlsx')
oc_402e1 = pd.read_excel('../DATA/02_Greenland/Building_ID_402/02_Checklists/402e_Spring2021_Officechecklist1.xlsx')

#403
oc_403a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/02_Checklists/403a_Spring2021_Officechecklist1.xlsx')
oc_403b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/02_Checklists/403b_Spring2021_Officechecklist1.xlsx')
oc_403c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/02_Checklists/403c_Spring2021_Officechecklist1.xlsx')
oc_403d1 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/02_Checklists/403d_Spring2021_Officechecklist1.xlsx')

#404
oc_404a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_404/02_Checklists/404a_Spring2021_Officechecklist1.xlsx')
oc_404b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_404/02_Checklists/404b_Spring2021_Officechecklist1.xlsx')

#405
oc_405a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_405/02_Checklists/405a_Spring2021_Officechecklist1.xlsx')
oc_405b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_405/02_Checklists/405b_Spring2021_Officechecklist1.xlsx')
oc_405c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_405/02_Checklists/405c_Spring2021_Officechecklist1.xlsx')
oc_405d1 = pd.read_excel('../DATA/02_Greenland/Building_ID_405/02_Checklists/405d_Spring2021_Officechecklist1.xlsx')

#406
oc_406a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_406/02_Checklists/406a_Spring2021_officechecklist1.xlsx')
oc_406b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_406/02_Checklists/406b_Spring2021_officechecklist1.xlsx')
oc_406c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_406/02_Checklists/406c_Spring2021_officechecklist1.xlsx')

#407
oc_407a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_407/02_Checklists/407a_Spring2021_Officechecklist1.xlsx')
oc_407b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_407/02_Checklists/407b_Spring2021_Officechecklist1.xlsx')
oc_407c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_407/02_Checklists/407c_Spring2021_Officechecklist1.xlsx')

#408
oc_408a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_408/02_Checklists/408a_Spring2021_Officechecklist1.xlsx')
oc_408b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_408/02_Checklists/408b_Spring2021_Officechecklist1.xlsx')
oc_408c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_408/02_Checklists/408c_Spring2021_Officechecklist1.xlsx')

#409
oc_409a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/02_Checklists/409a_Spring2021_Officechecklist1.xlsx')
oc_409b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/02_Checklists/409b_Spring2021_Officechecklist1.xlsx')
oc_409c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/02_Checklists/409c_Spring2021_Officechecklist1.xlsx')

#410
oc_410a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/02_Checklists/410a_Spring2021_Officechecklist1.xlsx')
oc_410b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/02_Checklists/410b_Spring2021_Officechecklist1.xlsx')
oc_410c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/02_Checklists/410c_Spring2021_Officechecklist1.xlsx')

#411
oc_411a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/02_Checklists/411a_Spring2021_Officechecklist1.xlsx')
oc_411b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/02_Checklists/411b_Spring2021_Officechecklist1.xlsx')
oc_411c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/02_Checklists/411c_Spring2021_Officechecklist1.xlsx')

#412
oc_412a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_412/02_Checklists/412a_Spring2021_Officechecklist1.xlsx')
oc_412b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_412/02_Checklists/412b_Spring2021_Officechecklist1.xlsx')
oc_412c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_412/02_Checklists/412c_Spring2021_Officechecklist1.xlsx')

#413
oc_413a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_413/02_Checklists/413a_Spring2021_Officechecklist1.xlsx')
oc_413b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_413/02_Checklists/413b_Spring2021_Officechecklist1.xlsx')
oc_413c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_413/02_Checklists/413c_Spring2021_Officechecklist1.xlsx')

#414
oc_414a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_414/02_Checklists/414a_Spring2021_Officechecklist1.xlsx')
oc_414b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_414/02_Checklists/414b_Spring2021_Officechecklist1.xlsx')
oc_414c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_414/02_Checklists/414c_Spring2021_Officechecklist1.xlsx')

#415
oc_415a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_415/02_Checklists/415a_Spring2021_Officechecklist1.xlsx')
oc_415b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_415/02_Checklists/415b_Spring2021_Officechecklist1.xlsx')
oc_415c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_415/02_Checklists/415c_Spring2021_Officechecklist1.xlsx')

#416
oc_416a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_416/02_Checklists/416a_Spring2021_Officechecklist1.xlsx')
oc_416b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_416/02_Checklists/416b_Spring2021_Officechecklist1.xlsx')
oc_416c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_416/02_Checklists/416c_Spring2021_Officechecklist1.xlsx')

#417
oc_417a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_417/02_Checklists/417a_Spring2021_Officechecklist1.xlsx')
oc_417b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_417/02_Checklists/417b_Spring2021_Officechecklist1.xlsx')
oc_417c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_417/02_Checklists/417c_Spring2021_Officechecklist1.xlsx')

#418
oc_418a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_418/02_Checklists/418a_Spring2021_Officechecklist1.xlsx')
oc_418b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_418/02_Checklists/418b_Spring2021_Officechecklist1.xlsx')
oc_418c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_418/02_Checklists/418c_Spring2021_Officechecklist1.xlsx')

#419
oc_419a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_419/02_Checklists/419a_Spring2021_Officechecklist1.xlsx')
oc_419b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_419/02_Checklists/419b_Spring2021_Officechecklist1.xlsx')
oc_419c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_419/02_Checklists/419c_Spring2021_Officechecklist1.xlsx')

#420
oc_420a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_420/02_Checklists/420a_Spring2021_Officechecklist1.xlsx')
oc_420b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_420/02_Checklists/420b_Spring2021_Officechecklist1.xlsx')
oc_420c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_420/02_Checklists/420c_Spring2021_Officechecklist1.xlsx')

#421
oc_421a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_421/02_Checklists/421a_Spring2021_Officechecklist1.xlsx')
oc_421b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_421/02_Checklists/421b_Spring2021_Officechecklist1.xlsx')
oc_421c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_421/02_Checklists/421c_Spring2021_Officechecklist1.xlsx')

#422
oc_422a1 = pd.read_excel('../DATA/02_Greenland/Building_ID_422/02_Checklists/422a_Spring2021_Officechecklist1.xlsx')
oc_422b1 = pd.read_excel('../DATA/02_Greenland/Building_ID_422/02_Checklists/422b_Spring2021_Officechecklist1.xlsx')
oc_422c1 = pd.read_excel('../DATA/02_Greenland/Building_ID_422/02_Checklists/422c_Spring2021_Officechecklist1.xlsx')



#%%


# Make dataframe of each checklist 1
oc1 = [oc_101b1, oc_101c1, oc_101d1, 
       oc_102a1, oc_102b1, 
       oc_103a1, oc_103b1, oc_103c1, oc_103d1,
       oc_301a1, oc_301b1, oc_301c1,
       oc_302a1, oc_302b1, oc_302c1, oc_302d1, oc_302e1,
       oc_303a1, oc_303b1, oc_303c1, oc_303d1,
       oc_304a1, oc_304b1, oc_304c1, oc_304d1, oc_304e1, oc_304f1, oc_304g1,
       
       oc_103E,oc_104, oc_105,
       
       oc_301E,
       oc_305A, oc_306,oc_307,oc_308,
       oc_309, oc_310, oc_311, oc_312, oc_313,
       
       oc_401b1,oc_401c1,oc_401d1,oc_401e1,
       oc_402a1,oc_402b1,oc_402c1,oc_402d1,oc_402e1,
       oc_403a1,oc_403b1,oc_403c1,oc_403d1,
       oc_404a1,oc_404b1,
       oc_405a1,oc_405b1,oc_405c1,oc_405d1,
       oc_406a1,oc_406b1,oc_406c1,
       oc_407a1,oc_407b1,oc_407c1,
       oc_408a1,oc_408b1,oc_408c1,
       oc_409a1,oc_409b1,oc_409c1,
       oc_410a1,oc_410b1,oc_410c1,
       oc_411a1,oc_411b1,oc_411c1,
       oc_412a1,oc_412b1,oc_412c1,
       oc_413a1,oc_413b1,oc_413c1,
       oc_414a1,oc_414b1,oc_414c1,
       oc_415a1,oc_415b1,oc_415c1,
       oc_416a1,oc_416b1,oc_416c1,
       oc_417a1,oc_417b1,oc_417c1,
       oc_418a1,oc_418b1,oc_418c1,
       oc_419a1,oc_419b1,oc_419c1,
       oc_420a1,oc_420b1,oc_420c1,
       oc_421a1,oc_421b1,oc_421c1,
       oc_422a1,oc_422b1,oc_422c1,]



# Make matrix
oc1 = pd.concat(oc1, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

oc1 = oc1.drop(['ID','officeID','completed', 'OO_officeName',
                'OO_BBR1','OO_BBR2','OO_BBR3','OO_BNR','OO_inspectors',
                'OO_address','OO_buildingTypology','OO_buildingID',
                'O1_roomNumber','O1_officeFloor','O1_relInfo',
                
                'OO_submitDate', 'O1a_submitDate', 'O1b_submitDate', 
                'O2a_submitDate', 'O2b_submitDate', 'O2c_submitDate', 
                'O2d_submitDate', 'O2e_submitDate', 'O2f_submitDate',
                'O2g_submitDate', 'O2h_submitDate', 'O2i_submitDate',
                
                'OO_submitTime', 'O1a_submitTime', 'O1b_submitTime', 
                'O2a_submitTime', 'O2b_submitTime', 'O2c_submitTime', 
                'O2d_submitTime', 'O2e_submitTime', 'O2f_submitTime', 
                'O2g_submitTime', 'O2h_submitTime', 'O2i_submitTime',
                
                'O1_equip1','O1_equip2','O1_equip3','O1_equip4',
                'O1_M1Info','O1_M2Info','O1_M3Info','O1_M4Info',
                
                'O1_otherWhat1','O1_otherWhat2','O1_otherWhat3',
                'O1_otherWhat4','O1_otherWhat5','O1_otherWhat6',
                'O1_otherWhat7','O1_otherWhat8','O1_otherWhat9','O1_otherWhat10',
                
                'O1_What1ID','O1_What2ID','O1_What3ID','O1_What4ID',
                'O1_What5ID','O1_What6ID','O1_What7ID','O1_What8ID',
                'O1_What9ID','O1_What10ID',
                
                'O1_What1relInfo','O1_What2relInfo','O1_What3relInfo','O1_What4relInfo',
                'O1_What5relInfo','O1_What6relInfo','O1_What7relInfo',
                'O1_What8relInfo','O1_What9relInfo','O1_What10relInfo',
                
                'O2_plenumHeight', 'O2_otherOfficeType',
                'O2_condensationWidth','O2_condensationHeight',
                
                'O2_paintWallboardComment','O2_fabricComment',
                'O2_metalComment','O2_wallpaperComment','O2_wallEvalComment','O2_woodpanelsComment',
                'O2_ceilingFabricComment',
                'O2_ceilingMetalComment','O2_ceilingConcreteComment','O2_ceilingBoardsComment',
                'O2_ceilingWoodPanelsComment','O2_ceilingEvalComment',
                
                'O2_floorCarpetComment','O2_floorWoodComment','O2_floorPlasticComment','O2_floorConcreteComment',
                'O2_otherFloorComment',
                
                'O2_ventWallGrillComment','O2_ventLinCeilDifComment','O2_ventLowFloorGrillComment',
                'O2_ventLuminairesComment','O2_ventSideWallDifComment','O2_ventPerfCeilingComment',
                'O2_ventFloorRegComment','O2_ventFloorDifComment','O2_ventFancoilComment','O2_ventRoundDifComment',
                
                'O2_ventReturnCeilGrillComment','O2_ventReturnCeilSlotComment','O2_ventReturnSlotsLumComment',
                'O2_ventReturnFloorGrillComment','O2_ventReturnSideGrillComment',
                
                'O2_otherGreenPlantsComment','O2_otherArtComment','O2_otherWallColorComment','O2_otherWaterElComment',
                'O2_otherLoungeComment',
                
                'O2_noHumidifiers','O2_noDehumidifiers','O2_noDeskFans','O2_noNice','O2_otherOtherComment',
                
                
                #delete other comments that are not relevant for now
                'O2_viewOther','O2_otherLight','O2_ventOtherComment','O2_ventReturnOtherComment',
                'O2_otherConditioningComment'
                ],axis=1)


oc1.rename(columns={'buildingID': 'officeID'}, inplace=True)


oc1['buildingID'] = oc1['officeID'].map({'101b':101,'101c':101,'101d':101,
                                         '102a':102,'102b':102,
                                         '103a':103,'103b':103,'103c':103,'103d':103,
                                         '301a':301,'301b':301,'301c':301,
                                         '302a':302,'302b':302,'302c':302,'302d':302,'302e':302,
                                         '303a':303,'303b':303,'303c':303,'303d':303,
                                         '304a':304,'304b':304,'304c':304,'304d':304,'304e':304,'304f':304,'304g':304,
                                         
                                         '103_E2021a':'103_E2021','103_E2021b':'103_E2021','103_E2021c':'103_E2021',
                                         '104a':104,'104b':104,
                                         '105a':105,
                                         
                                         '301_E2021a':'301_E2021','301_E2021b':'301_E2021','301_E2021c':'301_E2021','301_E2021d':'301_E2021',
                                         '305b':'305A','305c':'305A','305d':'305A','305e':'305A','305f':'305A','305g':'305A','305h':'305A','305i':'305A',
                                         '3060A':306,'3060B':306,'3061A':306,
                                         '307a':307,
                                         '308Aa':'308A','308Ab':'308A',
                                         '308Ba':'308B','308Bb':'308B',
                                         
                                         '309a':309,'309b':309,'309c':309,
                                         '310a':310,'310b':310,
                                         '311a':311,'311b':311,
                                         '312a':312,'312b':312,'312c':312,
                                         '313a':313,'313b':313,'313c':313,'313d':313,'313e':313,'313f':313,
                                         
                                         '401b':401,'401c':401,'401d':401,'401e':401,
                                         '402a':402,'402b':402,'402c':402,'402d':402,'402e':402,
                                         '403a':403,'403b':403,'403c':403,'403d':403,'403e':403,
                                         '404a':404,'404b':404,
                                         '405a':405,'405b':405,'405c':405,'405d':405,
                                         '406a':406,'406b':406,'406c':406,
                                         '407a':407,'407b':407,'407c':407,
                                         '408a':408,'408b':408,'408c':408,
                                         '409a':409,'409b':409,'409c':409,
                                         '410a':410,'410b':410,'410c':410,
                                         '411a':411,'411b':411,'411c':411,
                                         '412a':412,'412b':412,'412c':412,
                                         '413a':413,'413b':413,'413c':413,
                                         '414a':414,'414b':414,'414c':414,
                                         '415a':415,'415b':415,'415c':415,
                                         '416a':416,'416b':416,'416c':416,
                                         '417a':417,'417b':417,'417c':417,
                                         '418a':418,'418b':418,'418c':418,
                                         '419a':419,'419b':419,'419c':419,
                                         '420a':420,'420b':420,'420c':420,
                                         '421a':420,'421b':421,'421c':421,
                                         '422a':420,'422b':422,'422c':422,
                                         })


oc1_bi_lst = ['O2_viewGreenNature','O2_viewRoadParking','O2_viewOtherBuildings',
             'O2_paintWallboard','O2_fabric','O2_wallpaper','O2_otherWallCov',
             'O2_woodPanels','O2_suspendedCeiling','O2_metal','O2_ceilingFabric',
             'O2_ceilingMetal','O2_ceilingConcrete','O2_ceilingBoards','O2_otherCeiling',
             'O2_ceilingWoodPanels',
             
             'O2_floorCarpet','O2_floorPlastic','O2_floorWood','O2_floorConcrete',
             
             'O2_lightLED','O2_lightIncan','O2_lightFlour',
             
             
             'O2_ventWallGrill','O2_ventLinCeilDif','O2_ventLowFloorGrill',
             'O2_ventLuminaires','O2_ventSideWallDif','O2_ventPerfCeiling',
             'O2_ventFloorReg','O2_ventFloorDif','O2_ventFancoil',
             'O2_ventRoundDif','O2_ventOther','O2_ventNoSupply',
             
             'O2_ventReturnCeilGrill','O2_ventReturnCeilSlot','O2_ventReturnSlotsLum','O2_ventReturnFloorGrill',
             'O2_ventReturnSideGrill','O2_ventReturnOther','O2_ventNoReturn',
             
             'O2_otherGreenPlants','O2_otherArt','O2_otherWallColor','O2_otherWaterEl','O2_otherLounge',
             'O2_otherOther']
  
for column in oc1_bi_lst:
    oc1[column] = oc1[column].map({-1: "True", np.nan:"False",
                                   False:"False",True:"True",
                                   'noSupply':"True",'noReturn':"True",
                                   "TRUE":"True", "FALSE":"False"})



oc1 = oc1.set_index('officeID',drop=False)





#%% --------- LOAD OFFICE CHECKLIST 2s 
#103
oc_101b2 = pd.read_excel('../DATA/01_Denmark/BuildingID_101/02_Checklists/101b_Winter2020_Officechecklist2.xlsx')
oc_101c2 = pd.read_excel('../DATA/01_Denmark/BuildingID_101/02_Checklists/101c_Winter2020_Officechecklist2.xlsx')
oc_101d2 = pd.read_excel('../DATA/01_Denmark/BuildingID_101/02_Checklists/101d_Winter2020_Officechecklist2.xlsx')
#102
oc_102a2 = pd.read_excel('../DATA/01_Denmark/BuildingID_102/02_Checklists/102a_Winter2020_Officechecklist2.xlsx')
oc_102b2 = pd.read_excel('../DATA/01_Denmark/BuildingID_102/02_Checklists/102b_Winter2020_Officechecklist2.xlsx')
#103
oc_103a2 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103a_Spring2021_Officechecklist_2.xlsx')
oc_103b2 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103b_Spring2021_Officechecklist_2.xlsx')
oc_103c2 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103c_Spring2021_Officechecklist_2.xlsx')
oc_103d2 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/02_Checklists/103(d)_Spring2021_Officechecklist_2.xlsx')
#301
oc_301a2 = pd.read_excel('../DATA/01_Denmark/BuildingID_301/02_Checklists/301a_Spring2021_Officechecklist2.xlsx')
oc_301b2 = pd.read_excel('../DATA/01_Denmark/BuildingID_301/02_Checklists/301b_Spring2021_Officechecklist2.xlsx')
oc_301c2 = pd.read_excel('../DATA/01_Denmark/BuildingID_301/02_Checklists/301c_Spring2021_Officechecklist2.xlsx')
#302
oc_302a2 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302a_Spring2021_Officechecklist2.xlsx')
oc_302b2 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302b_Spring2021_Officechecklist2.xlsx')
oc_302c2 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302c_Spring2021_Officechecklist2.xlsx')
oc_302d2 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302d_Spring2021_Officechecklist2.xlsx')
oc_302e2 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/02_Checklists/302(e)_Spring2021_Officechecklist2.xlsx')
#303
oc_303a2 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303a_Spring2021_Officechecklist2.xlsx')
oc_303b2 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303b_Spring2021_Officechecklist2.xlsx')
oc_303c2 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303c_Spring2021_Officechecklist2.xlsx')
oc_303d2 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/02_Checklists/303(d)_Spring2021_Officechecklist2.xlsx')
#304
oc_304a2 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304(a)_Spring2021_Officechecklist2.xlsx')
oc_304b2 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304b_Spring2021_Officechecklist2.xlsx')
oc_304c2 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304c_Spring2021_Officechecklist2.xlsx')
oc_304d2 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304d_Spring2021_Officechecklist2.xlsx')
oc_304e2 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304e_Spring2021_Officechecklist2.xlsx')
oc_304f2 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304f_Spring2021_Officechecklist2.xlsx')
oc_304g2 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/02_Checklists/304g_Spring2021_Officechecklist2.xlsx')

#401 Greenland
oc_401b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401a_Spring2021_Officechecklist2.xlsx')
oc_401c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401b_Spring2021_Officechecklist2.xlsx')
oc_401d2 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401c_Spring2021_Officechecklist2.xlsx')
oc_401e2 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/02_Checklists/401d_Spring2021_Officechecklist2.xlsx')

#406
oc_406a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_406/02_Checklists/406a_Spring2021_officechecklist2.xlsx')
oc_406b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_406/02_Checklists/406b_Spring2021_officechecklist2.xlsx')
oc_406c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_406/02_Checklists/406c_Spring2021_officechecklist2.xlsx')

#407
oc_407a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_407/02_Checklists/407a_Spring2021_Officechecklist2.xlsx')
oc_407b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_407/02_Checklists/407b_Spring2021_Officechecklist2.xlsx')
oc_407c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_407/02_Checklists/407c_Spring2021_Officechecklist2.xlsx')

#408
oc_408a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_408/02_Checklists/408a_Spring2021_Officechecklist2.xlsx')
oc_408b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_408/02_Checklists/408b_Spring2021_Officechecklist2.xlsx')
oc_408c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_408/02_Checklists/408c_Spring2021_Officechecklist2.xlsx')

#409
oc_409a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/02_Checklists/409a_Spring2021_Officechecklist2.xlsx')
oc_409b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/02_Checklists/409b_Spring2021_Officechecklist2.xlsx')
oc_409c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/02_Checklists/409c_Spring2021_Officechecklist2.xlsx')

#410
oc_410a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/02_Checklists/410a_Spring2021_Officechecklist2.xlsx')
oc_410b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/02_Checklists/410b_Spring2021_Officechecklist2.xlsx')
oc_410c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/02_Checklists/410c_Spring2021_Officechecklist2.xlsx')

#411
oc_411a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/02_Checklists/411a_Spring2021_Officechecklist2.xlsx')
oc_411b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/02_Checklists/411b_Spring2021_Officechecklist2.xlsx')
oc_411c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/02_Checklists/411c_Spring2021_Officechecklist2.xlsx')

#412
oc_412a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_412/02_Checklists/412a_Spring2021_Officechecklist2.xlsx')
oc_412b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_412/02_Checklists/412b_Spring2021_Officechecklist2.xlsx')
oc_412c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_412/02_Checklists/412c_Spring2021_Officechecklist2.xlsx')

#413
oc_413a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_413/02_Checklists/413a_Spring2021_Officechecklist2.xlsx')
oc_413b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_413/02_Checklists/413b_Spring2021_Officechecklist2.xlsx')
oc_413c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_413/02_Checklists/413c_Spring2021_Officechecklist2.xlsx')

#414
oc_414a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_414/02_Checklists/414a_Spring2021_Officechecklist2.xlsx')
oc_414b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_414/02_Checklists/414b_Spring2021_Officechecklist2.xlsx')
oc_414c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_414/02_Checklists/414c_Spring2021_Officechecklist2.xlsx')

#415
oc_415a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_415/02_Checklists/415a_Spring2021_Officechecklist2.xlsx')
oc_415b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_415/02_Checklists/415b_Spring2021_Officechecklist2.xlsx')
oc_415c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_415/02_Checklists/415c_Spring2021_Officechecklist2.xlsx')

#416
oc_416a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_416/02_Checklists/416a_Spring2021_Officechecklist2.xlsx')
oc_416b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_416/02_Checklists/416b_Spring2021_Officechecklist2.xlsx')
oc_416c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_416/02_Checklists/416c_Spring2021_Officechecklist2.xlsx')

#417
oc_417a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_417/02_Checklists/417a_Spring2021_Officechecklist2.xlsx')
oc_417b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_417/02_Checklists/417b_Spring2021_Officechecklist2.xlsx')
oc_417c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_417/02_Checklists/417c_Spring2021_Officechecklist2.xlsx')

#418
oc_418a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_418/02_Checklists/418a_Spring2021_Officechecklist2.xlsx')
oc_418b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_418/02_Checklists/418b_Spring2021_Officechecklist2.xlsx')
oc_418c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_418/02_Checklists/418c_Spring2021_Officechecklist2.xlsx')

#419
oc_419a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_419/02_Checklists/419a_Spring2021_Officechecklist2.xlsx')
oc_419b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_419/02_Checklists/419b_Spring2021_Officechecklist2.xlsx')
oc_419c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_419/02_Checklists/419c_Spring2021_Officechecklist2.xlsx')

#420
oc_420a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_420/02_Checklists/420a_Spring2021_Officechecklist2.xlsx')
oc_420b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_420/02_Checklists/420b_Spring2021_Officechecklist2.xlsx')
oc_420c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_420/02_Checklists/420c_Spring2021_Officechecklist2.xlsx')

#421
oc_421a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_421/02_Checklists/421a_Spring2021_Officechecklist2.xlsx')
oc_421b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_421/02_Checklists/421b_Spring2021_Officechecklist2.xlsx')
oc_421c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_421/02_Checklists/421c_Spring2021_Officechecklist2.xlsx')

#422
oc_422a2 = pd.read_excel('../DATA/02_Greenland/Building_ID_422/02_Checklists/422a_Spring2021_Officechecklist2.xlsx')
oc_422b2 = pd.read_excel('../DATA/02_Greenland/Building_ID_422/02_Checklists/422b_Spring2021_Officechecklist2.xlsx')
oc_422c2 = pd.read_excel('../DATA/02_Greenland/Building_ID_422/02_Checklists/422c_Spring2021_Officechecklist2.xlsx')



#%%%
# Make dataframe of each checklist 2
oc2 = [oc_101b2 , oc_101c2, oc_101d2, 
       oc_102a2, oc_102b2, 
       oc_103a2, oc_103b2, oc_103c2, oc_103d2,
       oc_301a2, oc_301b2, oc_301c2,
       oc_302a2, oc_302b2, oc_302c2, oc_302d2, oc_302e2,
       oc_303a2, oc_303b2, oc_303c2, oc_303d2,
       oc_304a2, oc_304b2, oc_304c2, oc_304d2, oc_304e2, oc_304f2, oc_304g2,
       
       oc_401b2,oc_401c2,oc_401d2,oc_401e2,
       oc_406a2,oc_406b2,oc_406c2,
       oc_407a2,oc_407b2,oc_407c2,
       oc_408a2,oc_408b2,oc_408c2,
       oc_409a2,oc_409b2,oc_409c2,
       oc_410a2,oc_410b2,oc_410c2,
       oc_411a2,oc_411b2,oc_411c2,
       oc_412a2,oc_412b2,oc_412c2,
       oc_413a2,oc_413b2,oc_413c2,
       oc_414a2,oc_414b2,oc_414c2,
       oc_415a2,oc_415b2,oc_415c2,
       oc_416a2,oc_416b2,oc_416c2,
       oc_417a2,oc_417b2,oc_417c2,
       oc_418a2,oc_418b2,oc_418c2,
       oc_419a2,oc_419b2,oc_419c2,
       oc_420a2,oc_420b2,oc_420c2,
       oc_421a2,oc_421b2,oc_421c2,
       oc_422a2,oc_422b2,oc_422c2]

# Make dataframe
oc2 = pd.concat(oc2, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)


#%%%

#Drop doubles
oc2 = oc2.drop(['ID','officeID','completed','O1_roomNumber',
                'O3_useWindowsOpen','O3_useLightsOn','O3_useDoorOpen',
                
                'O3a_submitDate','O3b_submitDate','O3c_submitDate',
                'O3a_submitTime','O3b_submitTime','O3c_submitTime',
                
                'O3_useWindowsOpenComment','O3_useLightsOnComment',
                'O3_useDoorOpenComment','O3_useWorkStation','O3_useWorkStationComment',
                
                'O3_indoorBodyOdorComment','O3_indoorCosmeticsComment','O3_indoorTobaccoComment',
                'O3_indoorFoodComment','O3_indoorDampComment','O3_indoorExhaustComment',
                'O3_indoorChemicalComment','O3_indoorOtherComment',
                
                'O3_noiseOfficeMachinesComment','O3_noiseInOutComment','O3_noisePhonesComment',
                'O3_noiseVentComment','O3_noiseRadioComment','O3_noiseTrafficComment','O3_noiseConversationComment',
                'O3_noiseOtherComment',
                
                'O3_sourceTobaccoComment','O3_sourceAdhesiveComment','O3_sourcePaintComment',
                'O3_sourcePesticideComment','O3_sourceCleanerComment','O3_sourcePhotoCopyComment',
                'O3_sourceOtherComment'
                ],axis=1)

oc2.rename(columns={'buildingID': 'officeID'}, inplace=True)


#%%%
oc2['buildingID'] = oc2['officeID'].map({'101b':101,'101c':101,'101d':101,
                                         '102a':102,'102b':102,
                                         '103a':103,'103b':103,'103c':103,'103d':103,
                                         '301a':301,'301b':301,'301c':301,
                                         '302a':302,'302b':302,'302c':302,'302d':302,'302e':302,
                                         '303a':303,'303b':303,'303c':303,'303d':303,
                                         '304a':304,'304b':304,'304c':304,'304d':304,'304e':304,'304f':304,'304g':304,
                                         
                                         '401b':401,'401c':401,'401d':401,'401e':401,
                                         '406a':406,'406b':406,'406c':406,
                                         '407a':407,'407b':407,'407c':407,
                                         '408a':408,'408b':408,'408c':408,
                                         '409a':409,'409b':409,'409c':409,
                                         '410a':410,'410b':410,'410c':410,
                                         '411a':411,'411b':411,'411c':411,
                                         '412a':412,'412b':412,'412c':412,
                                         '413a':413,'413b':413,'413c':413,
                                         '414a':414,'414b':414,'414c':414,
                                         '415a':415,'415b':415,'415c':415,
                                         '416a':416,'416b':416,'416c':416,
                                         '417a':417,'417b':417,'417c':417,
                                         '418a':418,'418b':418,'418c':418,
                                         '419a':419,'419b':419,'419c':419,
                                         '420a':420,'420b':420,'420c':420,
                                         '421a':420,'421b':421,'421c':421,
                                         '422a':420,'422b':422,'422c':422})

oc2_bi_lst = ['O3_indoorBodyOdor','O3_indoorCosmetics','O3_indoorTobacco','O3_indoorFood',
              'O3_indoorDamp','O3_indoorExhaust','O3_indoorChemical','O3_indoorOther',
              
              'O3_noiseVent','O3_noiseRadio','O3_noiseOfficeMachines','O3_noiseInOut','O3_noisePhones',
              'O3_noiseTraffic','O3_noiseConversation','O3_noiseOther',
              
              'O3_sourceAdhesive','O3_sourcePaint','O3_sourcePesticide',
              'O3_sourcePhotoCopy','O3_sourceOther','O3_sourceTobacco','O3_sourceCleaner']
  
for column in oc2_bi_lst:
    oc2[column] = oc2[column].map({'on':"True", np.nan:"False", -1:"True"},)
    





#%%

# make 'True' 1 and 'False' 0:
oc2_bi_lst = ['O3_indoorBodyOdor','O3_indoorCosmetics','O3_indoorTobacco','O3_indoorFood',
              'O3_indoorDamp','O3_indoorExhaust','O3_indoorChemical','O3_indoorOther',
              
              'O3_noiseVent','O3_noiseRadio','O3_noiseOfficeMachines','O3_noiseInOut','O3_noisePhones',
              'O3_noiseTraffic','O3_noiseConversation','O3_noiseOther',
              
              'O3_sourceAdhesive','O3_sourcePaint','O3_sourcePesticide',
              'O3_sourcePhotoCopy','O3_sourceOther','O3_sourceTobacco','O3_sourceCleaner']
for column in oc2_bi_lst:
    oc2[column] = oc2[column].map({"True":1, "False":0})

oc2.reset_index(inplace=True, drop=True)


oc2['office_smell']='' # to create an empty column
for col_name in oc2[['O3_indoorBodyOdor','O3_indoorCosmetics','O3_indoorTobacco','O3_indoorFood','O3_indoorDamp','O3_indoorExhaust','O3_indoorChemical','O3_indoorOther']].columns:
    oc2.loc[oc2[col_name]==1,'office_smell']= oc2['office_smell']+' '+col_name

oc2['office_noise']='' # to create an empty column
for col_name in oc2[['O3_noiseVent','O3_noiseRadio','O3_noiseOfficeMachines','O3_noiseInOut','O3_noisePhones',
'O3_noiseTraffic','O3_noiseConversation','O3_noiseOther']].columns:
    oc2.loc[oc2[col_name]==1,'office_noise']= oc2['office_noise']+' '+col_name

oc2['office_pollutant']='' # to create an empty column
for col_name in oc2[['O3_sourceAdhesive','O3_sourcePaint','O3_sourcePesticide','O3_sourcePhotoCopy','O3_sourceOther','O3_sourceTobacco','O3_sourceCleaner']].columns:
    oc2.loc[oc2[col_name]==1,'office_pollutant']= oc2['office_pollutant']+' '+col_name





oc2 = oc2.drop(['O3_indoorBodyOdor','O3_indoorCosmetics','O3_indoorTobacco','O3_indoorFood',
                'O3_indoorDamp','O3_indoorExhaust','O3_indoorChemical','O3_indoorOther',
                
                'O3_noiseVent','O3_noiseRadio','O3_noiseOfficeMachines','O3_noiseInOut','O3_noisePhones',
                'O3_noiseTraffic','O3_noiseConversation','O3_noiseOther',
                
                'O3_sourceAdhesive','O3_sourcePaint','O3_sourcePesticide',
                'O3_sourcePhotoCopy','O3_sourceOther','O3_sourceTobacco','O3_sourceCleaner'],axis=1)




oc2 = oc2.set_index('officeID',drop=False)
#%%%
'''MERGE office checlists'''

#office_checklists = pd.concat([oc1, oc2], axis=1)


#writing office checklist 2 out of code
#office_checklists = oc1.combine_first(oc2)
office_checklists = oc1
#%%%

# Merge all checklists
#df_temp = pd.concat([mb_checklists, office_checklists], axis=1)
#df_temp = office_checklists.merge(mb_checklists, how='cross', on="buildingID")
df_check = pd.merge(mb_non_sVent_checklists,office_checklists, how='right', on="buildingID")
df_check = df_check.set_index('officeID',drop=False)

#%% - Delete unwanted dataframes

del [building_checklist_101,building_checklist_102,building_checklist_103, building_checklist_301, 
     building_checklist_302, building_checklist_303,building_checklist_304,
     building_checklist_401, building_checklist_402, building_checklist_403,
     building_checklist_404, building_checklist_405, building_checklist_406,
     building_checklist_407, building_checklist_408,building_checklist_409,
     building_checklist_410, building_checklist_411,building_checklist_412,
     building_checklist_413,building_checklist_414,building_checklist_415,
     building_checklist_416,building_checklist_417,building_checklist_418,
     building_checklist_419,building_checklist_420,
     building_checklist_421,building_checklist_422,
     
     building_checklist_103E, building_checklist_104, building_checklist_105,
     building_checklist_301E, building_checklist_305A, building_checklist_306,
     building_checklist_307,
     building_checklist_309, building_checklist_310, building_checklist_311,
     building_checklist_312,building_checklist_313,
     
     mc_101, mc_102, mc_103, mc_301, mc_302, mc_303, mc_304,
     mc_401,mc_402,mc_403,mc_404,mc_405,mc_406,mc_407,mc_408,
     mc_409,mc_410, mc_411,mc_412,mc_413,mc_414,mc_415,mc_416,
     mc_417,mc_418,mc_419,mc_420,mc_421, mc_422,
     mc_103E,mc_104, mc_105, mc_301E, mc_305A, mc_306, mc_307,
     mc_309, mc_310, mc_311, mc_312, mc_313,
     
     oc_101b1, oc_101c1, oc_101d1, 
     oc_102a1, oc_102b1,
     oc_103a1, oc_103b1, oc_103c1, oc_103d1,
     oc_301a1, oc_301b1, oc_301c1, 
     oc_302a1, oc_302b1, oc_302c1, oc_302d1, oc_302e1, 
     oc_303a1, oc_303b1, oc_303c1,oc_303d1,
     oc_304a1, oc_304b1, oc_304c1, oc_304d1, oc_304e1,oc_304f1,oc_304g1,
     
     oc_401b1,oc_401c1,oc_401d1,oc_401e1,
     oc_402a1,oc_402b1,oc_402c1,oc_402d1,oc_402e1,
     oc_403a1,oc_403b1,oc_403c1,oc_403d1,
     oc_404a1,oc_404b1,
     oc_405a1,oc_405b1,oc_405c1,oc_405d1,
     oc_406a1,oc_406b1,oc_406c1,
     oc_407a1,oc_407b1,oc_407c1,
     oc_408a1,oc_408b1,oc_408c1,
     oc_409a1,oc_409b1,oc_409c1,
     oc_410a1,oc_410b1,oc_410c1,
     oc_411a1,oc_411b1,oc_411c1,
     oc_412a1,oc_412b1,oc_412c1,
     oc_413a1,oc_413b1,oc_413c1,
     oc_414a1,oc_414b1,oc_414c1,
     oc_415a1,oc_415b1,oc_415c1,
     oc_416a1,oc_416b1,oc_416c1,
     oc_417a1,oc_417b1,oc_417c1,
     oc_418a1,oc_418b1,oc_418c1,
     oc_419a1,oc_419b1,oc_419c1,
     oc_420a1,oc_420b1,oc_420c1,
     oc_421a1,oc_421b1,oc_421c1,
     oc_422a1,oc_422b1,oc_422c1,
     
     oc_101b2 , oc_101c2, oc_101d2, 
     oc_102a2, oc_102b2, 
     oc_103a2, oc_103b2, oc_103c2, oc_103d2,
     oc_301a2, oc_301b2, oc_301c2,
     oc_302a2, oc_302b2, oc_302c2, oc_302d2, oc_302e2,
     oc_303a2, oc_303b2, oc_303c2, oc_303d2,
     oc_304a2, oc_304b2, oc_304c2, oc_304d2, oc_304e2, oc_304f2, oc_304g2,
     
     oc_103E,oc_104, oc_105,
     
     oc_301E,
     oc_305A, oc_306,oc_307,
     oc_309, oc_310, oc_311, oc_312, oc_313,
     
     
     oc_401b2,oc_401c2,oc_401d2,oc_401e2,
     oc_406a2,oc_406b2,oc_406c2,
     oc_407a2,oc_407b2,oc_407c2,
     oc_408a2,oc_408b2,oc_408c2,
     oc_409a2,oc_409b2,oc_409c2,
     oc_410a2,oc_410b2,oc_410c2,
     oc_411a2,oc_411b2,oc_411c2,
     oc_412a2,oc_412b2,oc_412c2,
     oc_413a2,oc_413b2,oc_413c2,
     oc_414a2,oc_414b2,oc_414c2,
     oc_415a2,oc_415b2,oc_415c2,
     oc_416a2,oc_416b2,oc_416c2,
     oc_417a2,oc_417b2,oc_417c2,
     oc_418a2,oc_418b2,oc_418c2,
     oc_419a2,oc_419b2,oc_419c2,
     oc_420a2,oc_420b2,oc_420c2,
     oc_421a2,oc_421b2,oc_421c2,
     oc_422a2,oc_422b2,oc_422c2,
     
     column,m_bi_lst,oc2_bi_lst,oc1_bi_lst
     ] 

# %%

df_check.to_csv("../temp_data/df_check.csv", index=False)