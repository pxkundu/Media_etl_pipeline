# Media & Entertainment ETL Pipeline

This project is a Proof of Concept (POC) for an automated **ETL pipeline** that extracts data from **Meta (Facebook), YouTube, and Google Analytics (GA4)** APIs, transforms it, and loads it into **AWS S3, Athena, and Redshift** for analysis. The pipeline is scheduled using **Apache Airflow** and **AWS Lambda**, with infrastructure deployed via **AWS CDK and Terraform**.

## **Project Features**
- **Data Extraction**: Fetches data from Meta Graph API, YouTube API, and Google Analytics (GA4) API.
- **Data Transformation**: Cleans, reshapes, and enriches data for analysis.
- **Data Storage**: Saves raw and processed data in **AWS S3**.
- **Querying**: Uses **AWS Athena & Redshift** for analytics.
- **Automation**: Orchestrated using **Airflow & AWS Lambda**.
- **Infrastructure as Code (IaC)**: Deployed via **AWS CDK & Terraform**.
- **Dashboards**: Integrates with **Tableau, Power BI, and Looker**.

---

## **1. Prerequisites**
Ensure you have the following installed:
- **Python 3.8+**
- **AWS CLI** (`pip install awscli`)
- **Terraform** (`brew install terraform` or [download](https://www.terraform.io/downloads.html))
- **AWS CDK** (`npm install -g aws-cdk`)
- **Apache Airflow** (`pip install apache-airflow`)
- **Required Python Packages** (`pip install -r requirements.txt`)

---

## **2. Project Setup**

### **Step 1: Clone the Repository**
```sh
# Clone the repository
git clone https://github.com/pxkundu/Media_etl_pipeline.git
cd Media_etl_pipeline
```

### **Step 2: Set Up Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
```

### **Step 3: Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Step 4: Set Up AWS Credentials**
```sh
aws configure
# Enter your AWS Access Key, Secret Key, Region, and Output format
```

### **Step 5: Deploy Infrastructure (Choose One)**

#### **Option 1: Using AWS CDK**
```sh
cd infrastructure/
cdk bootstrap
cdk deploy
```

#### **Option 2: Using Terraform**
```sh
cd infrastructure/terraform/
terraform init
terraform apply -auto-approve
```

---

## **3. Running the ETL Pipeline**

### **Step 1: Run Data Extraction Scripts**
```sh
python src/extract/fetch_meta.py
python src/extract/fetch_youtube.py
python src/extract/fetch_ga4.py
```

### **Step 2: Run Data Transformation**
```sh
python src/transform/clean_data.py
python src/transform/reshape_data.py
python src/transform/enrich_data.py
```

### **Step 3: Store Processed Data in AWS S3**
```sh
python src/load/store_s3.py
```

### **Step 4: Register Athena Tables**
```sh
python src/load/register_athena.py
```

### **Step 5: Load Data into Redshift (Optional)**
```sh
python src/load/load_redshift.py
```

### **Step 6: Automate with Airflow**
```sh
airflow dags list
airflow dags trigger media_etl_pipeline
```

---

## **4. Running Tests**
```sh
pytest tests/
```

---

## **5. Querying the Data**
### **Run SQL Queries in AWS Athena**
```sql
SELECT * FROM media_analytics.meta_data LIMIT 10;
```

### **Run SQL Queries in AWS Redshift**
```sql
SELECT title, views FROM youtube_analytics ORDER BY views DESC LIMIT 10;
```

---

## **6. Monitoring and Debugging**
- **AWS CloudWatch**: Monitor Lambda and Airflow logs.
- **Athena Query Editor**: Run SQL queries on S3 data.
- **Redshift Query Editor**: Run analytics queries.

---

## **7. Next Steps**
- **Enhance Dashboard Integration** (Tableau, Power BI, Looker).
- **Optimize Query Performance** using partitions & indexes.
- **Implement CI/CD** with GitHub Actions for auto-deployments.

---

## **8. License**
MIT License. Feel free to use and modify.
