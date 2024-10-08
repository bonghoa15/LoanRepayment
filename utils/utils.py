import pandas as pd
import numpy as np
import lightgbm as lgb

def status_categorize(is_collection, status):
    """ 
    Categorize loan status to repayment status
    """
    if is_collection ==1:
        return 'loan_in_default'
    else:
        if status in ['New Loan', 'Pending Application', 'Pending Application Fee']:
            return 'active_loan'
        elif status in ['Paid Off Loan', 'Charged Off Paid Off', 'Settlement Paid Off', 'Settled Bankruptcy']:
            return 'repayment_completed'
        elif status in ['Charged Off','Internal Collection', 'External Collection', 'Pending Rescind', 'Settlement Pending Paid Off']:
            return 'loan_in_default'
        elif status in ['Withdrawn Application', 'Rejected', 'CSR Voided New Loan', 'Customer Voided New Loan', 'Voided New Loan', 'Customver Voided New Loan']:
            return 'withdrawl_or_cancel'
        elif status in ['Pending Paid Off', 'Returned Item', 'Credit Return Void']:
            return 'pending'
        else:
            return 'other'
        
def remove_outliers(df, column):
    """
    Remove outlier to using inter-quartile
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def label_encode(lb):
    if lb == 'repayment_completed':
        return 0
    elif lb =='loan_in_default':
        return 1
    else:
        return 2
    
