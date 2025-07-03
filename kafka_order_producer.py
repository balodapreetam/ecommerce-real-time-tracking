from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

categories = ["Electronics", "Clothing", "Books"]
items = ["Mouse", "T-shirt", "Notebook"]
order_id = 4400

while True:
    data = {
        "user_id": random.randint(10000, 99999),
        "order_id": f"ORD{order_id}",
        "item_name": random.choice(items),
        "category": random.choice(categories),
        "price": random.randint(100, 1000),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    print("Sending:", data)
    producer.send("orders", data)
    order_id += 1
    time.sleep(3)





