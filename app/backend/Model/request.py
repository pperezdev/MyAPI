from app.backend.Model.requestgetfile import RequestGetFile
from app.backend.Model.requestgetdb import RequestGetDB

class Request:
    def __init__(self, name, description, properties):
        self.name = name
        self.description = description
        self.request = self.init_request_type(properties)
        
    def init_request_type(self, property):
        request_name = property["type"]
        class_ = eval(request_name)
        return class_(**property)

    def execute(self):
        data = self.request.launch_request()
        return self.request.execute(data)