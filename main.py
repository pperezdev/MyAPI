from flask import Flask, request, jsonify
from app.backend import services

app = Flask(__name__)

@app.route('/get-schema', methods=['GET'])
def get_schema():
	return services.get_schema()
    

@app.route('/my-request', methods=['POST'])
def my_request():
	data = request.json
	return services.execute(data)

@app.route('/get-connector-schema', methods=['POST'])
def connector_schema():
    data = request.json
    message = services.get_connector_schema(data)
    return message

@app.route('/connection-connector', methods=['POST'])
def connection_connector():
    data = request.json
    message = services.run_connector(data)
    return message

@app.route("/reload", methods=['GET'])
def reload():
    services.build()
    return "APP RELOAD !"

@app.route('/')
def API():
    return "TEST"

if __name__ == '__main__':
	services.build()
	app.run(port=7825,debug=True)