import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist
import logging


def delete_all_objects_from_s3_folder():
    """ This method deletes all file in a S3 buckets. """
    s3_client = boto3.client("s3")
    # get the list of buckets
    # bucket_name = "s3bucket4me2test01"
    bucket_names = get_bucketlist()
    if bucket_names != False:
        print("Available S3 Buckets : ", bucket_names)
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

                        elif userinput == str(input(f"Do you want to delete this {fileCount} file,Enter '1' or anything else to skip : ")):
                            response = s3_client.list_objects_v2(Bucket=bucket_name) 
                            files_in_folder = response["Contents"]
                            files_to_delete = []
                            # Deletes multiple files, here we will create Key array to pass to delete_objects function
                            for f in files_in_folder:
                                files_to_delete.append({"Key": f["Key"]})

                            # This will delete all files in a folder
                            response_list = []
                            response = s3_client.delete_objects(
                                Bucket=bucket_name, Delete={"Objects": files_to_delete}
                            )
                            response_list.append(response)
                            print("\n Deleted files : ", files_to_delete)
                            delete_all_objects_from_s3_folder()
                        else:
                            print("you will not be able to delete the S3 bucket unless its empty!")
                            continue
                
                    # print("S3 Buckets left out: ", bucket_names)
                    return True
        else:
            print("No Buckets found!")
            return False
    except ClientError as e:
        logging.error(e)
        return False

# check_delete = delete_all_objects_from_s3_folder() 
# if check_delete == True: # Need to move these code to userchoide.py 
#     print("Deletion was successfully completed!")
# else:
#     print("\nNothing Deleted!\n")

# ----- new method - checks if there is any object files before trying to delete the buckets---- 
# import boto3
# import botocore
# from botocore.exceptions import ClientError

# def listS3():
#    client = boto3.client('s3')
#    response = client.list_buckets()
#    filelist = []
#    for bucket in response['Buckets']:
#      filelist = bucket['Name']
#      print(bucket['Name'])
#    return filelist
   
    
# def deleteS3(s3,AWS_BUCKET_NAME):  
#     resource_s3_list = boto3.client("s3")
#     get_response = resource_s3_list.list_buckets()
#     buckets = get_response["Buckets"]
#     print("Before Deleting buckets count : ",len(buckets))
#     print("Before deleting the bucket we need to check if its empty. Cheking ...")
#     objects = resource_s3_list.list_objects_v2(Bucket=AWS_BUCKET_NAME)
#     fileCount = objects['KeyCount']

#     for bucket in buckets:
#         print("S3 bucket name : ",bucket["Name"])
    
#     # client = boto3.client('s3')
#     if fileCount == 0:
#          response = resource_s3_list.delete_bucket(Bucket=AWS_BUCKET_NAME)
#          print("{} has been deleted successfully !!!".format(AWS_BUCKET_NAME))
#     else:
#          print("{} is not empty, {} objects present".format(AWS_BUCKET_NAME,fileCount))
#          print("Deleting Objects inside S3 bucket")
#          resource_s3_list.delete_object(Bucket='AWS_BUCKET_NAME', Key='folder/file_client.txt') # Make Sure Access is given to delete
         
         

    
    
# # A Good practice before deleting files is to download if needed for references
# BUCKET_NAME = 'mynews3bucket2test01' # replace with your bucket name
# KEY = 'test03.txt' # replace with your object key

# s3 = boto3.resource('s3')

# try:
#     s3.Bucket(BUCKET_NAME).download_file(KEY, 'test03.txt') #this downloads to the current location execution file
# except botocore.exceptions.ClientError as e:
#     if e.response['Error']['Code'] == "404":
#         print("The object does not exist.")
#     else:
#         raise
# print("List all the S3 Buckets : \n",listS3())
# print("Deleting S3 buckets now ... ", deleteS3(s3,BUCKET_NAME))
