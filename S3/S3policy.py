# By default AWS has made the S3 bucket as private!
import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist
import logging

def check_bucket_status():
    """ This method checks if bucket has public access or private access. """
    s3_client = boto3.client("s3")
    bucket_list = str(get_bucketlist())
    if bucket_list != False:
        # send the bucket list to Bucket
        for bucket_name in bucket_list:
            try:
                response = s3_client.get_bucket_policy_status(Bucket=bucket_name)
                return response["PolicyStatus"]
            except ClientError as e:
                # if you do not have any policy attached to bucket it will throw error
                # An error occurred (NoSuchBucketPolicy) when calling the GetBucketPolicyStatus operation:
                # The bucket policy does not exist
                logging.error(e)
                print("No policy attached to this bucket")
    else:
        print("No buckets found to change the policy!")
  

def set_bucket_policy():
    """ This method adds public policy to a bucket. """
    # policy for making all objects in bucket public by default
    public_policy = """{
      "Id": "Policy1577423306792",
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "Stmt1577423305093",
          "Action": "s3:*",
          "Effect": "Allow",
          "Resource": "arn:aws:s3:::ReplacewithBucket-Name/*",
          "Principal": {
            "AWS": [
              "*"
            ]
          }
        }
      ]
    }"""
    s3_client = boto3.client("s3")
    bucket_list = get_bucketlist()
    try:
        response = s3_client.put_bucket_policy(
            Bucket=bucket_list, Policy=public_policy
        )
        print(response)
        # checking bucket status. This should show us s3 bucket is public now
        check_bucket_status()
    except ClientError as e:
        # if you do not have any policy attached to bucket it will throw error
        # An error occurred (NoSuchBucketPolicy) when calling the GetBucketPolicyStatus operation:
        # The bucket policy does not exist
        print(e)


import json

# refer - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-bucket-policies.html

# Create a bucket policy
bucket_name = 'BUCKET_NAME'
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
