




###abaixo do exercício
# FROM python:3.10.6-buster
# COPY requirements.txt /requirements.txt
# COPY taxifare taxifare
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# #CMD uvicorn app.simple:app --host 0.0.0.0 (assim é como está na aula)
# CMD uvicorn taxifare.api.fast:app --host 0.0.0.0
