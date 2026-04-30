# Data Dictionary

This project uses AdventureWorks-style sales data.

## FactSales

| Column | Description |
| --- | --- |
| SalesOrderID | Sales order identifier |
| SalesOrderDetailID | Sales order line identifier |
| OrderDate | Date the order was placed |
| CustomerID | Customer identifier |
| ProductID | Product identifier |
| TerritoryID | Sales territory identifier |
| OrderQty | Quantity ordered |
| UnitPrice | Unit price before discount |
| UnitPriceDiscount | Discount applied to unit price |
| LineTotal | Revenue for the sales line |
| StandardCost | Product cost used for profit analysis |
| Profit | LineTotal minus estimated product cost |

## DimDate

| Column | Description |
| --- | --- |
| DateKey | Date identifier |
| Date | Calendar date |
| Year | Calendar year |
| Quarter | Calendar quarter |
| MonthNumber | Month number |
| MonthName | Month name |
| DayOfMonth | Day of month |

## DimProduct

| Column | Description |
| --- | --- |
| ProductID | Product identifier |
| ProductName | Product name |
| ProductNumber | Product number |
| CategoryName | Product category |
| SubcategoryName | Product subcategory |
| StandardCost | Product cost |
| ListPrice | Product list price |

## DimCustomer

| Column | Description |
| --- | --- |
| CustomerID | Customer identifier |
| AccountNumber | Customer account number |
| CustomerName | Customer or store name |
| CustomerType | Individual or store customer grouping |

## DimTerritory

| Column | Description |
| --- | --- |
| TerritoryID | Sales territory identifier |
| TerritoryName | Territory name |
| CountryRegionCode | Country or region code |
| TerritoryGroup | Territory group |
