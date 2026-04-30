# Architecture

## Overview

This project uses a lakehouse-style architecture on Azure. Raw AdventureWorks data is copied into Azure storage, transformed with PySpark, exposed through SQL, and visualized in Power BI.

```text
Source Data
  AdventureWorks CSV or SQL export

Ingestion
  Azure Data Factory

Storage
  ADLS Gen2
  - bronze
  - silver
  - gold

Transformation
  Azure Databricks
  - PySpark cleaning
  - data quality checks
  - star-schema preparation

Serving
  Azure Synapse serverless SQL
  - external data source
  - external file format
  - views over gold files

Reporting
  Power BI
  - executive KPIs
  - regional sales
  - product profitability
  - customer trends
```

## Why Bronze, Silver, Gold?

The medallion pattern separates data by readiness.

`Bronze` preserves raw data exactly as received. This gives us a recovery point if a cleaning rule is wrong.

`Silver` contains cleaned and standardized data. Examples include fixed data types, removed duplicates, validated keys, and normalized date columns.

`Gold` contains business-ready tables. For this project, the gold layer is a star schema optimized for Power BI reporting.

## Why Star Schema?

A star schema separates measurable business events from descriptive lookup tables.

Fact table:

- `FactSales`: revenue, quantity, cost, profit, order count

Dimension tables:

- `DimDate`: year, quarter, month, day
- `DimProduct`: product, category, subcategory
- `DimCustomer`: customer attributes
- `DimTerritory`: region and country

This design usually improves reporting clarity and Power BI performance because filters flow from dimensions into the fact table.
