The final models of the tool are found in “finalModels.py”. When running this document the models are retrained in the first section. In the next section, the use case from the report is seen. This shows how the models are used in order to make a prediction and print a force plot of the diagnosis. It also shows how values in the input can be changed to see how it will influence the prediction. 

The file loads the data frames that are saved in the folder “temp_data”, and the trained models that are saved in the folder “trained_models”. It is therefore not necessary to load the entire program from the beginning. If new data is gathered, and the models are retrained, then it is of course necessary to run through the files from Load to feature selection. In that case the files should be run in the order shown by the numbers below. The files that are not numbered are not saving files to the final model, and therefore do not need to be run to update the final data frame. 

1. Load raw data into python and merge data frames (folder: “load”, function: “load_utils.py”). If downloaded from GitHub, do not run this, as the raw data loaded is not available. 
1.1 Run load_measurements.py
1.2 Run load_questionnaires.py
1.3. Run load_checklists.py
1.4. Run “merge_df” to merge data frames and save the final data frame as a file. 
 

2.   Data cleaning  (folder: “cleaning”, functions: “clean_utils.py”)
2.1 Run “clean_check_num.py”
2.2 Run “rev_1hot.py”
2.3 Run “cat_clean.py”


3.   Feature selection (folder: “feature_selection”, functions: “fs_utils.py”)
3.1 Run predictor_dfs.py
Filter selection correlation-type statistics: 
 - For Chi2 correlation run: “FScat_chi2.py”
 - For Mutual information correlation run: “FScat_MI.py”
 - For ANOVA and Kendall’s Tau run: “fs_num_stat.py”


Model training and evaluation (folder: “ml_alg_test”, functions: “util_ml.py”)
Comparison of different algorithms is seen in “compare_models.py”
The selected models using “model_tuning.py”
Test performance and plot SHAP summary plots of tuned models in “test_tuned_models.py”. 