import json
from kafka import KafkaConsumer
from sqlalchemy import create_engine, Column, String, Numeric, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration
KAFKA_TOPIC = 'stock-data'
KAFKA_SERVER = 'kafka:9092'
POSTGRES_DB = 'stock_data'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'password'
POSTGRES_HOST = 'postgres'
POSTGRES_PORT = '5432'

# Set up SQLAlchemy
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define the Stocks table
class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(String, primary_key=True, autoincrement=True)
    timestamp = Column(TIMESTAMP)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    volume = Column(Numeric)

# Create the table
Base.metadata.create_all(engine)

# Initialize Kafka consumer
consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER, auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    stock_data = message.value
    stock_record = Stock(
        timestamp=stock_data['timestamp'],
        open=stock_data['open'],
        high=stock_data['high'],
        low=stock_data['low'],
        close=stock_data['close'],
        volume=stock_data['volume']
    )
    session.add(stock_record)
    session.commit()
