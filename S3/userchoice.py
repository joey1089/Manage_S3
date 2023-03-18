import logging
import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist, clrscrn, get_bkt_location
from verify_awscredentials import credentials_check
from createS3 import create_S3_bucket
from deleteS3 import delete_all_objects_from_s3_folder
from uploadS3 import upload2S3
from Dwnld_S3File import download_files
import pandas as pd
import os
import time

def userchoice():
    '''Users are given a choice to choose an operation to do on S3 Buckets.'''
    clrscrn()
    print("========================= S3 Operations Avaiable Now ===============================")
    print("List the S3 Buckets, Press '1' : ")
    print("Create a S3 Bucket, Press '2' : ")
    print("Delete a S3 Bucket, Press '3' : ")
    print("Upload file to a S3 Bucket, Press '4' : ")
    print("Download file from a S3 Bucket, Press '5' : ")
    print("Press anything else to skip all the options to exit!")
    userchoice = str(input("\n Select Operations you want to perform on S3 Buckets : "))
    if userchoice == '1':
        print("\n List of buckets available now : \n",get_bucketlist())
    elif userchoice == '2':
        print("\n Created these S3 Buckets : ", create_S3_bucket())
    elif userchoice == '3':
        print("\n Deleted S3 Buckets : ", delete_all_objects_from_s3_folder())
    elif userchoice == '4':
        print("\n Uploaded file to S3 Bucket : ", upload2S3())
    elif userchoice == '5':
        print("\n Download file from S3 Bucket : ", download_files())
    else:
        print("Exiting ...")
        time.sleep(5)
        exit()


userchoice()



