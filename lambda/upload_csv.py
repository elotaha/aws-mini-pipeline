import boto3
import csv
from io import StringIO

bucket_name = "aws-mini-pipeline-demo-123456"
file_key = "example.csv"

s3 = boto3.client("s3")
obj = s3.get_object(Bucket=bucket_name, Key=file_key)
content = obj['Body'].read().decode('utf-8')

reader = csv.DictReader(StringIO(content))
for row in reader:
    print(row)
