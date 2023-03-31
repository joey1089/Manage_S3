import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist
import os.path


def upload2S3(res_s3, buckets_list):
    ''' Uploads given file to s3 buckets in the list. '''
    # print(s3)
    available_bucket = []
    user_file = str(input("\nGive full path details or just name if file is in current dir- : "))
    # file2upload = user_file #should be same as the data   
    file_exists = os.path.exists(user_file) # check if files exist or not      
    if get_bucketlist(): # Redundant check need to change the logic to better efficient way.
        # for loop doesn't show the files in bucket, its getting the bucket name.
       

        if file_exists == True:
            # clrscrn()
            for bucket_name in buckets_list:
                available_bucket.append(bucket_name)
            # print("Available buckets : ",available_bucket)

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
            if len(user_file) == 0:
                print(f'The given file {user_file} does not exist!')  
            return False
    else:
        print("\n No Buckets are found in this account!")
      


