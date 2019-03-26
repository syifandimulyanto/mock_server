from flask import Flask, jsonify, request
from app.api_handling import api_handling

app = Flask(__name__)
data = api_handling('mock_blueprint/test.csv')

@app.route('/health')
def health_checker():
    return ('', 204)

@app.route('/', defaults={'path': ''}, methods=['GET','POST','UPDATE','PUT'])
@app.route('/<path:path>', methods=['GET','POST','UPDATE','PUT'])
def catch_all(path):
    response = data.path.get('/' + path,{}).get(request.method, False)
    
    if response is False or response is None:
        return jsonify({'status':'Error','msg':'Not Found'}), 404

    return jsonify(response), 200