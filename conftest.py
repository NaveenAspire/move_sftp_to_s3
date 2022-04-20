import boto3
import pytest
from moto import mock_s3

@pytest.fixture
def s3_client():
    with mock_s3():
        conn = boto3.client("s3", region_name="us-east-1")
        print(conn)
        yield conn
        
        
@pytest.fixture
def sftp_client(sftp_server):
    print(sftp_server.host)
    with sftp_server.client('sample-user') as client:
        sftp = client.open_sftp()
        yield sftp