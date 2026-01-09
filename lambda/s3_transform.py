import boto3
import csv
import io

# CONFIG AWS
bucket_name = "aws-mini-pipeline-demo-123456"
input_key = "example.csv"
output_key = "example_transformed.csv"

def read_csv_from_s3():
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket_name, Key=input_key)
    content = response['Body'].read().decode('utf-8').splitlines()
    reader = csv.DictReader(content)
    data = [row for row in reader]
    return data

def transform_data(data):
    # Exemple : on double le montant
    for row in data:
        row['amount'] = str(int(row['amount']) * 2)
    return data

def write_csv_to_s3(data):
    s3 = boto3.client('s3')
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    s3.put_object(Bucket=bucket_name, Key=output_key, Body=output.getvalue())
    print(f"{output_key} uploaded to s3://{bucket_name}/{output_key}")

if __name__ == "__main__":
    data = read_csv_from_s3()
    print("Original data:", data)
    transformed = transform_data(data)
    print("Transformed data:", transformed)
    write_csv_to_s3(transformed)
