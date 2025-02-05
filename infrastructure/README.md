
### **1. Infrastructure Setup Guide 
# Infrastructure Setup Guide

This folder contains the **Infrastructure as Code (IaC)** setup for deploying AWS resources using **AWS CDK** and **Terraform**.

## **1. Prerequisites**
Before deploying, ensure you have:
- **AWS CLI** installed and configured (`aws configure`).
- **AWS CDK** installed (`npm install -g aws-cdk`).
- **Terraform** installed (`terraform -v`).
- **Python 3.8+** with required dependencies (`pip install -r ../requirements.txt`).

---

## **2. Deploy Infrastructure Using AWS CDK**
To deploy infrastructure using **AWS CDK**, follow these steps:

### **Step 1: Install AWS CDK**
```sh
npm install -g aws-cdk
```

### **Step 2: Navigate to the Infrastructure Folder**
```sh
cd infrastructure
```

### **Step 3: Bootstrap AWS CDK (Run Once)**
```sh
cdk bootstrap
```

### **Step 4: Deploy Infrastructure**
```sh
cdk deploy
```

### **Step 5: Verify Deployment**
```sh
cdk list
```
---

## **3. Deploy Infrastructure Using Terraform**
Alternatively, you can use Terraform to deploy the infrastructure.

### **Step 1: Navigate to the Terraform Folder**
```sh
cd terraform
```

### **Step 2: Initialize Terraform**
```sh
terraform init
```

### **Step 3: Validate Terraform Configuration**
```sh
terraform validate
```

### **Step 4: Deploy Infrastructure**
```sh
terraform apply -auto-approve
```

### **Step 5: Verify Deployment Outputs**
```sh
terraform output
```

---

## **4. AWS Resources Deployed**
This setup deploys the following AWS resources:
- **S3 Bucket** for data storage.
- **AWS Glue Database** for metadata.
- **AWS Lambda** for ETL automation.
- **Redshift Cluster** for analytics.
- **Airflow DAG** for orchestration.

---

## **5. Destroying Infrastructure**
To clean up AWS resources, use:
```sh
cdk destroy  # For AWS CDK
terraform destroy -auto-approve  # For Terraform
```

For any issues, check **AWS CloudWatch Logs** or use **AWS Console** to debug.

---

### **2. Terraform Setup Guide - `infrastructure/terraform/README.md`**

# Terraform Infrastructure Deployment

This folder contains **Terraform scripts** for deploying AWS resources.

## **1. Prerequisites**
Ensure the following tools are installed:
- **Terraform** (`terraform -v`)
- **AWS CLI** (`aws configure`)
- **Python 3.8+** (`pip install -r ../../requirements.txt`)

---

## **2. Terraform Deployment Steps**

### **Step 1: Initialize Terraform**
```sh
terraform init
```

### **Step 2: Validate Terraform Configuration**
```sh
terraform validate
```

### **Step 3: Deploy AWS Infrastructure**
```sh
terraform apply -auto-approve
```

### **Step 4: Check Deployed Resources**
```sh
terraform output
```

---

## **3. AWS Resources Managed**
Terraform deploys:
- **S3 Bucket** (`media-etl-data-bucket`)
- **IAM Roles & Policies** for AWS Lambda
- **AWS Redshift Cluster**
- **AWS Lambda Function**
- **Glue Catalog Database**
- **Airflow DAG (MWAA)**

---

## **4. Destroying Resources**
To remove all AWS resources, run:
```sh
terraform destroy -auto-approve
```
This will **delete all resources** deployed via Terraform.

---

## **5. Troubleshooting**
- **Authentication Issues**: Run `aws configure` to set up AWS credentials.
- **Deployment Errors**: Use `terraform plan` to preview changes.
- **Logs & Debugging**: Check AWS Console logs for Lambda & Redshift.

For detailed logs, check **AWS CloudWatch**.
```

