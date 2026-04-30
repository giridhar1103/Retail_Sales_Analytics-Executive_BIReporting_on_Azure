-- Synapse serverless SQL setup for querying ADLS Gen2 gold files.
-- Replace the storage account name before running.

CREATE DATABASE RetailSalesAnalytics;
GO

USE RetailSalesAnalytics;
GO

CREATE SCHEMA gold;
GO

CREATE EXTERNAL DATA SOURCE RetailSalesLake
WITH (
    LOCATION = 'https://<storage-account-name>.dfs.core.windows.net/gold'
);
GO

CREATE EXTERNAL FILE FORMAT ParquetFileFormat
WITH (
    FORMAT_TYPE = PARQUET
);
GO
