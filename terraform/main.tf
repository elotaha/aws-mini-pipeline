# Configure the AWS provider
provider "aws" {
  region = "us-east-1"  # You can choose any Free Tier eligible region
}

# Create an S3 bucket with versioning enabled
resource "aws_s3_bucket" "data_bucket" {
  bucket = "aws-mini-pipeline-demo-123456"  # Must be globally unique
  acl    = "private"

  versioning {
    enabled = true
  }
}

# Output the name of the S3 bucket
output "bucket_name" {
  value = aws_s3_bucket.data_bucket.bucket
}
