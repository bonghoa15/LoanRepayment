# Loan Repayment Prediction

This repository hosts a comprehensive **machine learning project** designed to predict the likelihood of successful loan repayment by borrowers.  
Accurate loan repayment prediction is vital for financial institutions to make informed lending decisions, reduce risk, and promote responsible lending practices.

---

## 🚀 Project Goals and Objectives

- Perform **data analysis** on loan status and payment datasets.  
- Develop **predictive models** for loan repayment at different stages of the lending process.  
- Leverage **machine learning techniques** to predict the probability of borrowers successfully repaying their loans.  
- Provide actionable insights for financial institutions to improve lending decisions.

---

## 📊 Data Overview

Datasets used in this project:

1. **loan** – attributes of successful loan applications  
2. **payment** – history of installment payments for loans  
3. **clarity_underwriting_variables** – underwriting performance, mainly leveraging `clarityFraudScore`

**Data Wrangling**:

- Categorize loan statuses into broader groups for modeling.  
- Handle missing values and potential outliers.  
- Perform descriptive statistics to understand variable distributions.

---

## 🔍 Exploratory Data Analysis (EDA)

- Explore relationships between variables.  
- Uncover correlations and visualize trends.  
- Identify potential predictors of loan repayment behavior.  

---

## 🤖 Predictive Modeling

**Modeling Approach**:

- **LightGBM** used for multi-class prediction.  
- Techniques for robust training:  
  - Handle imbalanced classes using **undersampling**  
  - **Stratified K-Fold** for training/validation split  
  - Hyperparameter tuning with **Optuna**

**Model Evaluation**:

- Metrics: **Precision**, **Recall**, **F1-Score**  
- Feature importance analysis using **SHAP**  

**Suggestions for additional features**:

- Debt-to-Income ratio (DTI)  
- Loan purpose  
- Credit score  
- Number of credit inquiries in the last 6 months  

---

## 🧩 Model Versions

Three predictive models designed for different lending stages:

| Version | Stage | Classes | Notes |
|---------|-------|---------|-------|
| **V1** | Loan Application Created | Withdrawn/Cancelled, Repaid, Default | Ignores new/pending loans |
| **V2** | After Underwriting | Withdrawn/Cancelled (after underwriting), Repaid, Default | Balances performance & practicality |
| **V3** | After First Payment | Repaid, Default | Binary classification; withdrawn/cancelled removed |

> Each model is tailored to leverage **more features** as the loan process progresses.

---

## 📈 Conclusions

- **V2 (After Underwriting)** provides the best balance between model performance and practical applicability.  
- Adding more features could improve predictive power.  
- This project demonstrates how **ML models can support automated lending decisions** and help reduce default risks.  

---

## ⚙️ Skills Demonstrated

- Python, Pandas, NumPy for **data wrangling and analysis**  
- LightGBM for **gradient boosting modeling**  
- Optuna for **hyperparameter optimization**  
- SHAP for **explainable AI**  
- Handling **imbalanced datasets** and **multi-stage classification**
