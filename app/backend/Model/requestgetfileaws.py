from datetime import datetime
import json
import os
import config

class RequestGetFileAws:
    def __init__(self, type, connector, bucket_name, directory, name_format, **kwargs):
        self.type = type
        self.directory = directory
        self.bucket_name = bucket_name
        self.connector = connector
        self.name_format = name_format

    def get_name_format(self):
        date = ""
        if self.name_format['date'] == "true":
            now = datetime.now()
            date = now.strftime("_%d%m%Y")

        return f"{self.name_format['name']}{date}.{self.name_format['end']}"

    def launch_request(self):
        file_name = os.path.join(self.directory, self.get_name_format())
        request = {
            "bucket_name" : self.bucket_name,
            "file_name" : file_name
            }
        return config.builder.execute_connector(self.connector, request)

    def execute(self, data):
        return data
