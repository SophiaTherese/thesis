#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:07:02 2022

@author: Sophia
"""
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import pandas as pd
import xgboost
import shap
from sklearn.preprocessing import MaxAbsScaler
from sklearn import model_selection
#from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve, auc




#normalize df for KNN and SVC algorithms
def norm(df):
    scaler = MaxAbsScaler()
    scaler.fit(df)
    scaled = scaler.transform(df)
    df_norm = pd.DataFrame(scaled, columns=df.columns)
    
    return df_norm



# Tree-based models:
""" input:  dataframe, target label, list of hyper-parameters
    output: model performance, SHAP summary plot"""
def tree_model(df,label,model):
    
    cols = [x for x in df.columns if x != label]
    X = df[cols]
    y = df[label]

    #create dummies
    X = pd.get_dummies(X,drop_first=True)
    
    # split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    mdl = model
    # Train random forrest classifier
    mdl.fit(X_train,y_train)
    y_pred = mdl.predict(X_test)
    
    # print performance
    print("Accuracy:",accuracy_score(y_test,y_pred))
    print("F1 score:",f1_score(y_test,y_pred))
    print("AUC:",roc_auc_score(y_test,y_pred))
    
    #SHAP summary plot
    explainer = shap.KernelExplainer(mdl.predict, X_train)
    shap_values= explainer.shap_values(X_test)
    shap.summary_plot(shap_values, X_test)
    
    
# XGB model: 
""" input:  dataframe, target label, list of hyper-parameters
    output: model performance, SHAP summary plot"""
def xgboost_classifier(df,label,param_dist):
    
    cols = [x for x in df.columns if x != label]
    
    X_t = df[cols]
    #create dummies
    X_t = pd.get_dummies(X_t,drop_first=True)
   # X_t = norm(X_t)
    y = df[label]
    
    X_train, X_test, y_train, y_test = train_test_split(X_t, y, test_size = 0.2, random_state = 42)
    
    
    
    xgb_model = xgb.XGBClassifier(**param_dist)
    
    
    
    model = xgb_model.fit(X_train,y_train)
    y_pred = xgb_model.predict(X_test)
    
    explainer = shap.TreeExplainer(xgb_model)
    shap_values = explainer.shap_values(X_train)
    shap_values_test = explainer.shap_values(X_test)
    shap.summary_plot(shap_values_test,X_test, show = False)
    plt.show()
    # plt.savefig("output_data/shap/shap_summary.png")
    # plt.show()
    # plt.close()
    
    #SHAP explainer values (NumPy array)
    explainer = shap.TreeExplainer(xgb_model)
    shap_values = explainer.shap_values(X_test)
    #The SHAP *force* plot itself (using this method, I think you can 
    #also do Beeswarm plots but I have not tried it)
    #shap_plot = shap.force_plot(explainer.expected_value, 
    #shap_values[-1:], features=X_test.iloc[-1:], 
    #feature_names=X_test.columns[0:20],
    #matplotlib=True, show=False, plot_cmap=['#77dd77', '#f99191'])
    
    
    print("XGBoost accuracy:",accuracy_score(y_test,y_pred))
    print("XGBoost F1:",f1_score(y_test,y_pred))
    print("XGBoost auc:",roc_auc_score(y_test,y_pred))
    
    # df_feat_imps = pd.DataFrame()
    # sorted_idx = xgb_model.feature_importances_.argsort()
    
    # df_feat_imps["features"] = X_test.columns[sorted_idx]
    
    # fig = xgb.plot_importance(xgb_model, max_num_features = 50)
    # plt.xlabel("XGBoost Feature Importance")
    # plt.savefig("output_data/shap/feature_importance.png")
    # plt.show()
    # plt.close()

    
# models where input needs to be normalized
""" input:  dataframe, target label, list of hyper-parameters
    output: model performance, SHAP summary plot """    
def norm_models(df,label,model):
    
    cols = [x for x in df.columns if x != label]
    X = df[cols]
    y = df[label]
    
    #create dummies
    X = pd.get_dummies(X,drop_first=True)
    X = norm(X)
    
    # split into training and testing set: 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    
    # Train random forrest classifier
    model.fit(X_train,y_train)
    
    #make predictions:
    y_pred = model.predict(X_test)
    
    #print performance
    print("accuracy:",accuracy_score(y_test,y_pred))
    print("F1 score:",f1_score(y_test,y_pred))
    print("auc:",roc_auc_score(y_test,y_pred))
    
    #print SHAP summary plots
    explainer = shap.KernelExplainer(model.predict, X_train)
    shap_values = explainer.shap_values(X_test)
    shap.summary_plot(shap_values, X_test)







""" input:  dataframe, target label, 
    output: box plots of perormance, and printed mean and STD of performance """   

def compare_mlAlg(df,label):
    cols = [x for x in df.columns if x != label]
    X = df[cols]
    
    #create dummies
    X = pd.get_dummies(X,drop_first=False)
    
    # normalize 
    X = norm(X)
    
    y = df[label]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    
    seed = 42
    
    kfold = model_selection.KFold(n_splits=5,shuffle=True, random_state=seed)

    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('KNN', KNeighborsClassifier()))

    models.append(('GNB', GaussianNB()))
    models.append(('SVM', SVC(kernel='linear', probability=True)))

    models.append(('DT', DecisionTreeClassifier()))
    models.append(('rFor', RandomForestClassifier()))
    models.append(('xgB', xgb.XGBClassifier()))

    #models.append(('ANN', MLPClassifier()))

    results = []
    results_f1 = []
    results_auc = []
    names = []
    for name, model in models:
        kfold = model_selection.KFold(n_splits=5,shuffle=True, random_state=seed)
        cv_results = model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy' )
        cv_results_f1 = model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring='f1')
        cv_results_auc = model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring='roc_auc')
        results.append(cv_results)
        results_f1.append(cv_results_f1)
        results_auc.append(cv_results_auc)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        msg_f1 = "%s: %f (%f)" % (name, cv_results_f1.mean(), cv_results_f1.std())
        msg_auc = "%s: %f (%f)" % (name, cv_results_auc.mean(), cv_results_auc.std())
        print("Accuracy:",msg)
        print("F1 score:",msg_f1)
        print("AUC:",msg_auc)

        
    fig = plt.figure(figsize=(5,5))
    fig.suptitle('Accuracy')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()

    fig = plt.figure(figsize=(5,5))
    fig.suptitle('F1 scores')
    ax = fig.add_subplot(111)
    plt.boxplot(results_f1)
    ax.set_xticklabels(names)
    plt.show()

    fig = plt.figure(figsize=(5,5))
    fig.suptitle('AUC scores')
    ax = fig.add_subplot(111)
    plt.boxplot(results_auc)
    ax.set_xticklabels(names)
    plt.show()



    


""" input:  dataframe, target label, 
    output: ROC curve for different models"""   
def roc_curve_models(df,label):
    cols = [x for x in df.columns if x != label]
    X = df[cols]
    
    #create dummies
    X = pd.get_dummies(X)
    
    # normalize 
    X = norm(X)
    
    y = df[label]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    
    clf1 = LogisticRegression(solver='lbfgs', max_iter=100)

    clf2 = KNeighborsClassifier()
    
    clf3 = GaussianNB()

    clf4 = SVC(kernel='linear', probability=True)

    clf5 = DecisionTreeClassifier()
    clf6 = RandomForestClassifier()
    clf7 = xgb.XGBClassifier()
    
    #clf8 = MLPClassifier()

    models = []



    probas1_ = clf1.fit(X_train, y_train).predict_proba(X_test)
    y_pred1 = clf1.predict(X_test)

    probas2_ = clf2.fit(X_train, y_train).predict_proba(X_test)
    y_pred2 = clf2.predict(X_test)

    probas3_ = clf3.fit(X_train, y_train).predict_proba(X_test)
    y_pred3 = clf3.predict(X_test)

    probas4_ = clf4.fit(X_train, y_train).predict_proba(X_test)
    y_pred4 = clf4.predict(X_test)

    probas5_ = clf5.fit(X_train, y_train).predict_proba(X_test)
    y_pred5 = clf5.predict(X_test)

    probas6_ = clf6.fit(X_train, y_train).predict_proba(X_test)
    y_pred6 = clf6.predict(X_test)
    
    probas7_ = clf7.fit(X_train, y_train).predict_proba(X_test)
    y_pred7 = clf7.predict(X_test)
    
    # probas8_ = clf8.fit(X_train, y_train).predict_proba(X_test)
    # y_pred8 = clf8.predict(X_test)

    fp1, tp1, thresholds1 = roc_curve(y_test, probas1_[:, 1])
    roc_auc_model1 = auc(fp1, tp1)

    fp2, tp2, thresholds2 = roc_curve(y_test, probas2_[:, 1])
    roc_auc_model2 = auc(fp2, tp2)

    fp3, tp3, thresholds3 = roc_curve(y_test, probas3_[:, 1])
    roc_auc_model3 = auc(fp3, tp3)

    fp4, tp4, thresholds4 = roc_curve(y_test, probas4_[:, 1])
    roc_auc_model4 = auc(fp4, tp4)

    fp5, tp5, thresholds5 = roc_curve(y_test, probas5_[:, 1])
    roc_auc_model5 = auc(fp5, tp5)
    
    fp6, tp6, thresholds6 = roc_curve(y_test, probas6_[:, 1])
    roc_auc_model6 = auc(fp6, tp6)
    
    fp7, tp7, thresholds6 = roc_curve(y_test, probas7_[:, 1])
    roc_auc_model7 = auc(fp7, tp7)


    plt.figure(figsize=(12, 7))
    plt.clf()

    plt.plot(fp1, tp1, label='Logistic Model (area = %0.2f)' % roc_auc_model1)
    plt.plot(fp2, tp2, label='KNN Model (area = %0.2f)' % roc_auc_model2)
    plt.plot(fp3, tp3, label='GaussianNB Model (area = %0.2f)' % roc_auc_model3)
    plt.plot(fp4, tp4, label='SVC Model (area = %0.2f)' % roc_auc_model4)
    plt.plot(fp5, tp5, label='Decision Tree Model (area = %0.2f)' % roc_auc_model5)
    plt.plot(fp6, tp6, label='Random Forest Model (area = %0.2f)' % roc_auc_model6)
    plt.plot(fp7, tp7, label='xgBoost Model (area = %0.2f)' % roc_auc_model7)
    # plt.plot(fp8, tp8, label='ANN Model (area = %0.2f)' % roc_auc_model8)
    
    
    plt.plot([0, 1], [0, 1], color='blue', linestyle='--', label='Baseline')

    plt.title('ROC Curve', size=20)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc="lower right")
    plt.show()





# tune xgBoost
""" input:  dataframe, target label, hyper-parameter grid
    output: best hyper-parameters"""   

def tune_xgBoost(df,label,grid):
    cols = [x for x in df.columns if x != label]
    X = df[cols]
    
    #create dummies
    X = pd.get_dummies(X,drop_first=True)
    y = df[label]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    
    param_dist = {"objective": "binary:logistic",
                  'n_estimators': 100,
                  "random_state": 42,
                  "eval_metric":"auc"}
    
    optimal_params = GridSearchCV(estimator = xgb.XGBClassifier(**param_dist, subsanple = 0.5, colsample_bytree = 0.5),
                                  param_grid = grid,
                                  scoring = "roc_auc",
                                  verbose = 2)
    
    
    optimal_params.fit(X_train,y_train, eval_set = [(X_test, y_test)])
    
    print(optimal_params.best_params_)




# tune rf
""" input:  dataframe, target label, hyper-parameter grid
    output: best hyper-parameters"""   
def tune_randomF(df,label,grid):
    cols = [x for x in df.columns if x != label]
    X = df[cols]
    
    #create dummies
    X = pd.get_dummies(X)
    y = df[label]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    

    
    #max_depth = 4, n_estimators = 100, criterion = "gini")
    optimal_params = GridSearchCV(RandomForestClassifier(#random_state= 42,
                                                         #max_depth = 4, 
                                                         #min_samples_leaf = 8,
                                                         #min_samples_split= 10,
                                                         n_estimators=100,
                                                         #max_features= 9,
                                                         #class_weight="balanced_subsample"
                                                         ), 
                                  param_grid = grid,
                                  cv=5,
                                  scoring = "roc_auc",
                                  verbose = 2)
    
    
    optimal_params.fit(X_train,y_train)
    
    print(optimal_params.best_params_)

# tune decision tree
""" input:  dataframe, target label, hyper-parameter grid
    output: best hyper-parameters"""   
def tune_dt(df,label,grid):
    cols = [x for x in df.columns if x != label]
    X = df[cols]
    
    #create dummies
    X = pd.get_dummies(X)
    y = df[label]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    

    
    #max_depth = 4, n_estimators = 100, criterion = "gini")
    optimal_params = GridSearchCV(DecisionTreeClassifier(random_state= 42), 
                                  param_grid = grid,
                                  cv=5,
                                  scoring = "roc_auc",
                                  verbose = 2)
    
    
    optimal_params.fit(X_train,y_train)
    
    print(optimal_params.best_params_)


    
# tune GNB
""" input:  dataframe, target label, hyper-parameter grid
    output: best hyper-parameters"""   
def tune_GNB(df,label,grid):
    cols = [x for x in df.columns if x != label]
    X = df[cols]
    
    #create dummies
    X = pd.get_dummies(X,drop_first=True)
    X = norm(X)
    
    y = df[label]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
 
    
    optimal_params = GridSearchCV(GaussianNB(
                                             priors=None, 
                                             var_smoothing=1e-09), 
                                  param_grid = grid,
                                  cv=5,
                                  scoring = "roc_auc",
                                  verbose = 2)
    
    
    optimal_params.fit(X_train,y_train)
    
    print(optimal_params.best_params_)
    # plot_grid_search(optimal_params)
    # table_grid_search(optimal_params)
    
    
    
# tune SVC
""" input:  dataframe, target label, hyper-parameter grid
    output: best hyper-parameters"""   
def tune_svc(df,label,grid):
    cols = [x for x in df.columns if x != label]
    X = df[cols]
    
    
    #create dummies
    X = pd.get_dummies(X)
    X = norm(X)
    y = df[label]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    

    optimal_params = GridSearchCV(SVC(kernel='rbf', probability=True),
                                  param_grid = grid,
                                  cv=5,
                                  scoring = "roc_auc",
                                  verbose = 2)
    
    
    optimal_params.fit(X_train,y_train)
    
    print(optimal_params.best_params_)
    
    