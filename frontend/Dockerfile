FROM python:3.11-slim

WORKDIR /frontend

COPY requirements.txt /frontend/requirements.txt
RUN python -m pip install --upgrade pip && pip install -r /frontend/requirements.txt

COPY ./dashboard.py /frontend/dashboard.py

EXPOSE 8501

CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
