from app.backend.Controller import MyRequest
from datetime import datetime
import csv
import os
import requests

class RequestGetFile:
    def __init__(self, type, url, method, directory, name_format, **kwargs):
        self.type = type
        self.directory = directory
        self.name_format = name_format
        self.method = method
        self.url = url

    def get_name_format(self):
        date = ""
        if self.name_format['date']:
            now = datetime.now()
            date = now.strftime("_%d%m%Y")

        return f"{self.name_format['name']}{date}.{self.name_format['end']}"

    def launch_request(self):
        return requests.request(self.method,
                        self.url)

    def execute(self, data):
        output = os.path.join(self.directory, self.get_name_format())

        if self.name_format['end'] == "csv":
            decoded_content = data.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=';')
            content = list(cr)
            return MyRequest.download_file_csv(content, output)
            
        return "error"
