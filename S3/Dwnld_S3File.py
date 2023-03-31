import logging
import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist, clrscrn, get_bkt_location
from verify_awscredentials import credentials_check
from pathlib import Path
import uuid


def gen_filename(file_name):
    '''Generate file name for the file download'''  
    # def gen_filename(file_name)
    # print(file_name)  
    gen_uuid = str(uuid.uuid4()) # random uuid generated 
    d_filename = str('DLfile_'+ gen_uuid[0:5] + '_' + file_name)
    # print(d_filename)
    return d_filename



def get_files(bucket_list):
    '''gets all the files from all the buckets!'''
    s3_resource = boto3.resource('s3') # using boto3 resources instead of client

    files = []
    try:
        for bucket_name in bucket_list:
            search_bucket = s3_resource.Bucket(bucket_name)
            for current_bucket_obj in search_bucket.objects.all():
                print(f"Downloading file {current_bucket_obj.key} found in this {bucket_name}")
                search_bucket.download_file(current_bucket_obj.key, gen_filename(current_bucket_obj.key))
                # s3_resource.download_file(bucket_name,current_bucket_obj, gen_filename(current_bucket_obj))
                # files.append(current_bucket_obj.key)  
        
        return True
    except ClientError as e:
        logging.error(e)
        print(e)
        return False



# def get_files(s3_client, bucket_list ):
#     '''Download Files from S3 Buckets'''

#     # gen_filename = gen_filename()
#     files = list_of_files(bucket_list) # gets all the files from all the buckets
    
#     # Get the files if found in these buckets        
#     # for bucket_name in bucket_list:
#     #     # go through the list of files in the bucket.
#     #     count = 0
#     #     for file in files:                                  
#     #             file_size = key_existing_size__head(s3_client,bucket_name,file)  
#     #             count += 1     
#     #             if file_size != None:
#     #                 try:      
#     #                     # print(f"\n Downloading all the {gen_filename(file)} from the bucket {bucket_name}!")      
#     #                     s3_client.download_file(bucket_name,file, gen_filename(file))  # gen_filename() - downloaded file name
#     #                     if count == len(files):
#     #                         return True
#     #                     continue
#     #                 except ClientError as e:
#     #                     logging.error(e)
#     #                     return False

# def key_existing_size__head(client, bucket, key):
#     """return the key's size if it exist, else None"""    
#     try:
#         obj = client.head_object(Bucket=bucket, Key=key)
#         # print(obj)
#         return obj['ContentLength']
#     except ClientError as exc:
#         if exc.response['Error']['Code'] != '404':
#             raise
    
