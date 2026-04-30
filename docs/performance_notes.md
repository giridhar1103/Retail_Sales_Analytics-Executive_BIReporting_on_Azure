# Performance Notes

This file will track performance improvements made during the project.

## Baseline

The baseline model is a raw or wide sales table used directly for reporting.

Metrics to capture:

- Power BI refresh duration
- size of imported model
- query duration for common KPIs
- number of relationships and calculated columns

## Optimized Model

The optimized model is a star schema served from the gold layer.

Expected improvements:

- fewer duplicated descriptive columns in the fact table
- clearer relationships
- reusable DAX measures
- faster filtering by date, product, customer, and territory

## Measurement Template

| Test | Baseline | Optimized | Improvement |
| --- | ---: | ---: | ---: |
| Power BI refresh time | TBD | TBD | TBD |
| Total revenue query | TBD | TBD | TBD |
| Regional revenue query | TBD | TBD | TBD |
| Product profitability query | TBD | TBD | TBD |

## Resume Claim Rule

Only claim a specific improvement percentage after measuring it. If the measured improvement is not 40%, update the resume to the real number.
