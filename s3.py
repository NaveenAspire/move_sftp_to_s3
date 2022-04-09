"""This module has s3 service connection and uploading file into s3"""
import configparser
import boto3
from botocore.exceptions import ClientError

config = configparser.ConfigParser()
config.read("sftp_config.ini")


class S3Service:
    """This class has the methods for s3 service"""

    def __init__(self):
        """This is the init method of the class S3Service"""
        self.s3_obj = boto3.client(
            "s3",
            aws_access_key_id=config["s3"]["aws_access_key_id"],
            aws_secret_access_key=config["s3"]["aws_secret_access_key"],
        )
        self.bucket_name = config["s3"]["bucket"]
        self.bucket_path = config["s3"]["bucket_path"]

    def put_object_to_bucket(self, body, key):
        """This function done the file uploading in s3 aspire-data-dev bucket"""
        try:
            self.s3_obj.put_object(
                Bucket=self.bucket_name, Body=body, Key=self.bucket_path + key
            )
        except ClientError as error:
            print(error)
