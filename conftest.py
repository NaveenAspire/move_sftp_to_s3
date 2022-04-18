from xmlrpc.client import Server
import boto3
import os
import pytest

from moto import mock_s3
from mocksftp import server



@pytest.fixture
def s3_client():
    with mock_s3():
        conn = boto3.client("s3", region_name="us-east-1")
        yield conn
        
# @pytest.fixture
# def sftp_client():
#     with server.Server.client('127.0.0.1'):
#         yield 