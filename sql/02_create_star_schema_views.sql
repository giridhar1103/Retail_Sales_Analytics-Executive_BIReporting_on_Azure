-- Gold-layer star schema views.
-- These views let Power BI query curated parquet files through Synapse serverless SQL.

USE RetailSalesAnalytics;
GO

CREATE OR ALTER VIEW gold.FactSales AS
SELECT
    SalesOrderID,
    SalesOrderDetailID,
    CAST(OrderDate AS date) AS OrderDate,
    CustomerID,
    ProductID,
    TerritoryID,
    CAST(OrderQty AS int) AS OrderQty,
    CAST(UnitPrice AS decimal(18, 2)) AS UnitPrice,
    CAST(UnitPriceDiscount AS decimal(18, 4)) AS UnitPriceDiscount,
    CAST(LineTotal AS decimal(18, 2)) AS LineTotal,
    CAST(StandardCost AS decimal(18, 2)) AS StandardCost,
    CAST(Profit AS decimal(18, 2)) AS Profit
FROM OPENROWSET(
    BULK 'FactSales/',
    DATA_SOURCE = 'RetailSalesLake',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW gold.DimProduct AS
SELECT
    ProductID,
    ProductName,
    ProductNumber,
    CategoryName,
    SubcategoryName,
    CAST(StandardCost AS decimal(18, 2)) AS StandardCost,
    CAST(ListPrice AS decimal(18, 2)) AS ListPrice
FROM OPENROWSET(
    BULK 'DimProduct/',
    DATA_SOURCE = 'RetailSalesLake',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW gold.DimCustomer AS
SELECT
    CustomerID,
    AccountNumber,
    CustomerName,
    CustomerType
FROM OPENROWSET(
    BULK 'DimCustomer/',
    DATA_SOURCE = 'RetailSalesLake',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW gold.DimTerritory AS
SELECT
    TerritoryID,
    TerritoryName,
    CountryRegionCode,
    TerritoryGroup
FROM OPENROWSET(
    BULK 'DimTerritory/',
    DATA_SOURCE = 'RetailSalesLake',
    FORMAT = 'PARQUET'
) AS rows;
GO

CREATE OR ALTER VIEW gold.DimDate AS
SELECT
    DateKey,
    CAST(Date AS date) AS Date,
    Year,
    Quarter,
    MonthNumber,
    MonthName,
    DayOfMonth
FROM OPENROWSET(
    BULK 'DimDate/',
    DATA_SOURCE = 'RetailSalesLake',
    FORMAT = 'PARQUET'
) AS rows;
GO
