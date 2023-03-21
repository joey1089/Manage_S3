import logging
import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist, clrscrn, get_bkt_location
from verify_awscredentials import credentials_check
from pathlib import Path


def get_files(s3_client, bucket_list ):
    '''Download Files from S3 Buckets'''
    # Getting the object:
    # print("Getting S3 object...")
    # for bucket_name in bucket_list:
    #     response = s3_client.get_object(Bucket=bucket_name,
    #                                     Key='encrypt-key')
    # #s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
    # print("Done, response body:")
    # print(response['Body'].read())
    
    # Get the files if found in these buckets        
    for bucket_name in bucket_list:
        # check if file is found in the given bucket
        file = 'test01.txt' # change this to dynamic file name
        file_size = key_existing_size__head(s3_client,bucket_name,file)     
        if file_size != None:
            try:            
                s3_client.download_file(bucket_name,file, 'DownloadedTMP.txt')            
                return True
            except ClientError as e:
                logging.error(e)
                return False

def key_existing_size__head(client, bucket, key):
    """return the key's size if it exist, else None"""
    
    try:
        obj = client.head_object(Bucket=bucket, Key=key)
        return obj['ContentLength']
    except ClientError as exc:
        if exc.response['Error']['Code'] != '404':
            raise
