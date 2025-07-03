from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col 
from pyspark.sql.types import StructType, IntegerType, StringType

spark = SparkSession.builder \
.appName("KafkaToMySQL") \
.master("local[*]") \
.getOrCreate()

schema = StructType() \
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
parsed_df = json_df.select(from_json(col("json"), schema).alias("data")).select("data.*")


def write_to_mysql (batch_df, batch_id):
    print("🔥 Spark received a batch, writing to MySQL...")
    batch_df.show()
    batch_df.write \
    .format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/ecommerce") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", "orders") \
    .option("user", "root") \
    .option("password", "sunita123") \
    .mode("append") \
    .save()


query = parsed_df.writeStream \
.foreachBatch(write_to_mysql) \
.outputMode("append") \
.start()

query.awaitTermination()
