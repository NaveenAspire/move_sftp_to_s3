""""This module that is used for migrate the files from sftp to s3 bucket"""
import re
from datetime import datetime
from sftp_connection import SftpCon
from s3 import S3Service


class MoveFileSftpToS3:
    """This is the class for moving file sftp to s3"""

    def __init__(self) -> None:
        """This is the init method for the class of MoveFileSftpToS3"""
        self.sftp_conn = SftpCon()
        self.s3_client = S3Service()

    def move_file(self):
        """This method is used for move the file sftp to s3"""
        sftp_file_list = self.sftp_conn.list_files()
        for file_name in sftp_file_list:
            # file_obj = self.sftp_conn.read_file(file_name)
            self.sftp_conn.download_file(file_name)
            key = self.get_key_name(file_name)
            if key:
                # self.s3_client.put_object(file_obj.read(), key)
                self.s3_client.upload_file(file_name, key)
                self.sftp_conn.rename_file(file_name)

    def get_key_name(self, file_name):
        """This method is used to set the key name for uploading s3"""
        try:
            d_match = re.search(
                "([0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,4})", file_name
            ).group()
            date_object = datetime.strptime(d_match, "%m.%d.%y")
            key = (
                "pt_year="
                + date_object.strftime("%Y")
                + "/pt_month="
                + date_object.strftime("%m")
                + "/pt_day="
                + date_object.strftime("%d")
                + "/"
                + file_name
            )
        except Exception as err:
            key = False
            print(err)
        return key


def main():
    """This is the main method for the module name move_file_sftp_to_s3"""
    move_sftp_to_s3 = MoveFileSftpToS3()
    move_sftp_to_s3.move_file()


if __name__ == "__main__":
    main()
