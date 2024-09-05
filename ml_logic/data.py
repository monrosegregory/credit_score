import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import pickle


# def load_data(id, customer_id, month, name, age, ssn, occupation, annual_income,
#                monthly_inhand_salary, num_bank_accounts, num_credit_card,
#                interest_rate, num_of_loan, type_of_loan, delay_from_due_date,
#                num_of_delayed_payment, changed_credit_limit, num_credit_inquiries,
#                credit_mix, outstanding_debt, credit_utilization_ratio,
#                credit_history_age, payment_of_min_amount, total_emi_per_month,
#                amount_invested_monthly, payment_behaviour, monthly_balance):




def load_data( customer_id, month, age, occupation, annual_income,
               num_bank_accounts, num_credit_card,
               interest_rate, num_of_loan, delay_from_due_date,
               num_of_delayed_payment, changed_credit_limit, num_credit_inquiries,
               credit_mix, outstanding_debt, credit_utilization_ratio,
               credit_history_age, payment_of_min_amount, total_emi_per_month,
               amount_invested_monthly, payment_behaviour, monthly_balance):

    ###QUAIS LIMITANTES PARA LOAD MODEL?
    if not (0 <= age <= 100):
        raise ValueError(f"Age {age} out of permited (0-100).")


    data = {
        'Customer_ID': [customer_id],
        'Month': [month],
        'Age': [age],
        'Occupation': [occupation],
        'Annual_Income':[annual_income],
        'Num_Bank_Accounts':[num_bank_accounts],
        'Num_Credit_Card':[num_credit_card],
        'Interest_Rate':[interest_rate],
        'Num_of_Loan':[num_of_loan],
        'Delay_from_due_date':[delay_from_due_date],
        'Num_of_Delayed_Payment':[num_of_delayed_payment],
        'Changed_Credit_Limit':[changed_credit_limit],
        'Num_Credit_Inquiries':[num_credit_inquiries],
        'Credit_Mix':[credit_mix],
        'Outstanding_Debt':[outstanding_debt],
        'Credit_Utilization_Ratio':[credit_utilization_ratio],
        'Credit_History_Age':[credit_history_age],
        'Payment_of_Min_Amount':[payment_of_min_amount],
        'Total_EMI_per_month':[total_emi_per_month],
        'Amount_invested_monthly':[amount_invested_monthly],
        'Payment_Behaviour':[payment_behaviour],
        'Monthly_Balance':[monthly_balance],
    }

    df = pd.DataFrame(data)

    return df


########### FUNCAO DE TRATAMENTO ############

def cronological(df: pd.DataFrame):
    months_in_year = 12
    dic_date = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    df['Month'] = df['Month'].map(dic_date)

    df["sin_Month"] = np.sin(2*np.pi*df[["Month"]] / months_in_year)
    df["cos_Month"] = np.cos(2*np.pi*df[["Month"]] / months_in_year)

    # Extract years and months from 'Credit_History_Age' column
    df['Credit_History_Years'] = df['Credit_History_Age'].str.extract(r'(\d+)\s*Years?').astype(float)
    df['Credit_History_Months'] = df['Credit_History_Age'].str.extract(r'(\d+)\s*Months?').astype(float)

    # Handle missing or NaN values
    df['Credit_History_Years'] = df['Credit_History_Years'].fillna(0)
    df['Credit_History_Months'] = df['Credit_History_Months'].fillna(0)

    # Convert years to months and add with months to get total months
    df['Credit_History_Age_Months'] = (df['Credit_History_Years'] * 12 + df['Credit_History_Months']).astype(int)

    # Drop the intermediate columns used for calculation (optional, if you no longer need them)
    df.drop(columns=['Credit_History_Years', 'Credit_History_Months'], inplace=True)

    # Display counts of unique values in 'Credit_History_Age_Months'
    value_counts = df['Credit_History_Age_Months'].value_counts()

    # Replace 0 with NaN in the 'Credit_History_Age_Months' column
    df['Credit_History_Age_Months'] = df['Credit_History_Age_Months'].replace(0, np.nan)

    # Group by 'Customer_ID' and calculate the mean for 'Credit_History_Age_Months' within each group
    mean_by_Customer_ID = df.groupby('Customer_ID')['Credit_History_Age_Months'].transform(lambda x: x.mean())

    # Fill NaN values in 'Credit_History_Age' with the mean for each group
    df['Credit_History_Age_Months'] = df['Credit_History_Age_Months'].fillna(mean_by_Customer_ID)

    df.drop(columns=['Credit_History_Age', 'Month'], inplace=True)

    #print("Cronological features: DONE ✅")
    return df



########## ONDE CARREGA LOAD MODEL? DENTRO DO FAST API

def load_pipe(filepath):
    """Load the pipe from a file using joblib."""
    return joblib.load(filepath)


##########



def preproc(df, pipe):
    """Preproc the data"""

    # Edit data with cronological funtion
    df = cronological(df)

    # Normalize and encode the 'already fitted' pipe
    df = pipe.transform(df)

    return df
