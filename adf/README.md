# Azure Data Factory

This folder will contain the exported Azure Data Factory pipeline JSON after the pipeline is created in Azure.

## First Pipeline Goal

Copy AdventureWorks source files into the ADLS Gen2 bronze container.

Expected flow:

```text
Source files -> ADF copy activity -> ADLS Gen2 bronze/adventureworks/raw
```

## Terms

- Linked service: connection to a system, such as ADLS Gen2.
- Dataset: source or destination data definition.
- Pipeline: workflow containing activities.
- Copy activity: movement of data from source to destination.

## Artifact To Add Later

```text
adf/adventureworks_ingestion_pipeline.json
```
