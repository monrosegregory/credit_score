
#Fast API Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

#My package Imports
from ml_logic.data import load_data, preproc, load_pipe
from ml_logic.predict import predict_main


app = FastAPI()

# Setup logging | Não faço ideia do que isso faz
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"]  # Allows all headers
)



@app.get("/")
def index():
    return {"Welcome": "Credit Score Analysis"}


@app.get("/predict")
def predict(
        id: str,
        customer_id: str,
        month: str,
        name: str,
        age: int,
        ssn: str,
        occupation: str,
        annual_income: float,
        monthly_inhand_salary: float,
        num_bank_accounts: int,
        num_credit_card: int,
        interest_rate: float,
        num_of_loan: int,
        type_of_loan: str,
        delay_from_due_date: int,
        num_of_delayed_payment: int,
        changed_credit_limit: float,
        num_credit_inquiries: int,
        credit_mix: str,
        outstanding_debt: float,
        credit_utilization_ratio: float,
        credit_history_age: str,
        payment_of_min_amount: str,
        total_emi_per_month: float,
        amount_invested_monthly: float,
        payment_behaviour: str,
        monthly_balance: float
    ):
    try:
        model_path = 'models/best_xgb_5.sav' ###??? 'models/crime_prediction_lightgbm_model.joblib'
        df = load_data(id, customer_id, month, name, age, ssn, occupation, annual_income,
                        monthly_inhand_salary, num_bank_accounts, num_credit_card,
                        interest_rate, num_of_loan, type_of_loan, delay_from_due_date,
                        num_of_delayed_payment, changed_credit_limit, num_credit_inquiries,
                        credit_mix, outstanding_debt, credit_utilization_ratio,
                        credit_history_age, payment_of_min_amount, total_emi_per_month,
                        amount_invested_monthly, payment_behaviour, monthly_balance)

        pipe = load_pipe('models/preproc_deploy.pkl') #qual caminho????) ('models/scaler.joblib')

        df_processed = preproc(df, pipe)

        prediction = predict_main(model_path, df_processed)

        return {"Score: ": prediction}

    #peguei de precog, será que vale a pena manter?
    except ValueError as e:
        logger.error(f"Error occurred: {e}")
        return {"error": str(e)}
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return {"error": str(e)}



###### abaixo do chat gpt, analisar, comparar e juntar
# from fastapi import FastAPI, HTTPException
# import logging
# app = FastAPI()
# logger = logging.getLogger(__name__)
# @app.get("/predict")
# def predict(
#     id: str,
#     customer_id: str,
#     month: str,
#     name: str,
#     age: int,
#     ssn: str,
#     occupation: str,
#     annual_income: float,
#     monthly_inhand_salary: float,
#     num_bank_accounts: int,
#     num_credit_card: int,
#     interest_rate: float,
#     num_of_loan: int,
#     type_of_loan: str,
#     delay_from_due_date: int,
#     num_of_delayed_payment: int,
#     changed_credit_limit: float,
#     num_credit_inquiries: int,
#     credit_mix: str,
#     outstanding_debt: float,
#     credit_utilization_ratio: float,
#     credit_history_age: str,
#     payment_of_min_amount: str,
#     total_emi_per_month: float,
#     amount_invested_monthly: float,
#     payment_behaviour: str,
#     monthly_balance: float
# ):
#     try:
#         # Definir o caminho correto para o modelo e pipeline de pré-processamento
#         model_path = 'models/best_xgb_5.sav'
#         pipe_path = 'models/preproc_deploy.pkl'
#         # Carregar os dados fornecidos pelo usuário
#         df = load_data(
#             id, customer_id, month, name, age, ssn, occupation, annual_income,
#             monthly_inhand_salary, num_bank_accounts, num_credit_card,
#             interest_rate, num_of_loan, type_of_loan, delay_from_due_date,
#             num_of_delayed_payment, changed_credit_limit, num_credit_inquiries,
#             credit_mix, outstanding_debt, credit_utilization_ratio,
#             credit_history_age, payment_of_min_amount, total_emi_per_month,
#             amount_invested_monthly, payment_behaviour, monthly_balance
#         )
#         # Carregar o pipeline de pré-processamento
#         pipe = load_pipe(pipe_path)
#         # Processar os dados
#         df_processed = preproc(df, pipe)
#         # Fazer a previsão usando o modelo carregado
#         prediction = predict_main(model_path, df_processed)
#         # Retornar o resultado como JSON
#         return {"Score": prediction}
#     except ValueError as ve:
#         logger.error(f"ValueError occurred: {ve}")
#         raise HTTPException(status_code=400, detail=f"Invalid input: {str(ve)}")
#     except FileNotFoundError as fnfe:
#         logger.error(f"FileNotFoundError occurred: {fnfe}")
#         raise HTTPException(status_code=500, detail=f"Model or preprocessing file not found: {str(fnfe)}")
#     except Exception as e:
#         logger.error(f"An unexpected error occurred: {e}")
#         raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
