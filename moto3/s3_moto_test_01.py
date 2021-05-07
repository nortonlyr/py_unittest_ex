import os
import boto3
from moto import mock_s3

class S3Handler:
    def __init__(self):
        self.s3_session = boto3.session.Session()
        self.s3_client = self.s3_session.client('s3')
        self.bucket = 'my_bucket'
        self.file_name = 'bucket_file.txt'
        self.file_path = 'E:/dev/py_unittest_ex/moto3/'

    def upload_s3_file(self):
        path_to_file = os.path.join(self.file_path, self.file_name)

        self.s3_client.upload_file(
            path_to_file,
            self.bucket,
            self.file_name
            )




@mock_s3
def test_upload_s3_file():
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Bucket='my_bucket')
    s3_handler = S3Handler()
    s3_handler.upload_s3_file()