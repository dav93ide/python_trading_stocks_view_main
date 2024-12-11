import os

class FileUtils(object):

    def check_file_exists(file):
        return os.path.exists(file)

    def join_filepath(dir, filename):
        return os.path.join(dir, filename)