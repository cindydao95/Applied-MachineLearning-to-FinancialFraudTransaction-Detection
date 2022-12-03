# Predict Financial Fraud Transactions for JPMorgan Chase using Machine Learning


## Abstract

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nowadays, with the development of technology, financial organizations are facing a global issue where customers’ credit cards and financial information are stolen frequently. Mark Crichton mentioned in his article “Transaction Fraud, How to Protect your Business & Customers” (2021) that transaction fraud is defined as illegal transactions created from financial information which are stolen or counterfeit. According to the Payments Fraud and Control Survey Report from J.P.Morgan (2021), the percentage of organizations that experienced actual payment fraud from 2014 to 2020 increased from 62% to 74%. Especially, in 2018 and 2019, an estimated 82% and 81% respectively of financial companies confronted this problem; then the number decreased to 74% in 2020 which was explained in the report due to the pandemic, Covid-19. Technology and online retail industries have changed people's shopping behavior from in-person stores to e-commerce which results in potential fraudulent transactions and payments such as “account acquisition, financial information theft, fake chargeback, money laundry, and many more.” (Rao et al., 2021). For example, fraudsters may steal customer’s credit card information which is saved on the website from the previous check-out, or they might hack to get people’s account login to make fraudulent purchase transactions. Transaction fraud detection has been a prominent topic for many researchers to pick and various detecting models and techniques have been developed as well; however, it’s not ending. In this work, well build the machine learning models to predict the financal fraud transactions using JPMorgan Chase

## Step 1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To run our source code, we need the dataset from JPMorgan. Due to confidential issue, we couldn't share the dataset; however, for whom might want to run our source code, the link [here](https://www.jpmorgan.com/synthetic-data/payments-data-for-fraud-detection) is where the data can be requested.

 ## Step 2
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Run the FinancialTransactionFraudDetection.ipynb file

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; It includes the following steps:
* Explore missing values and explain why they exists

* Cleaning data

* (EDA) Exploration data analysis, 

* Feature Engineering

* One-Hot Encoding Transformation, 

* Split dataset into Train and Test datasets

* Write the train and test dataset into .csv files (train_dataset.csv and test_dataset.csv)

## Step 3
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Run the  build_model.ipynb file

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This file includes:

* Read the "train_dataset.csv" and "test_dataset.csv"

* Use SMOTE to Balance the Imbalance dataset "train_dataset.csv" with Upsampling 

* Feature Scaling 

* Run three Machine Learning models (Logistic Regression, Random Forest, and K-Neighbor Classifier)

* Write the performance scores (accuracy, presicion, recall, f1-score) into .json file