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
        try:
            sftp_file_list = self.sftp_conn.list_files()
            print("sftp files list are ready..")
            for file_name in sftp_file_list:
                # file_obj = self.sftp_conn.read_file(file_name)
                self.sftp_conn.download_file(file_name)
                key = self.get_key_name(file_name)
                if key:
                    # self.s3_client.put_object(file_obj.read(), key)
                    self.s3_client.upload_file(file_name, key)
                    self.sftp_conn.rename_file(file_name)
                    print(file_name + "is sucessfully moved to s3")
            status = "Success"
        except Exception as err:
            print(err)
            status = "Failed"
        return status

    def get_key_name(self, file_name):
        """This method is used to set the key name for uploading s3"""
        try:
            d_match = re.search("([0-9]{1,2}.[0-9]{1,2}.[0-9]{2,4})", file_name).group()
            year = d_match.split(".")[-1]
            print(len(year))
            date_object = self.get_date_object(d_match)
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

    def get_date_object(self, date_str):
        """This method used for check year format for generate key name"""
        year = date_str.split(".")[-1]
        print(len(year))
        if len(year) == 2:
            date_object = datetime.strptime(date_str, "%d.%m.%y")
        elif len(year) == 4:
            date_object = datetime.strptime(date_str, "%d.%m.%Y")
        else:
            date_object = None
        return date_object


def main():
    """This is the main method for the module name move_file_sftp_to_s3"""
    move_sftp_to_s3 = MoveFileSftpToS3()
    move_sftp_to_s3.move_file()


if __name__ == "__main__":
    main()
