# This code returns the list of buckets if it exist in the account
# Use aws configure in awscli to pass the access key
import boto3
from botocore.exceptions import ClientError
import os
import logging

def clrscrn():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def get_bucketlist():
    ''' This method returns list of buckets names if found.'''
    
    resource_s3 = boto3.client("s3")
    try:
        # get the list of buckets from S3
        get_response = resource_s3.list_buckets()
        buckets = get_response["Buckets"] 
        bucket_list = []

        if buckets != []:
            for bucket in buckets:
                # print("S3 bucket name : ",bucket["Name"])
                bucket_list.append(bucket["Name"])        
            return bucket_list
        else:
            return False
    except ClientError as e:
        logging.error(e)
        return False

    
# print(get_bucketlist())

def get_bkt_location():
    ''' Gets the Location of the S3 buckets'''
    client = boto3.client("s3")
    for bucket_name in get_bucketlist():
        response = client.get_bucket_location(
          Bucket=bucket_name,
        )

    # print(response)
    return response['LocationConstraint']
    # bucket_location.append(resource_s3.get_bucket_location(Bucket=bucket['Name']))
    # bucket_location.append(bucket_location['LocationConstraint'])

