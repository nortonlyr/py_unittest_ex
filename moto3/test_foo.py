import boto3
import os
from moto import mock_s3
import pytest


def dl(src_f, dest_f):
    s3 = boto3.resource('s3')
    s3.Bucket('mybucket').download_file(src_f, dest_f)

@mock_s3
def test_dl():
    s3 = boto3.client('s3', region_name='us-east-1')
    # We need to create the bucket since this is all in Moto's 'virtual' AWS account
    s3.create_bucket(Bucket='mybucket')

    s3.put_object(Bucket='mybucket', Key= 'bucket_file.txt', Body='')
    dl('bucket_file.txt', 'bucket_file.txt')

    assert os.path.isfile('bucket_file.txt')