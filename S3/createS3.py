# This code creates S3 Buckets
# Use aws configure in awscli to pass the access key
import logging
import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist, clrscrn, get_bkt_location
from verify_awscredentials import credentials_check
import pandas as pd


def create_S3_bucket(bucket_list, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """
    # Create a new bucket   
    created_bktlist = []  
    try:
        if region is None:
            # if region is not given then it defaults to 'us-east-1' .
            s3_client = boto3.client('s3')
            for bucket_name in bucket_list:
                s3_client.create_bucket(Bucket=bucket_name)
        else:
            if region == 'us-east-1':
                s3_client = boto3.client('s3', region_name=region)
                # location = {'LocationConstraint': region}
                for bucket_name in bucket_list:
                    s3_client.create_bucket(Bucket=bucket_name,)
                                        # CreateBucketConfiguration=location)
                    created_bktlist.append[bucket_name]                
                print("Created buckets list : ",created_bktlist)
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                for bucket_name in bucket_list:
                    s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
                    created_bktlist.append[bucket_name]                
                print("Created buckets list : ",created_bktlist)
    except ClientError as e:
        logging.error(e)
        return False
    return True

clrscrn()
# Check if there are S3 Buckets available in the account:
if credentials_check() != False:

    if  get_bucketlist() != False:
        S3_bucket_list = ','.join(map(str,get_bucketlist()))
        print("Current S3 bucket list : ", S3_bucket_list)
        S3_bucket_location = str(get_bkt_location())
        print("Current S3 bucket region : ",S3_bucket_location)
    # S3_bucket_list = str(get_bucketlist())
    else: 
        print("No S3 Buckets Found in this Account!")

        
    print("\n======================== Create your AWS S3 buckets! ================================\n")
    # region_input = None # should trigger default region us-east-1 but its giving errors
    region_input = str(input("Which region do you like to create the buckets(default 'us-east-1') : ").strip())
    if len(region_input) == 0:
        region_input = 'us-east-1'
    # use the csv file to get the bucket name.
    data = pd.read_csv("s3/S3_buckets.csv") # pandas pd gets the csv file
    # print(data)
    # print(data.loc[0:4,'bucketnames']) # prints the all the lists
    S3bucket_list = data['bucketnames'].to_list() # get the column and converts it to a list.
    # print(data.loc[0:2]) # get the 3 rows from the start
    create_S3_bucket(S3bucket_list, region_input)
else:
    print("\nInvalid AWS Access keys!\n")