# AWS S3 bucket Management
Do Creation, deletion of buckets and its object, uploading objects to S3 and downloading them on demand.

![Manage S3 - 800x350px (3)](https://github.com/joey1089/Manage_S3/assets/90427049/47aa75c2-db25-46e4-b1bf-3466e26ae8b7)


Check out the youtube demo -> https://youtu.be/1076mS2xkdU

#Tasks to do:
AWS user credentials verification.
Built a user interface in CLI, so user can choose what actions they can perform on S3 buckets.
List out the S3 buckets in the account.
Create five S3 buckets from a .csv file.
Uploading file objects to S3 buckets.
Delete S3 buckets and file object.
Download the file objects.
Task 1: — AWS user credentials verification.
Before we can do any operations in AWS, it's important to verify our credentials without which we can’t proceed to do anything with our code. So, let's look at the code that does the verification. 
As per referred AWS document, this code — STS.Client.get_caller_identity()
Returns details about the IAM user or role whose credentials are used to call the operation. In our code we used get_call_identity method to verify the AWS credentials. When we pass wrong credentials through the AWSCLI the exception client error logs the error to the screen.
Task 2: —Built a CLI interface for User to choose S3 Operations.
Building a CLI interface for the user to manage the S3 bucket operations. This means user can perform any options that are mentioned in the interface to perform on the S3 bucket. As of now, user can do following:
1. List the S3 buckets,
2. Create a S3 bucket,
3. Delete a S3 bucket,
4. Upload file to a S3 bucket,
5. Download file from a S3 bucket.

As you can see, the user is given a choice of operation to perform on the S3 bucket. Let's use the code to see how this is done through the code. Once the credientials_check() returns true we proceed to show the list of operations in the CLI. To simplify user input, I used numbers rather than letters or words.


Task:3 — List out the S3 buckets in the account
Its better to verify if we have buckets in the account before proceeding to create a bucket. So wrote a method to get the list of bucket names using the method get_bucketlist(). Here we make use of boto3 client object to get the list of buckets with help of the list_buckets() method.


Task:4— Create five S3 buckets from a .csv file.
When creating S3 Bucket, S3 bucket name is globally unique, and the namespace is shared by all AWS accounts. This means that after a bucket is created, the name of that bucket cannot be used by another AWS account in any AWS Region until the bucket is deleted. Also, location constraints can be used if you want to limit to a certain region only. Limiting it to five S3 buckets for demo purposes but you can create more buckets as you need up-to 100 buckets in an account. Here I used python’s panda library to read the S3 bucket names from the .csv file.


Task:5 — Uploading file objects to S3 buckets.
To upload a file to a S3 bucket I’m using upload_fileobj method provided by the boto3 client. Its parameters are file name, bucket name and object name or key.
Task:6 — Delete S3 buckets and file object.
The bucket must be empty; if you want to delete the bucket, we must delete the files in the bucket; then only it will allow us to delete the bucket itself.
This Delete_All_S3Buckets() method does delete empty buckets, if it comes across a bucket with files then it calls this delete_all_files_in_bucket(s3_client,bucket_name,buckets) method to delete all the files in the bucket.


Task:7-Download file objects from S3 Buckets
I made use of AWS boto3 documentation extensively for this purpose. Here I used the boto3.client to download the files from a S3 Bucket. If you want, you can also use boto3.resource to do the downloads.The download_file method accepts the names of the bucket and object to download and the filename to save the file to.


for full article -> https://medium.com/devops-dudes/managing-amazon-s3-buckets-made-easy-with-python-and-aws-boto3-4d05c9ee06ee

