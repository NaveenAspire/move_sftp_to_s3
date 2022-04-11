"""This is the test module for the task"""

import pytest
from s3 import S3Service
from sftp_connection import SftpCon

class Test_s3:
    """This class test for s3 module"""
    
    def test_s3_object(self):
        """This method test the instance belong to the class of S3Service"""
        self.s3_obj = S3Service()
        assert isinstance(self.s3_obj,S3Service)

    def test_put_object(obj_body,key_name):
        s3_put = S3Service()
        response = s3_put.put_object_to_bucket(obj_body,key_name)
        assert type(response) == dict
        
class Test_sftp:
    """This class test for sftp_connection module"""
    
    def test_sftp_object(self):
        """This method test the instance belong to the class of SftpCon"""
        self.sftp_obj = SftpCon()
        assert isinstance(self.sftp_obj,SftpCon)
        
    def test_list_sftp_files(self):
        """This method test weather list_sftp_files return files or not"""
        result = self.sftp_obj.list_sftp_files()
        assert type(result) == list
        
    def test_read_file(self,sftp_file):
        """This method test weather sftp read file or not"""
        result = self.sftp_obj.read_file(sftp_file)
        assert type(result) == object
    
    
    