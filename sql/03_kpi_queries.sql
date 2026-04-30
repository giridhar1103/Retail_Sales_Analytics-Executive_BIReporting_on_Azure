-- SQL practice and validation queries for the executive dashboard.

USE RetailSalesAnalytics;
GO

-- 1. Executive KPI summary
SELECT
    SUM(LineTotal) AS TotalRevenue,
    SUM(Profit) AS TotalProfit,
    COUNT(DISTINCT SalesOrderID) AS TotalOrders,
    SUM(OrderQty) AS UnitsSold,
    SUM(Profit) / NULLIF(SUM(LineTotal), 0) AS ProfitMargin
FROM gold.FactSales;
GO

-- 2. Revenue by year and quarter
SELECT
    d.Year,
    d.Quarter,
    SUM(f.LineTotal) AS TotalRevenue,
    SUM(f.Profit) AS TotalProfit
FROM gold.FactSales f
JOIN gold.DimDate d
    ON f.OrderDate = d.Date
GROUP BY
    d.Year,
    d.Quarter
ORDER BY
    d.Year,
    d.Quarter;
GO

-- 3. Regional revenue ranking
SELECT
    t.TerritoryGroup,
    t.TerritoryName,
    SUM(f.LineTotal) AS TotalRevenue,
    COUNT(DISTINCT f.SalesOrderID) AS TotalOrders
FROM gold.FactSales f
JOIN gold.DimTerritory t
    ON f.TerritoryID = t.TerritoryID
GROUP BY
    t.TerritoryGroup,
    t.TerritoryName
ORDER BY
    TotalRevenue DESC;
GO

-- 4. Product profitability
SELECT
    p.CategoryName,
    p.SubcategoryName,
    p.ProductName,
    SUM(f.LineTotal) AS TotalRevenue,
    SUM(f.Profit) AS TotalProfit,
    SUM(f.Profit) / NULLIF(SUM(f.LineTotal), 0) AS ProfitMargin
FROM gold.FactSales f
JOIN gold.DimProduct p
    ON f.ProductID = p.ProductID
GROUP BY
    p.CategoryName,
    p.SubcategoryName,
    p.ProductName
ORDER BY
    TotalProfit DESC;
GO

-- 5. Year-over-year revenue using a window function
WITH yearly_revenue AS (
    SELECT
        d.Year,
        SUM(f.LineTotal) AS TotalRevenue
    FROM gold.FactSales f
    JOIN gold.DimDate d
        ON f.OrderDate = d.Date
    GROUP BY d.Year
)
SELECT
    Year,
    TotalRevenue,
    LAG(TotalRevenue) OVER (ORDER BY Year) AS PreviousYearRevenue,
    (TotalRevenue - LAG(TotalRevenue) OVER (ORDER BY Year))
        / NULLIF(LAG(TotalRevenue) OVER (ORDER BY Year), 0) AS YoYGrowth
FROM yearly_revenue
ORDER BY Year;
GO
