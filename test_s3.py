"""This is the test module for the task"""

import pytest
from s3 import S3Service

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
        assert objects['Contents'][0]['Key'] == True
    
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
    