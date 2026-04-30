# Databricks notebook: Data quality checks
#
# Purpose:
# Validate cleaned and modeled data before it is used by Synapse and Power BI.

gold_path = "abfss://gold@<storage-account-name>.dfs.core.windows.net"

fact_sales = spark.read.parquet(f"{gold_path}/FactSales")
dim_product = spark.read.parquet(f"{gold_path}/DimProduct")
dim_customer = spark.read.parquet(f"{gold_path}/DimCustomer")
dim_territory = spark.read.parquet(f"{gold_path}/DimTerritory")
dim_date = spark.read.parquet(f"{gold_path}/DimDate")

checks = []

checks.append(("FactSales row count > 0", fact_sales.count() > 0))
checks.append(("FactSales SalesOrderID not null", fact_sales.filter("SalesOrderID IS NULL").count() == 0))
checks.append(("FactSales ProductID not null", fact_sales.filter("ProductID IS NULL").count() == 0))
checks.append(("FactSales LineTotal non-negative", fact_sales.filter("LineTotal < 0").count() == 0))
checks.append(("DimProduct ProductID unique", dim_product.select("ProductID").distinct().count() == dim_product.count()))
checks.append(("DimCustomer CustomerID unique", dim_customer.select("CustomerID").distinct().count() == dim_customer.count()))
checks.append(("DimTerritory TerritoryID unique", dim_territory.select("TerritoryID").distinct().count() == dim_territory.count()))
checks.append(("DimDate Date unique", dim_date.select("Date").distinct().count() == dim_date.count()))

failed_checks = [name for name, passed in checks if not passed]

for name, passed in checks:
    print(f"{'PASS' if passed else 'FAIL'}: {name}")

if failed_checks:
    raise ValueError(f"Data quality checks failed: {failed_checks}")

print("All data quality checks passed.")
