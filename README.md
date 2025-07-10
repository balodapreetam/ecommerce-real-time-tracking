# E_Commerce Order Tracking Pipeline

A real-time data pipeline using Apache Kafka, Apache Spark, and My SQL foe tracking e-commerce orders.

## 🚀 Teck Stack 
- Apache Kafka
- Apache Spark Structured Streaming
- MySQL
- Python

## 📦 Project Overview
This project simulates a real-time e-commerce environment where order data is:
1. **Produced** via Kafka.
2. **Consumed and processed** by Spark.
3. **Stored** in MySQL for persistent analytics or dashboarding.

## 📌 Workflow
1. 🧾 Kafka Producer sends JSON messages representing order events.
2. 🔄 Spark Structured Streaming consumes the Kafka topic in micro-batches.
3. 🛢️ Parsed data is written and appended to a MySQL table.

---

## 🔧 Sample Input Message
json
{
  "user_id": 11111,
  "order_id": "ORD002",
  "item_name": "Shoes",
  "category": "Footwear",
  "price": 1499,
  "timestamp": "2025-06-25 14:00:00"
} ```

🗃️ MySQL Table Structure
Column Name                Data type 
user_id                    INT
order_id                   VARCHAR
item_name                  VARCHAR
category                   VARCHAR
price                      INT
timestamp                  DATETIME

💡 Features
	•	Real-time stream processing using Spark.
	•	JSON parsing and schema enforcement.
	•	Batch-wise writing to MySQL.
	•	Easy to extend with Apache Airflow and dashboards.

 ## 📁 Project Files

- `kafka_order_producer.py` – Sends sample order messages to Kafka topic `orders`.
- `spark_to_mysql.py` – Reads Kafka stream and stores processed data in MySQL.
- `spark_order_consumer.py` – (Optional) Displays Kafka messages using Spark, for testing/debugging.

🙋🏻 About Me

I’m a final-year B.Tech student in Data Science 🎓
This project reflects my hands-on learning in real-time data engineering and stream processing.
Actively exploring opportunities to learn and grow in data infrastructure and big data pipelines 🚀

🔗 Connect with me : 
• 💼 http://linkedin.com/in/preetambaloda






