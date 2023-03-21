import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist
import logging


def delete_all_files_in_bucket(s3_client,bucket_name,buckets):
    '''This method deletes all files in the bucket!'''
    response = s3_client.list_objects_v2(Bucket=bucket_name) 
    files_in_folder = response["Contents"]
    files_to_delete = []
    # Deletes multiple files, here we will create Key array to pass to delete_objects function
    for f in files_in_folder:
        files_to_delete.append({"Key": f["Key"]})

    # This will delete all files in a folder    
    # for f in len(files_to_delete):
    userinput = str(input(f"Proceed deleting this {files_to_delete[0]['Key']} file found in {bucket_name},Enter '1' or anything else to skip : ")).strip()
    if userinput == '1':
        response = s3_client.delete_objects(
            Bucket=bucket_name, Delete={"Objects": files_to_delete}
        )
        print(f"\n Deleted file {files_to_delete[0]['Key']} from {bucket_name} bucket!")
       
        if len(buckets) != 0:                
            Delete_All_S3Buckets()                
        else:
            return True
    else:
        print("you will not be able to delete the S3 bucket unless its empty!")
        return False
        # continue #need a while or for loop
 


def Delete_All_S3Buckets():
    """ This method delete all S3 buckets if no files found else it call on delete_all_files_in_bucket(). """
    s3_client = boto3.client("s3")
    # get the list of buckets
    # bucket_name = "s3bucket4me2test01"
    bucket_names = get_bucketlist()
 
    if bucket_names != False:        
        print("Available S3 Buckets to be deleted : ", bucket_names)
    else:
        print("No Buckets found!")
        return False
    try:
        get_response = s3_client.list_buckets()
        buckets = get_response["Buckets"]
        # print("Before Deleting buckets count : ",len(buckets))        
        if len(buckets) != 0:
            userinput = str(input(f"Do you want to delete the {len(buckets)} buckets, Enter '1' to delete : "))
            if userinput == '1':
                # print("Prechecks Deleting process ... \n")
                count = len(buckets)
                while count != 0: # change this to while loop to continue deletion.
                    
                    for bucket_name in bucket_names:
                        print("Checking if the buckets are empty ...")
                        fileObj = s3_client.list_objects_v2(Bucket=bucket_name)
                        fileCount = fileObj['KeyCount']
                        print(f"Found {bucket_name} bucket has this much files : {fileCount}")                    
                        if fileCount == 0:
                            print(f"Deleting {bucket_name} ...")
                            response = s3_client.delete_bucket(Bucket=bucket_name)
                            print("S3 bucket {} has been deleted successfully !!!".format(bucket_name))
                            count -= count
                            continue

                        else:
                            if (delete_all_files_in_bucket(s3_client,bucket_name,buckets)) != False:
                                return True                           
                
                    # print("S3 Buckets left out: ", bucket_names)
                    return True
        else:
            print("No Buckets found!")
            return False
    except ClientError as e:
        logging.error(e)
        return False

