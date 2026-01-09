import boto3
import csv
from io import StringIO

def read_csv_from_s3():
    s3 = boto3.client("s3")

    bucket_name = "aws-mini-pipeline-demo-123456"
    file_key = "example.csv"  

    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    content = response["Body"].read().decode("utf-8")

    reader = csv.DictReader(StringIO(content))
    for row in reader:
        print(row)

if __name__ == "__main__":
    read_csv_from_s3()
