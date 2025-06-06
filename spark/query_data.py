from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Consulta IoT") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

df = spark.read.format("delta").load("/tmp/delta/bronze/iot_sensores")

print("\n📊 Exibindo os 10 últimos registros ordenados por timestamp:")
df.orderBy("timestamp", ascending=False).show(10, truncate=False)
