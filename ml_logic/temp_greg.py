import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import Counter
#from streamlit.modal import Modal
import streamlit as st
import requests
#import time
import plotly.graph_objects as go


import numpy as np
import pandas as pd

st.markdown("""
            # F&G Data Science & AI Consultant 👨‍💼🧑‍💼📈
            ## - We provide data-driven insights for banks looking to understand their B2C customers.
            ### - Please enter the customer's data, and we will develop our algorithm to deliver a Score Classification (Good, Standard, or Bad).
            """)


st.markdown("[You can check here our Machine Learning code on GitHub](https://github.com/monrosegregory/credit_score)", unsafe_allow_html=True)

#

#customer_id CUS_0x5407 | AAA_0x1234
st.markdown("<h4>Customer ID 👤</h4>", unsafe_allow_html=True)
customer_id_title = st.text_input('Insert Customer ID (only string in this format: AAA_0x1234 because it is anonymized)', 'AAA_0x1234')

#month
st.markdown("<h4>Month 📅</h4>", unsafe_allow_html=True)
month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_selected_option = st.selectbox("Select an option:", month_options)


#age
st.markdown("<h4>Age 🧓</h4>", unsafe_allow_html=True)
age_title = st.text_input('Insert Age (only numbers eg.: 21)', '21')


#occupation
st.markdown("<h4>Occupation 🧑‍💻</h4>", unsafe_allow_html=True)
occupation_options = ["Scientist", "Teacher", "Engineer", "Entrepreneur", "Entrepreneur", "Developer", "Lawyer", "Media_Manager", "Doctor", "Journalist", "Manager", "Accountant", "Musician", "Mechanic", "Writer", "Architect"]
occupation_selected_option = st.selectbox("Select an option:", occupation_options)


#annual_income
st.markdown("<h4>Annual Income 🪙</h4>", unsafe_allow_html=True)
annual_income_title = st.text_input('Insert Annual Income (only numbers eg.: 30.000)', '30.000')


#num_bank_accounts
st.markdown("<h4>Number of Bank Accounts 🏦</h4>", unsafe_allow_html=True)
num_bank_accounts_title = st.text_input('Insert Annual Income (only numbers eg.: 2)', '2')


#num_credit_card
st.markdown("<h4>Number of Credit Cards 💳</h4>", unsafe_allow_html=True)
num_credit_card_title = st.text_input('Number of Credit Cards (only numbers eg.: 2)', '2')


#interest_rate
st.markdown("<h4>% Interest rate 💲</h4>", unsafe_allow_html=True)
interest_rate_title = st.text_input('Number of the interest rate (only numbers eg.: 2)', '2')


#num_of_loan
st.markdown("<h4>Number of Loans taken 🤝</h4>", unsafe_allow_html=True)
num_of_loan_title = st.text_input('Number of Loans taken (only numbers eg.: 2)', '2')


#delay_from_due_date
st.markdown("<h4>Days delayed from due date ⏳</h4>", unsafe_allow_html=True)
delay_from_due_date_of_loan_title = st.text_input('Days delayed from due date (only numbers eg.: 2)', '2')


#num_of_delayed_payment
st.markdown("<h4>Number of delayed payments 💵</h4>", unsafe_allow_html=True)
num_of_delayed_payment_title = st.text_input('Number of delayed payments (only numbers eg.: 2)', '2')


#changed_credit_limit
st.markdown("<h4>% of Changed credit limit 🔄</h4>", unsafe_allow_html=True)
changed_credit_limit_title = st.text_input('Changed credit limit (only numbers eg.: 2.00)', '2.00')


#num_credit_inquiries
st.markdown("<h4>Number of credit inquiries 🔍</h4>", unsafe_allow_html=True)
num_credit_inquiries_title = st.text_input('Number of credit inquiries (only numbers eg.: 2)', '2')


#credit_mix
st.markdown("<h4>Credit Mix 🎛️</h4>", unsafe_allow_html=True)
credit_mix_options = ["Good", "Standard", "Bad"]
credit_mix_selected_options = st.selectbox("Select an option:", credit_mix_options)


#outstanding_debt
st.markdown("<h4>Outstanding debt 💸</h4>", unsafe_allow_html=True)
outstanding_debt_title = st.text_input('Outstanding debt (only numbers eg.: 502.10)', '502.10')


#credit_utilization_ratio
st.markdown("<h4>Credit utilization ratio 📊</h4>", unsafe_allow_html=True)
credit_utilization_ratio_title = st.text_input('Credit utilization ratio (only numbers eg.: 20.10)', '20.10')


#credit_history_age
st.markdown("<h4>Credit History Age 🕰️</h4>", unsafe_allow_html=True)
years = st.slider("Select years", 0, 100, 0)
months = st.slider("Select months", 0, 11, 0)
result_history_age = f"{years} Years and {months} Months"
st.write(result_history_age)


#payment_of_min_amount
st.markdown("<h4>Payment of min amount 💵</h4>", unsafe_allow_html=True)
payment_of_min_amount_options = ["Yes", "No"]
payment_of_min_amount_selected_options = st.selectbox("Select an option:", payment_of_min_amount_options)


#total_emi_per_month
st.markdown("<h4>Total emi per month 🧾</h4>", unsafe_allow_html=True)
total_emi_per_month_title = st.text_input('Total emi per month (only numbers eg.: 70.47)', '70.47')


#amount_invested_monthly 162.44
st.markdown("<h4>Amount invested monthly 📈</h4>", unsafe_allow_html=True)
mount_invested_monthly_title = st.text_input('Amount invested monthly (only numbers eg.: 162.44)', '162.44')


#payment_behaviour - LowspentLargevaluepayments
st.markdown("<h4>Payment Behaviour 📅</h4>", unsafe_allow_html=True)
payment_behaviour_options = ['LowspentSmallvaluepayments', 'HighspentMediumvaluepayments', 'LowspentMediumvaluepayments', 'HighspentLargevaluepayments', 'HighspentSmallvaluepayments', 'LowspentLargevaluepayments']
payment_behaviour_selected_options = st.selectbox("Select an option:", payment_behaviour_options)

#monthly_balance
st.markdown("<h4>Monthly balance 💰</h4>", unsafe_allow_html=True)
monthly_balance_title = st.text_input('Monthly balancey (only numbers eg.: 162.44)', '162.44')



if st.button("Calculate Score"):

    input_data = {
                    "customer_id": customer_id_title,
                    "month": month_selected_option,
                    "age": age_title,
                    "occupation": occupation_selected_option,
                    "annual_income": annual_income_title,
                    "num_bank_accounts": num_bank_accounts_title,
                    "num_credit_card": num_credit_card_title,
                    "interest_rate": interest_rate_title,
                    "num_of_loan": num_of_loan_title,
                    "delay_from_due_date": delay_from_due_date_of_loan_title,
                    "num_of_delayed_payment": num_of_delayed_payment_title,
                    "changed_credit_limit": changed_credit_limit_title,
                    "num_credit_inquiries": num_credit_inquiries_title,
                    "credit_mix": credit_mix_selected_options,
                    "outstanding_debt": outstanding_debt_title,
                    "credit_utilization_ratio": credit_utilization_ratio_title,
                    "credit_history_age": result_history_age,
                    "payment_of_min_amount": payment_of_min_amount_selected_options,
                    "total_emi_per_month": total_emi_per_month_title,
                    "amount_invested_monthly": mount_invested_monthly_title,
                    "payment_behaviour": payment_behaviour_selected_options,
                    "monthly_balance": monthly_balance_title
                }

    #url = "https://credit-score-v4-1032836634135.us-west1.run.app/predict"
    url = "https://credit-score-v5-1032836634135.us-west1.run.app/predict"
    #url = https://credit-score-v4-1032836634135.us-west1.run.app

# Initialisation des variables
result = None
proba = None

# Requête API
response = requests.get(url, params=input_data)

# Vérification de la réponse
if response.status_code == 200:
    result = response.json()  # Ici se trouve le score

    # Affichage du message basé sur "Credit_Score"
    if result.get("Credit_Score") == 0:
        st.markdown(f"<h1 style='font-size: 40px;'>Credit Good 💰✅</h1>", unsafe_allow_html=True)
    elif result.get("Credit_Score") == 2:
        st.markdown(f"<h1 style='font-size: 40px;'>Credit Standard 😐</h1>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h1 style='font-size: 40px;'>Credit Bad ❌</h1>", unsafe_allow_html=True)

    # Affichage de la probabilité associée
    st.markdown(f"<h1 style='font-size: 40px;'>Probability of the Score Class: {result.get('Prob', 0) * 100:.0f}%</h1>", unsafe_allow_html=True)

    # Initialisation de la probabilité
    proba = result.get('Prob', 0)  # Assurez-vous que proba est un nombre entre 0 et 1
else:
    st.write("Error: Could not get a prediction")

# Affichage de la barre de progression
if proba is not None:
    percentage = int(proba * 100)  # Convertir la probabilité en pourcentage

    # Définir la couleur en fonction du pourcentage
    if percentage < 50:
        color = 'red'
    elif 50 <= percentage < 75:
        color = 'orange'
    else:
        color = 'green'

    # Afficher la barre de progression avec une couleur dynamique en utilisant HTML + CSS
    progress_bar_html = f"""
    <div style="width: 100%; background-color: lightgray; border-radius: 25px;">
        <div style="width: {percentage}%; background-color: {color}; height: 25px; border-radius: 25px;"></div>
    </div>
    """

    # Rendre la barre de progression stylisée
    st.markdown(progress_bar_html, unsafe_allow_html=True)

    # Afficher le texte du pourcentage
    st.text(f"Probability of the Score Class: {percentage}%")
else:
    st.warning("Result data is not available. Please run the calculation or check your inputs.")




import streamlit as st
import requests

# Définir la mise en page en colonnes
col1, col2 = st.columns([2, 1])

# Colonne de gauche (inputs)
with col1:
    st.markdown("""
                ## F&G AI Consultant 👨‍💼🧑‍💼📈
                """)

    st.markdown("[You can check here our Machine Learning code on GitHub](https://github.com/monrosegregory/credit_score)", unsafe_allow_html=True)

    st.markdown("<h4>Customer ID 👤</h4>", unsafe_allow_html=True)
    customer_id_title = st.text_input('Insert Customer ID (only string in this format: AAA_0x1234 because it is anonymized)', 'AAA_0x1234')

    st.markdown("<h4>Month 📅</h4>", unsafe_allow_html=True)
    month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_selected_option = st.selectbox("Select an option:", month_options)

    st.markdown("<h4>Age 🧓</h4>", unsafe_allow_html=True)
    age_title = st.text_input('Insert Age (only numbers eg.: 21)', '21')

    st.markdown("<h4>Occupation 🧑‍💻</h4>", unsafe_allow_html=True)
    occupation_options = ["Scientist", "Teacher", "Engineer", "Entrepreneur", "Developer", "Lawyer", "Media_Manager", "Doctor", "Journalist", "Manager", "Accountant", "Musician", "Mechanic", "Writer", "Architect"]
    occupation_selected_option = st.selectbox("Select an option:", occupation_options)

    st.markdown("<h4>Annual Income 🪙</h4>", unsafe_allow_html=True)
    annual_income_title = st.text_input('Insert Annual Income (only numbers eg.: 30.000)', '30.000')

    st.markdown("<h4>Number of Bank Accounts 🏦</h4>", unsafe_allow_html=True)
    num_bank_accounts_title = st.text_input('Insert Annual Income (only numbers eg.: 2)', '2')

    st.markdown("<h4>Number of Credit Cards 💳</h4>", unsafe_allow_html=True)
    num_credit_card_title = st.text_input('Number of Credit Cards (only numbers eg.: 2)', '2')

    st.markdown("<h4>% Interest rate 💲</h4>", unsafe_allow_html=True)
    interest_rate_title = st.text_input('Number of the interest rate (only numbers eg.: 2)', '2')

    st.markdown("<h4>Number of Loans taken 🤝</h4>", unsafe_allow_html=True)
    num_of_loan_title = st.text_input('Number of Loans taken (only numbers eg.: 2)', '2')

    st.markdown("<h4>Days delayed from due date ⏳</h4>", unsafe_allow_html=True)
    delay_from_due_date_of_loan_title = st.text_input('Days delayed from due date (only numbers eg.: 2)', '2')

    st.markdown("<h4>Number of delayed payments 💵</h4>", unsafe_allow_html=True)
    num_of_delayed_payment_title = st.text_input('Number of delayed payments (only numbers eg.: 2)', '2')

    st.markdown("<h4>% of Changed credit limit 🔄</h4>", unsafe_allow_html=True)
    changed_credit_limit_title = st.text_input('Changed credit limit (only numbers eg.: 2.00)', '2.00')

    st.markdown("<h4>Number of credit inquiries 🔍</h4>", unsafe_allow_html=True)
    num_credit_inquiries_title = st.text_input('Number of credit inquiries (only numbers eg.: 2)', '2')

    st.markdown("<h4>Credit Mix 🎛️</h4>", unsafe_allow_html=True)
    credit_mix_options = ["Good", "Standard", "Bad"]
    credit_mix_selected_options = st.selectbox("Select an option:", credit_mix_options)

    st.markdown("<h4>Outstanding debt 💸</h4>", unsafe_allow_html=True)
    outstanding_debt_title = st.text_input('Outstanding debt (only numbers eg.: 502.10)', '502.10')

    st.markdown("<h4>Credit utilization ratio 📊</h4>", unsafe_allow_html=True)
    credit_utilization_ratio_title = st.text_input('Credit utilization ratio (only numbers eg.: 20.10)', '20.10')

    st.markdown("<h4>Credit History Age 🕰️</h4>", unsafe_allow_html=True)
    years = st.slider("Select years", 0, 100, 0)
    months = st.slider("Select months", 0, 11, 0)
    result_history_age = f"{years} Years and {months} Months"
    st.write(result_history_age)

    st.markdown("<h4>Payment of min amount 💵</h4>", unsafe_allow_html=True)
    payment_of_min_amount_options = ["Yes", "No"]
    payment_of_min_amount_selected_options = st.selectbox("Select an option:", payment_of_min_amount_options)

    st.markdown("<h4>Total emi per month 🧾</h4>", unsafe_allow_html=True)
    total_emi_per_month_title = st.text_input('Total emi per month (only numbers eg.: 70.47)', '70.47')

    st.markdown("<h4>Amount invested monthly 📈</h4>", unsafe_allow_html=True)
    mount_invested_monthly_title = st.text_input('Amount invested monthly (only numbers eg.: 162.44)', '162.44')

    st.markdown("<h4>Payment Behaviour 📅</h4>", unsafe_allow_html=True)
    payment_behaviour_options = ['LowspentSmallvaluepayments', 'HighspentMediumvaluepayments', 'LowspentMediumvaluepayments', 'HighspentLargevaluepayments', 'HighspentSmallvaluepayments', 'LowspentLargevaluepayments']
    payment_behaviour_selected_options = st.selectbox("Select an option:", payment_behaviour_options)

    st.markdown("<h4>Monthly balance 💰</h4>", unsafe_allow_html=True)
    monthly_balance_title = st.text_input('Monthly balancey (only numbers eg.: 162.44)', '162.44')

# Colonne de droite (outputs)
with col2:
    if st.button("Calculate Score"):

        input_data = {
                        "customer_id": customer_id_title,
                        "month": month_selected_option,
                        "age": age_title,
                        "occupation": occupation_selected_option,
                        "annual_income": annual_income_title,
                        "num_bank_accounts": num_bank_accounts_title,
                        "num_credit_card": num_credit_card_title,
                        "interest_rate": interest_rate_title,
                        "num_of_loan": num_of_loan_title,
                        "delay_from_due_date": delay_from_due_date_of_loan_title,
                        "num_of_delayed_payment": num_of_delayed_payment_title,
                        "changed_credit_limit": changed_credit_limit_title,
                        "num_credit_inquiries": num_credit_inquiries_title,
                        "credit_mix": credit_mix_selected_options,
                        "outstanding_debt": outstanding_debt_title,
                        "credit_utilization_ratio": credit_utilization_ratio_title,
                        "credit_history_age": result_history_age,
                        "payment_of_min_amount": payment_of_min_amount_selected_options,
                        "total_emi_per_month": total_emi_per_month_title,
                        "amount_invested_monthly": mount_invested_monthly_title,
                        "payment_behaviour": payment_behaviour_selected_options,
                        "monthly_balance": monthly_balance_title
                    }

        # URL de l'API
        url = "https://credit-score-v5-1032836634135.us-west1.run.app/predict"

        # Initialisation des variables
        result = None
        proba = None

        # Requête API
        response = requests.get(url, params=input_data)

        # Vérification de la réponse
        if response.status_code == 200:
            result = response.json()  # Ici se trouve le score

            # Affichage du message basé sur "Credit_Score"
            if result.get("Credit_Score") == 0:
                st.markdown(f"<h1 style='font-size: 40px;'>Credit Good 💰✅</h1>", unsafe_allow_html=True)
            elif result.get("Credit_Score") == 2:
                st.markdown(f"<h1 style='font-size: 40px;'>Credit Standard 😐</h1>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h1 style='font-size: 40px;'>Credit Bad ❌</h1>", unsafe_allow_html=True)

        # Affichage de la barre de progression
        if proba is not None:
            percentage = int(proba * 100)  # Convertir la probabilité en pourcentage

            # Définir la couleur en fonction du pourcentage
            if percentage < 50:
                color = 'red'
            elif 50 <= percentage < 75:
                color = 'orange'
            else:
                color = 'green'

            # Afficher la barre de progression avec une couleur dynamique en utilisant HTML + CSS
            progress_bar_html = f"""
            <div style="width: 100%; background-color: lightgray; border-radius: 25px;">
                <div style="width: {percentage}%; background-color: {color}; height: 25px; border-radius: 25px;"></div>
            </div>
            """

            # Rendre la barre de progression stylisée
            st.markdown(progress_bar_html, unsafe_allow_html=True)

            # Afficher le texte du pourcentage
            st.text(f"Probability of the Score Class: {percentage}%")
