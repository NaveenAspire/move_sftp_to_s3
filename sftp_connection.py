"""This module that is used for connect the sftp"""
import configparser
import pysftp

config = configparser.ConfigParser()
config.read("develop.ini")


class SftpCon:
    """This is the class that contains methods for get file from sftp and upload to s3"""

    def __init__(self):
        """This is the init method of the class of SftpCon"""
        self.conn = pysftp.Connection(
            host=config["SFTP"]["host"],
            username=config["SFTP"]["username"],
            password=config["SFTP"]["password"],
        )
        self.sftp_path = config["SFTP"]["sftp_path"]
        self.local_path = config["Local"]['local_path']
    
    def download_file(self,file):
        """This is method used to dwonload the file from sftp to local"""
        self.conn.get(self.sftp_path+file,self.local_path+file)
        return self.local_path+file

    def list_files(self):
        """This method that returns the list of files names for the given path"""
        sftp_file_list = [file for file in self.conn.listdir(self.sftp_path) if not file.startswith('prcssd.')]
        return sftp_file_list

    def read_file(self, file):
        """This method is used for move the file sftp to s3"""
        with self.conn.open(self.sftp_path + file) as file_obj:
            return file_obj

    def rename_file(self, file):
        """This method is used for rename the sftp file or directory"""
        new_name = self.sftp_path + "prcssd." + file
        self.conn.rename(self.sftp_path + file, new_name)
        return new_name
