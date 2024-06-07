FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

# Increase the timeout for pip install
RUN pip install --default-timeout=100 -r requirements.txt

COPY data_consumer.py data_consumer.py

CMD ["python", "data_consumer.py"]
