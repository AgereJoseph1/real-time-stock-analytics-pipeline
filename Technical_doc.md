### Overview

This guide provides detailed instructions on how to set up a real-time data pipeline that fetches stock data from an external API, processes it through Kafka, and stores it in a PostgreSQL database. The implementation uses Docker to containerize the application, making it easy to deploy and manage.

### Project Structure

```
DATA_ENGINEERING_CAPSTONE_PROJECT/
├── data-consumer/
│   ├── data_consumer.py
│   ├── Dockerfile
│   └── requirements.txt
├── data-producer/
│   ├── data_producer.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

### Step-by-Step Setup

#### 1. Prerequisites

- Ensure Docker and Docker Compose are installed on your machine.
- Have a working internet connection to pull Docker images and install dependencies.

#### 2. Clone the Repository

1. **Clone the repository from GitHub**:

    ```bash
    git clone <repository_url>
    cd DATA_ENGINEERING_CAPSTONE_PROJECT
    ```

#### 3. Configuration

1. **Configure Environment Variables**:
    - Ensure you have the correct API key, stock symbol, and Kafka server details in the `data_producer.py` script.
    - Ensure you have the correct Kafka server and PostgreSQL database details in the `data_consumer.py` script.

2. **Ensure Directory Structure**:
    - Verify that the directory structure matches the provided project structure.

#### 4. Build and Start Docker Containers

1. **Build and start the Docker containers using Docker Compose**:

    ```bash
    docker-compose up --build
    ```

    This command will:
    - Build the Docker images for the data producer and consumer.
    - Start the Kafka and Zookeeper services.
    - Start the PostgreSQL database service.
    - Start the data producer and consumer services.

2. **Check Logs**:
    - Monitor the logs to ensure all services are running correctly:

    ```bash
    docker-compose logs -f
    ```

#### 5. Verify Setup

1. **Verify Kafka and Zookeeper**:
    - Ensure that Kafka and Zookeeper are running without errors.

2. **Verify PostgreSQL**:
    - Ensure that PostgreSQL is running and accessible.
    - You can use a database client like `psql` or any PostgreSQL GUI client to connect and verify the database.

3. **Verify Data Flow**:
    - Ensure that the data producer is successfully fetching data from the API and sending it to Kafka.
    - Ensure that the data consumer is receiving data from Kafka and storing it in PostgreSQL.

#### 6. Stopping the Setup

1. **Stop the Docker containers**:

    ```bash
    docker-compose down
    ```

    This command will stop all running containers and remove them.

### Additional Tips

- **Managing Dependencies**: If you need to add additional Python dependencies, update the `requirements.txt` files in both `data-producer` and `data-consumer` directories and rebuild the Docker images.
- **Scaling**: You can scale the data consumer service by adjusting the `docker-compose.yml` file to run multiple instances if needed.

### Troubleshooting

- **Network Issues**: Ensure Docker has access to the internet to pull necessary images.
- **Permission Issues**: Ensure you have the necessary permissions to run Docker commands.
- **Log Monitoring**: Use the `docker-compose logs` command to check for errors and debug issues.

By following these steps, you should be able to set up and run the real-time data pipeline on your local machine. 