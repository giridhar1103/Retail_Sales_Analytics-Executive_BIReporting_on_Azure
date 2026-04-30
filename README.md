# Retail Sales Analytics & Executive BI Reporting on Azure

This project builds an end-to-end Azure analytics pipeline for AdventureWorks retail sales data and turns it into an executive Power BI reporting model.

## Project Goal

The goal is to support this portfolio/resume story with real implementation artifacts:

- Build an Azure data pipeline using Azure Data Factory, ADLS Gen2, Databricks, Synapse serverless SQL, and Power BI.
- Model a star-schema analytics layer for sales, product, customer, territory, and date reporting.
- Create executive BI dashboards that surface sales KPIs, regional revenue trends, product profitability, and customer insights.
- Implement PySpark data quality checks and secure service credentials with Azure Key Vault and Azure role-based access control.

## Target Architecture

```text
AdventureWorks source data
        -> Azure Data Factory
        -> ADLS Gen2 bronze layer
        -> Azure Databricks PySpark cleaning
        -> ADLS Gen2 silver layer
        -> Gold star-schema tables
        -> Azure Synapse serverless SQL
        -> Power BI executive dashboard
```

## Repository Structure

```text
adf/                 Azure Data Factory pipeline exports and notes
data/sample/         Small sample files for local development and documentation
docs/                Architecture, setup guide, data dictionary, and performance notes
notebooks/           Databricks PySpark notebooks for bronze, silver, gold, and quality checks
powerbi/             DAX measures, dashboard screenshots, and Power BI notes
sql/                 Synapse SQL scripts for external data access, star schema, and KPI queries
```

## Learning Roadmap

1. Azure fundamentals: resource groups, storage accounts, containers, permissions, and cost control.
2. Data lake design: bronze, silver, and gold layers.
3. Azure Data Factory: linked services, datasets, copy activity, and pipeline monitoring.
4. Databricks and PySpark: reading raw data, cleaning records, validating quality, and writing curated data.
5. SQL modeling: facts, dimensions, star schema design, joins, aggregations, and KPI queries.
6. Synapse serverless SQL: querying curated files from the lake.
7. Power BI: relationships, DAX measures, executive dashboards, and performance tuning.

## Current Status

This repository is being built step by step. The first milestone is to create the project scaffold and learning notes before deploying Azure resources.

## Cost Control

All Azure resources should be created inside one resource group, for example `rg-retail-bi-dev`. Delete that resource group when done testing to avoid unnecessary charges. Prefer serverless or free-tier-friendly services where possible.
