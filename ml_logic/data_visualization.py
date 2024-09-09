import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# # Logo
# logo_url = "https://img.freepik.com/fotos-premium/bandeira-nacional-do-brasil-e-franca-background-para-designers_659987-40312.jpg?w=900"  # Substitua pelo URL ou caminho da sua logo
# st.markdown(
#     f"""
#     <style>
#     .logo {{
#         position: absolute;
#         top: 15;
#         left: 15;
#         margin: 0px;
#     }}
#     </style>
#     <div class="logo">
#         <img src="{logo_url}" alt="Company Logo" width="100"/>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# App title and description
# st.markdown("""
#      ## Cirone & Monrose Data Science & AI Consultant 👨‍💼🧑‍💼📈
#      #### - We provide data-driven insights for banks looking to understand their B2C customers.
#      ##### - Please enter the customer's data, and we will develop our algorithm to deliver a Score Classification (Good, Standard, or Bad).
# """)

# Définir le style CSS pour l'infobulle
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
        width: 160px; /* Ajustez la largeur si nécessaire */
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 5px;
        padding: 5px 10px;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Position en dessus du texte */
        left: 50%;
        margin-left: -80px; /* Centrer l'infobulle */
        opacity: 0;
        transition: opacity 0.3s;
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
    st.markdown("""<h8><div class="tooltip">👤 Name<span class="tooltiptext">Enter name.</span></div></h8>""", unsafe_allow_html=True)
    customer_id = st.text_input('', value='AAA_0x1234', label_visibility="collapsed")

# Age
with cols[1]:
    st.markdown("""<h8><div class="tooltip">🧓 Age<span class="tooltiptext">Enter age.</span></div></h8>""", unsafe_allow_html=True)
    age = st.text_input('', '21', label_visibility="collapsed")
    valid_age, age_value = validate_input(age, int, 0, 100, "Age")

# Occupation
with cols[2]:
    st.markdown("<h8>🧑‍💻 Occupation</h8>", unsafe_allow_html=True)
    occupation_options = ["Scientist", "Teacher", "Engineer", "Entrepreneur", "Developer", "Lawyer", "Doctor", "Manager", "Musician", "Mechanic"]
    occupation = st.selectbox("", occupation_options, label_visibility="collapsed")

# Month
with cols[3]:
    st.markdown("<h8>📅 Month</h8>", unsafe_allow_html=True)
    month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = st.selectbox('', month_options, label_visibility="collapsed")

# Section 2: Financial Details
st.markdown("<h4>Financial Details</h4>", unsafe_allow_html=True)
cols2 = st.columns(4)

# Annual Income
with cols2[0]:
    st.markdown("<h8>💰 Annual Income</h8>", unsafe_allow_html=True)
    annual_income = st.text_input('', '30000', label_visibility="collapsed")
    valid_income, annual_income_value = validate_input(annual_income.replace(',', '.'), float, 0, None, "Annual income")

# Number of Bank Accounts
with cols2[1]:
    st.markdown("<h8>🏦 # Bank Accounts</h8>", unsafe_allow_html=True)
    num_bank_accounts = st.text_input('', '3', label_visibility="collapsed")
    valid_bank_accounts, num_bank_accounts_value = validate_input(num_bank_accounts, int, 0, None, "Number of Bank Accounts")

# Number of Credit Cards
with cols2[2]:
    st.markdown("<h8>💳 # Credit Cards</h8>", unsafe_allow_html=True)
    num_credit_cards = st.text_input('', '2', label_visibility="collapsed")
    valid_credit_cards, num_credit_cards_value = validate_input(num_credit_cards, int, 0, None, "Number of Credit Cards")

# Interest Rate
with cols2[3]:
    st.markdown("<h8>📈 % Interest</h8>", unsafe_allow_html=True)
    interest_rate = st.text_input('', '2.5', label_visibility="collapsed")
    valid_interest_rate, interest_rate_value = validate_input(interest_rate.replace(',', '.'), float, 0, None, "Interest rate")

# Section 3: Credit Information
st.markdown("<h4>Credit Information</h4>", unsafe_allow_html=True)
cols3 = st.columns(4)

# Number of Loans
with cols3[0]:
    st.markdown("<h8>💵 # Loans</h8>", unsafe_allow_html=True)
    num_loans = st.text_input('', '7', label_visibility="collapsed")
    valid_loans, num_loans_value = validate_input(num_loans, int, 0, None, "Number of Loans")

# Days Delayed
with cols3[1]:
    st.markdown("<h8>⌛ Delay / Due Date</h8>", unsafe_allow_html=True)
    days_delayed = st.text_input('', '10', label_visibility="collapsed")
    valid_days_delayed, days_delayed_value = validate_input(days_delayed, int, 0, None, "Days delayed")

# Number of Delayed Payments
with cols3[2]:
    st.markdown("<h8>🔄 # Late Payments</h8>", unsafe_allow_html=True)
    num_delayed_payments = st.text_input('', '11', label_visibility="collapsed")
    valid_delayed_payments, num_delayed_payments_value = validate_input(num_delayed_payments, int, 0, None, "Number of Delayed Payments")

# Changed Credit Limit
with cols3[3]:
    st.markdown("<h8>📊 % Changed Limit</h8>", unsafe_allow_html=True)
    changed_credit_limit = st.text_input('', '3.00', label_visibility="collapsed")
    valid_credit_limit, changed_credit_limit_value = validate_input(changed_credit_limit.replace(',', '.'), float, 0, None, "Changed credit limit")

# Number of Credit Inquiries
with cols3[0]:
    st.markdown("<h8>🔍 # Inquiries</h8>", unsafe_allow_html=True)
    num_credit_inquiries = st.text_input('', '13', label_visibility="collapsed")
    valid_credit_inquiries, num_credit_inquiries_value = validate_input(num_credit_inquiries, int, 0, None, "Number of Credit Inquiries")

# Credit Mix
with cols3[1]:
    st.markdown("<h8>💳 Credit Mix</h8>", unsafe_allow_html=True)
    credit_mix_options = ["Good", "Standard", "Bad"]
    credit_mix = st.selectbox("", credit_mix_options, label_visibility="collapsed")

# Outstanding Debt
with cols3[2]:
    st.markdown("<h8>💰 Unpaid Debt</h8>", unsafe_allow_html=True)
    outstanding_debt = st.text_input('', '502.10', label_visibility="collapsed")
    valid_outstanding_debt, outstanding_debt_value = validate_input(outstanding_debt.replace(',', '.'), float, 0, None, "Outstanding debt")

# Credit Utilization Ratio
with cols3[3]:
    st.markdown("<h8>📈 % Credit Use</h8>", unsafe_allow_html=True)
    credit_utilization_ratio = st.text_input('', '20.10', label_visibility="collapsed")
    valid_credit_utilization, credit_utilization_ratio_value = validate_input(credit_utilization_ratio.replace(',', '.'), float, 0, None, "Credit utilization ratio")

# Section 4: Payment Information
st.markdown("<h4>Payment Information</h4>", unsafe_allow_html=True)
cols4 = st.columns(4)

# Credit History Age
with cols4[0]:
    st.markdown("<h8>🕰️ Credit Age Months</h8>", unsafe_allow_html=True)
    credit_history_age = st.text_input('', '19', label_visibility="collapsed")
    valid_credit_age, credit_history_age_value = validate_input(credit_history_age, int, 0, None, "Credit Age")

# Payment of Min Amount
with cols4[1]:
    st.markdown("<h8>📝 Minimum Payment</h8>", unsafe_allow_html=True)
    payment_of_min_amount_options = ["Yes", "No"]
    payment_of_min_amount = st.selectbox("", payment_of_min_amount_options, label_visibility="collapsed")

# Total EMI per Month
with cols4[2]:
    st.markdown("<h8>💸 Monthly EMI Total</h8>", unsafe_allow_html=True)
    total_emi_per_month = st.text_input('', '70.47', label_visibility="collapsed")
    valid_total_emi, total_emi_per_month_value = validate_input(total_emi_per_month.replace(',', '.'), float, 0, None, "Total EMI per Month")

# Amount Invested Monthly
with cols4[3]:
    st.markdown("<h8>📊 Monthly Investment</h8>", unsafe_allow_html=True)
    amount_invested_monthly = st.text_input('', '162.43', label_visibility="collapsed")
    valid_invested_amount, amount_invested_monthly_value = validate_input(amount_invested_monthly.replace(',', '.'), float, 0, None, "Amount invested monthly")

# Section 5: Behavioral and Balance Information
st.markdown("<h4>Behavioral and Balance Information</h4>", unsafe_allow_html=True)
cols5 = st.columns(4)

# Payment Behaviour
with cols5[0]:
    st.markdown("<h8>📅 Payment Habits</h8>", unsafe_allow_html=True)
    payment_behaviour_options = ['LowspentSmallvaluepayments', 'HighspentMediumvaluepayments', 'LowspentMediumvaluepayments', 'HighspentLargevaluepayments', 'HighspentSmallvaluepayments', 'LowspentLargevaluepayments']
    payment_behaviour = st.selectbox("Select an option:", payment_behaviour_options, label_visibility="collapsed")

# Monthly Balance
with cols5[2]:
    st.markdown("<h8>💰 Monthly Balance</h8>", unsafe_allow_html=True)
    monthly_balance = st.text_input('', '162.44', label_visibility="collapsed")
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

if 'expander_open' not in st.session_state:
    st.session_state.expander_open = False

# Section 6: Button
st.markdown("<h4>Credit Score</h4>", unsafe_allow_html=True)

# Button to calculate the score based on the input data
if st.button("Calculate Score", type="primary"):
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

    results_df = None

    # Error handling block
    try:
        # Sending the request to the API
        response = requests.get(url, params=input_data)

        st.session_state.expander_open = True

        with st.expander("The result is", expanded=st.session_state.expander_open):

            # Check if the request was successful
            if response.status_code == 200:
                result = response.json()  # Fetch the result containing the credit score

                # Displaying the score classification based on the 'Credit_Score' value
                if result["Credit_Score"] == 0:
                    st.markdown(
                        """
                        <h1 style='font-size: 40px;'>Credit Good 💰✅</h1>
                        <p style='font-size: 20px;'>F&G Recommendation: authorize loan.</p>
                        """,
                        unsafe_allow_html=True
                    )
                elif result["Credit_Score"] == 2:
                    st.markdown(
                        """
                        <h1 style='font-size: 40px;'>Credit Standard 😐</h1>
                        <p style='font-size: 20px;'>F&G Recommendation: review details.</p>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        """
                        <h1 style='font-size: 40px;'>Credit Bad ❌</h1>
                        <p style='font-size: 20px;'>F&G Recommendation: reavaluate. </p>
                        """,
                        unsafe_allow_html=True
                    )

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

                # Load the dataset
                persona = pd.read_csv('raw_data/df_cleaned_31082024.csv')

                # Filter the DataFrame to include only rows with 'Credit_Score' as 'Good'
                persona_good = persona[persona['Credit_Score'] == 'Good']

                # Filter the DataFrame to include only rows with 'Credit_Score' as 'Standard'
                persona_standard = persona[persona['Credit_Score'] == 'Standard']

                # Filter the DataFrame to include only rows with 'Credit_Score' as 'Poor'
                persona_poor = persona[persona['Credit_Score'] == 'Poor']

                # # Define persona_list
                # persona_list = [
                #     "Persona",
                #     "NS",
                #     round(persona['Age'].mean()),
                #     persona['Occupation'].mode()[0],
                #     round(persona['Annual_Income'].mean()),
                #     round(persona['Num_Bank_Accounts'].mean()),
                #     round(persona['Num_Credit_Card'].mean()),
                #     round(persona['Interest_Rate'].mean()),
                #     round(persona['Num_of_Loan'].mean()),
                #     round(persona['Delay_from_due_date'].mean()),
                #     round(persona['Num_of_Delayed_Payment'].mean()),
                #     round(persona['Changed_Credit_Limit'].mean()),
                #     round(persona['Num_Credit_Inquiries'].mean()),
                #     persona['Credit_Mix'].mode()[0],
                #     round(persona['Outstanding_Debt'].mean()),
                #     round(persona['Credit_Utilization_Ratio'].mean()),
                #     round(persona['Credit_History_Age_Months'].mean()),
                #     persona['Payment_of_Min_Amount'].mode()[0],
                #     round(persona['Total_EMI_per_month'].mean()),
                #     round(persona['Amount_invested_monthly'].mean()),
                #     persona['Payment_Behaviour'].mode()[0],
                #     round(persona['Monthly_Balance'].mean()),
                #     persona['Credit_Score'].mode()[0],
                #     "NS"
                #     ]

                # Define persona_good_list
                persona_good_list = [
                    "Persona Good",
                    "NS",
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
                    persona_good['Credit_Score'].mode()[0],
                    "NS"
                    ]

                # Define persona_standard_list
                persona_standard_list = [
                    "Persona Standard",
                    "NS",
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
                    persona_standard['Credit_Score'].mode()[0],
                    "NS"
                    ]

                # Define persona_poor_list
                persona_poor_list = [
                    "Persona Poor",
                    "NS",
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
                    persona_poor['Credit_Score'].mode()[0],
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
                    # "Persona": persona_list,
                    "Persona Good": persona_good_list,
                    "Persona Standard": persona_standard_list,
                    "Persona Poor": persona_poor_list
                })

                # # Adding previous results if available
                # if 'previous_results' in st.session_state and st.session_state.previous_results:
                #     previous_results = st.session_state.previous_results
                # else:
                #     previous_results = {field: "N/A" for field in results_df["Field"]}

                # results_df["Previous Value"] = results_df["Field"].map(previous_results)

                st.subheader("Detailed Results")
                st.dataframe(results_df, width=1200, hide_index=True)  # Remove index column

                # Réorganiser le DataFrame pour être compatible avec Plotly (melt)
                results_melted = results_df.melt(id_vars='Field', var_name='Persona', value_name='Value')

                # Créer un graphique avec les features en X et les valeurs en Y, avec Persona en légende couleur
                fig = px.bar(results_melted, x='Field', y='Value', color='Persona',
                            title='Graphique des Résultats par Feature et Persona',
                            labels={'Field': 'Features', 'Value': 'Valeurs'})

                # Afficher le graphique dans Streamlit
                st.plotly_chart(fig)

                # Update previous results
                st.session_state.previous_results = dict(zip(results_df["Field"], results_df["Current Value"]))

            else:
                st.error(f"API request failed with status code {response.status_code}. Please check your inputs or try again later.")

    except Exception as e:
            st.error(f"An error occurred: {str(e)}")


    # Download button
    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode("utf-8")

    csv = convert_df(results_df)

    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name=f"{customer_id}_data.csv",
    mime="text/csv",
    )


    # Reset results button
    if st.button("Reset Results"):
        # Clear stored values in the session
        st.session_state.result = None
        st.session_state.proba = None
        st.session_state.previous_results = {}

    # Finish button
    if st.button("Finish Presentation"):
                st.markdown(
                    """
                    <h1 style='font-size: 40px;'>Thank you all</h1>
                    <p style='font-size: 20px;'>If you want to get in touch: let's chat on LinkedIn!</p>
                    <p style='font-size: 20px;'>Fernando Cirone & Gregory Monrose</p>
                    """,
                    unsafe_allow_html=True
                )

    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
