# Databricks notebook: Bronze ingestion
#
# Purpose:
# Read raw AdventureWorks files and preserve them in the bronze layer.
# Bronze data should stay close to the source so we can reprocess if logic changes.

from pyspark.sql import functions as F

bronze_path = "abfss://bronze@<storage-account-name>.dfs.core.windows.net/adventureworks"

source_files = {
    "SalesOrderHeader": "SalesOrderHeader.csv",
    "SalesOrderDetail": "SalesOrderDetail.csv",
    "Product": "Product.csv",
    "ProductCategory": "ProductCategory.csv",
    "ProductSubcategory": "ProductSubcategory.csv",
    "Customer": "Customer.csv",
    "SalesTerritory": "SalesTerritory.csv",
}

for table_name, file_name in source_files.items():
    source_path = f"{bronze_path}/raw/{file_name}"
    target_path = f"{bronze_path}/tables/{table_name}"

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(source_path)
        .withColumn("_ingested_at", F.current_timestamp())
        .withColumn("_source_file", F.lit(file_name))
    )

    df.write.mode("overwrite").parquet(target_path)

    print(f"Wrote bronze table {table_name} to {target_path}")
