# Databricks notebook: Silver cleaning
#
# Purpose:
# Read bronze data, standardize column types, remove duplicates, and write clean silver data.

from pyspark.sql import functions as F

bronze_path = "abfss://bronze@<storage-account-name>.dfs.core.windows.net/adventureworks/tables"
silver_path = "abfss://silver@<storage-account-name>.dfs.core.windows.net/adventureworks"

sales_header = spark.read.parquet(f"{bronze_path}/SalesOrderHeader")
sales_detail = spark.read.parquet(f"{bronze_path}/SalesOrderDetail")
product = spark.read.parquet(f"{bronze_path}/Product")
customer = spark.read.parquet(f"{bronze_path}/Customer")
territory = spark.read.parquet(f"{bronze_path}/SalesTerritory")

sales_header_clean = (
    sales_header
    .withColumn("SalesOrderID", F.col("SalesOrderID").cast("int"))
    .withColumn("CustomerID", F.col("CustomerID").cast("int"))
    .withColumn("TerritoryID", F.col("TerritoryID").cast("int"))
    .withColumn("OrderDate", F.to_date("OrderDate"))
    .dropDuplicates(["SalesOrderID"])
    .filter(F.col("SalesOrderID").isNotNull())
)

sales_detail_clean = (
    sales_detail
    .withColumn("SalesOrderID", F.col("SalesOrderID").cast("int"))
    .withColumn("SalesOrderDetailID", F.col("SalesOrderDetailID").cast("int"))
    .withColumn("ProductID", F.col("ProductID").cast("int"))
    .withColumn("OrderQty", F.col("OrderQty").cast("int"))
    .withColumn("UnitPrice", F.col("UnitPrice").cast("decimal(18,2)"))
    .withColumn("UnitPriceDiscount", F.col("UnitPriceDiscount").cast("decimal(18,4)"))
    .withColumn("LineTotal", F.col("LineTotal").cast("decimal(18,2)"))
    .dropDuplicates(["SalesOrderID", "SalesOrderDetailID"])
    .filter(F.col("SalesOrderID").isNotNull())
)

product_clean = (
    product
    .withColumn("ProductID", F.col("ProductID").cast("int"))
    .withColumn("StandardCost", F.col("StandardCost").cast("decimal(18,2)"))
    .withColumn("ListPrice", F.col("ListPrice").cast("decimal(18,2)"))
    .dropDuplicates(["ProductID"])
    .filter(F.col("ProductID").isNotNull())
)

customer_clean = customer.withColumn("CustomerID", F.col("CustomerID").cast("int")).dropDuplicates(["CustomerID"]).filter(F.col("CustomerID").isNotNull())
territory_clean = territory.withColumn("TerritoryID", F.col("TerritoryID").cast("int")).dropDuplicates(["TerritoryID"]).filter(F.col("TerritoryID").isNotNull())

silver_tables = {
    "SalesOrderHeader": sales_header_clean,
    "SalesOrderDetail": sales_detail_clean,
    "Product": product_clean,
    "Customer": customer_clean,
    "SalesTerritory": territory_clean,
}

for table_name, df in silver_tables.items():
    df.write.mode("overwrite").parquet(f"{silver_path}/{table_name}")
    print(f"Wrote silver table {table_name}")
