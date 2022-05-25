from app.backend.Model.request import Request
from app.backend.Model.connector import Connector
import json
import os

class Builder:
    def __init__(self):
        self.connectors = []
        self.requests = []

    def open_files(self, path, fct):
        objects = []

        folder_path = os.path.abspath(os.path.join('.data', path))
        entries = os.listdir(folder_path)
        for entry in entries:
            file_path = os.path.join(folder_path, entry)
            file = open(file_path, encoding='utf-8')
            data = json.load(file)
            objects.append(fct(data))

        return objects

    def build_request(self):
        return self.open_files("requests", self.create_request)

    def build_connectors(self):
        return self.open_files("connectors", self.create_connector)

    def create_connector(self, data):
        m_connector = Connector(**data)
        return m_connector

    def create_request(self, data):
        m_request = Request(**data)
        return m_request

    def builder(self):
        self.connectors = self.build_connectors()
        self.requests = self.build_request()

    def find_and_execute(self, execution_name, execution_list, execution_item_name, fct_name, *args,**kwargs):
        pointed_execution = [execution for execution in execution_list if execution.name == execution_item_name]
        if len(pointed_execution) == 0:
            return f"ERROR, YOUR {execution_name} '{execution_item_name}' DOESNT EXIST"
        fct = getattr(pointed_execution[0], fct_name)
        return fct(*args, **kwargs)

    def run_request(self, request_name):
        return self.find_and_execute("REQUEST", self.requests, request_name, "execute")

    def run_connector(self, connector_name):
        return self.find_and_execute("CONNECTOR", self.connectors, connector_name, "connection_test")

    def execute_connector(self, connector_name, data):
        return self.find_and_execute("CONNECTOR", self.connectors, connector_name, "execute", data)
        
    def get_schema(self):
        l = []
        for request in self.requests:
            l.append(request.name)

        return json.dumps(l)