# aws-mini-pipeline

This is a small, hands-on project to showcase some key data engineering concepts in a cloud-like environment. It’s simple but practical, designed to demonstrate what I can do in Python, cloud, and DevOps.

---

## What you’ll find here

- **AWS Free Tier concepts** – S3-like storage, a simulated Lambda function, and Terraform for Infrastructure as Code.  
- **Python ETL/ELT** – Read, process, and display CSV data.  
- **Reproducibility** – Everything is versioned and organized so it’s easy to follow and extend.  
- **Interview-ready** – A clear example of hands-on skills in data pipelines, cloud basics, and DevOps practices.

---

## Project Structure

- `terraform/` – Terraform code to create S3 bucket.  
- `lambda/` – Python scripts simulating AWS Lambda functions: reading, transforming, and uploading CSV files.  
- `sample_data/` – Example CSV files to test the pipeline.

---

## Objective

- Automate S3 bucket creation with Terraform.  
- Upload, read, and transform CSV files in S3 using Python (`boto3`).  
- Demonstrate a small end-to-end, reproducible ETL workflow.

---

## How to Use

1. **Create the S3 bucket with Terraform**:
```bash
cd terraform
terraform init
terraform apply
````

2. **Upload a CSV file to S3**:

```bash
python ../lambda/upload_csv.py
```

3. **Read CSV from S3**:

```bash
python ../lambda/s3_reader.py
```

4. **Transform CSV and upload the result**:

```bash
python ../lambda/s3_transform.py
```

---

## Outcome

* CSV files are stored in S3.
* Python scripts can read and transform data automatically.
* Demonstrates a reproducible ETL pipeline using Python, Terraform, and AWS S3.


