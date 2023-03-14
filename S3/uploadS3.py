import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist, clrscrn
import os


def upload2S3(res_s3, buckets_list):
    ''' Uploads given file to s3 buckets in the list. '''
    # print(s3)
    file2upload = 'text01.txt' #should be same as the data
    clrscrn()
    for bucket_name in buckets_list:
        print("Select a bucket from the list : ",bucket_name) # only first bucket in the list gets the to upload files
        # Need to change logic to check the list of buckets then user decided which buckets to upload files.
        # Write try catch block to catch if file not found error.
        # write code to select a bucket that user wants.
        user_input = str(input(f"Confirm this {bucket_name} to upload file - Press 'y/Y' or anyother key to skip : "))
        if user_input in ['y','Y']:
            with open('test01.txt', 'rb') as data:

                res_s3.upload_fileobj(
                    Fileobj=data, 
                    Bucket=bucket_name, 
                    Key=file2upload
                )
            return f"This Bucket {bucket_name} got uploaded with file {data.name}"
        else:
            return "No files uploaded!"
        


resource_s3 = boto3.client("s3")
# # get the list of buckets from S3
# get_response = resource_s3.list_buckets()
# buckets = get_response["Buckets"]
S3_bucket_list = get_bucketlist()

# for bucket in buckets:
#     print("S3 bucket name : ",bucket["Name"])
if S3_bucket_list != False:
    print(upload2S3(resource_s3,S3_bucket_list))
else:
    print("\n No S3 Buckets exist in the account! \n")