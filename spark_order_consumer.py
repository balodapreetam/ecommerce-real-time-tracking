from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder \
    .appName("KafkaOrderConsumer") \
    .master("local[*]") \
    .getOrCreate()

order_schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("order_id", StringType()) \
    .add("item_name", StringType()) \
    .add("category", StringType()) \
    .add("price", IntegerType()) \
    .add("timestamp", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders") \
    .option("startingOffsets", "latest") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING) as json")

orders_df = json_df.select(
    from_json(col("json"), order_schema).alias("data")
).select("data.*")

# 🔄 Console Output Instead of CSV
query = orders_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()
