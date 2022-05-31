import config 
from app.backend.Controller import builder

def get_schema():
    return config.builder.get_schema()

def get_connector_schema(data):
    connector_name = data["connector_name"]
    return config.builder.get_connector_schema(connector_name, data)

def execute(data):
    request_name = data["request_name"]
    return config.builder.run_request(request_name)

def run_connector(data):
    connector_name = data["connector_name"]
    return config.builder.run_connector(connector_name)

def build():
    config.builder = builder.Builder()
    config.builder.builder()