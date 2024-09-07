import streamlit as st
import requests
import pandas as pd

# App title and description
st.markdown("""
    # F&G Data Science & AI Consultant 👨‍💼🧑‍💼📈
    ## - We provide data-driven insights for banks looking to understand their B2C customers.
    ### - Please enter the customer's data, and we will develop our algorithm to deliver a Score Classification (Good, Standard, or Bad).
""")

# GitHub link
st.markdown("[You can check here our Machine Learning code on GitHub](https://github.com/monrosegregory/credit_score)", unsafe_allow_html=True)

### START ###

# Input fields with validation
def validate_input(value, type_func, min_value=None, max_value=None, field_name="Field"):
    """Validate input data and return validity status and converted value."""
    valid = True
    converted_value = None  # Initialize with a default value
    try:
        converted_value = type_func(value)
        if min_value is not None and converted_value < min_value:
            st.error(f"{field_name} must be at least {min_value}.")
            valid = False
        if max_value is not None and converted_value > max_value:
            st.error(f"{field_name} must not exceed {max_value}.")
            valid = False
    except ValueError:
        st.error(f"Invalid input! Please enter a valid {field_name}.")
        valid = False
    return valid, converted_value

# Customer ID
customer_id = st.text_input('Insert Customer ID', 'AAA_0x1234')

# Month
month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = st.selectbox("Select month:", month_options)

# Age
age = st.text_input('Insert Age', '21')
valid_age, age_value = validate_input(age, int, 0, 100, "Age")

# Occupation
occupation_options = ["Scientist", "Teacher", "Engineer", "Entrepreneur", "Developer", "Lawyer", "Media_Manager", "Doctor", "Journalist",
                      "Manager", "Accountant", "Musician", "Mechanic", "Writer", "Architect"]
occupation = st.selectbox("Select occupation:", occupation_options)

# Annual Income
annual_income = st.text_input('Insert Annual Income', '30.000')
valid_income, annual_income_value = validate_input(annual_income.replace(',', '.'), float, 0, None, "Annual income")

# Number of Bank Accounts
num_bank_accounts = st.text_input('Insert Number of Bank Accounts', '2')
valid_bank_accounts, num_bank_accounts_value = validate_input(num_bank_accounts, int, 0, None, "Number of Bank Accounts")

# Number of Credit Cards
num_credit_cards = st.text_input('Number of Credit Cards', '2')
valid_credit_cards, num_credit_cards_value = validate_input(num_credit_cards, int, 0, None, "Number of Credit Cards")

# Interest Rate
interest_rate = st.text_input('Interest rate', '2.5')
valid_interest_rate, interest_rate_value = validate_input(interest_rate.replace(',', '.'), float, 0, None, "Interest rate")

# Number of Loans
num_loans = st.text_input('Number of Loans taken', '2')
valid_loans, num_loans_value = validate_input(num_loans, int, 0, None, "Number of Loans")

# Days Delayed
days_delayed = st.text_input('Days delayed from due date', '2')
valid_days_delayed, days_delayed_value = validate_input(days_delayed, int, 0, None, "Days delayed")

# Number of Delayed Payments
num_delayed_payments = st.text_input('Number of delayed payments', '2')
valid_delayed_payments, num_delayed_payments_value = validate_input(num_delayed_payments, int, 0, None, "Number of Delayed Payments")

# Changed Credit Limit
changed_credit_limit = st.text_input('Changed credit limit', '2.00')
valid_credit_limit, changed_credit_limit_value = validate_input(changed_credit_limit.replace(',', '.'), float, 0, None, "Changed credit limit")

# Number of Credit Inquiries
num_credit_inquiries = st.text_input('Number of credit inquiries', '2')
valid_credit_inquiries, num_credit_inquiries_value = validate_input(num_credit_inquiries, int, 0, None, "Number of Credit Inquiries")

# Credit Mix
credit_mix = st.selectbox("Select Credit Mix:", ["Good", "Standard", "Bad"])

# Outstanding Debt
outstanding_debt = st.text_input('Outstanding debt', '502.10')
valid_outstanding_debt, outstanding_debt_value = validate_input(outstanding_debt.replace(',', '.'), float, 0, None, "Outstanding debt")

# Credit Utilization Ratio
credit_utilization_ratio = st.text_input('Credit utilization ratio', '20.10')
valid_credit_utilization, credit_utilization_ratio_value = validate_input(credit_utilization_ratio.replace(',', '.'), float, 0, None, "Credit utilization ratio")

# Credit History Age
years = st.slider("Credit History Age - Years", 0, 100, 0)
months = st.slider("Credit History Age - Months", 0, 11, 0)
credit_history_age = f"{years} Years and {months} Months"

# Payment of Min Amount
payment_of_min_amount = st.selectbox("Select Payment of Min Amount:", ["Yes", "No"])

# Total EMI per Month
total_emi_per_month = st.text_input('Total EMI per month', '70.47')
valid_total_emi, total_emi_per_month_value = validate_input(total_emi_per_month.replace(',', '.'), float, 0, None, "Total EMI per Month")

# Amount Invested Monthly
amount_invested_monthly = st.text_input('Amount invested monthly', '162.44')
valid_invested_amount, amount_invested_monthly_value = validate_input(amount_invested_monthly.replace(',', '.'), float, 0, None, "Amount invested monthly")

# Payment Behaviour
payment_behaviour = st.selectbox("Select Payment Behaviour:", ['LowspentSmallvaluepayments', 'HighspentMediumvaluepayments', 'LowspentMediumvaluepayments',
                                                                'HighspentLargevaluepayments', 'HighspentSmallvaluepayments', 'LowspentLargevaluepayments'])

# Monthly Balance
monthly_balance = st.text_input('Monthly balance', '162.44')
valid_monthly_balance, monthly_balance_value = validate_input(monthly_balance.replace(',', '.'), float, 0, None, "Monthly balance")

# Collect errors
errors = []
if not valid_age: errors.append("Age")
if not valid_income: errors.append("Annual income")
if not valid_bank_accounts: errors.append("Number of Bank Accounts")
if not valid_credit_cards: errors.append("Number of Credit Cards")
if not valid_interest_rate: errors.append("Interest rate")
if not valid_loans: errors.append("Number of Loans")
if not valid_days_delayed: errors.append("Days delayed")
if not valid_delayed_payments: errors.append("Number of Delayed Payments")
if not valid_credit_limit: errors.append("Changed credit limit")
if not valid_credit_inquiries: errors.append("Number of Credit Inquiries")
if not valid_outstanding_debt: errors.append("Outstanding debt")
if not valid_credit_utilization: errors.append("Credit utilization ratio")
if not valid_total_emi: errors.append("Total EMI per Month")
if not valid_invested_amount: errors.append("Amount invested monthly")
if not valid_monthly_balance: errors.append("Monthly balance")

# Button to calculate the score based on the input data
if st.button("Calculate Score"):
    # Initialize session state to store result and probability
    if 'result' not in st.session_state:
        st.session_state.result = None  # Will store the API response
    if 'proba' not in st.session_state:
        st.session_state.proba = None  # Will store the probability of the score

    # Initialize variables before the button is clicked to avoid 'NameError' on refresh
    url = "https://credit-score-v5-1032836634135.us-west1.run.app/predict"
    result = None  # Initialize result variable
    proba = None  # Initialize probability variable

    # Prepare input data
    input_data = {
        "customer_id": customer_id,
        "month": month,
        "age": age_value,
        "occupation": occupation,
        "annual_income": annual_income_value,
        "num_bank_accounts": num_bank_accounts_value,
        "num_credit_card": num_credit_cards_value,
        "interest_rate": interest_rate_value,
        "num_of_loan": num_loans_value,
        "delay_from_due_date": days_delayed_value,
        "num_of_delayed_payment": num_delayed_payments_value,
        "changed_credit_limit": changed_credit_limit_value,
        "num_credit_inquiries": num_credit_inquiries_value,
        "credit_mix": credit_mix,
        "outstanding_debt": outstanding_debt_value,
        "credit_utilization_ratio": credit_utilization_ratio_value,
        "credit_history_age": credit_history_age,
        "payment_of_min_amount": payment_of_min_amount,
        "total_emi_per_month": total_emi_per_month_value,
        "amount_invested_monthly": amount_invested_monthly_value,
        "payment_behaviour": payment_behaviour,
        "monthly_balance": monthly_balance_value
    }

    # Error handling block
    try:
        # Sending the request to the API
        response = requests.get(url, params=input_data)

        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()  # Fetch the result containing the credit score

            # Displaying the score classification based on the 'Credit_Score' value
            if result.get("Credit_Score") == 0:
                st.markdown(f"<h1 style='font-size: 40px;'>Credit Good 💰✅</h1>", unsafe_allow_html=True)
            elif result.get("Credit_Score") == 2:
                st.markdown(f"<h1 style='font-size: 40px;'>Credit Standard 😐</h1>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h1 style='font-size: 40px;'>Credit Bad ❌</h1>", unsafe_allow_html=True)

            # Displaying the probability of the score classification
            st.markdown(f"<h1 style='font-size: 40px;'>Probability of the Score Class: {result.get('Prob', 0) * 100:.0f}%</h1>", unsafe_allow_html=True)

            # Storing the probability
            proba = result.get('Prob', 0)  # Ensure proba is a number between 0 and 1

            # Store the result and probability in session state
            st.session_state.result = result
            st.session_state.proba = proba

            # If the probability is available, display a dynamic progress bar
            if proba is not None:
                percentage = int(proba * 100)  # Convert the probability into a percentage

                # Assign color based on the percentage range
                if percentage < 50:
                    color = 'red'
                elif 50 <= percentage < 75:
                    color = 'orange'
                else:
                    color = 'green'

                # HTML/CSS for the progress bar with dynamic color
                progress_bar_html = f"""
                <div style="width: 100%; background-color: lightgray; border-radius: 25px;">
                    <div style="width: {percentage}%; background-color: {color}; height: 25px; border-radius: 25px;"></div>
                </div>
                """

                # Render the progress bar in the app
                st.markdown(progress_bar_html, unsafe_allow_html=True)

                # Display the percentage text
                st.text(f"Probability of the Score Class: {percentage}%")
            else:
                st.warning("Result data is not available. Please run the calculation or check your inputs.")

            df_static_values = pd.read_csv('raw_data/df_cleaned_31082024.csv')

            # Define static values
            static_values = [
                "Customer Persona",
                "NS",
                round(df_static_values['Age'].mean()),
                df_static_values['Occupation'].mode()[0],
                round(df_static_values['Annual_Income'].mean()),
                round(df_static_values['Num_Bank_Accounts'].mean()),
                round(df_static_values['Num_Credit_Card'].mean()),
                round(df_static_values['Interest_Rate'].mean()),
                round(df_static_values['Num_of_Loan'].mean()),
                round(df_static_values['Delay_from_due_date'].mean()),
                round(df_static_values['Num_of_Delayed_Payment'].mean()),
                round(df_static_values['Changed_Credit_Limit'].mean()),
                round(df_static_values['Num_Credit_Inquiries'].mean()),
                df_static_values['Credit_Mix'].mode()[0],
                round(df_static_values['Outstanding_Debt'].mean()),
                round(df_static_values['Credit_Utilization_Ratio'].mean()),
                "NS",
                df_static_values['Payment_of_Min_Amount'].mode()[0],
                round(df_static_values['Total_EMI_per_month'].mean()),
                round(df_static_values['Amount_invested_monthly'].mean()),
                df_static_values['Payment_Behaviour'].mode()[0],
                round(df_static_values['Monthly_Balance'].mean()),
                df_static_values['Credit_Score'].mode()[0],
                "NS"
            ]

            # Display detailed results in a compact table
            results_df = pd.DataFrame({
                "Field": [
                    "Customer ID", "Month", "Age", "Occupation", "Annual Income",
                    "Number of Bank Accounts", "Number of Credit Cards", "Interest Rate",
                    "Number of Loans", "Days Delayed", "Number of Delayed Payments",
                    "Changed Credit Limit", "Number of Credit Inquiries", "Credit Mix",
                    "Outstanding Debt", "Credit Utilization Ratio", "Credit History Age",
                    "Payment of Min Amount", "Total EMI per Month", "Amount Invested Monthly",
                    "Payment Behaviour", "Monthly Balance", "Credit Score", "Probability of the Score Class"
                ],
                "Current Value": [
                    customer_id, month, age_value, occupation, annual_income_value,
                    num_bank_accounts_value, num_credit_cards_value, interest_rate_value,
                    num_loans_value, days_delayed_value, num_delayed_payments_value,
                    changed_credit_limit_value, num_credit_inquiries_value, credit_mix,
                    outstanding_debt_value, credit_utilization_ratio_value, credit_history_age,
                    payment_of_min_amount, total_emi_per_month_value, amount_invested_monthly_value,
                    payment_behaviour, monthly_balance_value,
                    'Good' if result.get('Credit_Score') == 0 else 'Standard' if result.get('Credit_Score') == 2 else 'Bad',
                    f"{result.get('Prob', 0) * 100:.0f}%"
                ],
                "Reference": static_values
            })

            # Adding previous results if available
            if 'previous_results' in st.session_state and st.session_state.previous_results:
                previous_results = st.session_state.previous_results
            else:
                previous_results = {field: "N/A" for field in results_df["Field"]}

            results_df["Previous Value"] = results_df["Field"].map(previous_results)

            st.subheader("Detailed Results")
            st.dataframe(results_df, width=1200, hide_index=True)  # Remove index column

            # Update previous results
            st.session_state.previous_results = dict(zip(results_df["Field"], results_df["Current Value"]))

        else:
            st.error(f"API request failed with status code {response.status_code}. Please check your inputs or try again later.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Reset results button
if st.button("Reset Results"):
    # Clear stored values in the session
    st.session_state.result = None
    st.session_state.proba = None
    st.session_state.previous_results = {}
