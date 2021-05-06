# foo.py
import boto3

def dl(src_f, dest_f):
    s3 = boto3.resource('s3')
    s3.Bucket('mybucket').download_file(src_f, dest_f)