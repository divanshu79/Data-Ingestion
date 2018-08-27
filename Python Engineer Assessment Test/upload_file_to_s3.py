import boto3
from botocore.client import Config
import os
# os.environ["HTTPS_PROXY"] = "https://ipg_2014037:Divanshu79@192.168.1.107:3128"

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = 'data-file79'


data = open('file.json', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

s3.Bucket(BUCKET_NAME).put_object(Key='file.json', Body=data, ContentEncoding='utf-8')

print("Done")