import boto3
from botocore.exceptions import ClientError
import os
import logging

def credentials_check():
    '''Verify if aws access key are valid to proceed!'''
    sts = boto3.client('sts')
    try:
        sts.get_caller_identity()
        print("Credentials are valid.")
        return True
    except ClientError as e:
        logging.error(e)
        print("Credentials are NOT valid.")
        return False