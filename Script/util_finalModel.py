"""Created on Thu Nov  3 17:07:02 2022@author: Sophia"""# libraries used import numpy as npimport pandas as pdfrom sklearn.tree import DecisionTreeClassifierfrom sklearn.naive_bayes import GaussianNBfrom sklearn.svm import SVCfrom sklearn.model_selection import train_test_splitfrom sklearn.metrics import accuracy_score, roc_auc_scorefrom sklearn.ensemble import RandomForestClassifierimport shapfrom sklearn.preprocessing import MaxAbsScalerfrom sklearn.metrics import f1_scorefrom sklearn.ensemble import RandomForestRegressorshap.initjs()import pickleimport joblib    #pip install shap #install shapimport shap # import shap moduleshap.initjs() #initialize javascript to enable plotsfrom scipy.special import softmaximport shapimport pandas as pdfrom sklearn.datasets import fetch_california_housingfrom sklearn.model_selection import train_test_splitfrom sklearn.ensemble import RandomForestRegressorimport numpy as npimport pandas as pdimport osfrom sklearn.model_selection import train_test_splitfrom sklearn.ensemble import RandomForestClassifierfrom sklearn import metrics#normalize dfdef norm(df):    scaler = MaxAbsScaler()    scaler.fit(df)    scaled = scaler.transform(df)    df_norm = pd.DataFrame(scaled, columns=df.columns)    df_norm = round(df_norm, 2)    return df_norm# performance modeldef performance(df):        cols = [x for x in df.columns if x != 'performanceOverall']    X = df[cols]    y = df['performanceOverall']    #create dummies    X = pd.get_dummies(X,drop_first=True)            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)    # Train random forrest classifier    model = RandomForestClassifier(random_state=42,                                      n_estimators= 100,                                      max_depth =6,                                       min_samples_leaf = 1,                                      min_samples_split= 3,                                      class_weight=None)        model.fit(X_train,y_train)    y_pred = model.predict(X_test)    pickle.dump(model, open('./trained_models/performance_model.pkl', 'wb'))        print("Random Forest accuracy:",accuracy_score(y_test,y_pred))    print("Random Forest F1 score:",f1_score(y_test,y_pred))    print("Random Forrest auc:",roc_auc_score(y_test,y_pred))        explainer = shap.KernelExplainer(model.predict, X_train)    shap_values= explainer.shap_values(X_test)    shap.summary_plot(shap_values, X_test)# Function to retrain indoor climate modeldef indoorClimate(df):    cols = [x for x in df.columns if x != 'indoorClimate']    X = df[cols]    y = df['indoorClimate']        #create dummies    X = pd.get_dummies(X,drop_first=True)        #Nomralize all values in X    X = norm(X)        #Devide data frame into trainigng and testing data.      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)        #Defining support vector machine algorithm and sigmoid kernel.    model =  SVC(kernel='sigmoid',probability=True)        #Train model    model.fit(X_train,y_train)        # Calculate predictions    y_pred = model.predict(X_test)    # save the model    filename = './trained_models/indoorClimate_model.sav'    joblib.dump(model, filename)            #calculate model performance metrics and print    print("SVC accuracy:",accuracy_score(y_test,y_pred))    print("SVC F1 score:",f1_score(y_test,y_pred))    print("SVC auc:",roc_auc_score(y_test,y_pred))        # Fits the explainer    explainer = shap.Explainer(model.predict, X_train)    # Calculates the SHAP values - It takes some time    shap_values = explainer(X_test)    shap.summary_plot(shap_values, X_test)       def model_indoorClimate(df,df2,row):    cols = [x for x in df.columns if x != 'indoorClimate']    X = df[cols]    y = df['indoorClimate']        #create dummies    X = pd.get_dummies(X,drop_first=True)        #Nomralize all values in X    X = norm(X)        #Devide data frame into trainigng and testing data.      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)        #Defining support vector machine algorithm and sigmoid kernel.    model =  SVC(kernel='sigmoid',probability=True)        #Train model    model.fit(X_train,y_train)        # predictions of test data    y_pred = model.predict(X_test)        # force plot    cols = [x for x in df2.columns if x != 'indoorClimate']    X2 = df2[cols]    y = df2['indoorClimate']        #create dummies    X2 = pd.get_dummies(X2,drop_first=True)        #Nomralize all values in X    X2 = norm(X2)        choosen_instance = X.iloc[[row]]    y_pred_obs = model.predict(choosen_instance)    print("Indoor climate prediction: ", y_pred_obs)        explainer = shap.KernelExplainer(model.predict_proba, X_train)    shap_values = explainer.shap_values(choosen_instance)            shap.initjs()    shap.force_plot(explainer.expected_value[1], shap_values[1], choosen_instance,link = "logit", matplotlib = True)    shap.initjs()             def symptoms(df):        cols = [x for x in df.columns if x != 'SBS2']    X = df[cols]    y = df['SBS2']        #create dummies    X = pd.get_dummies(X,drop_first=True)        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)            # Train random forrest classifier    model = RandomForestClassifier(random_state= 42,                                   max_depth = 4,                                    min_samples_leaf = 2,                                   min_samples_split= 5,                                   n_estimators=100,                                   max_features= 12,                                   class_weight='balanced_subsample')        model.fit(X_train,y_train)    y_pred = model.predict(X_test)        #save model    pickle.dump(model, open('./trained_models/symptoms_model.pkl', 'wb'))        print("Random Forest accuracy:",accuracy_score(y_test,y_pred))    print("Random Forest F1 score:",f1_score(y_test,y_pred))    print("Random Forrest auc:",roc_auc_score(y_test,y_pred))        explainer = shap.KernelExplainer(model.predict, X_train)    shap_values= explainer.shap_values(X_test)    shap.summary_plot(shap_values, X_test)    # 0: Dry or irritated eyesdef s0(df):        cols = [x for x in df.columns if x != 's0_better']    X = df[cols]    y = df['s0_better']    #create dummies    X = pd.get_dummies(X,drop_first=True)            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)    # d_train = lgb.Dataset(X_train, label=y_train)    # d_test = lgb.Dataset(X_test, label=y_test)        # Train random forrest classifier    model = RandomForestClassifier(random_state= 42,                                   max_depth = 4,                                    min_samples_leaf = 7,                                   min_samples_split= 9,                                   class_weight="balanced")        model.fit(X_train,y_train)    y_pred = model.predict(X_test)    pickle.dump(model, open('./trained_models/s0_model.pkl', 'wb'))        print("Random Forest accuracy:",accuracy_score(y_test,y_pred))    print("Random Forest F1 score:",f1_score(y_test,y_pred))    print("Random Forrest auc:",roc_auc_score(y_test,y_pred))        explainer = shap.KernelExplainer(model.predict, X_train)    shap_values= explainer.shap_values(X_test)    shap.summary_plot(shap_values, X_test)         # 1: Headachedef s1(df):          cols = [x for x in df.columns if x != 's1_better']     X = df[cols]     y = df['s1_better']     #create dummies     X = pd.get_dummies(X,drop_first=True)               X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)     # d_train = lgb.Dataset(X_train, label=y_train)     # d_test = lgb.Dataset(X_test, label=y_test)          # Train classifier     model = DecisionTreeClassifier(random_state= 42,                                    max_depth=15,                                    min_samples_leaf=9,                                    min_samples_split= 2,                                    class_weight="balanced")          model.fit(X_train,y_train)     y_pred = model.predict(X_test)     pickle.dump(model, open('./trained_models/s1_model.pkl', 'wb'))          print("accuracy:",accuracy_score(y_test,y_pred))     print("F1 score:",f1_score(y_test,y_pred))     print("auc:",roc_auc_score(y_test,y_pred))          explainer = shap.KernelExplainer(model.predict, X_train)     shap_values= explainer.shap_values(X_test)     shap.summary_plot(shap_values, X_test)        # 3: Tiredness or fatiguedef s3(df):          cols = [x for x in df.columns if x != 's3_better']     X = df[cols]     y = df['s3_better']     #create dummies     X = pd.get_dummies(X,drop_first=True)     X = norm(X)          X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)          # Train classifier     model = GaussianNB(priors=None,                         var_smoothing=5.336699231206313e-07)     model.fit(X_train,y_train)     y_pred = model.predict(X_test)     pickle.dump(model, open('./trained_models/s3_model.pkl', 'wb'))          print("Accuracy:",accuracy_score(y_test,y_pred))     print("F1 score:",f1_score(y_test,y_pred))     print("AUC:",roc_auc_score(y_test,y_pred))          explainer = shap.KernelExplainer(model.predict, X_train)     shap_values= explainer.shap_values(X_test)     shap.summary_plot(shap_values, X_test)             # 7:  Difficult to concentratedef s7(df):        cols = [x for x in df.columns if x != 's7_better']    X = df[cols]    y = df['s7_better']    #create dummies    X = pd.get_dummies(X,drop_first=True)            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)    # d_train = lgb.Dataset(X_train, label=y_train)    # d_test = lgb.Dataset(X_test, label=y_test)        # Train random forrest classifier    model = RandomForestClassifier(random_state= 42,                                         max_depth = 2,                                          min_samples_leaf = 8,                                         min_samples_split= 2,                                         n_estimators=100,                                         class_weight="balanced_subsample")        model.fit(X_train,y_train)    y_pred = model.predict(X_test)    pickle.dump(model, open('./trained_models/s7_model.pkl', 'wb'))        print("Random Forest accuracy:",accuracy_score(y_test,y_pred))    print("Random Forest F1 score:",f1_score(y_test,y_pred))    print("Random Forrest auc:",roc_auc_score(y_test,y_pred))        explainer = shap.KernelExplainer(model.predict, X_train)    shap_values= explainer.shap_values(X_test)    shap.summary_plot(shap_values, X_test)                           # perforamnce prediction and visualizationdef performance_model(df,input_row):        cols = [x for x in df.columns if x != 'performanceOverall']    X = df[cols]    y = df['performanceOverall']    #create dummies    X = pd.get_dummies(X,drop_first=True)            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)    # d_train = lgb.Dataset(X_train, label=y_train)    # d_test = lgb.Dataset(X_test, label=y_test)        # Calculate Shap values    choosen_instance = X.iloc[[input_row]]        model = pickle.load(open('./trained_models/performance_model.pkl', 'rb'))    y_pred = model.predict(choosen_instance)    print("Performance prediction: ", y_pred)        # Create an object that can calculate shap values    # explainer = shap.Explainer(model, X_test)    explainer = shap.TreeExplainer(model)        shap_values = explainer.shap_values(choosen_instance)        shap.initjs()    shap.force_plot(explainer.expected_value[1], shap_values[1], choosen_instance,                    link = "logit",                     matplotlib = True)                def indoorClimate_model(df,input_row):    #https://analyticsindiamag.com/a-complete-guide-to-shap-shapley-additive-explanations-for-practitioners/    cols = [x for x in df.columns if x != 'indoorClimate']    X = df[cols]    y = df['indoorClimate']    #create dummies    X = pd.get_dummies(X,drop_first=True)            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)        # Calculate Shap values    choosen_instance = X.iloc[[input_row]]    # load the model from disk    model = joblib.load('./trained_models/indoorClimate_model.sav')    #model = pickle.load(open('./trained_models/indoorClimate_model.pkl', 'rb'))    y_pred = model.predict(X)    print("Indoor Climate prediction: ", y_pred)        # Create an object that can calculate shap values    # explainer = shap.Explainer(model, X_test)    #explainer = shap.Explainer(model.predict, X_test)    # explainer = shap.Explainer(model, X_train)    # # # Calculate Shap values    # #shap_values = explainer.shap_values(X.iloc[input_row])    # shap_values = explainer.shap_values(choosen_instance)            # explainer = shap.KernelExplainer(model.predict_proba, X_train)    # shap_values = explainer.shap_values(choosen_instance)            # shap.initjs()    # shap.force_plot(explainer.expected_value[1], shap_values[1], choosen_instance, matplotlib = True)    # shap.initjs()                def symptoms_model(df,input_row):        cols = [x for x in df.columns if x != 'SBS2']    X = df[cols]    y = df['SBS2']    #create dummies    X = pd.get_dummies(X,drop_first=True)            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)    # d_train = lgb.Dataset(X_train, label=y_train)    # d_test = lgb.Dataset(X_test, label=y_test)        # Calculate Shap values    choosen_instance = X.iloc[[input_row]]        model = pickle.load(open('./trained_models/symptoms_model.pkl', 'rb'))    y_pred = model.predict(choosen_instance)    print("Symptoms prediction: ", y_pred)        # Create an object that can calculate shap values    # explainer = shap.Explainer(model, X_test)    explainer = shap.TreeExplainer(model)        # # Calculate Shap values    #shap_values = explainer.shap_values(X.iloc[input_row])    shap_values = explainer.shap_values(choosen_instance)        shap.initjs()    #shap.force_plot(explainer.expected_value[1],shap_values[1],X.iloc[[input_row]])    shap.force_plot(explainer.expected_value[1], shap_values[1], choosen_instance,link = "logit", matplotlib = True)    shap.initjs()        # 0: Dry or irritated eyesdef s0_model(df,input_row):    cols = [x for x in df.columns if x != 's0_better']    X = df[cols]    y = df['s0_better']    #create dummies    X = pd.get_dummies(X,drop_first=True)            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)    # d_train = lgb.Dataset(X_train, label=y_train)    # d_test = lgb.Dataset(X_test, label=y_test)        # Calculate Shap values    choosen_instance = X.iloc[[input_row]]        model = pickle.load(open('./trained_models/s0_model.pkl', 'rb'))    y_pred = model.predict(choosen_instance)    print("Symptom: Dry or irritated eyes prediction: ", y_pred)        # Create an object that can calculate shap values    # explainer = shap.Explainer(model, X_test)    explainer = shap.TreeExplainer(model)        # # Calculate Shap values    #shap_values = explainer.shap_values(X.iloc[input_row])    shap_values = explainer.shap_values(choosen_instance)        shap.initjs()    shap.force_plot(explainer.expected_value[1], shap_values[1], choosen_instance, matplotlib = True) # 1: Headachedef s1_model(df,input_row):          cols = [x for x in df.columns if x != 's1_better']     X = df[cols]     y = df['s1_better']     #create dummies     X = pd.get_dummies(X,drop_first=True)          choosen_instance = X.iloc[[input_row]]         model = pickle.load(open('./trained_models/s1_model.pkl', 'rb'))     y_pred = model.predict(choosen_instance)     print("Symptom: Headache: ", y_pred)        # Create an object that can calculate shap values    # explainer = shap.Explainer(model, X_test)     explainer = shap.TreeExplainer(model)        # # Calculate Shap values    #shap_values = explainer.shap_values(X.iloc[input_row])     shap_values = explainer.shap_values(choosen_instance)         shap.initjs()     shap.force_plot(explainer.expected_value[1], shap_values[1], choosen_instance, matplotlib = True) # 3: Tiredness or fatiguedef s3_model(df,input_row):          cols = [x for x in df.columns if x != 's3_better']     X = df[cols]     y = df['s3_better']     #create dummies     X = pd.get_dummies(X,drop_first=True)     X = norm(X)          choosen_instance = X.iloc[[input_row]]         model = pickle.load(open('./trained_models/s3_model.pkl', 'rb'))     y_pred = model.predict(choosen_instance)     print("Symptom: Tiredness or fatigue: ", y_pred)  # 7: Difficult to concentratedef s7_model(df,input_row):    cols = [x for x in df.columns if x != 's7_better']    X = df[cols]    y = df['s7_better']    #create dummies    X = pd.get_dummies(X,drop_first=True)            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)    # d_train = lgb.Dataset(X_train, label=y_train)    # d_test = lgb.Dataset(X_test, label=y_test)        # Calculate Shap values    choosen_instance = X.iloc[[input_row]]        model = pickle.load(open('./trained_models/s7_model.pkl', 'rb'))    y_pred = model.predict(choosen_instance)    print("Symptom: Difficult to concentrate: ", y_pred)        # Create an object that can calculate shap values    # explainer = shap.Explainer(model, X_test)    explainer = shap.TreeExplainer(model)        # # Calculate Shap values    #shap_values = explainer.shap_values(X.iloc[input_row])    shap_values = explainer.shap_values(choosen_instance)        shap.initjs()    shap.force_plot(explainer.expected_value[1], shap_values[1], choosen_instance, matplotlib = True)