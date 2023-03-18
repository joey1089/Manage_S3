import logging
import boto3
from botocore.exceptions import ClientError
from listbuckets import get_bucketlist, clrscrn, get_bkt_location
from verify_awscredentials import credentials_check
from pathlib import Path



def get_file_folders(s3_client, bucket_name, prefix=""):
    file_names = []
    folders = []

    default_kwargs = {
        "Bucket": bucket_name,
        "Prefix": prefix
    }
    next_token = ""

    while next_token is not None:
        updated_kwargs = default_kwargs.copy()
        if next_token != "":
            updated_kwargs["ContinuationToken"] = next_token

        response = s3_client.list_objects_v2(**default_kwargs)
        contents = response.get("Contents")

        for result in contents:
            key = result.get("Key")
            if key[-1] == "/":
                folders.append(key)
            else:
                file_names.append(key)

        next_token = response.get("NextContinuationToken")

    return file_names, folders


def download_files(s3_client, bucket_name, local_path, file_names, folders):

    local_path = Path(local_path)

    for folder in folders:
        folder_path = Path.joinpath(local_path, folder)
        folder_path.mkdir(parents=True, exist_ok=True)

    for file_name in file_names:
        file_path = Path.joinpath(local_path, file_name)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        s3_client.download_file(
            bucket_name,
            file_name,
            str(file_path)
        )



# S3_dwnld = boto3.client("s3")
# bucket_list = get_bucketlist()
# if bucket_list != False:
#     file_names, folders = get_file_folders(S3_dwnld, bucket_list)
#     download_files(
#         S3_dwnld,
#         bucket_list,
#         "/myS3_backup",
#         file_names,
#         folders
#     )
# else:
#     print("\nNo Buckets found!\n")
