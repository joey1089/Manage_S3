# This code creates S3 Buckets
# Use aws configure in awscli to pass the access key
import logging
import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist, clrscrn, get_bkt_location
from verify_awscredentials import credentials_check
import pandas as pd
from deleteS3 import delete_all_objects_from_s3_folder
from uploadS3 import upload2S3
from Dwnld_S3File import download_files
import time
import sys


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
                    [created_bktlist[bucket_name] for bucket_name in range(len(bucket_list)-1)]    
                    print(created_bktlist)
                
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                for bucket_name in bucket_list:
                    s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
                    # created_bktlist.append[bucket_name]   
                    [created_bktlist[bucket_name] for bucket_name in range(len(bucket_list)-1)]             
                print("Created buckets list : ",bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# clrscrn()
# # Check if there are S3 Buckets available in the account:
# if credentials_check() != False:

#     if  get_bucketlist() != False:
#         S3_bucket_list = ','.join(map(str,get_bucketlist()))
#         print("Current S3 bucket list : ", S3_bucket_list)
#         S3_bucket_location = str(get_bkt_location())
#         print("Current S3 bucket region by default its us-east-1 if its none : ",S3_bucket_location)
#     # S3_bucket_list = str(get_bucketlist())
#     else: 
#         print("No S3 Buckets Found in this Account!")

        
#     print("\n======================== Create your AWS S3 buckets! ================================\n")
#     # region_input = None # should trigger default region us-east-1 but its giving errors
#     region_input = str(input("Which region do you like to create the buckets(default 'us-east-1') : ").strip())
#     if len(region_input) == 0:
#         region_input = None #if None then it uses 'us-east-1' by default
#     # use the csv file to get the bucket name.
#     data = pd.read_csv("S3/S3_buckets.csv") # pandas pd gets the csv file
#     # print(data)
#     # print(data.loc[0:4,'bucketnames']) # prints the all the lists
#     S3bucket_list = data['bucketnames'].to_list() # get the named column and converts it to a list.
#     # print(data.loc[0:2]) # get the 3 rows from the start
#     created_S3 = create_S3_bucket(S3bucket_list, region_input)
#     if created_S3 == True:
#         print("Created S3 buckets : ", get_bucketlist())
#     else:
#         print("Unable to create S3 buckets - check error details!")
# else:
#     print("\nInvalid AWS Access keys!\n")

# def userchoice():
#     '''Users are given a choice to choose an operation to do on S3 Buckets.'''
#     clrscrn()
#     print("========================= S3 Operations Avaiable Now ===============================")
#     print("List the S3 Buckets, Press '1' : ")
#     print("Create a S3 Bucket, Press '2' : ")
#     print("Delete a S3 Bucket, Press '3' : ")
#     print("Upload file to a S3 Bucket, Press '4' : ")
#     print("Download file from a S3 Bucket, Press '5' : ")
#     print("Press anything else to skip all the options to exit!")
#     userchoice = str(input("\n Select Operations you want to perform on S3 Buckets : "))
#     if userchoice == '1':
#         print("\n List of buckets available now : \n",get_bucketlist())
#     elif userchoice == '2':
#         print("\n Created these S3 Buckets : ", create_S3_bucket())
#     elif userchoice == '3':
#         print("\n Deleted S3 Buckets : ", delete_all_objects_from_s3_folder())
#     elif userchoice == '4':
#         print("\n Uploaded file to S3 Bucket : ", upload2S3())
#     elif userchoice == '5':
#         print("\n Download file from S3 Bucket : ", download_files())
#     else:
#         print("Exiting ...")
#         time.sleep(5)
#         exit()
#     return exit()

# if __name__ == '__main__':
#     # Execute when the module is not initialized from an import statement.
#     if credentials_check():
#         userchoice()
#     else:
#         print("Invalid Credentials!")
#         sys.exit(userchoice())  