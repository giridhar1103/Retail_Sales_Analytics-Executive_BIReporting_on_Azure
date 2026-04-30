# Setup Guide

This guide is the step-by-step build path for the project.

## Step 1: Create The Azure Resource Group

A resource group is a logical folder for Azure resources. For this project, every Azure service should live in one resource group so cost tracking and cleanup are simple.

Recommended name:

```text
rg-retail-bi-dev
```

Why this matters:

- It keeps all project resources together.
- It makes cost tracking easier.
- It lets you delete all project resources at once when testing is done.

## Step 2: Create ADLS Gen2 Storage

Azure Data Lake Storage Gen2 is where the raw, cleaned, and curated data files will live.

Recommended containers:

```text
bronze
silver
gold
scripts
```

Layer meaning:

- `bronze`: raw source files copied into Azure.
- `silver`: cleaned and standardized files.
- `gold`: business-ready tables designed for reporting.

## Step 3: Create Azure Data Factory

Azure Data Factory orchestrates movement of data. In this project, its first job is to copy AdventureWorks source files into the bronze layer.

Core terms:

- Linked service: connection information for a system.
- Dataset: a named representation of data.
- Pipeline: a workflow made of activities.
- Copy activity: an activity that moves data from a source to a sink.

## Step 4: Create Databricks Workspace

Databricks runs PySpark transformations. It will read bronze files, clean them, run quality checks, and write silver/gold outputs.

Use the smallest available compute option. Stop compute when not in use.

## Step 5: Create Synapse Serverless SQL Access

Synapse serverless SQL lets us query files in the data lake with T-SQL without running a dedicated SQL pool.

We will use it to expose gold-layer files as SQL views for Power BI.

## Step 6: Build Power BI Model

Power BI connects to the gold star schema. The model should include:

- FactSales
- DimDate
- DimProduct
- DimCustomer
- DimTerritory

## Step 7: Document Evidence

The final repository should include architecture notes, ADF pipeline export, Databricks notebooks, Synapse SQL scripts, DAX measures, Power BI screenshots, and performance notes.
