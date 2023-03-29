# This code creates S3 Buckets
# Use aws configure in awscli to pass the access key
import logging
import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist, clrscrn, get_bkt_location



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
                    # created_bktlist.append[str(bucket_name)] #bucket names are objects so can't subscript - to add them with append(listnames)
                    s3_client.create_bucket(Bucket=bucket_name,)
                                        # CreateBucketConfiguration=location)
                    # [created_bktlist[bucket_name] for bucket_name in range(len(bucket_list)-1)]    
                    # print(created_bktlist)
                
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                for bucket_name in bucket_list:
                    s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)                   
    except ClientError as e:
        logging.error(e)
        return False
    return True

