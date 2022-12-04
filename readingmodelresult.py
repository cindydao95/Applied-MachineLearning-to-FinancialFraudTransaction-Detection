
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


result = pd.read_json("ML_report.json")





macro_f1_validation_fold =  [np.mean(result[i]["macro_f1_folds"]) for i in result]


macro_f1_validation_fold


accuracy_test = result.loc["accuracy_test",:]
macro_f1_test = result.loc["macro_f1_test",:]
recall_score_test = result.loc["recall_score_test",:]
precision_score_test = result.loc["precision_score_test",:]
running_time_mins = result.loc["running_time_(min)",:]
running_time_hous = result.loc["running_time_(hours)",:]


result_df = pd.DataFrame({"model":['Logistic Regression','Random Forest','K-Neighbor'], "macro_f1_validation_fold":macro_f1_validation_fold, "accuracy_test": accuracy_test,
"macro_f1_test":macro_f1_test, "recall_score_test":recall_score_test, "precision_score_test":precision_score_test, "running_time_mins":running_time_mins,"running_time_hous":running_time_hous})


result_df


for column in result_df.columns[1:]:
    plt.bar(result_df["model"],result_df[column])
    plt.title(column)
    plt.show()


