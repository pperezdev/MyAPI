from app.backend.Model.connectors.postgresql import PostGreSqlConnector

class Connector:
    def __init__(self, type, name, description, property):
        self.name = name
        self.type = type
        self.description = description
        self.connector = self.create_connector(property)
    
    def create_connector(self, property):
        connector_name = property["connector_name"]
        class_ = eval(connector_name)
        return class_(**property)

    def get_schema(self, data):
        return self.connector.get_schema(data)

    def connection_test(self):
        return self.connector.connection_test()

    def execute(self, data):
        return self.connector.execute(data)
