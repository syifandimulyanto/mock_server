# import configparser
# from time import sleep

from flask import Flask

# from app.api_handling import api_handling
from app.membership.web.urls import membership

app = Flask(__name__)

app.register_blueprint(membership, url_prefix='/membership')

# cfg = configparser.ConfigParser()
# cfg.read('config.cfg')
# data = api_handling(cfg['file']['mock_test'])

# @app.route('/health')
# def health_checker():
#     return ('', 204)

# @app.route('/', defaults={'path': ''}, methods=['GET','POST','UPDATE','PUT'])
# @app.route('/<path:path>', methods=['GET','POST','UPDATE','PUT'])
# def catch_all(path):
#     result = data.path.get('/' + path,{}).get(request.method, False)
    
#     if result is False or result is None:
#         return jsonify({'status':'Error','msg':'Not Found'}), 404
    
#     response = result.get('response',{})
#     wait = int(result.get('wait',0))

#     if wait > 0:
#         sleep(wait/1000)

#     return jsonify(response), 200