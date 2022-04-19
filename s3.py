"""This module has s3 service connection and uploading file into s3"""
import configparser
import boto3
from botocore.exceptions import ClientError

config = configparser.ConfigParser()
config.read("develop.ini")


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
        print(self.bucket_name)
        self.bucket_path = config["s3"]["bucket_path"]
        self.local_path = config["Local"]["local_path"]


    def upload_file(self,file,key):
        """This method is used to upload the file into s3 bucket"""
        try:
            self.s3_obj.upload_file(
                 self.local_path + file,self.bucket_name,self.bucket_path + key
                # self.local_path + file, self.bucket_path + key
            )
        except ClientError as error:
            print(error)
        return self.bucket_path + key

    def put_object(self, body, key):
        """This method is used to put object in s3 bucket"""
        try:
            res = self.s3_obj.put_object(
                Bucket=self.bucket_name, Body=body, Key=self.bucket_path + key
            )
            return self.bucket_path + key
        except ClientError as error:
            print(error)
            return False
    
def main():
    s3_service = S3Service()
    
if __name__ == '__main__':
    main()    