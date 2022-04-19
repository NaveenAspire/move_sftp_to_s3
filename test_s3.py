

# Not completed 

"""This is the test module for the task"""

import os
import pytest
from responses import mock
from s3 import S3Service
import boto3
from sftp_connection import SftpCon

class Test_s3:
    """This class test for s3 module"""
    
    @pytest.fixture
    def bucket_name(self):
        return "my-test-bucket"


    @pytest.fixture
    def s3_test(self,s3_client,bucket_name ):
        print(s3_client)
        s3_client.create_bucket(Bucket=bucket_name)
        yield
    
    @pytest.mark.xfail
    def test_upload_file(self,s3_client,s3_test):
        my_client = S3Service()
        print(s3_client)
        res = my_client.upload_file('sample.csv','sample.csv')
        objects = s3_client.list_objects(Bucket='my-test-bucket')
        assert objects['Contents'][0]['Key'] == res
    
    @pytest.mark.xfail    
    def test_put_object(self,s3_client,s3_test):
        my_client = S3Service()
        res = my_client.put_object(b'hai hello','hello.txt')
        objects = s3_client.list_objects(Bucket='my-test-bucket')
        assert objects['Contents'][0]['Key'] == res
    
    @pytest.mark.xfail    
    def test_s3_object(self):
        """This method test the instance belong to the class of S3Service"""
        self.s3_obj = S3Service()
        assert isinstance(self.s3_obj,S3Service)
    
    
        
class Test_sftp:
    """This class test for sftp_connection module"""
    
    def test_sfpt_conntion(self,sftp_client):
            sftp_client.put('opt/data/sample.csv','sample.csv')
            print(sftp_client.listdir())
            assert sftp_client.listdir() == ['sample.csv']
    
    # def test_sftp_object(self,sftp_client,sftp_server):
    #     """This method test the instance belong to the class of SftpCon"""
    #     self.sftp_obj = SftpCon()
    #     assert isinstance(self.sftp_obj,SftpCon)
        
    # def test_list_files(self,sftp_client):
    #     """This method test weather list_sftp_files return files or not"""
    #     sftp_obj =SftpCon()
    #     result = sftp_obj.list_files()
    #     assert type(result) == list
        
    # def test_read_file(self,sftp_file):
    #     """This method test weather sftp read file or not"""
    #     result = self.sftp_obj.read_file(sftp_file)
    #     assert type(result) == object
    
    # def test_rename_file(self,sftp_file):
    #     """This method will test the if the name changed or not"""
    #     result = self.sftp_obj.rename_file(sftp_file)
    #     assert self.sftp_obj.conn.exists(result) == True
        
    # def test_download_file(self,sftp_file):
    #     """This method will test the when the file downloaded or not"""
    #     result = self.sftp_obj.download_file(sftp_file)
    #     assert os.path.exists(result) == True