# Databricks notebook: Gold star schema
#
# Purpose:
# Build fact and dimension tables optimized for Synapse SQL and Power BI reporting.

from pyspark.sql import functions as F

silver_path = "abfss://silver@<storage-account-name>.dfs.core.windows.net/adventureworks"
gold_path = "abfss://gold@<storage-account-name>.dfs.core.windows.net"

sales_header = spark.read.parquet(f"{silver_path}/SalesOrderHeader")
sales_detail = spark.read.parquet(f"{silver_path}/SalesOrderDetail")
product = spark.read.parquet(f"{silver_path}/Product")
customer = spark.read.parquet(f"{silver_path}/Customer")
territory = spark.read.parquet(f"{silver_path}/SalesTerritory")

fact_sales = (
    sales_detail.alias("d")
    .join(sales_header.alias("h"), "SalesOrderID", "inner")
    .join(product.select("ProductID", "StandardCost"), "ProductID", "left")
    .select(
        F.col("d.SalesOrderID"),
        F.col("d.SalesOrderDetailID"),
        F.col("h.OrderDate"),
        F.col("h.CustomerID"),
        F.col("d.ProductID"),
        F.col("h.TerritoryID"),
        F.col("d.OrderQty"),
        F.col("d.UnitPrice"),
        F.col("d.UnitPriceDiscount"),
        F.col("d.LineTotal"),
        F.col("StandardCost"),
        (F.col("d.LineTotal") - (F.col("d.OrderQty") * F.col("StandardCost"))).alias("Profit"),
    )
)

dim_product = product.select(
    "ProductID",
    F.col("Name").alias("ProductName"),
    "ProductNumber",
    "StandardCost",
    "ListPrice",
)

dim_customer = customer.select("CustomerID", "AccountNumber").withColumn("CustomerName", F.col("AccountNumber")).withColumn("CustomerType", F.lit("AdventureWorks Customer"))

dim_territory = territory.select(
    "TerritoryID",
    F.col("Name").alias("TerritoryName"),
    "CountryRegionCode",
    F.col("Group").alias("TerritoryGroup"),
)

dim_date = (
    fact_sales.select(F.col("OrderDate").alias("Date"))
    .dropDuplicates()
    .filter(F.col("Date").isNotNull())
    .withColumn("DateKey", F.date_format("Date", "yyyyMMdd").cast("int"))
    .withColumn("Year", F.year("Date"))
    .withColumn("Quarter", F.quarter("Date"))
    .withColumn("MonthNumber", F.month("Date"))
    .withColumn("MonthName", F.date_format("Date", "MMMM"))
    .withColumn("DayOfMonth", F.dayofmonth("Date"))
)

gold_tables = {
    "FactSales": fact_sales,
    "DimProduct": dim_product,
    "DimCustomer": dim_customer,
    "DimTerritory": dim_territory,
    "DimDate": dim_date,
}

for table_name, df in gold_tables.items():
    df.write.mode("overwrite").parquet(f"{gold_path}/{table_name}")
    print(f"Wrote gold table {table_name}")
