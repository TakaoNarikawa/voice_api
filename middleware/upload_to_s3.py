import boto3
import json

json_open = open('./config/aws.json', 'r')
json_load = json.load(json_open)

ACCESSKEY = json_load['access_key']
SECRETKEY = json_load['secret_key']
REGION = json_load['region']
BACKET = json_load['backet_name']

def upload_image(filename, filepath):
    s3 = boto3.client('s3', aws_access_key_id=ACCESSKEY, aws_secret_access_key= SECRETKEY, region_name=REGION)

    bucket_name = BACKET

    s3.upload_file(filepath, bucket_name, filename)

if __name__ == "__main__":
    pass