#!/usr/bin/env python3
import boto3

#ECS credential
access_key_id = '131604634577647851@ecstestdrive.emc.com'  
secret_key = 'UrSsdKjfgOP3b2zoRcgTjPXEnQTH4eKFXu2m+7WY'
endpoint = 'https://object.ecstestdrive.com'

s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_key, endpoint_url=endpoint)

# AWS S3 no need endpoint_url parameter


def main():

    # create bucket
    bucket_name = 'thangndu'
    print("creating bucket...")
    s3.create_bucket(Bucket=bucket_name)
    print("bucket created!")

    # upload file

    metadata = {
        'file-name': 'piper.png',
        'file-owner': 'thangndu'
        }

    #The metadata can be seen in S3 in the "http headers" tab
    #It gets stored as "x-amz-meta-object-metadata:piper"


    file_name = "piper.png"
    f = open(file_name,'rb')

    print("uploading file...")
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=f.read(), Metadata=metadata)
    print("file uploaded!")

    f.close()

    # change permission
    # s3.put_object_acl(Bucket=bucket_name, Key=file_name, ACL='public-read')
    # print("file permission changed to public-read")

    # retrive object metadata
    #response = s3.head_object(Bucket=bucket_name, Key=file_name)
    #print(response)

if __name__ == "__main__":
    main()
