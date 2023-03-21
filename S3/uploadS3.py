import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist, clrscrn
import os.path


def upload2S3(res_s3, buckets_list):
    ''' Uploads given file to s3 buckets in the list. '''
    # print(s3)
    fileinbucket = []
    user_file = str(input("\nGive full path details for the file you want to upload : "))
    # file2upload = user_file #should be same as the data   
    file_exists = os.path.exists(user_file) # check if files exist or not      
    if get_bucketlist(): # Redundant check need to change the logic to fit all options
        for bucket_name in buckets_list:
            fileinbucket.append(bucket_name)
        print("Available buckets : ",fileinbucket)

        if file_exists == True:
            # clrscrn()
            for bucket_name in buckets_list:
                # print("Current Bucket Name :- ",bucket_name) # only first bucket in the list gets the to upload files
                # Need to change logic to check the list of buckets then user decided which buckets to upload files.
                # Write try catch block to catch if file not found error.
                # write code to select a bucket that user wants.
                user_input = str(input(f"Do you want to upload file to this {bucket_name} bucket, Enter '1' or anyother key to skip : "))
                while user_input == '1':
                # if user_input in ['y','Y']:
                    with open(user_file, 'rb') as data:

                        res_s3.upload_fileobj(
                            Fileobj=data, 
                            Bucket=bucket_name, 
                            Key=user_file
                        )
                    print(f"This Bucket {bucket_name} got uploaded with file {data.name}")
                    return True
                continue
                # else:
                #     return f"No files uploaded for {bucket_name}!"
        else:
            print(f'The given file {user_file} or S3 bucket does not exist!')  
            return False
    else:
        print("\n No Buckets are found in this account!")
        


# resource_s3 = boto3.client("s3")
# # # get the list of buckets from S3
# # get_response = resource_s3.list_buckets()
# # buckets = get_response["Buckets"]
# S3_bucket_list = get_bucketlist()

# # for bucket in buckets:
# #     print("S3 bucket name : ",bucket["Name"])
# if S3_bucket_list != False:
#     print(upload2S3(resource_s3,S3_bucket_list))
# else:
#     print("\n No S3 Buckets exist in the account! \n")