#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LOAD QUESTIONIRES

Created on Fri Aug 29 13:20:15 2022

@author: Sophia
"""
import pandas as pd
import numpy as np
import load_utils as lu

import seaborn as sns
import matplotlib.pyplot as plt

# Import data sheets to python with pandas

#%%%
""" LOADING questionaires"""
'''The column "pizza" is the nr. meesurements mox used in the office, and is 
    bellow manually connected with office ID.'''

# Load in building  checklists from excel to pandas
q_101 = pd.read_excel('../DATA/01_Denmark/BuildingID_101/03_Questionnaire/Copy_101_Winter2020_Questionnaire.xlsx')
q_102 = pd.read_excel('../DATA/01_Denmark/BuildingID_102/03_Questionnaire/Copy_102_Winter2020_Questionnaire.xlsx')
q_103 = pd.read_excel('../DATA/01_Denmark/BuildingID_103/03_Questionnaire/Copy103_Spring2021_Questionnaire.xlsx')

q_103['officeID'] = q_103['pizza'].map({1:'103a', 3:'103a',  8:'103a', 2:'103b', 25:'103b', 
                                        7:'103c', 22:'103c', 12:'103d' })

q_103E = pd.read_excel('../DATA/01_Denmark/BuildingID_103F/03_Questionnaire/103_F2021_Questionnaire.xlsx')
q_103E['officeID'] = q_103E['pizza'].map({10:'103_E2021a', 11:'103_E2021a', 13:'103_E2021b',12:'103_E2021c'})

q_104 = pd.read_excel('../DATA/01_Denmark/BuildingID_104/03_Questionnaire/104_Q.xlsx')
q_104['officeID'] = q_104['pizza'].map({22:'104a', 24:'104b'})

q_105 = pd.read_excel('../DATA/01_Denmark/BuildingID_105/03_Questionnaire/105_Q.xlsx')
q_105['officeID'] = q_105['pizza'].map({22:'105a', 24:'105a',10:'105a'})


q_301 = pd.read_excel('../DATA/01_Denmark/BuildingID_301/03_Questionnaire/Copy301_Spring2021_Questionnaire.xlsx')
q_301['officeID'] = q_301['pizza'].map({16:'301a', 3:'301b', 14:'301c', 13:'301d', 
                                        15:'301e', 12:'301f', 17:'301g' })

q_302 = pd.read_excel('../DATA/01_Denmark/BuildingID_302/03_Questionnaire/Copy302_Spring2021_Questionnaire.xlsx')
q_302['officeID'] = q_302['pizza'].map({5:'302a', 2:'302b', 21:'302c', 8:'302d', 11:'302e'})

q_303 = pd.read_excel('../DATA/01_Denmark/BuildingID_303/03_Questionnaire/Copy303_Spring2021_Questionnaire.xlsx')
q_303['officeID'] = q_303['pizza'].map({15:'303a', 12:'303b', 17:'303c', 13:'303d', 14:'303d'})

q_304 = pd.read_excel('../DATA/01_Denmark/BuildingID_304/03_Questionnaire/Copy304_Spring2021_Questionnaire.xlsx')
q_304['officeID'] = q_304['pizza'].map({16:'304a', 3:'304b', 14:'304c', 13:'304d', 
                                        15:'304e', 12:'304f', 17:'304g' })

q_301E = pd.read_excel('../DATA/01_Denmark/BuildingID_301_E20/03_Questionnaire/301_E2021_Questionnaire.xlsx')
q_301E['officeID'] = q_301E['pizza'].map({8:'301_E2021a', 22:'301_E2021b', 23:'301_E2021c', 17:'301_E2021d'})

q_305A = pd.read_excel('../DATA/01_Denmark/BuildingID_305A/03_Questionnaire/305A_Q.xlsx')
q_305A['officeID'] = q_305A['pizza'].map({1:'305b', 2:'305c',3:'305d',4:'305e',5:'305f',
                                          6:'305g', 7:'305h', 9:'305i'})

q_306 = pd.read_excel('../DATA/01_Denmark/BuildingID_306/03_Questionnaire/306_F2021_Questionnaire.xlsx')
q_306['officeID'] = q_306['pizza'].map({13:'3060A', 11:'3060B',12:'3061A',10:'3061A'})

q_307 = pd.read_excel('../DATA/01_Denmark/BuildingID_307/03_Questionnaire/307_Fall2021_Questionnaire.xlsx')
q_307['officeID'] = q_307['pizza'].map({8:'307a', 17:'307a',22:'307a',23:'307a'})

q_308 = pd.read_excel('../DATA/01_Denmark/BuildingID_307/03_Questionnaire/307_Fall2021_Questionnaire.xlsx')
q_308['officeID'] = q_308['pizza'].map({10:'308Ab', 22:'308Ab',
                                        11:'308Ba',12:'308Ba',13:'308Bb'})


q_309 = pd.read_excel('../DATA/01_Denmark/BuildingID_309/03_Questionnaire/309_Q.xlsx')
q_309['officeID'] = q_309['pizza'].map({4:'309a', 7:'309a',2:'309b',15:'309b',17:'309c'})

q_310 = pd.read_excel('../DATA/01_Denmark/BuildingID_310/03_Questionnaire/310_Q.xlsx')
q_310['officeID'] = q_310['pizza'].map({18:'310a', 19:'310a',16:'310b'})


q_311 = pd.read_excel('../DATA/01_Denmark/BuildingID_311/03_Questionnaire/311_Q.xlsx')
q_311['officeID'] = q_311['pizza'].map({11:'311a', 12:'311a',8:'311b'})


q_312 = pd.read_excel('../DATA/01_Denmark/BuildingID_312/03_Questionnaire/312_Q.xlsx')
q_312['officeID'] = q_312['pizza'].map({20:'312a', 21:'312a',23:'312b',25:'312c'})

q_313 = pd.read_excel('../DATA/01_Denmark/BuildingID_313/03_Questionnaire/313_Q.xlsx')
q_313['officeID'] = q_313['pizza'].map({11:'313a', 12:'313a',13:'313a',
                                        14:'313b',16:'313b',
                                        18:'313c',19:'313c',
                                        8:'313d', 20:'313e',
                                        23:'313f',25:'313f'})





q_401 = pd.read_excel('../DATA/02_Greenland/Building_ID_401/03_Questionnaire/Copy_401_Spring2021_Questionnaire.xlsx')

q_402 = pd.read_excel('../DATA/02_Greenland/Building_ID_402/03_Questionnaire/402_Spring2021_Questionnaire.xlsx')
q_402['officeID'] = q_402['pizza'].map({8:'402b', 11:'402e', 4:'402d', 9:'402a', 10:'402c' })


q_403 = pd.read_excel('../DATA/02_Greenland/Building_ID_403/03_Questionnaire/403_Spring2021_Questionnaire.xlsx')
q_403['officeID'] = q_403['pizza'].map({13:'403a', 12:'403b', 14:'403c', 2:'403d' })

q_404 = pd.read_excel('../DATA/02_Greenland/Building_ID_404/03_Questionnaire/404_Spring2021_Questionnaire.xlsx')
q_404['officeID'] = q_404['pizza'].map({20:'404a', 19:'404b'})

q_405 = pd.read_excel('../DATA/02_Greenland/Building_ID_405/03_Questionnaire/405_Spring2021_Questionnaire.xlsx')
q_405['officeID'] = q_405['pizza'].map({17:'405a', 21:'405b',18:'405c',1:'405d'})

q_407 = pd.read_excel('../DATA/02_Greenland/Building_ID_407/03_Questionnaire/407_Spring2021_Questionnaire.xlsx')
q_407['officeID'] = q_407['pizza'].map({18:'407a', 19:'407b',17:'407c'})

q_409 = pd.read_excel('../DATA/02_Greenland/Building_ID_409/03_Questionnaire/409_Spring2021_Questionnaire.xlsx')
q_409['officeID'] = q_409['pizza'].map({9:'409a', 11:'409b',12:'409c'})

q_410 = pd.read_excel('../DATA/02_Greenland/Building_ID_410/03_Questionnaire/410_Spring2021_Questionnaire.xlsx')
q_410['officeID'] = q_410['pizza'].map({3:'410a', 2:'410b',4:'410c'})

q_411 = pd.read_excel('../DATA/02_Greenland/Building_ID_411/03_Questionnaire/411_Spring2021_QuestionnaireKopi.xlsx')
q_411['officeID'] = q_411['pizza'].map({6:'411a', 5:'411b',8:'411c'})

q_412 = pd.read_excel('../DATA/02_Greenland/Building_ID_412/03_Questionnaire/412_Spring2021_QuestionnaireKopi.xlsx')
q_412['officeID'] = q_412['pizza'].map({20:'412a', 23:'412b',21:'412c'})

q_413 = pd.read_excel('../DATA/02_Greenland/Building_ID_413/03_Questionnaire/413_Spring2021_Questionnaire.xlsx')
q_413['officeID'] = q_413['pizza'].map({29:'413a', 33:'413b',35:'413c'})

q_414 = pd.read_excel('../DATA/02_Greenland/Building_ID_414/03_Questionnaire/414_Spring2021_Questionnaire.xlsx')
q_414['officeID'] = q_414['pizza'].map({31:'414a', 32:'414b',24:'414c'})

q_415 = pd.read_excel('../DATA/02_Greenland/Building_ID_415/03_Questionnaire/415_Spring2021_Questionnaire.xlsx')
q_415['officeID'] = q_415['pizza'].map({30:'415a', 25:'415b',28:'415c'})

q_416 = pd.read_excel('../DATA/02_Greenland/Building_ID_416/03_Questionnaire/416_Spring2021_Questionnaire.xlsx')
q_416['officeID'] = q_416['pizza'].map({34:'416a',26:'416b',27:'416c'})

q_417 = pd.read_excel('../DATA/02_Greenland/Building_ID_417/03_Questionnaire/417_Spring2021_Questionnaire.xlsx')
q_417['officeID'] = q_417['pizza'].map({7:'417a',10:'417b',13:'417c'})

q_418 = pd.read_excel('../DATA/02_Greenland/Building_ID_418/03_Questionnaire/418_Spring2021_Questionnaire.xlsx')
q_418['officeID'] = q_418['pizza'].map({7:'418a',10:'418b',13:'418c'})

q_419 = pd.read_excel('../DATA/02_Greenland/Building_ID_419/03_Questionnaire/419_Spring2021_Questionnaire.xlsx')
q_419['officeID'] = q_419['pizza'].map({9:'419a',8:'419b',3:'419c'})

q_420 = pd.read_excel('../DATA/02_Greenland/Building_ID_420/03_Questionnaire/420_Spring2021_Questionnaire.xlsx')
q_420['officeID'] = q_420['pizza'].map({2:'420a',5:'420b',4:'420c'})

q_421 = pd.read_excel('../DATA/02_Greenland/Building_ID_421/03_Questionnaire/Copy_421_Spring2021_Questionnaire.xlsx')
q_421['officeID'] = q_421['pizza'].map({17:'421a',18:'421b',19:'421c'})

q_422 = pd.read_excel('../DATA/02_Greenland/Building_ID_422/03_Questionnaire/Copy_422_Spring2021_Questionnaire.xlsx')
q_422['officeID'] = q_422['pizza'].map({22:'422a',1:'422b',15:'422c'})



# Make dataframe of each checklist
q_lst = [q_101,q_103E,q_102,q_103,q_104,q_105,
         
         q_301,q_301E,
         q_302,q_303,q_304,
         
         q_305A,q_306,q_307,q_308,
         q_309,q_310,q_311,q_312,q_313,
         
         q_401, q_402, q_403, q_404,q_405,q_407,q_409,
         q_410,q_411,q_412,q_413,q_414,q_415,q_416,q_417,
         q_418,q_419,q_420,q_421,q_422]

q_df = pd.concat(q_lst, axis=0, join='outer', ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=False)

#%%%

# make feature of the month
q_df['month']  = pd.to_datetime(q_df['submitDate'], dayfirst=True).dt.month
                                     


#%%
'''Remove unnecesary features and early clean'''

q_df = q_df.drop(['ID','userID','submitTime','lang','completed','submitDate',
                  't','b','kode','floor','otherOfficeInterior','yearsinoffice',
                  'daysInOffice', 'otherSeating','otherConstellation','otherJob',
                  
                  'gangarealer','kantine','skrivebord','noMask','kontor',
                  
                  'commentLight','lightOtherDissatisfaction',
                  
                  'airqualStuffy','airqualSmelly','commentAirqual',
                  
                  'commentNoise','seating','officeHome','noiseOtherOutdoor',
                  'otherAirqualSource','noiseOther',
                  
                  
                  'commentIndoorClimate'],axis=1)


'''The binary features are given as 1 and nan. The nan features must, 
    thus, be replaced by 0'''

q_bi_lst = ['photocopier', 'outside', 'printer',
            'perfume','food','tobaccoSmoke','cleaningProd','carpet',
                  
            'noiseTraffic','noiseOverhearing','noiseOfficeEquipment',
            'noisePhoneTalk','noiseNeighborTalk','noisemechanical',
            'noiseTelephones',
                  
            'lightTooDark','lightTooBright','lightTooLittleDaylight','lightTooMuchDaylight',
            'lightFlicker', 'lightReflections','lightColor',
            'lightColor', 'lightNoTask']
  
for column in q_bi_lst:
    q_df[column] = q_df[column].map({ 1:True,np.nan:False})

#%%%
''' Make DF only with people sat in meassured offices'''

q_office_df = q_df[q_df['pizza'].apply(lambda x: isinstance(x, (float,int, np.int64)))]

q_office_df = q_office_df[q_office_df['officeID'].notna()]



#%%%
''' Make sure only symptoms that disapear when occupant leaves the office 
    are taken into account.'''
    

q_office_df= q_office_df.reset_index()

# The following refers to function in load_utils, that reduces the the four
# classes of each symptom into two, where 0 is no symptom in the last 4 weeks
# and 1 is the experience of the symptom. 
q_office_df['symp0'] = q_office_df['symp0'].apply(lu.reduce_s)
q_office_df['symp1'] = q_office_df['symp1'].apply(lu.reduce_s)
q_office_df['symp2'] = q_office_df['symp2'].apply(lu.reduce_s)
q_office_df['symp3'] = q_office_df['symp3'].apply(lu.reduce_s)
q_office_df['symp4'] = q_office_df['symp4'].apply(lu.reduce_s)
q_office_df['symp5'] = q_office_df['symp5'].apply(lu.reduce_s)
q_office_df['symp6'] = q_office_df['symp6'].apply(lu.reduce_s)
q_office_df['symp7'] = q_office_df['symp7'].apply(lu.reduce_s)
q_office_df['symp8'] = q_office_df['symp8'].apply(lu.reduce_s)
q_office_df['symp9'] = q_office_df['symp9'].apply(lu.reduce_s)

# When an occupant experiences a symptom, they will either feel worse,
# better or no change after leaving the office. We are only interested 
# in the office related symtoms. 
#symp0: 
q_office_df['betterorworse0'] = q_office_df['betterorworse0'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s0_better'] = ''
lu.sBetter(q_office_df,'symp0','betterorworse0','s0_better')

#symp1: 
q_office_df['betterorworse1'] = q_office_df['betterorworse1'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s1_better'] = ''
lu.sBetter(q_office_df,'symp1','betterorworse1','s1_better')
#symp2: 
q_office_df['betterorworse2'] = q_office_df['betterorworse2'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s2_better'] = ''
lu.sBetter(q_office_df,'symp2','betterorworse2','s2_better')

#symp3: 
q_office_df['betterorworse3'] = q_office_df['betterorworse3'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s3_better'] = ''
lu.sBetter(q_office_df,'symp3','betterorworse1','s3_better')

#symp4: 
q_office_df['betterorworse4'] = q_office_df['betterorworse4'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s4_better'] = ''
lu.sBetter(q_office_df,'symp4','betterorworse4','s4_better')



#symp5: 
q_office_df['betterorworse5'] = q_office_df['betterorworse5'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s5_better'] = ''
lu.sBetter(q_office_df,'symp5','betterorworse5','s5_better')

#symp6: 
q_office_df['betterorworse6'] = q_office_df['betterorworse6'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s6_better'] = ''
lu.sBetter(q_office_df,'symp6','betterorworse6','s6_better')


#symp7: 
q_office_df['betterorworse7'] = q_office_df['betterorworse7'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s7_better'] = ''
lu.sBetter(q_office_df,'symp7','betterorworse7','s7_better')

#symp8: 
q_office_df['betterorworse8'] = q_office_df['betterorworse8'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s8_better'] = ''
lu.sBetter(q_office_df,'symp8','betterorworse8','s8_better')


#symp9: 
q_office_df['betterorworse9'] = q_office_df['betterorworse9'].map({"worse":0,
                                                                   "nochange":0,
                                                                   "better":1, 
                                                                   np.nan: 0})
q_office_df['s9_better'] = ''
lu.sBetter(q_office_df,'symp9','betterorworse9','s9_better')



# Below the experience of at least one or two different office-related 
# symptoms are made into a binary feature
lu.SBS_1(q_office_df,'s0_better','s1_better','s2_better','s3_better','s4_better','s5_better','s6_better','s7_better','s8_better','s9_better','SBS1')
lu.SBS_2(q_office_df,'s0_better','s1_better','s2_better','s3_better','s4_better','s5_better','s6_better','s7_better','s8_better','s9_better','SBS2')

#%%%
# The following was used to assess the distributions of each symptom, to see
# what symptoms to make single symptom models of. 

# plot symptoms in SBS

# fig, axs = plt.subplots(5, 2, figsize=(20, 8))
# sns.catplot(data=q_office_df, x="s0", kind="count", palette="ch:.25",aspect=1).set(title='Dry or irritated eyes')
# sns.catplot(data=q_office_df, x="s1", kind="count", palette="ch:.25",aspect=1).set(title='Headache')
# sns.catplot(data=q_office_df, x="s2", kind="count", palette="ch:.25",aspect=1).set(title='Sore or dry throat')
# sns.catplot(data=q_office_df, x="s3", kind="count", palette="ch:.25",aspect=1).set(title='Tiredness or fatigue')
# sns.catplot(data=q_office_df, x="s4", kind="count", palette="ch:.25",aspect=1).set(title='Stuffy or runny nose')
# sns.catplot(data=q_office_df, x="s5", kind="count", palette="ch:.25",aspect=1).set(title='Cough')
# sns.catplot(data=q_office_df, x="s6", kind="count", palette="ch:.25",aspect=1).set(title='Sneezing')
# sns.catplot(data=q_office_df, x="s7", kind="count", palette="ch:.25",aspect=1).set(title='Difficult to concentrate')
# sns.catplot(data=q_office_df, x="s8", kind="count", palette="ch:.25",aspect=1).set(title='Shortness of breath')
# sns.catplot(data=q_office_df, x="s9", kind="count", palette="ch:.25",aspect=1).set(title='Dry skin')
# plt.show()


#symp0: Dry or irritated eyes - good
#symp0: Headache - good
#symp3: Tiredness or fatigue - good
#symp7: Difficult to concentrate - good


#symp2: Sore or dry throat - less than 30 
#symp4: Stuffy or runny nose - less than 20
#symp5: cough - less than 20 
#symp6: sneezing - less than 20
#symp8: Shortness of breath - less than 10 
#symp9: dry skin - less than 20 


print("s0",q_office_df['s0'].value_counts())
print("s1",q_office_df['s1'].value_counts())
print("s2",q_office_df['s2'].value_counts())
print("s3",q_office_df['s3'].value_counts())
print("s4",q_office_df['s4'].value_counts())
print("s5",q_office_df['s5'].value_counts())
print("s6",q_office_df['s6'].value_counts())
print("s7",q_office_df['s7'].value_counts())
print("s8",q_office_df['s8'].value_counts())
print("s9",q_office_df['s9'].value_counts())


'''0: Not in the past 4 weeks
   1: 1-3 days in the past 4 weeks
   2: 1-3 days per week in the past 4 weeks
   3: Every workday in the past 4 weeks
'''

#%%%


sns.catplot(data=q_office_df, x="SBS1", kind="count", palette="ch:.25",aspect=40/10)
print(q_office_df['SBS1'].value_counts())
#%%%

#plot distribution of at least two office-related symptoms
sns.catplot(data=q_office_df, x="SBS2", kind="count", palette="ch:.25",height=4,aspect=3/2).set(title='Multiple symptoms')
plt.show()
print(q_office_df['SBS2'].value_counts())


#%%%

#Drop features that are not used as targets

q_office_df = q_office_df.drop(['index',
                            'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
                            'q11','thisweek_0','thisweek_1','thisweek_2','thisweek_3',
                            'thisweek_4','thisweek_5','thisweek_6','thisweek_7',
                            'thisweek_8','thisweek_9','thisweek_10','thisweek_11',
                            
                            'betterorworse0','symp0',
                            'betterorworse1','symp1',
                            'betterorworse3','symp3',
                            'betterorworse7','symp7',
                            
                            's2_better','s4_better','s5_better',
                            's6_better','s8_better','s9_better',
                            
                            'symp2','symp4','symp5',
                            'symp6','symp8','symp9',
                            'betterorworse2','betterorworse4',
                            'betterorworse5','betterorworse6',
                            'betterorworse8','betterorworse9',
                            
                            's0','s1','s2','s3','s4','s5','s6','s7','s8','s9',
                            
                            'performanceFactor0','performanceFactor1',
                            'performanceFactor2','performanceFactor3',
                            'performanceFactor4','performanceFactor5',
                            'performanceFactor6','performanceFactor7',
                            'performanceFactor8','performanceFactor9',
                            'performanceFactor10','pizza'],axis=1)
#%%%
#symp0: Dry or irritated eyes - good
#symp3: Tiredness or fatigue - good
#symp7: Difficult to concentrate - good


#symp2: Sore or dry throat - less than 30 
#symp4: Stuffy or runny nose - less than 20
#symp5: cough - less than 20 
#symp6: sneezing - less than 20
#symp8: Shortness of breath - less than 10 
#symp9: dry skin - less than 20 

# sns.catplot(data=q_office_df, x="symp7", kind="count", palette="ch:.25",aspect=40/10)
# sns.catplot(data=q_office_df, x="betterorworse7", kind="count", palette="ch:.25",aspect=40/10)

#%% - Delete unwanted dataframes

del [q_101,q_102,q_103,q_104,q_105,q_103E,
     
     q_301,q_302,q_303,q_304,
     
     q_301E,
     
     q_305A,q_306,q_307,q_308,
     q_309,q_310,q_311,q_312,q_313,
     
     q_401, q_402, q_403, q_404,q_405,q_407,q_409,
     q_410,q_411,q_412,q_413,q_414,q_415,q_416,q_417,q_418,q_419,
     q_420, q_421, q_422,
     q_lst, q_bi_lst,column]

# %%

q_office_df.to_csv('../temp_data/q_office_df.csv', index=False)
