**This repository hosts a comprehensive machine learning project designed to predict the likelihood of successful loan repayment by borrowers**

# Project Goals and Objectives
=============================================================================================

* Data analysis: Loan status & exploration Dataset of payment & underwriting 
* Develop predictive model loan status in different lending process stages

This project aims to leverage machine learning techniques to predict the probability of borrowers successfully repaying their loans. Accurate loan repayment prediction is vital for financial institutions to make informed lending decisions, reduce risks and promote responsible lending practices. 

## Data analysis & Conclusion
----------------------------------------------------------------------------------------------

In this project, I leverage datasets: 
* loan : which includes attributes of succesfful loan application
* payment: history of installment payment of loans
* clarity_underwriting_variables: performance of underwriting each loan application. Mostly leverage clarityFraudScore. 

Data wrangling: categorize loan status to bigger group <br\ >

Descriptive statistics: Checking missing values, potential outliers, perform descriptive statistics to understand the distribution of variables <br\ >

Exploratory Data Analysis (EDA): was conducted to explore relationships between variables, uncover correlations and visualize data trends. This step helped identify potential predictors of loan repayment behavior. <br\ >


## Predictive modelling 
----------------------------------------------------------------------------------------------

Utilize Lightgbm model for multi-class prediction. Techniques using for robusting training process:
* Handle imbalanced class using undersampling technique
* Stratified K-fold to split training, testing & validation
* Take advantage of Optuna for hyper-parameter tuning
* Report model performance: Concentrate on precision, recall, f1-score
* Report feature importance using SHAPELY: feature importance plots for each model reveal significant predictors influencing loan repayment decisions.  
* Suggestion for adding feature into models: debt-to-income (DTI), loan purpose, credit score, The number of inquiries by creditors made on the borrower's credit history in the last 6 months etc.  

Design 3 versions of predictive model.Each model predict in a stage of lending process, that is why it can utilize more features in deeper process. Also the training dataset in each model also adjust:
* V1 - Successfully create application: Ignore the loan application in new loan & pending as well as other status. This loan not finalize the status yet. Label 3 classes: Withdrawn_or_cancel, repayment successfully, or default loan
* V2 - After underwriting: Some Withdrawn/cancel loan application not going to underwriting process then ignore these application. Label 3 classes: Withdrawn_or_cancel (remains after underwriting), repayment successfully, or default loan repayment
* V3 - After 1st payment: Remove withdrawn/cancel loan application. Design model for binary classificatoin: Repayment succesfully or default loan repayment 

## Conclusions
----------------------------------------------------------------------------------------------
Multi-class model version 2 tends to balance between the model performance and practicality. Adding more features might bring stronger predictive power and making it a reliable tool for financial institutions to make well-informed decisions when auto approving loans application. 

