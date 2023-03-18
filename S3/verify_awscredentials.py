import boto3
from botocore.exceptions import ClientError
import logging

def credentials_check():
    '''Verify if aws access key are valid to proceed!'''
    sts = boto3.client('sts')
    try:
        sts.get_caller_identity()
        print("Valid AWS Credentials!") # all print statements related to validation can be commented out once we have proper modules
        return True
    except ClientError as e:
        # logging.error(e)
        print("Invalid AWS Credentials!")
        return False