""""This module that is used for migrate the files from sftp to s3 bucket"""
import argparse
from datetime import date
import time
import pysftp
import boto3


class MoveFileSftpToS3:
    """This is the class for moving file sftp to s3"""

    def __init__(self, host, username, password, bucket_name) -> None:
        """This is the init method for the class of MoveFileSftpToS3"""
        self.conn = pysftp.Connection(host=host, username=username, password=password)
        self.bucket_name = bucket_name
        self.s3_client = boto3.client("s3")

    def move_file(self,sftp_path):
        """This method is used for move the file sftp to s3"""
        sftp_file_list = self.conn.listdir(sftp_path)
        for file_name in sftp_file_list:
            with self.conn.open(sftp_path + file_name) as file_obj:
                key = self.get_key_name(file_name)
                self.s3_client.put_object(
                    Bucket=self.bucket_name, Body=file_obj.read(), Key=key
                )

    def get_key_name(self, file_name):
        """This method is used to set the key name for uploading s3"""
        t_date = str(date.today()).split("-")
        time_stamp = str(int(time.time()))
        filename = file_name.split(".")[0] + "_" + time_stamp + ".csv"
        key = (
            "spotify/source/pt_year="
            + t_date[0]
            + "/pt_month="
            + t_date[1]
            + "/pt_day="
            + t_date[2]
            + "/"
            + filename
        )
        return key


def main():
    """This is the main method for the module name move_file_sftp_to_s3"""
    parser = argparse.ArgumentParser("For giving cli inputs")
    parser.add_argument(
        "--host", type=str, help="Enter host name for SFTP", required=True
    )
    parser.add_argument(
        "--username", type=str, help="Enter user name for SFTP", required=True
    )
    parser.add_argument(
        "--password", type=str, help="Enter password for SFTP", required=True
    )
    parser.add_argument("--sftp_path", type=str, help="Enter sftp path", required=True)
    parser.add_argument(
        "--bucket_name",
        type=str,
        help="Enter th bucket name for store files retrived from sftp server",
        required=True,
    )
    args = parser.parse_args()
    move_sftp_to_s3 = MoveFileSftpToS3(
        args.host, args.username, args.password, args.bucket_name
    )
    move_sftp_to_s3.move_file(args.sftp_path)


if __name__ == "__main__":
    main()
