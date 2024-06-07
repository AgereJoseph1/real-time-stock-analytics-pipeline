FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --default-timeout=100 -r requirements.txt


COPY data_producer.py data_producer.py

CMD ["python", "data_producer.py"]
