# **NYPD Crime & Arrests Data Pipeline**  

## **Overview**  
This project focuses on designing a scalable and efficient data pipeline for NYPD crime and arrest data. The data is sourced from the NYPD website, updated regularly since June 5, 2018, and initially contained 260,503 records at the time of analysis.  

[![Tableau Dashboard Link](https://img.shields.io/badge/Tableau_Dashboard_Link-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://public.tableauD)

## **Technologies Used**  
![Snowflake](https://img.shields.io/badge/Snowflake-0093F1?style=for-the-badge&logo=snowflake&logoColor=white)
![Alteryx](https://img.shields.io/badge/Alteryx-E84D3D?style=for-the-badge&logoColor=white)
![Azure DataFactory](https://img.shields.io/badge/Azure%20DataFactory-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![ER Studio](https://img.shields.io/badge/ER%20Studio-4EA94B?style=for-the-badge&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## **Problem Statement**  

### **Challenge**  
- The dataset contained missing values, inconsistencies, and data type errors.  
- A robust data model was required to support analytical queries on crime and arrests.  
- Efficient data ingestion, transformation, and loading into Snowflake were needed for large-scale analysis.  

### **Solution**  
- **Dimensional Modeling**: Designed a star schema using **ER Studio** to optimize query performance.  
- **Data Profiling**: Used **yDataProfiling** to assess data quality issues and identify necessary transformations.  
- **Data Cleaning & Transformation**: Applied **Alteryx** workflows to clean and standardize the dataset.  
- **Data Pipeline Implementation**: Built an **Azure Data Factory** pipeline to load transformed data into **Snowflake** efficiently.  

### Step 1: Data Profiling
![Alt text](./screenshots/DataProfling.png)

### Step 2: Dimension Modeling
![Alt text](./models/image.png)

### Step 3: Data Cleaning and Transformation using Alteryx
![Alt text](./screenshots/Alteryx.png)

### Step 4: Azure Data Factory Mapping
![Alt text](./screenshots/ADFMapping.png)

### Step 5: Snowflake Data
![Alt text](./screenshots/snowflakeLoad.png)

### Step 6: Data Visualization and Analysis
![Alt text](./screenshots/NYPDArrests.png)