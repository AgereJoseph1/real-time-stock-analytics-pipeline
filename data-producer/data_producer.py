import requests
import json
from kafka import KafkaProducer
from sqlalchemy import create_engine
import time

# Configuration
API_KEY = 'H7XHHW9KSQCKWX11'
SYMBOL = 'AAPL'
INTERVAL = '1min'
KAFKA_TOPIC = 'stock-data'
KAFKA_SERVER = 'kafka:9092'
DATABASE_URI = 'postgresql://postgres:password@postgres:5432/stock_data'

# Initialize Kafka Producer
print("Initializing Kafka Producer...")
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
print("Kafka Producer initialized.")

def fetch_stock_data():
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval={INTERVAL}&apikey={API_KEY}'
    print(f"Fetching data from {url}")
    response = requests.get(url)
    data = response.json()
    if 'Time Series (1min)' in data:
        return data['Time Series (1min)']
    print("No data found.")
    return None

def create_tables():
    print("Connecting to database...")
    engine = create_engine(DATABASE_URI)
    with engine.connect() as connection:
        print("Creating tables if not exists...")
        connection.execute("""
        CREATE TABLE IF NOT EXISTS stocks (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume INTEGER
        )
        """)
        print("Tables created successfully.")

# Create tables
create_tables()

while True:
    print("Fetching stock data...")
    data = fetch_stock_data()
    if data:
        print("Data fetched, sending to Kafka...")
        for timestamp, values in data.items():
            record = {
                'timestamp': timestamp,
                'open': values['1. open'],
                'high': values['2. high'],
                'low': values['3. low'],
                'close': values['4. close'],
                'volume': values['5. volume']
            }
            producer.send(KAFKA_TOPIC, record)
            print(f'Sent data: {record}')
    else:
        print("No data fetched.")
    print("Sleeping for 60 seconds...")
    time.sleep(60)  
