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
  

    file = 'test01.txt' # change this to dynamic file name
    # for bucket_name in bucket_list:
    #     no_of_files = len(bucket_list)
    #     for file in bucket_list[0]:
    #         print(f"File name : {file}")
    s3_resource = boto3.resource('s3') # using boto3 resources instead of client
    for bucket_name in bucket_list:
        first_bucket = s3_resource.Bucket(name=bucket_name)
        first_object = s3_resource.Object(
        bucket_name=bucket_name, key=file)
        print(f"file name {first_object}")
    
    for bucket in s3_resource.buckets.all():
        print(bucket.name)
    
    for obj in first_bucket.objects.all():
        print(f"file {obj.key} inside S3 bucket!")
        
    file = obj.key

    # for bucket_dict in s3_client.meta.client.list_buckets().get('Buckets'):        #using client here
    #     print(f"S3 bucket name : {bucket_dict['Name']}")
    #     for obj in bucket_dict['Name'].objects.all():
    #         print(f"file {obj.key} inside S3 bucket!")
    
    # Get the files if found in these buckets        
    for bucket_name in bucket_list:
        # check if file is found in the given bucket
        
       
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
        print(obj['ContentLength'])
        return obj['ContentLength']
    except ClientError as exc:
        if exc.response['Error']['Code'] != '404':
            raise
    
