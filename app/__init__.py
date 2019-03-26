from flask import Flask, jsonify, request
import configparser
from time import sleep

from app.api_handling import api_handling

app = Flask(__name__)

cfg = configparser.ConfigParser()
cfg.read('config.cfg')
data = api_handling(cfg['file']['mock_test'])

@app.route('/health')
def health_checker():
    return ('', 204)

@app.route('/', defaults={'path': ''}, methods=['GET','POST','UPDATE','PUT'])
@app.route('/<path:path>', methods=['GET','POST','UPDATE','PUT'])
def catch_all(path):
    result = data.path.get('/' + path,{}).get(request.method, False)
    
    if result is False or result is None:
        return jsonify({'status':'Error','msg':'Not Found'}), 404
    
    response = result.get('response',{})
    wait = int(result.get('wait',0))

    if wait > 0:
        sleep(wait/1000)

    return jsonify(response), 200