FROM python:3.11-slim

WORKDIR /app

# system deps for psycopg2
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && pip install -r /app/requirements.txt

# copy app code (mounted in dev by docker-compose)
COPY ./app /app/app

# small wait helper
COPY wait_for_db.py /app/wait_for_db.py

EXPOSE 8000

# entrypoint: wait for DB then start uvicorn
CMD ["sh", "-c", "python /app/wait_for_db.py && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
