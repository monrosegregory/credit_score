import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import Counter
#from streamlit.modal import Modal
import streamlit as st
import requests
#from streamlit_modal import Modal
import numpy as np
import pandas as pd


backgroundColor = "#FFFFFF"





logo_url = "https://img.freepik.com/fotos-premium/bandeira-nacional-do-brasil-e-franca-background-para-designers_659987-40312.jpg?w=900"  # Substitua pelo URL ou caminho da sua logo


st.markdown(
    f"""
    <style>
    .logo {{
        position: absolute;
        top: 15;
        left: 15;
        margin: 0px;
    }}
    </style>
    <div class="logo">
        <img src="{logo_url}" alt="Company Logo" width="100"/>
    </div>
    """,
    unsafe_allow_html=True
)







st.markdown("""
     ## Cirone & Monrose Data Science & AI Consultant 👨‍💼🧑‍💼📈
     #### - We provide data-driven insights for banks looking to understand their B2C customers.
     ##### - Please enter the customer's data, and we will develop our algorithm to deliver a Score Classification (Good, Standard, or Bad).
""")


# Dividindo a página em 4 colunas
cols = st.columns(4)



# Primeira linha (4 features)
with cols[0]:
    st.markdown("<h6>Customer ID 👤</h6>", unsafe_allow_html=True)
    customer_id_title = st.text_input('', value='AAA_0x1234')
    #customer_id_title = st.text_input('Insert Customer ID', 'AAA_0x1234')

with cols[1]:
    st.markdown("<h6>Month 📅</h6>", unsafe_allow_html=True)
    month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_selected_option = st.selectbox('', month_options)

with cols[2]:
    st.markdown("<h6>Age 🧓</h6>", unsafe_allow_html=True)
    age_title = st.text_input('', '21')

with cols[3]:
    st.markdown("<h6>Occupation 🧑‍💻</h6>", unsafe_allow_html=True)
    occupation_options = ["Scientist", "Teacher", "Engineer", "Entrepreneur", "Developer", "Lawyer", "Doctor", "Manager", "Musician", "Mechanic"]
    occupation_selected_option = st.selectbox("", occupation_options)



# Segunda linha
with cols[0]:
    st.markdown("<h6>Annual Income 🪙</h6>", unsafe_allow_html=True)
    annual_income_title = st.text_input('', '30000')

with cols[1]:
    st.markdown("<h6># Bank Accounts 🏦</h6>", unsafe_allow_html=True)
    num_bank_accounts_title = st.text_input('', '3')

with cols[2]:
    st.markdown("<h6># Credit Cards 💳</h6>", unsafe_allow_html=True)
    num_credit_card_title = st.text_input('', '4')

with cols[3]:
    st.markdown("<h6>% Interest Rate💲</h6>", unsafe_allow_html=True)
    interest_rate_title = st.text_input('', '2')



# Terceira linha
with cols[0]:
    st.markdown("<h6># Loans 🤝</h6>", unsafe_allow_html=True)
    num_of_loan_title = st.text_input('', '5')

with cols[1]:
    st.markdown("<h6>Due Days (loan)⏳</h6>", unsafe_allow_html=True)
    delay_from_due_date_of_loan_title = st.text_input('', '1')

with cols[2]:
    st.markdown("<h6>Due (payment)💵</h6>", unsafe_allow_html=True)
    num_of_delayed_payment_title = st.text_input('', '6')

with cols[3]:
    st.markdown("<h6>% Limit Change🔄</h6>", unsafe_allow_html=True)
    changed_credit_limit_title = st.text_input('', '2.00')



# Quarta linha
with cols[0]:
    st.markdown("<h6>#Credit Inquiries🔍</h6>", unsafe_allow_html=True)
    num_credit_inquiries_title = st.text_input('', '7')

with cols[1]:
    st.markdown("<h6>Credit Mix 🎛️</h6>", unsafe_allow_html=True)
    credit_mix_options = ["Good", "Standard", "Bad"]
    credit_mix_selected_options = st.selectbox("", credit_mix_options)

with cols[2]:
    st.markdown("<h6>Pending Debt💸</h6>", unsafe_allow_html=True)
    outstanding_debt_title = st.text_input('', '502.10')

with cols[3]:
    st.markdown("<h6>Credit Use % 📊</h6>", unsafe_allow_html=True)
    credit_utilization_ratio_title = st.text_input('', '20.10')



# Quinta linha
with cols[0]:
     st.markdown("<h6>Balance (month)💰</h6>", unsafe_allow_html=True)
     monthly_balance_title = st.text_input('Monthly Balance', '162.44')

with cols[1]:
    st.markdown("<h6>Min. Payment💵</h6>", unsafe_allow_html=True)
    payment_of_min_amount_options = ["Yes", "No"]
    payment_of_min_amount_selected_options = st.selectbox("", payment_of_min_amount_options)

with cols[2]:
    st.markdown("<h6>EMI per Month🧾</h6>", unsafe_allow_html=True)
    total_emi_per_month_title = st.text_input('', '70.47')

with cols[3]:
    st.markdown("<h6>$ Invested 📈</h6>", unsafe_allow_html=True)
    amount_invested_monthly_title = st.text_input('', '162.44')



# Sexta linha
with cols[0]:
    st.markdown("<h6>$ Behaviour📅</h6>", unsafe_allow_html=True)
    payment_behaviour_options = ['LowspentSmallvaluepayments', 'HighspentMediumvaluepayments', 'LowspentMediumvaluepayments', 'HighspentLargevaluepayments', 'HighspentSmallvaluepayments', 'LowspentLargevaluepayments']
    payment_behaviour_selected_options = st.selectbox("Select an option:", payment_behaviour_options)

with cols[1]:
    st.markdown("<h6>Credit Age 🕰️</h6>", unsafe_allow_html=True)
    years = st.slider("Years", 0, 100, 0)
    months = st.slider("Months", 0, 11, 0)
    result_history_age = f"{years} Years and {months} Months"
    st.write(result_history_age)

with cols[2]:
    st.write(" ")

with cols[3]:
    st.write(" ")



if 'expander_open' not in st.session_state:
    st.session_state.expander_open = False




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
        "amount_invested_monthly": amount_invested_monthly_title,
        "payment_behaviour": payment_behaviour_selected_options,
        "monthly_balance": monthly_balance_title
    }

    url = "https://credit-score-v5-1032836634135.us-west1.run.app/predict"
    response = requests.get(url, params=input_data)

    st.session_state.expander_open = True

    with st.expander("The result is", expanded=st.session_state.expander_open):
        if response.status_code == 200:
            result = response.json()
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

            # Exibir a probabilidade se disponível
            if 'Prob' in result:
                st.markdown(f"<h1 style='font-size: 40px;'>Probability: {result['Prob'] * 100:.0f}%</h1>", unsafe_allow_html=True)




        else:
            st.write("Error: Could not get a prediction")






if st.button("Finish Presentation"):
                st.markdown(
                    """
                    <h1 style='font-size: 40px;'>Thank you all</h1>
                    <p style='font-size: 20px;'>If you want to get in touch: let's chat on LinkedIn!</p>
                    <p style='font-size: 20px;'>Fernando Cirone & Gregory Monrose</p>
                    """,
                    unsafe_allow_html=True
                )






# if 'show_finish_button' in st.session_state and st.session_state.show_finish_button:
#         if st.button("Finish Presentation"):
#             st.markdown(
#                 """
#                 <h1 style='font-size: 40px;'>Thank you all</h1>
#                 <p style='font-size: 20px;'>If you want to get in touch: let's chat on LinkedIn!</p>
#                 <p style='font-size: 20px;'>Fernando Cirone & Gregory Monrose</p>
#                 """,
#                 unsafe_allow_html=True
#             )


# if 'expander_open' not in st.session_state:
#     st.session_state.expander_open = False


# if st.button("Finish Presentation"):
#     st.session_state.expander_open = True
#     st.markdown(
#                 """
#                 <h1 style='font-size: 40px;'>Thank you all
#                 <p style='font-size: 20px;'>If you want to get in touch: let's chat on Lindkn !</p>
#                 <p style='font-size: 20px;'>Fernando Cirone & Gregory Monrose</p>
#                 """,
#                 unsafe_allow_html=True
#                 )




#st.markdown("- *Note: The input format is consistent with the customer base data.*")

st.markdown("[You can check here our Machine Learning code on GitHub](https://github.com/monrosegregory/credit_score)", unsafe_allow_html=True)



#BACKUP SE DER MERDA

# import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# from collections import Counter
# #from streamlit.modal import Modal
# import streamlit as st
# import requests

# import numpy as np
# import pandas as pd

# st.markdown("""
#             # F&G Data Science & AI Consultant 👨‍💼🧑‍💼📈
#             ## - We provide data-driven insights for banks looking to understand their B2C customers.
#             ### - Please enter the customer's data, and we will develop our algorithm to deliver a Score Classification (Good, Standard, or Bad).
#             """)


# st.markdown("[You can check here our Machine Learning code on GitHub](https://github.com/monrosegregory/credit_score)", unsafe_allow_html=True)


# #customer_id CUS_0x5407 | AAA_0x1234
# st.markdown("<h6>Customer ID 👤</h6>", unsafe_allow_html=True)
# customer_id_title = st.text_input('Insert Customer ID (only string in this format: AAA_0x1234 because it is anonymized)', 'AAA_0x1234')

# #month
# st.markdown("<h6>Month 📅</h6>", unsafe_allow_html=True)
# month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# month_selected_option = st.selectbox("Select an option:", month_options)


# #age
# st.markdown("<h6>Age 🧓</h6>", unsafe_allow_html=True)
# age_title = st.text_input('Insert Age (only numbers eg.: 21)', '21')


# #occupation
# st.markdown("<h6>Occupation 🧑‍💻</h6>", unsafe_allow_html=True)
# occupation_options = ["Scientist", "Teacher", "Engineer", "Entrepreneur", "Entrepreneur", "Developer", "Lawyer", "Media_Manager", "Doctor", "Journalist", "Manager", "Accountant", "Musician", "Mechanic", "Writer", "Architect"]
# occupation_selected_option = st.selectbox("Select an option:", occupation_options)


# #annual_income
# st.markdown("<h6>Annual Income 🪙</h6>", unsafe_allow_html=True)
# annual_income_title = st.text_input('Insert Annual Income (only numbers eg.: 30.000)', '30.000')


# #num_bank_accounts
# st.markdown("<h6>Number of Bank Accounts 🏦</h6>", unsafe_allow_html=True)
# num_bank_accounts_title = st.text_input('Insert Annual Income (only numbers eg.: 2)', '2')


# #num_credit_card
# st.markdown("<h6>Number of Credit Cards 💳</h6>", unsafe_allow_html=True)
# num_credit_card_title = st.text_input('Number of Credit Cards (only numbers eg.: 2)', '2')


# #interest_rate
# st.markdown("<h6>% Interest rate 💲</h6>", unsafe_allow_html=True)
# interest_rate_title = st.text_input('Number of the interest rate (only numbers eg.: 2)', '2')


# #num_of_loan
# st.markdown("<h6>Number of Loans taken 🤝</h6>", unsafe_allow_html=True)
# num_of_loan_title = st.text_input('Number of Loans taken (only numbers eg.: 2)', '2')


# #delay_from_due_date
# st.markdown("<h6>Days delayed from due date ⏳</h6>", unsafe_allow_html=True)
# delay_from_due_date_of_loan_title = st.text_input('Days delayed from due date (only numbers eg.: 2)', '2')


# #num_of_delayed_payment
# st.markdown("<h6>Number of delayed payments 💵</h6>", unsafe_allow_html=True)
# num_of_delayed_payment_title = st.text_input('Number of delayed payments (only numbers eg.: 2)', '2')


# #changed_credit_limit
# st.markdown("<h6>% of Changed credit limit 🔄</h6>", unsafe_allow_html=True)
# changed_credit_limit_title = st.text_input('Changed credit limit (only numbers eg.: 2.00)', '2.00')


# #num_credit_inquiries
# st.markdown("<h6>Number of credit inquiries 🔍</h6>", unsafe_allow_html=True)
# num_credit_inquiries_title = st.text_input('Number of credit inquiries (only numbers eg.: 2)', '2')


# #credit_mix
# st.markdown("<h6>Credit Mix 🎛️</h6>", unsafe_allow_html=True)
# credit_mix_options = ["Good", "Standard", "Bad"]
# credit_mix_selected_options = st.selectbox("Select an option:", credit_mix_options)


# #outstanding_debt
# st.markdown("<h6>Outstanding debt 💸</h6>", unsafe_allow_html=True)
# outstanding_debt_title = st.text_input('Outstanding debt (only numbers eg.: 502.10)', '502.10')


# #credit_utilization_ratio
# st.markdown("<h6>Credit utilization ratio 📊</h6>", unsafe_allow_html=True)
# credit_utilization_ratio_title = st.text_input('Credit utilization ratio (only numbers eg.: 20.10)', '20.10')


# #credit_history_age
# st.markdown("<h6>Credit History Age 🕰️</h6>", unsafe_allow_html=True)
# years = st.slider("Select years", 0, 100, 0)
# months = st.slider("Select months", 0, 11, 0)
# result_history_age = f"{years} Years and {months} Months"
# st.write(result_history_age)


# #payment_of_min_amount
# st.markdown("<h6>Payment of min amount 💵</h6>", unsafe_allow_html=True)
# payment_of_min_amount_options = ["Yes", "No"]
# payment_of_min_amount_selected_options = st.selectbox("Select an option:", payment_of_min_amount_options)


# #total_emi_per_month
# st.markdown("<h6>Total emi per month 🧾</h6>", unsafe_allow_html=True)
# total_emi_per_month_title = st.text_input('Total emi per month (only numbers eg.: 70.47)', '70.47')


# #amount_invested_monthly 162.44
# st.markdown("<h6>Amount invested monthly 📈</h6>", unsafe_allow_html=True)
# mount_invested_monthly_title = st.text_input('Amount invested monthly (only numbers eg.: 162.44)', '162.44')


# #payment_behaviour - LowspentLargevaluepayments
# st.markdown("<h6>Payment Behaviour 📅</h6>", unsafe_allow_html=True)
# payment_behaviour_options = ['LowspentSmallvaluepayments', 'HighspentMediumvaluepayments', 'LowspentMediumvaluepayments', 'HighspentLargevaluepayments', 'HighspentSmallvaluepayments', 'LowspentLargevaluepayments']
# payment_behaviour_selected_options = st.selectbox("Select an option:", payment_behaviour_options)

# #monthly_balance
# st.markdown("<h6>Monthly balance 💰</h6>", unsafe_allow_html=True)
# monthly_balance_title = st.text_input('Monthly balancey (only numbers eg.: 162.44)', '162.44')



# if st.button("Calculate Score"):

#     input_data = {
#                     "customer_id": customer_id_title,
#                     "month": month_selected_option,
#                     "age": age_title,
#                     "occupation": occupation_selected_option,
#                     "annual_income": annual_income_title,
#                     "num_bank_accounts": num_bank_accounts_title,
#                     "num_credit_card": num_credit_card_title,
#                     "interest_rate": interest_rate_title,
#                     "num_of_loan": num_of_loan_title,
#                     "delay_from_due_date": delay_from_due_date_of_loan_title,
#                     "num_of_delayed_payment": num_of_delayed_payment_title,
#                     "changed_credit_limit": changed_credit_limit_title,
#                     "num_credit_inquiries": num_credit_inquiries_title,
#                     "credit_mix": credit_mix_selected_options,
#                     "outstanding_debt": outstanding_debt_title,
#                     "credit_utilization_ratio": credit_utilization_ratio_title,
#                     "credit_history_age": result_history_age,
#                     "payment_of_min_amount": payment_of_min_amount_selected_options,
#                     "total_emi_per_month": total_emi_per_month_title,
#                     "amount_invested_monthly": mount_invested_monthly_title,
#                     "payment_behaviour": payment_behaviour_selected_options,
#                     "monthly_balance": monthly_balance_title
#                 }

#     url = "https://credit-score-v5-1032836634135.us-west1.run.app/predict"

#     response = requests.get(url, params=input_data)


#     if response.status_code == 200:
#         # Exibe o resultado com tamanho aumentado usando HTML e CSS
#         result = response.json()  # aqui é o score

#         # Verifica o valor de "Credit_Score" e exibe a mensagem correspondente
#         if result["Credit_Score"] == 0:
#             st.markdown(f"<h1 style='font-size: 40px;'>Credit Good 💰✅</h1>", unsafe_allow_html=True)
#         elif result["Credit_Score"] == 2:
#             st.markdown(f"<h1 style='font-size: 40px;'>Credit Standard 😐</h1>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<h1 style='font-size: 40px;'>Credit Bad ❌</h1>", unsafe_allow_html=True)

#         # Exibe a probabilidade associada
#         st.markdown(f"<h1 style='font-size: 40px;'>Probability of the Score Class: {result['Prob'] * 100:.0f}%</h1>", unsafe_allow_html=True)

#     else:
#         st.write("Error: Could not get a prediction")


# #Nota de rodape
# st.markdown("- *Note: The input format is consistent with the one used for the customer base data we have obtained.*")

# st.markdown("[You can check here our Machine Learning code on GitHub](https://github.com/monrosegregory/credit_score)", unsafe_allow_html=True)
