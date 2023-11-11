FROM python:3.11

WORKDIR /app

RUN mkdir -p src/
COPY src/ src/

COPY requirements.txt requirements.txt
RUN pip install -r requirements

RUN mkdir -p migrations/
COPY alembic.ini .
