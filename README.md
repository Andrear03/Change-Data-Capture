# Change-Data-Capture

# Change Data Capture with Debezium

## Introduction

This project demonstrates how to implement Change Data Capture (CDC) using **Debezium**, an open-source platform designed to capture real-time database changes. It integrates with **Apache Kafka** to handle data events and provides a simple Python consumer to process these events.

## Features

- Real-time database change capture.
- Synchronization between MySQL and Kafka.
- Example of a Python consumer to process Kafka events.

## Technologies Used

- **Debezium**: For CDC.
- **Apache Kafka**: To stream and store data events.
- **Docker**: To deploy services easily.
- **Python**: For building the consumer application.

## Project Structure

ChangeDataCapture/ ├── consumer.py # Python Kafka consumer script ├── docker-compose.yml # Docker configuration file └── README.md # Project documentation


## Getting Started

### Prerequisites

Make sure you have the following installed:
- [Docker](https://www.docker.com/)
- [Python 3.8+](https://www.python.org/)

### Setup

1. Clone the repository:

   ```markdown
   git clone https://github.com/Andrear03/Change-Data-Capture.git
   cd Change-Data-Capture

    Start the services using Docker Compose:

docker-compose up -d

Set up the Debezium connector:

curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
  "name": "mysql-connector",
  "config": {
    "connector.class": "io.debezium.connector.mysql.MySqlConnector",
    "database.hostname": "mysql",
    "database.port": "3306",
    "database.user": "debezium",
    "database.password": "dbz",
    "database.server.id": "184054",
    "database.server.name": "inventory",
    "database.include.list": "inventory",
    "include.schema.changes": "true"
  }
}'

Verify events in Kafka:

docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic inventory.inventory.customers --from-beginning

Run the Python consumer:

    python3 consumer.py

Python Consumer Example

The consumer listens to changes on the inventory.inventory.customers topic in Kafka. Below is the script used:

from kafka import KafkaConsumer
import json

# Configure the consumer
consumer = KafkaConsumer(
    'inventory.inventory.customers',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Connected to Kafka server. Waiting for events...\n")

# Process messages from the topic
for message in consumer:
    print(f"Received event:\n{json.dumps(message.value, indent=4)}\n")

Contributing

Contributions are welcome! If you want to improve the project or report issues, feel free to submit a pull request or open an issue.
License

This project is licensed under the MIT License. See the LICENSE file for details.
