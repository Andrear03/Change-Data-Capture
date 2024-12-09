from kafka import KafkaConsumer
import json

# Configura el consumidor
consumer = KafkaConsumer(
    'inventory.inventory.customers',  
    bootstrap_servers=['localhost:9092'],  
    auto_offset_reset='earliest', 
    enable_auto_commit=True,  
    group_id='consumer-group', 
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) 
)

print("Conectado al servidor Kafka. Esperando eventos...\n")

# Procesa los mensajes del tema
for message in consumer:
    print(f"Evento recibido:\n{json.dumps(message.value, indent=4)}\n")
