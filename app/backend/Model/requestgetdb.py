from datetime import datetime
import config
import json

class RequestGetDB:
    def __init__(self, type, query, connector, table_column, **kwargs):
        self.type = type
        self.query = query
        self.connector = connector
        self.columns_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_column}'"

    def get_name_format(self):
        date = ""
        if self.name_format['date'] == "true":
            now = datetime.now()
            date = now.strftime("_%d%m%Y")

        return f"{self.name_format['name']}{date}.{self.name_format['end']}"

    def launch_request(self):
        data = { 
            "rows" : str(config.builder.execute_connector(self.connector, self.query)),
            "column" : ''.join((config.builder.execute_connector(self.connector, self.columns_query)))
        }
        return data

    def execute(self, data):
        results = []
        print(data["rows"])
        print(data["column"])
        for row in data["rows"]:
            results.append(dict(zip(data["column"], row)))
        return json.dumps(results)
