
#FROM
#FROM python:3.10.14-bullseye (Fernando)
FROM python:3.10.6-buster

# Install HDF5 system libraries
RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#COPY
COPY requirements.txt requirements.txt
COPY api api
COPY ml_logic /ml_logic
COPY models /models
#COPY MANIFEST.txt /MANIFEST.txt
#COPY MANIFEST.in /MANIFEST.in
COPY setup.py setup.py


#RUN
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


#CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
CMD uvicorn api.fast:app --host 0.0.0.0 --port ${PORT:-8000}

#CMD uvicorn api.fast:app --host 0.0.0.0






###abaixo do exercício
# FROM python:3.10.6-buster
# COPY requirements.txt /requirements.txt
# COPY taxifare taxifare
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# #CMD uvicorn app.simple:app --host 0.0.0.0 (assim é como está na aula)
# CMD uvicorn taxifare.api.fast:app --host 0.0.0.0
