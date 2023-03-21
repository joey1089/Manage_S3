from listbuckets import get_bucketlist, clrscrn
from verify_awscredentials import credentials_check
from createS3 import create_S3_bucket, get_bucketlist, get_bkt_location
from deleteS3 import Delete_All_S3Buckets, delete_all_files_in_bucket
from uploadS3 import upload2S3
from Dwnld_S3File import get_files
import time
import sys
import pandas as pd
import boto3

def user_options():
    '''In this Method,Users are given a choice to choose an operation to do on S3 Buckets.   
    '''
    resource_s3 = boto3.client("s3")
    S3_bucket_list = get_bucketlist()
    # clrscrn()
    select_options = '''
    =============================== Manage S3 Bucket ===============================
    List the S3 Buckets, Enter '1' 
    Create a S3 Bucket, Enter '2' 
    Delete a S3 Bucket, Enter '3'
    Upload file to a S3 Bucket, Enter '4'
    Download file from a S3 Bucket, Enter '5'
    Enter anything else to exit!    
    '''
    print(select_options)
    userchoice = str(input("\n Enter your choice of operation to perform on S3 Buckets : "))    
    if userchoice == '1':
        print("\n Checking S3 buckets in this account ... \n")    
        time.sleep(2)    
        # # get the list of buckets from S3
        # get_response = resource_s3.list_buckets()
        # buckets = get_response["Buckets"]      

        # for bucket in buckets:
        #     print("S3 bucket name : ",bucket["Name"])
        if S3_bucket_list != False:
            print("List of buckets available now : ",S3_bucket_list) 
            anotherchoice = str(input("Do you want to upload a file, Enter '4' or anything else to exit : "))
            if anotherchoice == '4':
                upload2S3(resource_s3,S3_bucket_list)
                user_options()
            else:                
                anotherchoice1 = str(input("Want to continue, Enter '1' or anything else to exit : ")).strip()
                while anotherchoice1 != '1':                    
                    print("\n Exiting ... ")
                    time.sleep(2)
                    exit()
                else:
                    print("\n Proceed to main menu ... ") 
                    time.sleep(2)     
                    user_options()
        else:
            print("\n No S3 Buckets found in this account! \n")
            user_options()
    elif userchoice == '2':
        # Check if there are S3 Buckets available in the account:
        if credentials_check() != False:

            if  get_bucketlist() != False:
                S3_bucket_list = ','.join(map(str,get_bucketlist()))
                print("Available S3 bucket  : ", S3_bucket_list)
                # S3_bucket_location = str(get_bkt_location())
                print("S3 bucket region by default its us-east-1 if its none : ",str(get_bkt_location()))
            # S3_bucket_list = str(get_bucketlist())
            else: 
                print("No S3 Buckets Found in this Account!")
                
            print("\n======================== Create your AWS S3 buckets! ================================\n")
            # region_input = None # should trigger default region us-east-1 but its giving errors
            region_input = str(input("Which region do you like to create the buckets(default 'us-east-1' if nothing is given) : ").strip())
            if len(region_input) == 0:
                region_input = None #if None then it uses 'us-east-1' by default
            # use the csv file to get the bucket name.
            data = pd.read_csv("S3/S3_buckets.csv") # pandas pd gets the csv file
            # print(data)
            # print(data.loc[0:4,'bucketnames']) # prints the all the lists
            S3bucket_list = data['bucketnames'].to_list() # get the named column and converts it to a list.
            # print(data.loc[0:2]) # get the 3 rows from the start
            created_S3 = create_S3_bucket(S3bucket_list, region_input)
            if created_S3 == True:
                print("Created S3 buckets : ", get_bucketlist())
                user_options()
            else:
                print("Unable to create S3 buckets - check error details!")
                user_options()
        else:
            print("\nInvalid AWS Access keys!\n")
    elif userchoice == '3':
        # print("\n Deleted S3 Buckets : ")
        if get_bucketlist() != False:
            check_delete = Delete_All_S3Buckets()
            if check_delete == True: 
                print("Deletion was successfully completed!")
                user_options()
            else:
                print("\nNothing Deleted!\n")
                user_options()
    elif userchoice == '4':
        if upload2S3(resource_s3,S3_bucket_list):
            print("\n Uploaded file to S3 Bucket!")
            user_options()
        else:
            print("\n Upload Incomplete! \nProceed to main menu ... ") 
            time.sleep(2)     
            user_options()
    elif userchoice == '5':
        if get_bucketlist() != False:
            # local_path = str(input("Enter the local path : "))
            # file_names = str(input("Enter the file names : "))
            # folders = str(input("Enter the folder name : "))
            # if download_files(resource_s3,S3_bucket_list, local_path, file_names, folders):
            if get_files(resource_s3,S3_bucket_list):
                print("\n Downloaded file from S3 Bucket!")
                user_options()
            else:
                print("\n Download Incomplete! \nProceed to main menu ... ") 
                time.sleep(2)     
                user_options()
        else:
            print("\n No buckets found!")
            time.sleep(2)
            user_options()
    else:
        print("Exiting ...")
        time.sleep(2)
        exit()
    return exit()


# if __name__ == '__main__':   
count = 0
if count == 0:
    clrscrn()
    if credentials_check():
        count += 1
        user_options()
    else:
        print("Invalid AWS Credentials!")
        sys.exit()  



