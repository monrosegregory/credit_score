import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
# import pdfkit
import tempfile
import os
from PIL import Image

df_path = os.path.join(os.getcwd(), "ml_logic/df_cleaned_31082024.csv")

# HTML content with centered logo
html_content = """
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #4CAF50; text-align: center; }
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }
    </style>
</head>
</html>
"""

# Logo image
image = Image.open('ml_logic/logo.png')

# Display the HTML content in Streamlit
st.markdown(html_content, unsafe_allow_html=True)

# Streamlit image display
st.image(image, width=80, use_column_width=True)

# App title and description
st.markdown("""
    <h1 style='font-size: 36px; text-align: center;'>Providing data-driven insights for financial institutions</h1>
    <h3 style='text-align: center;'>Enter the customer's data to receive a detailed score classification from our algorithm.</h3>
""", unsafe_allow_html=True)

# Set CSS style for tooltip
tooltip_style = """
    <style>
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
        vertical-align: middle; /* Assure l'alignement vertical */
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px; /* Ajustez la largeur si nécessaire */
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 5px;
        padding: 5px 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Position en dessus du texte */
        left: 50%;
        margin-left: -80px; /* Centrer l'infobulle */
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 12px; /* Taille de police réduite */
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
"""

# Afficher le style CSS
st.markdown(tooltip_style, unsafe_allow_html=True)

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

# Section 1: Personal Information
st.markdown("<h4>Personal Information</h4>", unsafe_allow_html=True)
cols = st.columns(4)

# Customer ID
with cols[0]:
    st.markdown("""<h8><div class="tooltip">👤 Name<span class="tooltiptext">The customer's name.</span></div></h8>""", unsafe_allow_html=True)
    customer_id = st.text_input('', value='AAA_0x1234', label_visibility="collapsed")

# Age
with cols[1]:
    st.markdown("""<h8><div class="tooltip">🧓 Age<span class="tooltiptext">The age of the customer, typically in years.</span></div></h8>""", unsafe_allow_html=True)
    age = st.text_input('', '21', label_visibility="collapsed")
    valid_age, age_value = validate_input(age, int, 0, 100, "Age")

# Occupation
with cols[2]:
    st.markdown("""<h8><div class="tooltip">🧑‍💻 Occupation<span class="tooltiptext">The customer's job or profession.</span></div></h8>""", unsafe_allow_html=True)
    occupation_options = ["Scientist", "Teacher", "Engineer", "Entrepreneur", "Developer", "Lawyer", "Doctor", "Manager", "Musician", "Mechanic"]
    occupation = st.selectbox("", occupation_options, label_visibility="collapsed")

# Month
with cols[3]:
    st.markdown("""<h8><div class="tooltip">📅 Month<span class="tooltiptext">Indicates the month (e.g., January, February) for the corresponding data entry.</span></div></h8>""", unsafe_allow_html=True)
    month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = st.selectbox('', month_options, label_visibility="collapsed")

# Section 2: Financial Details
st.markdown("<h4>Financial Details</h4>", unsafe_allow_html=True)
cols2 = st.columns(4)

# Annual Income
with cols2[0]:
    st.markdown("""<h8><div class="tooltip">💰 Annual Income<span class="tooltiptext">The total yearly income of the customer, typically in their local currency.</span></div></h8>""", unsafe_allow_html=True)
    annual_income = st.text_input('', '30000', label_visibility="collapsed")
    valid_income, annual_income_value = validate_input(annual_income.replace(',', '.'), float, 0, None, "Annual income")

# Number of Bank Accounts
with cols2[1]:
    st.markdown("""<h8><div class="tooltip">🏦 # Bank Accounts<span class="tooltiptext">The number of bank accounts the customer holds.</span></div></h8>""", unsafe_allow_html=True)
    num_bank_accounts = st.text_input('', '3', label_visibility="collapsed")
    valid_bank_accounts, num_bank_accounts_value = validate_input(num_bank_accounts, int, 0, None, "Number of Bank Accounts")

# Number of Credit Cards
with cols2[2]:
    st.markdown("""<h8><div class="tooltip">💳 # Credit Cards<span class="tooltiptext">The number of credit cards the customer possessess.</span></div></h8>""", unsafe_allow_html=True)
    num_credit_cards = st.text_input('', '2', label_visibility="collapsed")
    valid_credit_cards, num_credit_cards_value = validate_input(num_credit_cards, int, 0, None, "Number of Credit Cards")

# Interest Rate
with cols2[3]:
    st.markdown("""<h8><div class="tooltip">📈 % Interest<span class="tooltiptext">The interest rate on the customer's credit cards.</span></div></h8>""", unsafe_allow_html=True)
    interest_rate = st.text_input('', '2.5', label_visibility="collapsed")
    valid_interest_rate, interest_rate_value = validate_input(interest_rate.replace(',', '.'), float, 0, None, "Interest rate")

# Section 3: Credit Information
st.markdown("<h4>Credit Information</h4>", unsafe_allow_html=True)
cols3 = st.columns(4)

# Number of Loans
with cols3[0]:
    st.markdown("""<h8><div class="tooltip">💵 # Loans<span class="tooltiptext">The number of loans the customer has taken.</span></div></h8>""", unsafe_allow_html=True)
    num_loans = st.text_input('', '7', label_visibility="collapsed")
    valid_loans, num_loans_value = validate_input(num_loans, int, 0, None, "Number of Loans")

# Days Delayed
with cols3[1]:
    st.markdown("""<h8><div class="tooltip">⌛ Delay / Due Date<span class="tooltiptext">The average number of days the customer has delayed payments beyond the due date.</span></div></h8>""", unsafe_allow_html=True)
    days_delayed = st.text_input('', '10', label_visibility="collapsed")
    valid_days_delayed, days_delayed_value = validate_input(days_delayed, int, 0, None, "Days delayed")

# Number of Delayed Payments
with cols3[2]:
    st.markdown("""<h8><div class="tooltip">🔄 # Late Payments<span class="tooltiptext">The total number of delayed payments made by the customer.</span></div></h8>""", unsafe_allow_html=True)
    num_delayed_payments = st.text_input('', '11', label_visibility="collapsed")
    valid_delayed_payments, num_delayed_payments_value = validate_input(num_delayed_payments, int, 0, None, "Number of Delayed Payments")

# Changed Credit Limit
with cols3[3]:
    st.markdown("""<h8><div class="tooltip">📊 % Changed Limit<span class="tooltiptext">The percentage change in the credit limit over time.</span></div></h8>""", unsafe_allow_html=True)
    changed_credit_limit = st.text_input('', '3.00', label_visibility="collapsed")
    valid_credit_limit, changed_credit_limit_value = validate_input(changed_credit_limit.replace(',', '.'), float, 0, None, "Changed credit limit")

# Number of Credit Inquiries
with cols3[0]:
    st.markdown("""<h8><div class="tooltip">🔍 # Inquiries<span class="tooltiptext">The number of credit inquiries made by financial institutions on behalf of the customer.</span></div></h8>""", unsafe_allow_html=True)
    num_credit_inquiries = st.text_input('', '13', label_visibility="collapsed")
    valid_credit_inquiries, num_credit_inquiries_value = validate_input(num_credit_inquiries, int, 0, None, "Number of Credit Inquiries")

# Credit Mix
with cols3[1]:
    st.markdown("""<h8><div class="tooltip">💳 Credit Mix<span class="tooltiptext">A classification of the mix of credit types (e.g., credit cards, loans).</span></div></h8>""", unsafe_allow_html=True)
    credit_mix_options = ["Good", "Standard", "Bad"]
    credit_mix = st.selectbox("", credit_mix_options, label_visibility="collapsed")

# Outstanding Debt
with cols3[2]:
    st.markdown("""<h8><div class="tooltip">💰 Unpaid Debt<span class="tooltiptext">The total amount of debt the customer still owes, usually in USD.</span></div></h8>""", unsafe_allow_html=True)
    outstanding_debt = st.text_input('', '502.10', label_visibility="collapsed")
    valid_outstanding_debt, outstanding_debt_value = validate_input(outstanding_debt.replace(',', '.'), float, 0, None, "Outstanding debt")

# Credit Utilization Ratio
with cols3[3]:
    st.markdown("""<h8><div class="tooltip">📈 % Credit Use<span class="tooltiptext">The ratio of credit used by the customer compared to their total credit limit.</span></div></h8>""", unsafe_allow_html=True)
    credit_utilization_ratio = st.text_input('', '20.10', label_visibility="collapsed")
    valid_credit_utilization, credit_utilization_ratio_value = validate_input(credit_utilization_ratio.replace(',', '.'), float, 0, None, "Credit utilization ratio")

# Section 4: Payment Information
st.markdown("<h4>Payment Information</h4>", unsafe_allow_html=True)
cols4 = st.columns(4)

# Credit History Age
with cols4[0]:
    st.markdown("""<h8><div class="tooltip">🕰️ Credit Age Months<span class="tooltiptext">The length of time the customer has had credit accounts.</span></div></h8>""", unsafe_allow_html=True)
    credit_history_age = st.text_input('', '19', label_visibility="collapsed")
    valid_credit_age, credit_history_age_value = validate_input(credit_history_age, int, 0, None, "Credit Age")

# Payment of Min Amount
with cols4[1]:
    st.markdown("""<h8><div class="tooltip">📝 Minimum Payment<span class="tooltiptext">Whether the customer pays only the minimum amount due on their credit card bills.</span></div></h8>""", unsafe_allow_html=True)
    payment_of_min_amount_options = ["Yes", "No"]
    payment_of_min_amount = st.selectbox("", payment_of_min_amount_options, label_visibility="collapsed")

# Total EMI per Month
with cols4[2]:
    st.markdown("""<h8><div class="tooltip">💸 Monthly EMI Total<span class="tooltiptext">The total Equated Monthly Installment (EMI) payments, which refers to the fixed amount a customer pays monthly to repay loans.</span></div></h8>""", unsafe_allow_html=True)
    total_emi_per_month = st.text_input('', '70.47', label_visibility="collapsed")
    valid_total_emi, total_emi_per_month_value = validate_input(total_emi_per_month.replace(',', '.'), float, 0, None, "Total EMI per Month")

# Amount Invested Monthly
with cols4[3]:
    st.markdown("""<h8><div class="tooltip">📊 Monthly Investment<span class="tooltiptext">The amount the customer invests on a monthly basis, usually in USD.</span></div></h8>""", unsafe_allow_html=True)
    amount_invested_monthly = st.text_input('', '162.43', label_visibility="collapsed")
    valid_invested_amount, amount_invested_monthly_value = validate_input(amount_invested_monthly.replace(',', '.'), float, 0, None, "Amount invested monthly")

# Section 5: Behavioral and Balance Information
st.markdown("<h4>Behavioral and Balance Information</h4>", unsafe_allow_html=True)
cols5 = st.columns(4)
cols5 = st.columns([2, 1, 1])

# Payment Behaviour
with cols5[0]:
    st.markdown("""<h8><div class="tooltip">:date: Payment Habits<span class="tooltiptext">This field describes the customer’s typical payment patterns. It includes factors such as how much they spend and the size of payments: whether they make small, medium, or large payments regularly, and whether they tend to spend a lot or a little.</span></div></h8>""", unsafe_allow_html=True)
    payment_behaviour_options = ['High Spent (Small Value)', 'High Spent (Medium Value)', 'High Spent (Large Value)', 'Low Spent (Small Value)', 'Low Spent (Medium Value)', 'Low Spent (Large Value)']
    payment_behaviour_temp = st.selectbox("Select an option:", payment_behaviour_options, label_visibility="collapsed")
    payment_mapping = {
        "High Spent (Small Value)": "HighspentSmallvaluepayments",
        "High Spent (Medium Value)": "HighspentMediumvaluepayments",
        "High Spent (Large Value)": "HighspentLargevaluepayments",
        "Low Spent (Small Value)": "LowspentSmallvaluepayments",
        "Low Spent (Medium Value)": "LowspentMediumvaluepayments",
        "Low Spent (Large Value)": "LowspentLargevaluepayments"
    }
    payment_behaviour = payment_mapping.get(payment_behaviour_temp)

# Monthly Balance
with cols5[1]:
    st.markdown("""<h8><div class="tooltip">💰 Monthly Balance<span class="tooltiptext">The remaining balance the customer has at the end of the month, usually in USD.</span></div></h8>""", unsafe_allow_html=True)
    monthly_balance = st.text_input('', '162.44', label_visibility="collapsed")
    valid_monthly_balance, monthly_balance_value = validate_input(monthly_balance.replace(',', '.'), float, 0, None, "Monthly balance")

# Comment
with cols5[2]:
    st.write("")
    # st.markdown("""<h8><div class="tooltip">📌 Comment<span class="tooltiptext">Please let your comment.</span></div></h8>""", unsafe_allow_html=True)
    # comment = st.text_input('', '', label_visibility="collapsed")

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

#Initialize session page
if 'calculate_score' not in st.session_state:
    st.session_state['calculate_score'] = False


# Section 6: Button
st.markdown("<h4>Credit Score</h4>", unsafe_allow_html=True)
cols6 = st.columns(4)

# Initialize Button to calculate the score based on the input data
if st.button("Calculate Score", type="primary"):
    st.session_state['calculate_score'] = True


# Button to calculate the score based on the input data
if st.session_state['calculate_score'] == True:

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

    results_df = None


    # Sending the request to the API
    response = requests.get(url, params=input_data)

    st.session_state.expander_open = True

    st.markdown("<h4>Credit Score Evaluation Result</h4>", unsafe_allow_html=True)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()  # Fetch the result containing the credit score

        # Displaying the score classification based on the 'Credit_Score' value
        if result["Credit_Score"] == 0:
            st.markdown(
                """
                <div style='background-color: #D4EDDA; padding: 30px; border-radius: 12px; text-align: center; margin-bottom: 20px;'>
                    <h1 style='font-size: 36px; color: #28A745; margin: 0;'>Good Credit Score</h1>
                    <p style='font-size: 18px; color: #155724; margin-top: 10px;'>Cirone & Monrose analysis and recommendation: <br>Lower Risk of Default | Better Loan Terms | Confidence in Borrower</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        elif result["Credit_Score"] == 2:
            st.markdown(
                """
                <div style='background-color: #FFECB3; padding: 30px; border-radius: 12px; text-align: center; margin-bottom: 20px;'>
                    <h1 style='font-size: 36px; color: #FF8C00; margin: 0;'>Standard Credit Score</h1>
                    <p style='font-size: 18px; color: #FF8C00; margin-top: 10px;'>Cirone & Monrose analysis and recommendation: <br> Moderate Risk | Competitive Loan Terms | Financial Stability</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div style='background-color: #F8D7DA; padding: 30px; border-radius: 12px; text-align: center; margin-bottom: 20px;'>
                    <h1 style='font-size: 36px; color: #DC3545; margin: 0;'>Bad Credit Score</h1>
                    <p style='font-size: 18px; color: #DC3545; margin-top: 10px;'>Cirone & Monrose analysis and recommendation: <br> Higher Risk of Default | Stricter Loan Terms | Increased Scrutiny</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Displaying the probability of the score classification

        st.markdown("<h4>Probability of the Score Class</h4>", unsafe_allow_html=True)

        # Storing the probability
        proba = result.get('Prob', 0)  # Ensure proba is a number between 0 and 1

        # Store the result and probability in session state
        st.session_state.result = result
        st.session_state.proba = proba

        # If the probability is available, display a dynamic progress bar
        if proba is not None:
            percentage = int(proba * 100)  # Convert the probability into a percentage

            # HTML/CSS for the progress bar
            progress_bar_html = f"""
            <div style="width: 100%; background-color: #e0e0e0; border-radius: 20px;">
                <div style="width: {percentage}%;background-color: gray; height: 30px; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 500;">
                    {percentage}%
                </div>
            </div>
            """

            # Render the progress bar in the app
            st.markdown(progress_bar_html, unsafe_allow_html=True)

        else:
            st.warning("Result data is not available. Please run the calculation or check your inputs.")

        # Load the dataset
        persona = pd.read_csv(df_path)

        # Filter the DataFrame to include only rows with 'Credit_Score' as 'Good'
        persona_good = persona[persona['Credit_Score'] == 'Good']

        # Filter the DataFrame to include only rows with 'Credit_Score' as 'Standard'
        persona_standard = persona[persona['Credit_Score'] == 'Standard']

        # Filter the DataFrame to include only rows with 'Credit_Score' as 'Poor'
        persona_poor = persona[persona['Credit_Score'] == 'Poor']


        # Define persona_good_list
        persona_good_list = [
            "Good",
            round(persona_good['Age'].mean()),
            persona_good['Occupation'].mode()[0],
            round(persona_good['Annual_Income'].mean()),
            round(persona_good['Num_Bank_Accounts'].mean()),
            round(persona_good['Num_Credit_Card'].mean()),
            round(persona_good['Interest_Rate'].mean()),
            round(persona_good['Num_of_Loan'].mean()),
            round(persona_good['Delay_from_due_date'].mean()),
            round(persona_good['Num_of_Delayed_Payment'].mean()),
            round(persona_good['Changed_Credit_Limit'].mean()),
            round(persona_good['Num_Credit_Inquiries'].mean()),
            persona_good['Credit_Mix'].mode()[0],
            round(persona_good['Outstanding_Debt'].mean()),
            round(persona_good['Credit_Utilization_Ratio'].mean()),
            round(persona_good['Credit_History_Age_Months'].mean()),
            persona_good['Payment_of_Min_Amount'].mode()[0],
            round(persona_good['Total_EMI_per_month'].mean()),
            round(persona_good['Amount_invested_monthly'].mean()),
            persona_good['Payment_Behaviour'].mode()[0],
            round(persona_good['Monthly_Balance'].mean()),
            persona_good['Credit_Score'].mode()[0]
            ]

        # Define persona_standard_list
        persona_standard_list = [
            "Standard",
            round(persona_standard['Age'].mean()),
            persona_standard['Occupation'].mode()[0],
            round(persona_standard['Annual_Income'].mean()),
            round(persona_standard['Num_Bank_Accounts'].mean()),
            round(persona_standard['Num_Credit_Card'].mean()),
            round(persona_standard['Interest_Rate'].mean()),
            round(persona_standard['Num_of_Loan'].mean()),
            round(persona_standard['Delay_from_due_date'].mean()),
            round(persona_standard['Num_of_Delayed_Payment'].mean()),
            round(persona_standard['Changed_Credit_Limit'].mean()),
            round(persona_standard['Num_Credit_Inquiries'].mean()),
            persona_standard['Credit_Mix'].mode()[0],
            round(persona_standard['Outstanding_Debt'].mean()),
            round(persona_standard['Credit_Utilization_Ratio'].mean()),
            round(persona_standard['Credit_History_Age_Months'].mean()),
            persona_standard['Payment_of_Min_Amount'].mode()[0],
            round(persona_standard['Total_EMI_per_month'].mean()),
            round(persona_standard['Amount_invested_monthly'].mean()),
            persona_standard['Payment_Behaviour'].mode()[0],
            round(persona_standard['Monthly_Balance'].mean()),
            persona_standard['Credit_Score'].mode()[0]
            ]

        # Define persona_poor_list
        persona_poor_list = [
            "Bad",
            round(persona_poor['Age'].mean()),
            persona_poor['Occupation'].mode()[0],
            round(persona_poor['Annual_Income'].mean()),
            round(persona_poor['Num_Bank_Accounts'].mean()),
            round(persona_poor['Num_Credit_Card'].mean()),
            round(persona_poor['Interest_Rate'].mean()),
            round(persona_poor['Num_of_Loan'].mean()),
            round(persona_poor['Delay_from_due_date'].mean()),
            round(persona_poor['Num_of_Delayed_Payment'].mean()),
            round(persona_poor['Changed_Credit_Limit'].mean()),
            round(persona_poor['Num_Credit_Inquiries'].mean()),
            persona_poor['Credit_Mix'].mode()[0],
            round(persona_poor['Outstanding_Debt'].mean()),
            round(persona_poor['Credit_Utilization_Ratio'].mean()),
            round(persona_poor['Credit_History_Age_Months'].mean()),
            persona_poor['Payment_of_Min_Amount'].mode()[0],
            round(persona_poor['Total_EMI_per_month'].mean()),
            round(persona_poor['Amount_invested_monthly'].mean()),
            persona_poor['Payment_Behaviour'].mode()[0],
            round(persona_poor['Monthly_Balance'].mean()),
            "Bad",
            ]

        # Display detailed results in a compact table
        results_df = pd.DataFrame({
            "Feature": [
                "Customer ID", "Age", "Occupation", "Annual Income",
                "Number of Bank Accounts", "Number of Credit Cards", "Interest Rate",
                "Number of Loans", "Days Delayed", "Number of Delayed Payments",
                "Changed Credit Limit", "Number of Credit Inquiries", "Credit Mix",
                "Outstanding Debt", "Credit Utilization Ratio", "Credit History Age",
                "Payment of Min Amount", "Total EMI per Month", "Amount Invested Monthly",
                "Payment Behaviour", "Monthly Balance", "Credit Score"
            ],
            "Current Value": [
                customer_id, age_value, occupation, annual_income_value,
                num_bank_accounts_value, num_credit_cards_value, interest_rate_value,
                num_loans_value, days_delayed_value, num_delayed_payments_value,
                changed_credit_limit_value, num_credit_inquiries_value, credit_mix,
                outstanding_debt_value, credit_utilization_ratio_value, credit_history_age,
                payment_of_min_amount, total_emi_per_month_value, amount_invested_monthly_value,
                payment_behaviour, monthly_balance_value,
                'Good' if result.get('Credit_Score') == 0 else 'Standard' if result.get('Credit_Score') == 2 else 'Bad'
            ],
            # "Persona": persona_list,
            "Persona Good": persona_good_list,
            "Persona Standard": persona_standard_list,
            "Persona Bad": persona_poor_list
        })


        st.markdown("""<h4><div class="tooltip">Comparative Analysis of Results<span class="tooltiptext">The comparative analysis evaluates the Credit Score against Good, Standard, and Bad Persona benchmarks to highlight areas for improvement.</span></div></h4>""", unsafe_allow_html=True)

        st.dataframe(results_df, width=1200, height=800, hide_index=True,)  # Remove index column

        # List of available features
        available_features = [
            "Age", "Annual Income",
            "Number of Bank Accounts", "Number of Credit Cards", "Interest Rate",
            "Number of Loans", "Days Delayed", "Number of Delayed Payments",
            "Changed Credit Limit", "Number of Credit Inquiries",
            "Outstanding Debt", "Credit Utilization Ratio", "Credit History Age",
            "Total EMI per Month", "Amount Invested Monthly",
            "Monthly Balance"
        ]

        # User selects features from the list
        selected_features = st.multiselect(
            "Select features to visualize:",
            options=available_features,
            default=[
                "Number of Bank Accounts", "Number of Credit Cards", "Interest Rate"
            ]
        )

        # Filter the DataFrame based on selected features
        results_df_filtered = results_df[results_df['Feature'].isin(selected_features)]

        # Reshape the DataFrame for Plotly (melt)
        results_melted = results_df_filtered.melt(id_vars='Feature', var_name='Persona', value_name='Value')

        # Create a scatter plot
        fig = px.scatter(
            results_melted,
            x='Feature',
            y='Value',
            color='Persona',
            title='Graph of Results by Feature and Persona',
            labels={'Feature': 'Features', 'Value': 'Values'},
            color_discrete_map={
                'Current Value': 'gray',
                'Persona Good': 'green',
                'Persona Standard': 'orange',
                'Persona Bad': 'red'
            }
        )

        # Modify marker size
        fig.update_traces(marker=dict(size=10))  # Increase the size of the points to 10

        fig.update_layout(
                            title_font=dict(size=24, color='gray'),  # Title
                            xaxis_title_font=dict(size=18, color='gray'),  # X axis title
                            yaxis_title_font=dict(size=18, color='gray'),  # Y axis title
                            legend_title_font=dict(size=16, color='gray'),  # Legend title
                            legend_font=dict(size=14, color='gray'),  # legend text

                            xaxis=dict(
                                linecolor='gray',  # X line
                                gridcolor='lightgray',   # X Gridline
                                tickfont=dict(color='gray')  # X ticks
                            ),
                            yaxis=dict(
                                linecolor='gray',  # Y line
                                gridcolor='lightgray',   # Y Gridline
                                tickfont=dict(color='gray')  # Y ticks
                            ),
                            plot_bgcolor='whitesmoke'  # Background
                        )


        # Display the scatter plot in Streamlit
        st.plotly_chart(fig)
